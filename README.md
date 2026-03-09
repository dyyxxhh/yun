# YunGame 规则结算 API

## 启动

```bash
cd x/yungame
npm start
```

## API

### POST `/api/resolve-round`

输入：
- `players[]`: `{ id, team?, alive, removed?, mana, yun|luck, tags?, disabledActions?, counters?, history?, action }`
- `action.type` 使用 `src/engine.js` 里的 `ACTIONS` 常量

输出：
- `players[]`: `{ id, team, alive, removed, mana, yun, tags, disabledActions, counters, history, events }`
- `winner`: 单人生还时返回玩家 id，否则 `null`
- `events[]`: 本回合全局事件流（copy_success / hammer_disabled / soil_broken / self_erased ...）

### POST `/api/run-examples`

运行 rules.md 的 20 个样例回归测试。

## 已实现规则（当前引擎）

- 资源：`yun` / `mana`（输入兼容 legacy `luck`，输出统一 `yun`）
- 基础攻防与伤害对冲
- 基础连招动作：气波/上勾/下勾/猫爪
- 范围伤害与队友免伤
- 复制 / 破解复制 / 循环复制失败
- 锤子禁用（后续回合生效）+ 对同一目标重复限制 + 钉子联动
- 土（pending->active、碎土、每回合扣2 mana）
- 准星（延迟生效、同回合多目标冲突清除、状态期防御强制为0、受伤反噬）
- 腐化基础标记（当前主要用于准星绕过）
- Magic YGG 基础状态机（6回合倒计时、每回合扣mana、失败终止、到期复活死人）
- YGG / Mark（复活与抹除）
- 枪 / 自杀 的自抹除与伤害
- 飞轮（本回合不可被选中；重复使用自爆）
- 魔防、格挡、玩手机、Magic玩手机、玩电脑（基础条件链）
- 邪眼护符（当回合未受忽防伤害则激活，持续回合防御加成）
- 椰子（高伤触发反击）
- 忽视防御伤害通道（气波/Magic气波）
- 炸弹基础阶段与中断惩罚（普通炸弹、Magic炸弹基础中断/返还）
- 腐化基础重映射（腐化者输出翻倍、入伤重映射）
- 照相机基础槽位（保存拍摄动作4回合，团战禁止拍队友）
- 镰刀基础解锁与高伤害（需5次破解复制计数）
- 杀死抵消基础链路（枪/自杀/镰刀触发）
- 亡语基础链路（枪/自杀/镰刀）
- 全灭时基础平局判定（按分层+受伤量）
- YGG + Mark 同回合交互（复活后下次死亡抹除）
- 多个YGG同指同一目标按“分别处理”结算，不互相触发自爆
- Magic YGG 与 YGG 同回合同指同一目标时分别处理（同回合不互斥）
- Magic枪改为逆时针链式传递；首目标为飞轮时该链路直接失效，但使用者仍抹除
- 强制在互相强制/环形强制时会抵消
- 复制恐惧震慑对Magic枪按总伤害判定
- 资源不足违规自爆（自抹除）
- `winner` 判定

## 未完整实现（已明确）

以下规则仍是**简化实现**或未完全覆盖：
- Magic 炸弹完整叠加细则（与复制版叠加、多段并行等）
- 腐化完整伤害重映射精确公式（准星后腐化的全局求和口径）
- 亡语全量优先级（全道具级别）
- 平局判定细则（受伤层级比较）
- 团战专属禁用全集
- 照相机、镰刀完整条件链（亡语细则、复杂目标限制等）

## 测试

```bash
npm test
```

- rules.md 样例：20 个
- 扩展边界测试：98 个（持续按 rules.md 补齐）
