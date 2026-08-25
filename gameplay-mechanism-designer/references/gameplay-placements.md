# Seven gameplay placements: WHERE the mechanism lives

A placement is the system layer that stores, executes, and feeds back a mechanism. It is not a new mechanism element. The same element at a different placement can change the decision scope and downstream consequences.

| # | Placement | Carriers | Useful questions | Common outcomes | Boundary |
|---|---|---|---|---|---|
| 01 | 实体 | character, enemy, item, device, vehicle, summon | Which individual object changes? Can the player observe or control it directly? | abilities, enemy states, item effects, mechanisms | Use 容器 when the important rule manages a set and its entry/exit. |
| 02 | 容器 | inventory, deck, hand, shop, prize pool, warehouse, quest list | What enters? What is capacity? How are items drawn, sorted, refreshed, or discarded? | inventory management, construction, draw systems, stock tradeoffs | A container is any system governing a set, not only a bag-shaped object. |
| 03 | 场地 | map, board, room, track, warzone, route, level region | Where may players go? Which areas are safe, dangerous, contested, opened, or closed? | exploration, occupation, route planning, terrain change | Placement 场地 is a system layer; domain 空间 is a state property such as position or facing. |
| 04 | 网络 | skill tree, tech tree, transit grid, production chain, relationship graph, dependency graph | Which nodes connect or depend on each other? Where does a change propagate? | system linkage, resource cycles, routes, chained effects | Networks contain concurrent structural links; 流程 emphasizes ordered steps. |
| 05 | 流程 | turn, quest, crafting sequence, combat phase, production, settlement, matchmaking | What happens first? What can be inserted, skipped, reversed, branched, or restarted? | phase play, missions, production, settlement rhythm | A process is ordered execution, even if its steps are displayed as nodes. |
| 06 | 规则 | permission, qualification, restriction, scoring, win/loss, trigger, formula | Who may act? What counts as success? Who bears the result? | eligibility play, triggers, scoring changes, rule exceptions | Rules are executed judgments and constraints, not explanatory text. |
| 07 | 局外 | account, permanent progression, collection, achievement, season, long-term record | What survives the run? What resets? How is the long-term goal made visible? | meta progression, collection, seasonal pursuit, player identity | A menu is not automatically meta; the state must persist beyond the current run. |

## Placement scan

1. Select a mechanism element or chain.
2. Test it against all seven placements.
3. Name the exact carrier at each promising placement.
4. Compare how the placement changes decision, risk, reward, information, and production cost.
5. Select the placement that best serves the player and experience goals.
6. Reconnect the result to a complete chain; an isolated placement idea is not yet gameplay.

## Example: 解锁

- 实体: open a character form or usable item.
- 容器: open inventory capacity, a deck region, or a shop tier.
- 场地: open an area, room, route, or board section.
- 网络: open a link between systems or nodes.
- 流程: open a phase, task segment, or settlement step.
- 规则: grant a new legal action or exception.
- 局外: open permanent capability, account feature, or future-season content.

Use placement variation to create structurally different directions, not seven compulsory outputs.

Source basis: 六边形老闪《一口气看懂7个玩法落点》v1.
