#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def error(path: Path | str, message: str) -> None:
    relative = Path(path)
    try:
        relative = relative.relative_to(ROOT)
    except (TypeError, ValueError):
        pass
    print(f"::error file={relative}::{message}")
    ERRORS.append(f"{relative}: {message}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        error(path, "file is not valid UTF-8")
        return ""


def frontmatter(path: Path) -> dict[str, str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        error(path, "SKILL.md must begin with YAML frontmatter")
        return {}

    end = text.find("\n---\n", 4)
    if end < 0:
        error(path, "frontmatter is missing its closing --- line")
        return {}

    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line or line[0].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")

    if not text[end + 5 :].lstrip().startswith("# "):
        error(path, "Skill body must begin with a level-one heading")
    return values


def validate_skills() -> list[str]:
    skill_dirs = sorted(path.parent for path in ROOT.glob("*/SKILL.md"))
    if not skill_dirs:
        error(ROOT, "no top-level Skill directories found")
        return []

    names: list[str] = []
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        values = frontmatter(skill_file)
        name = values.get("name", "")
        description = values.get("description", "")

        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            error(skill_file, "name must use lowercase kebab-case")
        if name != skill_dir.name:
            error(skill_file, f"name '{name}' must match directory '{skill_dir.name}'")
        if not description or description in {">", ">-", "|", "|-"}:
            error(skill_file, "description must be a non-empty single-line value")

        agent_file = skill_dir / "agents" / "openai.yaml"
        if not agent_file.is_file():
            error(agent_file, "missing agents/openai.yaml")
        else:
            agent = read_text(agent_file)
            for field in ("display_name", "short_description", "default_prompt"):
                if not re.search(rf"^\s+{field}:\s*\S", agent, re.MULTILINE):
                    error(agent_file, f"missing interface.{field}")
            invocation = "$" + name
            if name and invocation not in agent:
                error(agent_file, "default_prompt should explicitly invoke " + invocation)

        names.append(name)

    print(f"Validated {len(skill_dirs)} Skill directories.")
    return names


def validate_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    checked = 0

    for markdown in sorted(ROOT.rglob("*.md")):
        if ".git" in markdown.parts:
            continue
        text = read_text(markdown)
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = unquote(target.split("#", 1)[0])
            if not target:
                continue
            destination = (markdown.parent / target).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                error(markdown, f"relative link escapes repository: {raw_target}")
                continue
            if not destination.exists():
                error(markdown, f"broken relative link: {raw_target}")
            checked += 1

    print(f"Checked {checked} relative Markdown links.")


def validate_zip_packages(skill_names: list[str]) -> None:
    packages = sorted((ROOT / "dist").glob("*.zip"))
    for package in packages:
        try:
            with zipfile.ZipFile(package) as archive:
                files = [name for name in archive.namelist() if not name.endswith("/")]
                if not files:
                    error(package, "ZIP package is empty")
                    continue

                paths = [PurePosixPath(name) for name in files]
                unsafe = [
                    str(path)
                    for path in paths
                    if path.is_absolute() or ".." in path.parts
                ]
                if unsafe:
                    error(package, f"ZIP contains unsafe paths: {unsafe[:3]}")

                unwanted = [
                    str(path)
                    for path in paths
                    if "__MACOSX" in path.parts or path.name == ".DS_Store"
                ]
                if unwanted:
                    error(package, f"ZIP contains unwanted metadata: {unwanted[:3]}")

                roots = {path.parts[0] for path in paths if path.parts}
                if len(roots) != 1:
                    error(package, f"ZIP must contain one top-level Skill folder, found {sorted(roots)}")
                    continue

                root = next(iter(roots))
                if root not in skill_names:
                    error(package, f"ZIP root '{root}' does not match a repository Skill")
                if f"{root}/SKILL.md" not in files:
                    error(package, "ZIP is missing its top-level SKILL.md")
        except zipfile.BadZipFile:
            error(package, "file is not a valid ZIP archive")

    print(f"Validated {len(packages)} ZIP packages.")


def main() -> int:
    skill_names = validate_skills()
    validate_markdown_links()
    validate_zip_packages(skill_names)

    if ERRORS:
        print(f"\nValidation failed with {len(ERRORS)} error(s).")
        return 1

    print("\nAll Skill validation checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
