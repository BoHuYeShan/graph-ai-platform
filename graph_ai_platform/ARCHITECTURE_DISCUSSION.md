# PyGraph 多文件 / 多画布 / Debug 架构设计（讨论稿）

> **决策记录**：2026-06-17 确认
> - 多文件：子画布（A4纸）放在无限画布上
> - Debug：前后端同步做
> - 双视图：切换模式（蓝图↔拼图块）

## 1. 核心问题：Python ≠ 单文件

真实 Python 项目是多文件的：
```
project/
├── main.py          # 入口
├── utils.py         # 工具函数
├── models/
│   ├── __init__.py
│   └── user.py
└── config.py
```

节点编辑器如何表达这种结构？

## 2. 多画布方案（已确认）

### 确定方案：无限桌面 + 子画布（A4 纸模型）

```
┌─ 无限画布（桌面）──────────────────────────────────────┐
│                                                        │
│  ┌────────────────────────┐   ┌──────────────────────┐ │
│  │ 📄 main.py             │   │ 📄 utils.py          │ │
│  │  ┌─── function greet ─┐│   │  ┌─── function parse┐│ │
│  │  │ [return "hello"]   ││   │  │ [json.loads]     ││ │
│  │  └────────────────────┘│   │  └──────────────────┘│ │
│  │  ┌─── call greet ─────┐│   │                      │ │
│  │  │ [print result]     ││   │                      │ │
│  │  └────────────────────┘│   └──────────────────────┘ │
│  └────────────────────────┘                             │
│                    │ import                               │
│                    ↓                                     │
│  ┌────────────────────────┐                             │
│  │ 📄 models/user.py      │                             │
│  │  ┌─── class User ────┐│                             │
│  │  │ [name, email]     ││                             │
│  │  └───────────────────┘│                             │
│  └────────────────────────┘                             │
│                                                        │
│  [+ 新建文件]                                        │
└────────────────────────────────────────────────────────┘
```

**关键设计点**：

| 特性 | 实现方式 |
|------|---------|
| 子画布本质 | 一个带标题的矩形容器，内部是一个独立的 dagre/Rete 图 |
| 子画布移动 | 拖拽标题栏，内部所有节点跟随移动（React Flow parent 容器） |
| 子画布缩放 | 不影响内部节点大小，只改变容器在桌面上的缩放 |
| 文件树 | 左侧折叠面板，点击文件→聚焦到对应子画布 |
| 跨文件调用 | `import` 节点 + 跨子画布的可见连线 |
| 创建新文件 | 右下角 [+] 按钮，弹出命名对话框，生成空白子画布 |

**参考产品**：
- **Miro / Figma**：无限画布 + 可拖动矩形区域
- **Excalidraw**：自由画布 + 分组
- **Unreal Blueprint**：每个 Blueprint 一个编辑页，但可引用其他 Blueprint

## 3. 跨文件导入机制（更新）

基于子画布模型，跨文件导入用**可见连线**表示：

```
┌─ main.py 子画布 ───────────┐
│  ┌── import utils ──────┐  │
│  │  从 utils.json       │──┼──→ 连线到 utils.py 子画布
│  │  导入: parse         │  │        ↑
│  └───────────────────────┘  │        │ 跨画布边
│       ↓                      │        │
│  ┌── call parse ─────────┐  │        │
│  │  data = parse(text)   │  │        │
│  └───────────────────────┘  │        │
└─────────────────────────────┘        │
                                       │
┌─ utils.py 子画布 ──────────┐         │
│  ┌── function parse ────┐  │ ←───────┘
│  │  ⚡ 导出端口         │  │   跨画布边
│  └───────────────────────┘  │
└─────────────────────────────┘
```

- 跨画布边用虚线+特殊颜色
- 点击可跳转到目标画布
- 导出端口在函数/类节点上显式标记「可导出」

## 4. Debug 模式（前后端同步做）

### 后端 Stepping API

```python
# services/runtime/__init__.py 新增
class SteppingRuntime:
    """
    单步执行器，每次执行一个节点后返回状态。
    
    Usage:
        rt = SteppingRuntime(graph)
        while not rt.done:
            state = rt.step()  # 执行一个节点
            # state = {currentNode, variables, done}
    """
    
    def __init__(self, graph):
        self.graph = graph
        self.executor = NodeExecutor(graph)
        self._node_order = self._topological_sort()
        self._pc = 0  # program counter
    
    def step(self) -> dict:
        if self._pc >= len(self._node_order):
            return {"done": True, "variables": dict(self.executor.variables)}
        node_id = self._node_order[self._pc]
        self._pc += 1
        self.executor.execute_node(node_id)
        return {
            "currentNode": node_id,
            "variables": dict(self.executor.variables),
            "done": self._pc >= len(self._node_order),
        }
    
    def run_to_end(self) -> dict:
        while not self._is_done():
            self.step()
        return {"done": True, "variables": dict(self.executor.variables)}
```

**后端新 API 端点**：

| 端点 | 方法 | 功能 |
|------|------|------|
| `/debug/start` | POST | 初始化 stepping，传入 IR |
| `/debug/step` | POST | 执行一步，返回当前节点+变量 |
| `/debug/stop` | POST | 终止调试 |

### 前端 Debug 界面

```
┌─ 图视图 (Debug 模式) ───────────────────────────┐
│                                                  │
│  ┌─ function_def: factorial ─────────────────┐  │
│  │                                            │  │
│  │  ┌─ assign: result=1 ──┐   ← 🔵 高亮    │  │
│  │  │  边框发光 + 呼吸动画 │                  │  │
│  │  └──────────────────────┘                  │  │
│  │       ↓                                    │  │
│  │  ┌─ while ──────────────┐                  │  │
│  │  │  test: n > 1         │                  │  │
│  │  │  [body]              │                  │  │
│  │  └──────────────────────┘                  │  │
│  └────────────────────────────────────────────┘  │
├─ Debug 工具栏 ────────────────────────────────────┤
│  [⏩ 继续] [⏭ 下一步] [↩ 步入] [↩↩ 步出]       │
│  步骤: 3/12                                       │
├─ 变量面板 ───────────────────────────────────────┤
│  n: 5                                             │
│  result: 1                                        │
│  i: 2                                             │
└──────────────────────────────────────────────────┘
```

### 前端实现计划

1. App 状态新增 `debugMode`, `debugState`
2. Toolbar 新增 Debug 控制按钮
3. GraphView 新增节点高亮（通过 `selected` 或自定义样式）
4. 新增 `VariablePanel` 组件（底部/右侧）
5. 新增 `/debug/start`, `/debug/step` API 调用

## 5. 双视图切换：蓝图 ↔ 拼图（已确认切换模式）

```
┌─ 视图切换 [🔀 蓝图 | 🧩 拼图] ─────────────────┐
│                                                    │
│  同一画布，切换渲染引擎                             │
│                                                    │
│  蓝图模式 (dagre):     拼图模式 (Rete.js/Blockly): │
│  ┌── A ──┐  ┌── B ──┐  ┌──────────────────┐       │
│  │  x+1  │→│ print │  │  [if n > 0]       │       │
│  └───────┘  └───────┘  │  ┌─ [return -1] ─┐│       │
│                         │  └───────────────┘│       │
│                         │  [while n > 1]    │       │
│                         │  ┌─ [result*=n] ─┐│       │
│                         │  └───────────────┘│       │
│                         └──────────────────┘       │
│                                                    │
│  切换时自动布局，保持节点不变，只换视觉风格        │
└────────────────────────────────────────────────────┘
```

**实现方式**：
- 同一份 IR 数据，两套渲染器
- 蓝图渲染器：当前 dagre + React Flow（已就绪）
- 拼图渲染器：Rete.js（待集成）
- 切换时：`viewMode = 'blueprint' | 'puzzle'`
- 切换保留节点位置（蓝图用 dagre 算，拼图用 Rete 算）

## 6. 实施路线图（根据你的决策更新）

```
Phase 0 (已完成)
├── 代码编辑器 + LSP + 自动布局 + Run 输出
├── dagre 容器节点

Phase 1 (下一步)
├── 单个子画布容器（把当前图包进一个可拖动的「A4纸」）
├── 文件树侧边栏（+ 新建文件）
├── 多子画布：每文件一个子画布，可拖动
├── 跨画布 import 连线

Phase 2
├── Debug 后端 SteppingRuntime
├── Debug 前端（高亮 + 变量面板 + 控制按钮）
├── 蓝/拼图切换按钮（先集成 Rete.js 预览）

Phase 3
├── 跨画布连线完整语义
├── 多画布布局记忆
├── 项目保存/加载
```
