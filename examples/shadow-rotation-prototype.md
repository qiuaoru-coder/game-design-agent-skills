# Worked Example: Shadow Rotation / 完整案例：旋转影子移动

> This is an illustrative design-and-validation output, not evidence that the concept is fun. No prototype or playtest results are claimed.
>
> 这是一个“玩法设计＋现实校验”的示范输出，不代表玩法已经被证明好玩，也没有虚构任何原型或试玩结果。

This example shows how a sparse seed can pass through **gameplay-mechanism-designer** and then **game-design-reality-check**:

~~~text
seed → distinct directions → recommended structure → greybox prototype
     → assumptions and failure modes → cheapest decisive playtest
~~~

## 1. Input / 输入

~~~text
Seed / immutable requirement:
The player can move only by rotating their shadow.
玩家只能通过旋转自己的影子移动本体。

Experience goal:
Confusion followed by spatial insight.
先困惑，随后产生空间顿悟。

Format:
Single-player PC, 2D side view, keyboard controls.
PC 单人、2D 横版、键盘操作。

Constraints:
One programmer, one artist, Godot, two-week prototype.
1 名程序、1 名美术、Godot、两周原型。

Requested output:
Three structurally different directions, one recommendation,
a ten-minute greybox, and a reality check.
~~~

Material assumptions:

- The concept is a short spatial-puzzle prototype, not yet a full commercial-game pitch.
- “Rotate the shadow” may rotate a controllable light direction; this interpretation is original synthesis, not supplied evidence.
- Art, story, progression, market position, and accessibility requirements remain undecided.

## 2. Three structurally different directions / 三个不同玩法方向

| Direction | Gameplay promise | Primary coordinate: WHAT × HOW × WHERE | Repeated decision | Main risk |
| --- | --- | --- | --- | --- |
| **A. Anchor Orbit / 影锚公转** | Attach the shadow tip to an anchor, then rotate the light so the fixed tip drags the body around obstacles | Space × rotation plus coupled displacement × level field and player entity | Which anchor, direction, and release point creates a safe arc? | Players may rotate until snapping occurs instead of reasoning spatially |
| **B. Shadow Bridge / 影桥通行** | Rotate the shadow into a temporary walkable bridge; movement is legal only along the projected shape | Permission and space × rotation, connection, unlock × level field and rules | Which surface should receive the bridge, and when should it be committed? | It may become an ordinary bridge-placement puzzle with shadow only as presentation |
| **C. Borrowed Shadow / 借影而行** | Connect the player's shadow to moving objects and transfer movement control through the shared shadow | Relation and control × connection, control transfer, coupled displacement × entity network | Which object's motion should be borrowed, and when should the link break? | More AI, timing, collision, and readability work than a two-week prototype can safely carry |

### Recommendation / 推荐

Choose **A. Anchor Orbit**.

It makes rotation itself produce locomotion, preserves the immutable seed most directly, and isolates one unusual spatial mapping that a small greybox can test. Direction B is cheaper but less distinctive. Direction C has richer long-term potential but introduces too many dependencies before the core control idea is validated.

## 3. Recommended gameplay design / 推荐玩法设计

### Gameplay promise / 玩法承诺

The player cannot walk. They rotate a light, sweep their shadow across the room, attach its tip to a dark anchor, and keep rotating so the fixed shadow drags their body along an arc.

玩家不能普通行走，只能旋转光源让影子扫过场景；当影子尖端连接影锚后，继续旋转会牵引本体沿弧线移动。

### Goals / 目标

| Goal type | Goal | Status |
| --- | --- | --- |
| Player goal | Reach the exit by chaining legal shadow anchors | Designed, not yet observed |
| Experience goal | Move from confusion to prediction and spatial insight | Assumed |
| Design goal | Create understandable locomotion from one unusual rule with low content cost | Plausible but unproven |

### Core decision / 核心决策

For every move, the player chooses:

1. which visible anchor to target;
2. clockwise or counter-clockwise rotation;
3. when to attach and release;
4. whether the predicted arc clears walls and hazards.

A choice is meaningful only when at least two routes are readable and differ in safety, position, or future access. A room with one legal anchor is onboarding, not strategic depth.

### Design coordinates / 设计坐标

| Role | State domain | Mechanism element | Placement and carrier | Consequence |
| --- | --- | --- | --- | --- |
| Primary | Space | Rotation → coupled displacement | Field plus player entity; light angle, shadow tip, body position | Rotating the shadow changes the body's legal path |
| Support | Relation | Connection and disconnection | Anchor–shadow tether | Creates and ends the movement constraint |
| Support | Information | Detection and reveal | Anchor highlight and predicted arc | Lets the player learn why a move is legal |
| Support | Permission | Unlock | Exit rule | Opens completion only when the body reaches the exit |

### Mechanism-chain trace / 机制链来源与改编

These source chains are design references, not claims that the final composition appears verbatim in the source taxonomy.

| Source chain | Source formula | Use and adaptation |
| --- | --- | --- |
| H024, 朝向调整 | Actor choice → rotation → detection | **Extension:** rotating the light changes the shadow direction; detection then checks shadow-tip overlap |
| H019, 牵引物体 | Connection → actor choice → coupled displacement → placement | **Replacement and extension:** the fixed shadow tip becomes the anchor; continued rotation drives the linked body |
| H037, 拼块落位 | Actor choice → displacement → rotation → placement → detection | **Reordering:** rotation precedes constrained body displacement; final placement is checked against collision and exit rules |
| H042, 管线连通 | Rotation → connection → detection → unlock | **Cross-family composition:** a valid anchor path and final position unlock the exit |

### Causal chain / 因果链

~~~text
player rotation input
→ light-angle state changes
→ shadow-tip position changes
→ anchor-overlap state is detected
→ tether relation becomes available
→ player attaches
→ tether relation becomes active
→ continued rotation produces constrained body displacement
→ collision and length limits are detected
→ body is placed at the last legal position
→ new position changes the next available anchors
→ exit occupancy unlocks completion
~~~

Failure and cleanup branches:

- No anchor overlap: attachment input is ignored and the candidate highlight stays off.
- Arc hits a wall: body stops at the last legal point; tether remains only if the shadow-length constraint is still valid.
- Shadow length exceeds its limit: tether breaks with explicit feedback.
- Player releases: tether disconnects; body remains at the last legal position.
- Impossible state or geometry overlap: reset to the latest checkpoint.

### Core loop / 核心循环

Primary loop pattern: **错题本模式 / Learn-from-failure loop**

~~~text
observe geometry and anchors
→ predict an arc
→ choose anchor and rotation direction
→ execute the tethered move
→ collision, success, or route failure reveals spatial information
→ reset or continue from a changed position
→ revise the next prediction
~~~

- **Persistent carrier:** player knowledge of arc direction, anchor reach, and collision boundaries.
- **Reset:** instant room restart or checkpoint reset.
- **Escalation:** later rooms reduce safe anchors, add occlusion, or require release timing.
- **Interruption:** player may release a tether at any legal point.
- **Exit:** reaching the marked exit completes the room.
- **Risk:** if collision causes are unclear, failure teaches nothing and the loop becomes random trial and error.

## 4. Ten-minute greybox prototype / 十分钟灰盒原型

### Central hypothesis / 核心假设

~~~text
We believe puzzle players will experience spatial insight
because choosing an anchor and rotation direction lets them predict
and then observe an unusual but consistent movement arc.

We will consider this plausible when players begin predicting paths
before moving and can explain the rule without repeating the tutorial text.
~~~

### Required scope / 必做范围

- One controllable circular player body.
- One rotatable directional light.
- One generated shadow line with a visible tip.
- Static walls and collision.
- Shadow anchors with candidate, attached, and unavailable feedback.
- Attach, release, reset, completion, and checkpoint rules.
- Three rooms totaling about ten minutes.
- Minimal telemetry and an observer notes sheet.

Explicit exclusions:

- finished art, narrative, enemies, combat, economy, meta progression;
- procedural levels, multiple light sources, movable anchors;
- controller support, mobile controls, accessibility polish;
- market, retention, monetization, and content-volume claims.

### Controls / 操作

| Input | Action |
| --- | --- |
| A / D or Left / Right | Rotate light and shadow counter-clockwise / clockwise |
| Space | Attach to or release the highlighted anchor |
| R | Restart the current room |
| Esc | Pause and show controls |

### State model / 状态模型

| Entity | States and variables | Important transitions |
| --- | --- | --- |
| Player | position, collision state, checkpoint | Legal arc movement updates position; invalid overlap returns to last legal position |
| Light | angle, angular speed | Rotation input changes angle within the allowed range |
| Shadow | tip position, length, candidate anchor | Light angle recalculates tip; overlap reveals candidate |
| Tether | detached, candidate, attached, blocked | Space attaches candidate; release or length limit disconnects |
| Room | active, solved, resetting | Exit occupancy solves; R or invalid state resets |

### Rule table / 规则表

| Rule | Trigger and precondition | Result and feedback | Edge case |
| --- | --- | --- | --- |
| Rotate | Direction input; room active | Update light angle and shadow tip; draw predicted arc when attached | Clamp angular speed to avoid tunneling |
| Detect anchor | Shadow tip enters snap radius | Candidate anchor glows and emits a short sound | If two overlap, choose nearest then stable ID |
| Attach | Space; valid candidate | Fix shadow tip to anchor and enter attached state | Ignore repeat input during a short debounce window |
| Move by rotation | Rotation input; tether attached | Solve constrained body position and sweep collision | Stop at last legal position if the arc is blocked |
| Release | Space; tether attached | Keep body position and remove relation | If inside invalid geometry, restore last legal position |
| Solve | Player overlaps exit and is not blocked | Freeze input, show completion, load next room | Prevent completion during reset |

### Starter parameters / 初始参数

These are test values, not balance claims.

| Parameter | Initial value | Safe test range | Expected effect |
| --- | ---: | ---: | --- |
| Shadow maximum length | 240 px | 180–320 px | Controls reachable-anchor density |
| Light rotation speed | 90°/s | 60–140°/s | Trades precision against waiting |
| Anchor snap radius | 18 px | 10–28 px | Trades targeting clarity against accidental attachment |
| Player radius | 12 px | 10–18 px | Changes collision forgiveness |
| Wall clearance | 4 px | 2–8 px | Reduces ambiguous scraping and tunneling |
| Attach debounce | 0.15 s | 0.10–0.25 s | Prevents accidental attach–release |
| Restart delay | 0.25 s | 0–0.5 s | Keeps failure iteration fast |

### Three-room content plan / 三个房间

1. **Rule discovery:** one obvious anchor and no hazard; teaches that rotation alone does not move the body, but attached rotation does.
2. **Prediction:** two anchors and one blocking wall; only one direction produces a valid arc.
3. **Transfer:** two sequential anchors; the first move changes which second anchor is reachable.

Do not add a fourth room until the first test shows that players understand the causal mapping.

### Implementation order / 制作顺序

1. Light rotation and shadow-tip calculation.
2. Anchor detection and stable highlighting.
3. Tether constraint and body arc movement.
4. Swept collision and last-legal-position recovery.
5. Reset, checkpoint, and exit.
6. Three rooms and minimal feedback.
7. Telemetry and playtest build.
8. Only after validation: presentation experiments.

### Telemetry and observer notes / 数据与观察

Record:

- time to first valid attachment;
- number of invalid attachment attempts;
- rotation reversals before and after attachment;
- wall collisions and resets;
- whether the player pauses to inspect before moving;
- hints requested and exact facilitator wording;
- room completion time and chosen anchor sequence;
- whether the player predicts the path verbally or with cursor movement;
- the player's explanation of the rule after play.

Events may include: **room_start**, **anchor_candidate**, **attach**, **release**, **collision_stop**, **reset**, **room_complete**, each with room, anchor, angle, position, and elapsed-time properties where relevant.

## 5. Reality check / 现实校验

### Verdict / 结论

**Test-ready, not supported yet / 已具备测试条件，但尚未得到证据支持。**

The design has a coherent causal rule and a prototype that can isolate it. The weakest link is whether players form a predictive spatial model, rather than succeeding through indiscriminate rotation and generous snapping.

### Falsifiable promise / 可证伪承诺

For players who enjoy short spatial puzzles, during a ten-minute PC session, anchor-based shadow rotation is expected to cause visible path prediction before movement, which would support the intended feeling of spatial insight.

We should doubt this when players mostly rotate until something highlights, cannot predict the body's arc, or describe the movement as arbitrary after completing the tutorial.

### GMT causal map / GMT 因果图

| Goal | Means | Tools | Expected behavior | Claimed outcome | Evidence now |
| --- | --- | --- | --- | --- | --- |
| Reach the exit | Spatial prediction and route selection | Rotatable light, anchors, arc collision, reset | Inspect, predict, choose, execute, revise | Puzzle completion through understanding | Rules are derived; player behavior is assumed |
| Feel spatial insight | Surprise followed by a stable mental model | Consistent geometry, visible tether, immediate feedback, learnable rooms | Shift from trial to prediction | “I understand why that worked” | Unknown until observed |
| Produce a distinctive low-cost prototype | One rule reused across three rooms | Greybox geometry and parameterized anchors | Team builds and tests in two weeks | Useful go/no-go evidence | Scope is derived; schedule feasibility remains assumed |

### Evidence ledger / 证据账本

| Claim | Label | Current basis | Limitation and failure signal |
| --- | --- | --- | --- |
| The player cannot move without an active tether | Derived | Explicit movement rule | Implementation bugs may violate it |
| Rotation plus a fixed tip creates an arc-constrained position | Derived | State and geometry rules | Physical readability is not established |
| Players will understand anchor highlighting | Assumed | Conventional feedback pattern | Repeated invalid inputs or facilitator hints |
| Players will predict before moving | Assumed | Intended decision structure | Random sweeping, no inspection, no prediction |
| Failure will teach useful spatial information | Assumed | Fast reset and consistent collision | Same mistake repeats without changed explanation |
| Three rooms can test the core mapping | Derived and assumed | Each room isolates one learning step | Room design may accidentally teach only one solution |
| The prototype fits two people and two weeks | Assumed | Narrow scope and placeholder assets | Collision solver or shadow rendering consumes the schedule |
| The idea has market, retention, or content depth | Unknown | No relevant evidence | Not a decision this prototype can answer |

### Failure-first findings / 失败优先检查

1. **Major — discovery may replace decision.**  
   Players may sweep the shadow until an anchor glows, making generous detection do the puzzle-solving. Observe inspection and pre-move prediction; do not infer understanding from completion alone.

2. **Major — visual metaphor may conflict with rule geometry.**  
   A shadow that stretches, fixes its tip, and drags a body may violate player expectations. Clear feedback can teach a fictional rule, but the rule must remain consistent.

3. **Major — the “insight” may occur once.**  
   Understanding the control mapping may create one surprise without enough contextual decisions for repeated play. Do not build progression until room two and three show changed predictions.

4. **Minor — precision could hide the idea.**  
   If aiming and collision dominate, the test measures control tolerance rather than spatial reasoning. Tune snap radius and rotation speed before adding content.

5. **Production risk — collision can consume the prototype.**  
   Use simple circular bodies and convex greybox walls. If the constraint solver remains unstable, fake the shadow line and directly calculate the arc; visual physics accuracy is not the hypothesis.

### Cheapest decisive playtest / 最低成本试玩

- **Participants:** a small formative group containing puzzle players and at least two people who do not routinely play spatial puzzle games. This is a usability and causal-learning test, not market validation.
- **Context:** individual ten-minute sessions on keyboard, current greybox build, no design explanation beyond the controls.
- **Observe before asking:** scanning, rotation patterns, anchor choice, prediction, repeated errors, hint requests, and rule explanation.
- **Ask afterward:** “What caused the body to move?”, “What did you expect before the last move?”, and “How did you choose the anchor?”
- **Support signal:** most participants begin predicting a path before committing, solve the second room without a procedural hint, and explain the anchor–rotation–arc relationship in their own words.
- **Revise signal:** participants complete rooms mainly by sweeping until a highlight appears, understand the rule only after prompting, or see no meaningful choice between anchors.
- **Stop signal:** after one onboarding room, the causal mapping still feels inconsistent or the required input precision remains the dominant frustration.
- **Confounds:** facilitator prompting, oversized snap radius, one-solution rooms, novelty, prior puzzle expertise, and visible debug arcs.

### Decision after the test / 测试后的决定

- **Supported:** build two more rooms that vary anchor arrangement without adding a new mechanic.
- **Mixed:** revise feedback, snap rules, or room geometry and repeat the same test.
- **Contradicted:** stop content production; compare a simpler Shadow Bridge implementation against the original seed.
- **Still unknown:** market interest, long-term retention, accessibility, content volume, art appeal, and commercial scope.

## 6. What this example demonstrates / 这个案例展示了什么

- A seed is not treated as a complete game.
- Three directions differ by state domain, mechanism, placement, and repeated decision—not only by theme.
- Source mechanism chains are cited, and every adaptation is labeled.
- The recommendation is constrained by team and prototype cost.
- The prototype tests one central claim and explicitly excludes unrelated production.
- A coherent document is not presented as evidence that the game is fun.
- The reality check ends with observable behavior and a real design decision.

## 7. Reproduce the workflow / 复现方式

First use **$gameplay-mechanism-designer** with the input at the top and request Spark plus Prototype Pack. Then pass the resulting proposal to **$game-design-reality-check** and request a Validation Design review.

Treat any new output as a design proposal. Replace the assumptions in this document only with real prototype, playtest, technical, or external evidence.
