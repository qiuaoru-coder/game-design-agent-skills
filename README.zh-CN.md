# 游戏策划 Agent Skills

[English](README.md)

[![Validate skills](https://github.com/qiuaoru-coder/game-design-agent-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/qiuaoru-coder/game-design-agent-skills/actions/workflows/validate-skills.yml)

把一句模糊灵感扩展成可以制作和验证的玩法，也在投入大量制作前检查“我觉得会好玩”到底是设计逻辑、主观假设，还是已经有证据支持。

这个仓库只收录游戏策划相关的 Codex Skills，主要用于玩法创意、机制设计、策划案审查和最低成本原型规划。它们帮助你把思路说清楚、把系统连起来、把风险变成可验证的问题，但不会隔着文档假装预测游戏一定好玩。

## 应该使用哪个 Skill？

| Skill | 适合解决什么问题 | 常见输出 |
| --- | --- | --- |
| [gameplay-mechanism-designer](gameplay-mechanism-designer/) | 把关键词、道具、机制、画面、场景或粗略想法扩展成真正可玩的结构 | 不同玩法方向、机制链、核心循环、系统联动、制作范围和原型方案 |
| [game-design-reality-check](game-design-reality-check/) | 检查一个看起来很好的设计，究竟有多少是逻辑、有多少是策划自己的想象 | 证据账本、最弱假设、失败方式、修改优先级和最低成本试玩方案 |
| [game-gmt-review](game-gmt-review/) | 使用原始 Goal–Means–Tools 框架审查已有策划案 | GMT 因果图、断裂环节、缺失工具和修改建议 |

做新项目时，通常优先使用前两个 Skill。GMT Skill 作为范围更窄的旧版审查工具继续保留。

## 推荐工作流

~~~text
玩法种子
   ↓
玩法机制设计器
   ↓
形成可玩的结构和原型范围
   ↓
游戏策划现实校验器
   ↓
形成可验证的假设和试玩判断标准
   ↓
制作原型 → 观察玩家 → 修改设计
~~~

第一个 Skill 负责把玩法展开、补齐并连起来；第二个 Skill 负责防止一份逻辑通顺的策划案，被误认为“游戏已经被证明好玩”。

## 快速安装

### 1. 克隆仓库

~~~bash
git clone https://github.com/qiuaoru-coder/game-design-agent-skills.git
mkdir -p ~/.codex/skills
~~~

只复制自己需要的 Skill：

~~~bash
cp -R game-design-agent-skills/gameplay-mechanism-designer ~/.codex/skills/
cp -R game-design-agent-skills/game-design-reality-check ~/.codex/skills/
cp -R game-design-agent-skills/game-gmt-review ~/.codex/skills/
~~~

也可以在 [dist/](dist/) 下载已经打包的 ZIP 文件。

### 2. 明确调用 Skill

~~~text
使用 $gameplay-mechanism-designer：

种子：玩家只能通过改变影子的方向移动本体
体验目标：先困惑，随后产生空间顿悟
形式：PC、2D横版
约束：两人团队、两周原型
请给我三个结构真正不同的方向，推荐一个，
再输出核心循环和10分钟原型方案。
~~~

~~~text
使用 $game-design-reality-check：

不要先假设这个方案会好玩。
请区分观察、设计逻辑、主观假设和未知，
找到最脆弱的因果链，并设计一个最低成本、可能推翻它的测试。
~~~

更完整的大白话说明：

- [玩法机制设计器：大白话使用说明](docs/gameplay-mechanism-designer.md)
- [游戏策划现实校验器：大白话使用说明](game-design-reality-check/README.md)

## 最好输入什么？

只有一句灵感也可以开始。想让结果更准确，最好补充：

- 不可改变的核心灵感或玩法种子；
- 玩家反复做什么、决定什么；
- 希望玩家产生什么体验；
- 平台、视角、单局结构和目标玩家；
- 参考游戏，以及你希望和它有什么不同；
- 团队人数、引擎、时间、内容量和其他限制；
- 你现在究竟要做什么决定；
- 如果是审查方案：你为什么认为它会好玩，目前已有怎样的原型、试玩、数据或外部依据。

其中，最有价值的一项经常是：**你为什么认为它会好玩？**

## 可以得到什么结果？

根据你的要求，Skill 可以输出：

- 多个结构真正不同的玩法方向；
- 玩家目标、操作、规则、代价、失败、奖励和成长；
- 机制链、可重复循环和互相连接的系统网络；
- 灰盒范围、状态机、初始参数和制作顺序；
- 事实、推导、假设和未知组成的证据账本；
- 玩家可能怎样绕开、优化掉或误解设计；
- 试玩对象、观察行为、成功标准、修改信号和停止条件。

## 能力边界

这些 Skill 能提高设计完整度，让不确定性更容易被看见，但不能证明游戏一定好玩，不能预测市场成功，也不能替代品类经验、竞品研究、数值验证、原型制作和真人试玩。留存、平衡、内容量、市场与最终体验仍然需要外部证据。

## 方法论与来源

gameplay-mechanism-designer 的机制知识主要依据六边形老闪（张鹏）公开分享版的“游戏机制元素周期表”和“游戏机制链图谱”系列资料进行结构化整理，再结合 Goal–Means–Tools、制作约束和原型验证形成工作流。仓库不包含原始 PDF。

## 仓库结构

~~~text
gameplay-mechanism-designer/   玩法生成、机制与原型设计
game-design-reality-check/     基于证据的策划现实校验
game-gmt-review/               保留的 GMT 旧版审查 Skill
docs/                          面向使用者的说明文档
dist/                          ZIP 安装包
~~~

## 开源许可

本仓库采用 [MIT License](LICENSE)。方法论来源、作者署名与授权说明见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。

如果这些 Skill 对你的游戏策划工作有帮助，欢迎给仓库一个 Star，也欢迎通过 Issue 提交真实使用反馈。
