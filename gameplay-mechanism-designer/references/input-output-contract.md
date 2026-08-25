# Input and output contract

## Input quality

### Minimum

Any one seed is sufficient: keyword, theme, item, character, ability, enemy, resource, rule, mechanic sentence, screenshot, concept art, scene, reference game, or rough pitch.

With only a seed, use Spark: produce three structurally different directions, mark assumptions, and recommend one.

### Recommended

```text
Seed / immutable requirement:
Player goal:
Experience goal:
Platform and form: device, camera, controls, single/multiplayer
Desired depth: directions, full design, system network, or prototype
```

### Professional

```text
Seed / immutable requirement:
Target player and player fantasy:
Player goal:
Experience goal:
Design or product goal:
Genre and reference games:
Platform, camera, controls, player count:
Typical session and long-term structure:
Must-have / must-not-have:
Team, engine, time, and content budget:
Business or live-operation constraints:
Known systems that must connect:
Desired output mode:
```

Do not require every field. More fields reduce arbitrary assumptions; they do not guarantee a better design.

## Output modes

### Spark

Return:

1. three distinct gameplay promises;
2. player and experience goals;
3. primary `WHAT × HOW × WHERE` coordinate for each;
4. core decision and compact repeat loop;
5. 2-4 relevant source chains with IDs;
6. primary loop pattern when repeat play matters;
7. novelty, main risk, and prototype question;
8. one recommendation with reasoning.

Directions must differ structurally, not only in fiction, reward size, or presentation.

### Domain Scan

Return the object being scanned, meaningful findings across the ten domains, selected opportunity domains, associated elements, design consequences, and a recommended focus. Do not fabricate ten features merely to complete the list.

### Placement Variants

Return promising placements among 实体、容器、场地、网络、流程、规则、局外. For each, name the carrier, resulting player decision, mechanism chain, experience effect, production cost, and risk. Recommend the placement that best serves the goals.

### Mechanism Variants

Return 3-6 changes labeled as replacement, insertion, deletion, branch, reorder, loop, or cross-family composition. Name affected state domain, element, placement, experience tradeoff, and production tradeoff.

### Loop Builder

Return the input chain, persistent carrier, 2-3 candidate loop patterns, recommended pattern, explicit loop with state on every arrow, reset/escalation/exit conditions, player psychology, and open-loop risks.

### System Network

Return nodes, labeled edges, carriers, receiving rules, relation types, feedback polarity, limits/delays, player visibility, failure risks, and one simplified recommended topology. A diagram is useful when there are three or more nodes.

### Full Design

Use `design-output-spec.md`. Include design coordinates, mechanism chains, core loop, system relations when multiple systems exist, rules, content, progression, feedback, balance levers, and risks.

### Prototype Pack

Use `design-output-spec.md`. Include hypothesis, greybox scope, state variables, transition rules, parameters, minimum content, implementation order, test cases, telemetry, cut list, and post-test decisions.

### Reverse Design

Return observed facts, inferred affordances and verbs, meaningful state domains, possible placements, three player-goal interpretations, candidate chains, three directions, ambiguity, and assumptions.

### Audit

Return:

1. reconstructed player, experience, and design goals;
2. `WHAT × HOW × WHERE` map;
3. source/adapted chain map;
4. loop pattern and returned state;
5. system nodes, relations, and carriers when applicable;
6. issues ordered by earliest broken layer;
7. prioritized fixes and validation steps.

## Example prompts

Sparse:

```text
一把会记住历任主人的钥匙。帮我生成三个玩法方向。
```

Placement exploration:

```text
把“时间倒流”分别落在实体、场地、流程和规则上，比较会形成什么玩法，推荐一个。
```

Loop and network:

```text
我有探索、建造和防守三个系统。资源来自探索，建筑影响防守，但现在像三个功能拼在一起。请设计核心循环和系统关系。
```

Prototype-ready:

```text
种子：玩家只能通过改变影子的方向移动本体
体验目标：先困惑，随后产生空间顿悟
形式：PC单人、2D横版、键鼠
参考：Braid的规则谜题，但不要时间倒流
约束：1名程序、1名美术、Godot、两周
输出：核心循环、机制链、状态机、10分钟灰盒原型、参数表和测试计划
```
