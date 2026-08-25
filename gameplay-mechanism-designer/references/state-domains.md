# Ten state domains: WHAT changes

Use state domains to inspect a seed before choosing mechanism elements. They are ten views of a design object, not ten features that every design must contain.

| # | Domain | Design question | What it governs | Typical changes | Boundary check |
|---|---|---|---|---|---|
| 01 | 存在 | 它是否进入当前规则并参与后续结算？ | appearance, exit, participation | 生成、移除、进入或退出本轮 | Hidden objects can still exist; removal ends participation. |
| 02 | 身份结构 | 它是什么，由什么组成，整体和部分如何划分？ | identity, composition, object boundary | 替换、转化、合并、拆分 | A visual reskin is not an identity change unless rules read it differently. |
| 03 | 空间 | 它在哪里、朝向哪里、占据什么位置？ | position, facing, occupancy, adjacency | 放置、位移、旋转、耦合位移、置换 | Rotation is not displacement; ordinary movement is not structural reordering. |
| 04 | 关系 | 它与谁连接、依赖或从属？ | links, ownership, dependency, channels | 连接、断开、归属、依赖 | Proximity is not a relation unless rules can transmit or read an effect through it. |
| 05 | 量值资源 | 它有多少、还能使用或支付多少？ | quantities, stock, costs, distribution | 标量调整、消耗、分配、阈值 | A decrease is consumption only when it pays for a defined use. |
| 06 | 控制 | 谁能支配它、发出有效命令并承担结果？ | command, agency, responsibility | 控制权转移、行动者选择、夺取、委托 | Ownership does not automatically grant current action permission. |
| 07 | 信息 | 谁知道什么、能看见多少、信息是否可信？ | visibility, clues, uncertainty, deception | 揭示、隐藏、侦测、误导 | Detection can reveal a limited property; revelation exposes existing information. |
| 08 | 时间 | 何时触发、生效、持续和结算？ | timing, windows, queues, ordering | 延迟执行、倒计时、持续时间、队列 | Cooldown closes permission temporarily; delayed execution postpones a triggered result. |
| 09 | 权限 | 谁能做什么，现在是否可以执行？ | eligibility, legal actions, rule boundaries | 解锁、锁定、资格、通行权 | Seeing or owning something does not imply permission to use or enter it. |
| 10 | 决定 | 结果由谁或什么选出？ | choice ownership and result selection | 随机选择、行动者选择、系统判断、投票 | A fixed sequence is not random; one legal option is not a meaningful choice. |

## Scan procedure

1. Name the object or system being scanned.
2. Ask all ten questions internally.
3. Keep only domains where a change would alter player decisions, risks, information, or future state.
4. For each retained domain, state before, after, observer/controller, and downstream consequence.
5. Use the chosen domain plus a change type to select a mechanism element.

For sparse seeds, compare at least three structurally different domain emphases. Do not produce ten superficial variations. If every proposal concentrates on 量值资源, deliberately test whether 空间、关系、信息、权限 or 决定 creates a more meaningful structure.

## Diagnostic patterns

- **Quantity-only design**: most changes are scalar bonuses or costs; test another domain.
- **Appearance mistaken for identity**: presentation changes but no rule reads the new identity.
- **Visibility mistaken for existence**: hidden content is incorrectly treated as deleted.
- **Control confused with permission**: an actor controls an object but cannot legally perform the action, or vice versa.
- **Time confused with permission**: a postponed result is described as cooldown, or a locked action as delayed resolution.
- **Choice without alternatives**: the design claims agency but has one dominant or legal option.

Source basis: 六边形老闪《一口气看懂10个状态域》v4.
