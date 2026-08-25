# Twenty-five mechanism elements: HOW state changes

A mechanism element is one irreducible state change. Classify the before/after state first; do not name an element from feature vocabulary alone.

## Five change types

| Change type | Test |
|---|---|
| 建立 | A new object, position, relationship, information state, or permission becomes valid. |
| 撤销 | Something valid exits, is spent, hidden, disconnected, or loses permission. |
| 改写 | The continuing object remains but one state changes. |
| 转流 | Object, resource, information, control, or choice moves through the system. |
| 重构 | Object boundaries, membership, or structural correspondence are reorganized. |

## Element table

| ID | Element | Type × domain | Before → after | Typical output | Boundary |
|---|---|---|---|---|---|
| 01 | 生成 | 建立 × 存在 | absent → participating | new selectable or affectable object | Not display; the object did not exist in the rules before. |
| 02 | 移除 | 撤销 × 存在 | participating → exited | released position, relation, or slot | Not hiding; it no longer participates. |
| 03 | 替换 | 改写 × 身份结构 | old identity → successor identity | same duty/slot carried by a new identity | The continuing duty remains while its bearer changes. |
| 04 | 位移 | 改写 × 空间 | point A → point B | new position, adjacency, and distance | Identity stays continuous; only location changes. |
| 05 | 放置 | 建立 × 空间 | no legal occupancy → recognized occupancy | position structure readable by later rules | Not movement; it establishes a legal spatial/container relation. |
| 06 | 耦合位移 | 转流 × 空间 | mover changes → linked follower changes | constrained positions of multiple objects | Movements share one binding constraint. |
| 07 | 连接 | 建立 × 关系 | no active link → active link | channel for resource, risk, control, or action | Proximity alone is not a connection. |
| 08 | 断开 | 撤销 × 关系 | active link → inactive link | channel no longer transmits or is read | End objects remain; only the relation ends. |
| 09 | 旋转 | 改写 × 空间 | facing A → facing B | new coverage or effect direction | Position can remain unchanged. |
| 10 | 标量调整 | 改写 × 量值资源 | old value → new value | changed value and threshold state | Object identity stays; one measurable parameter changes. |
| 11 | 控制权转移 | 改写 × 控制 | controller A → controller B | new actor can issue valid commands | Object stays; command authority changes. |
| 12 | 消耗 | 撤销 × 量值资源 | available amount → lower available amount | paid action/result and remainder | The decrease must pay for a defined use. |
| 13 | 转化 | 转流 × 身份结构 | input identity → output identity | product eligible for new rules | The input participates in forming the output; not a simple successor swap. |
| 14 | 分配 | 转流 × 量值资源 | pooled amount → recipient shares | new holdings by recipient | Total is bounded; destination and share matter. |
| 15 | 揭示 | 建立 × 信息 | existing hidden fact → visible fact | observer can revise a judgment | Not generation; the fact already existed. |
| 16 | 隐藏 | 撤销 × 信息 | visible fact → unavailable fact | information gap and inference space | Not removal; the system still stores the object/fact. |
| 17 | 侦测 | 转流 × 信息 | query over unknown state → limited answer | partial evidence | It may answer only a property or yes/no, not expose the whole truth. |
| 18 | 延迟执行 | 改写 × 时间 | triggered result now → scheduled result later | predictable or interruptible future event | Not cancellation and not cooldown; the result is already scheduled. |
| 19 | 解锁 | 建立 × 权限 | illegal action → legal action | new action entry | It opens an existing capability rather than generating a new feature. |
| 20 | 锁定 | 撤销 × 权限 | legal action → temporarily illegal | closed action entry and constraint | The object remains but cannot currently act/use. |
| 21 | 随机选择 | 转流 × 决定 | unresolved legal candidates → probability-selected result | recordable random result | Legal candidates exist, but the actor does not specify the outcome. |
| 22 | 行动者选择 | 转流 × 控制 | valid candidates → actor-selected result | decision that alters later state | Choice authority belongs to an actor, not chance. |
| 23 | 合并 | 重构 × 身份结构 | separate objects → one whole | unified object for movement, scoring, or effect | Old boundaries disappear into a new whole. |
| 24 | 置换 | 重构 × 空间 | occupants mapped to positions A → remapped positions | new ordering, pairing, or adjacency | Objects and slots remain; their correspondence changes. |
| 25 | 拆分 | 重构 × 身份结构 | one whole → independent parts | separately selectable or operable objects | New parts gain their own boundaries and eligibility. |

## Formula construction

For each element state:

```text
input objects/state → trigger and guard → before/after change → output state → next reader
```

Name the state crossing every arrow. Add failure, cancellation, interruption, contention, and cleanup branches when relevant. Add a loop only when the output materially changes the next decision. Keep animation, sound, UI, and emotional meaning as supporting tools rather than state-change elements.

Common useful connections are hints, not laws: generation often needs placement; choice often precedes consumption or replacement; detection often precedes reveal, lock, unlock, or scalar change; connections often precede distribution, coupled movement, or later disconnection.

Source basis: 六边形老闪《一口气看懂25个机制元》v4 and the accompanying mechanism-chain graph.
