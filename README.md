# workbuddy-skills

个人使用的 Codex / WorkBuddy Skills 集合。

## Skills

### gameplay-mechanism-designer

把一个关键词、道具、角色、画面、机制或粗略游戏想法，扩展成更完整的玩法方向、机制链、核心循环、系统关系和可测试原型。

- Skill 源码：[gameplay-mechanism-designer/](gameplay-mechanism-designer/)
- 中文使用说明：[docs/gameplay-mechanism-designer.md](docs/gameplay-mechanism-designer.md)
- ZIP 安装包：[dist/gameplay-mechanism-designer.zip](dist/gameplay-mechanism-designer.zip)

最简单的调用方式：

```text
使用 $gameplay-mechanism-designer：

一把会记住历任主人的钥匙。
请给我三个不同的玩法方向，并推荐一个。
```

### game-gmt-review

### game-design-reality-check

把“我觉得很好玩”变成可以检查和验证的设计假设。它会区分观察、依据、推导、假设和未知，找出最可能翻车的环节，并设计最低成本的原型和试玩方案。

- Skill 源码：[game-design-reality-check/](game-design-reality-check/)
- 大白话使用说明：[game-design-reality-check/README.md](game-design-reality-check/README.md)
- ZIP 安装包：[dist/game-design-reality-check.zip](dist/game-design-reality-check.zip)

最简单的调用方式：

```text
使用 $game-design-reality-check，
检查这个游戏设计中哪些结论是事实、推导、假设或未知，
并告诉我下一步应该怎样验证。

使用 Goal-Means-Tools 框架审查游戏概念、玩法循环和系统策划案。

- Skill 源码：[game-gmt-review/](game-gmt-review/)

### ttcx4-lottery

天天彩选4历史数据更新与娱乐性号码筛选流程。Skill 文件位于仓库根目录。

## 安装 gameplay-mechanism-designer

方法一：下载 ZIP，解压后把 `gameplay-mechanism-designer` 文件夹放入 Codex 的 Skills 目录。

方法二：克隆仓库后复制目录：

```bash
git clone https://github.com/qiuaoru-coder/workbuddy-skills.git
cp -R workbuddy-skills/gameplay-mechanism-designer ~/.codex/skills/
```

安装后可以显式输入 `$gameplay-mechanism-designer` 调用；在玩法设计语境足够明确时，也可以由 Codex 自动选择。

## 方法论来源

`gameplay-mechanism-designer` 的机制知识框架主要依据六边形老闪（张鹏）的“游戏机制元素周期表”和“游戏机制链图谱”系列资料进行结构化整理，并结合 GMT、原型验证和制作约束形成工作流。具体参考文件中保留了来源说明。本仓库不包含原始 PDF。
