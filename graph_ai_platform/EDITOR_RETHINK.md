# PyGraph 节点编辑器 — 架构反思与 Rete.js 方案

## 当前 React Flow 实现的根本问题

### 1. 扁平图 vs 层次结构
Python 代码是**嵌套层次结构**：
```
function_def(greet) 
  └─ return
function_def(factorial)
  ├─ if (n < 0) → return -1
  ├─ if (n==0 or n==1) → return 1
  ├─ assign result = 1
  ├─ assign i = 2
  ├─ while (i <= n)
  │    ├─ assign result = result * i
  │    └─ assign i = i + 1
  └─ return result
```

但我们的渲染是 **15 个扁平的方块散落在画布上**。没有容器包含关系，控制流（if 的 body 在哪里？while 的 body 在哪里？）完全不可见。

### 2. 只有数据流，没有控制流
Python 有两套"流"：
- **数据流**：`x + 1` → `y = ...`（表达式之间传值）
- **控制流**：`if test:` → body 语句 → else 语句（执行顺序）

我们的边目前只尝试做了数据流（不完整），控制流完全缺失。

### 3. 单边编辑器 vs 函数式编辑器
一个真正的可视化编程编辑器需要：
- **Socket 类型匹配**：数字不能连到字符串上
- **节点创建/删除**：用户自己加节点
- **自动布局**：dagre/ELK 算法
- **撤销/重做**：操作历史
- **容器节点**：if 里面能放子节点

## Rete.js 的架构如何解决这些问题

### Rete.js 核心概念

```
NodeEditor (画布)
├── Node (节点)
│   ├── Control (UI控件: 输入框/下拉/滑块)
│   ├── Input (输入socket: 带类型)
│   └── Output (输出socket: 带类型)
├── Connection (连线: 连接output→input)
└── Plugins
    ├── AreaPlugin (画布缩放/平移)
    ├── ConnectionPlugin (交互式连线)
    ├── ReactPlugin (React渲染)
    ├── AutoArrangePlugin (自动布局)
    ├── HistoryPlugin (撤销/重做)
    └── ...
```

### 对我们 Python 场景的映射

| Python 语法 | Rete 节点 | Socket 设计 |
|-------------|----------|------------|
| `42` (字面量) | LiteralNode | output: value (int/str/bool) |
| `x` (变量) | NameNode | input: (无), output: value |
| `x + 1` (运算) | BinOpNode | input: left, right; output: result |
| `x = expr` (赋值) | AssignNode | input: value |
| `if test: body else: orelse` | IfNode | input: test; container: body[], orelse[] |
| `for i in iter: body` | ForNode | input: target, iter; container: body[] |
| `while test: body` | WhileNode | input: test; container: body[] |
| `def fn(args): body` | FunctionNode | input: arg_0...; container: body[] |
| `return expr` | ReturnNode | input: value |
| `import math` | ImportNode | output: module |

### 容器（Container）是关键
Rete 的 `ClassicPreset.Node` 原生不支持容器嵌套，但是：
- 可以用 `@retejs/scopes-plugin` 做作用域/容器管理
- 或者用 Node 的 `parent` 属性实现层次结构
- 或者自定义渲染 + 布局算法来模拟

**Blockly 做容器更自然**：拼图块天然地"套在一起"，if 的 body 块直接卡在 if 块的凹槽里。

## 建议方案

经过研究，我认为 **不应该继续在 React Flow 上修补**，而是：

### 方案 A: Rete.js（推荐）
```
优势：专业可视化编程框架，Socket 类型/自动布局/插件体系
集成方式：npm install rete rete-area-plugin rete-react-plugin rete-connection-plugin
工作流：
  Code(CodeMirror) → parse → Rete Editor Graph → generate → Code(CodeMirror)
劣势：学习成本，容器嵌套需要额外插件
```

### 方案 B: Blockly（如果你的"拼图块"偏好更强）
```
优势：Google 维护，拼图块视觉最自然，Python 代码生成器内置
劣势：非 React 原生，不适合自由画布/DAG
集成方式：react-blockly 或 iframe
```

### 方案 C: 深度改造 React Flow
```
优势：已集成
劣势：需要自己实现 socket 类型系统、容器嵌套、撤销/重做、自动布局
      相当于重新实现 Rete.js 的功能
```

## 我建议的下一步

1. 安装 Rete.js + React 插件
2. 定义 PyGraph 的节点类型（映射上面的 Python 类型）
3. 搭建 Parse → Rete Graph 的桥梁
4. 搭建 Rete Graph → Codegen 的桥梁
5. 实现 CodeMirror ↔ Rete 双向同步
6. 加上自动布局（dagre）

你觉得这个方向对吗？还是你更倾向保持 React Flow 深度改造？
