# workbuddy-skills

个人使用的 Codex / WorkBuddy Skills 集合。

## 游戏策划现实校验器

防止策划把“我觉得很好玩”误当成已经成立的事实。它会检查目标、机制和预期体验之间的因果关系，区分观察、依据、推导、假设和未知，并给出最低成本的原型或试玩验证方案。

- [Skill 源码](game-design-reality-check/)
- [大白话使用说明](game-design-reality-check/README.md)
- [ZIP 安装包](dist/game-design-reality-check.zip)

调用示例：

```text
使用 $game-design-reality-check，检查这个游戏设计中哪些结论是事实、
推导、假设或未知，并告诉我下一步该怎样验证。
```

## Game GMT Review

原有的 GMT Skill 继续完整保留，适合明确需要使用 Goal–Means–Tools 框架拆解和审查策划案的情况。

- [game-gmt-review](game-gmt-review/)

## TTCX4 Lottery

天天彩选4历史数据更新与娱乐性号码筛选流程。Skill 文件位于仓库根目录。

## 安装

下载 ZIP，解压后把 `game-design-reality-check` 文件夹放入 Codex 的 Skills 目录；也可以克隆本仓库后复制该目录：

```bash
git clone https://github.com/qiuaoru-coder/workbuddy-skills.git
cp -R workbuddy-skills/game-design-reality-check ~/.codex/skills/
```

安装后可以输入 `$game-design-reality-check` 显式调用；在游戏策划审查和玩法验证语境明确时，也可以由 Codex 自动选择。
