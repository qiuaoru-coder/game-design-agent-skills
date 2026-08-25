# Contributing / 贡献指南

Thank you for helping improve these game-design agent skills. Contributions that make outputs clearer, more testable, and more useful in real production are welcome.

感谢你帮助改进这些游戏策划 Agent Skills。我们欢迎能让输出更清楚、更可验证、更适合真实项目使用的贡献。

## Good contributions / 适合贡献的内容

- Fix unclear instructions, broken links, or validation errors.
- Add practical examples, edge cases, or low-cost prototype methods.
- Improve a skill without turning assumptions into facts.
- Report outputs that looked convincing but failed in prototyping or playtesting.
- 修正模糊说明、失效链接或校验错误。
- 补充真实案例、边界情况或低成本原型方法。
- 改进 Skill，同时明确区分事实、假设和待验证内容。
- 反馈“看起来合理但原型或试玩中不成立”的输出。

## Before a large change / 大改动之前

Please open an Issue first and explain the problem, intended users, expected output, and why the current skills do not cover it. This avoids duplicated work and makes the design direction visible before implementation.

较大改动请先创建 Issue，说明问题、目标用户、预期输出，以及现有 Skills 为什么无法覆盖。这样可以在动手前确认方向并避免重复工作。

## Contribution workflow / 贡献流程

1. Fork the repository and create a focused branch.
2. Make one coherent change per pull request.
3. Run: python3 scripts/validate_skills.py
4. Update documentation and any published package in dist when relevant.
5. Open a pull request and complete the checklist.

1. Fork 仓库并新建独立分支。
2. 每个 PR 尽量只解决一个明确问题。
3. 运行：python3 scripts/validate_skills.py
4. 如有需要，同步更新说明文档和 dist 中对应发布包。
5. 创建 PR，并完整填写检查清单。

## Skill change checklist / Skill 修改检查

- Keep the frontmatter name and description accurate.
- Keep SKILL.md focused; place detailed reusable material under references.
- Update agents/openai.yaml when the user-facing name, description, or starter prompt changes.
- Check every relative Markdown link.
- If a matching ZIP exists in dist, rebuild it and ensure the archive contains one top-level skill directory.
- Explain what was tested and what remains an assumption.

- 确保 frontmatter 中的 name 与 description 准确。
- 保持 SKILL.md 聚焦；较长的可复用材料放入 references。
- 如果用户可见名称、说明或启动提示发生变化，同步更新 agents/openai.yaml。
- 检查所有相对 Markdown 链接。
- 如果 dist 中存在对应 ZIP，请重新打包，并确保压缩包只有一个顶层 Skill 目录。
- 说明已经验证的内容，以及仍属于假设的部分。

## Sources, rights, and privacy / 来源、权利与隐私

Only contribute material that is original, publicly reusable under compatible terms, or explicitly authorized for publication and adaptation. Add attribution or notices when required. Do not submit confidential game documents, unreleased project data, personal information, credentials, or third-party material you are not allowed to share.

只提交原创内容、具有兼容公开许可的内容，或已获得明确公开和改编授权的内容；需要署名或声明时请一并补充。请勿提交未公开游戏资料、保密项目数据、个人信息、账号凭据，或无权分享的第三方内容。

By submitting a contribution, you agree that it may be distributed under this repository's MIT License.
