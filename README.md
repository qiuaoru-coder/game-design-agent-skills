# Game Design Agent Skills

[中文说明](README.zh-CN.md)

Turn rough game ideas into structured, testable gameplay—and challenge “this will be fun” before production.

This repository contains focused Codex Skills for gameplay ideation, mechanism design, design review, and low-cost prototype planning. The Skills help organize design reasoning; they do not pretend to predict fun from a document.

## Choose a Skill

| Skill | Use it when you need to | Typical result |
| --- | --- | --- |
| [gameplay-mechanism-designer](gameplay-mechanism-designer/) | Expand a keyword, prop, mechanic, image, scene, or rough pitch into playable structure | Distinct gameplay directions, mechanism chains, core loops, system links, scope, and a prototype plan |
| [game-design-reality-check](game-design-reality-check/) | Test whether a promising design is supported by logic and evidence rather than designer intuition | Evidence ledger, weakest assumption, failure modes, priorities, and the cheapest useful playtest |
| [game-gmt-review](game-gmt-review/) | Review an existing proposal with the original Goal–Means–Tools framework | Goal–Means–Tools map, broken links, missing tools, and concrete revisions |

New projects should usually start with the first two Skills. The GMT Skill is preserved as a narrower legacy review tool.

## Recommended Workflow

~~~text
design seed
    ↓
gameplay-mechanism-designer
    ↓
playable structure and prototype scope
    ↓
game-design-reality-check
    ↓
testable assumptions and playtest signals
    ↓
prototype → observe → revise
~~~

The first Skill expands and connects the design. The second prevents a coherent-looking document from being mistaken for evidence that the game is fun.

## Quick Start

### 1. Clone the repository

~~~bash
git clone https://github.com/qiuaoru-coder/game-design-agent-skills.git
mkdir -p ~/.codex/skills
~~~

Copy only the Skills you want:

~~~bash
cp -R game-design-agent-skills/gameplay-mechanism-designer ~/.codex/skills/
cp -R game-design-agent-skills/game-design-reality-check ~/.codex/skills/
cp -R game-design-agent-skills/game-gmt-review ~/.codex/skills/
~~~

Packaged ZIP files are also available in [dist/](dist/).

### 2. Invoke a Skill explicitly

~~~text
Use $gameplay-mechanism-designer.

Seed: The player can move only by rotating their shadow.
Experience goal: confusion followed by spatial insight.
Constraints: PC, 2D, two-person team, two-week prototype.
Give me three structurally different directions, recommend one,
then produce the core loop and a 10-minute prototype plan.
~~~

~~~text
Use $game-design-reality-check.

Review this proposal without assuming it will be fun.
Separate observations, design logic, assumptions, and unknowns.
Find the weakest causal link and design the cheapest test that could disprove it.
~~~

Chinese prompt examples and plain-language guides:

- [玩法机制设计器：大白话使用说明](docs/gameplay-mechanism-designer.md)
- [游戏策划现实校验器：大白话使用说明](game-design-reality-check/README.md)

## Best Inputs

A single idea is enough to begin. Better inputs usually include:

- the non-negotiable design seed;
- what the player repeatedly does and decides;
- the intended player experience;
- platform, perspective, session structure, and target audience;
- references and explicit differences from them;
- team size, engine, schedule, content budget, and other constraints;
- what decision you need to make now;
- for reviews: why you believe the design will be fun and what evidence already exists.

## What You Can Get

Depending on the request, the Skills can produce:

- multiple structurally distinct gameplay directions;
- player goals, actions, rules, costs, failure, rewards, and progression;
- mechanism chains, repeatable loops, and connected system networks;
- graybox scope, state machines, starter parameters, and build order;
- assumption and evidence ledgers;
- likely exploits, dominant strategies, misunderstandings, and failure signals;
- playtest participants, observations, success criteria, revision triggers, and stop conditions.

## Boundaries

These Skills can improve design completeness and make uncertainty explicit. They cannot prove that a game is fun, predict market success, replace genre expertise, or substitute for prototypes and real-player playtests. Market claims, balance, retention, content volume, and final experience still require external research and evidence.

## Repository Layout

~~~text
gameplay-mechanism-designer/   gameplay generation and prototype planning
game-design-reality-check/     evidence-based design stress testing
game-gmt-review/               preserved GMT review Skill
docs/                          user-facing guides
dist/                          packaged ZIP files
~~~

## License

Released under the [MIT License](LICENSE). Methodology attribution and permission notes are recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

If these Skills help your design work, consider starring the repository. Issues and concrete playtest feedback are welcome.
