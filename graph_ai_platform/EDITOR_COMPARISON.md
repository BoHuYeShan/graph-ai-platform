# 节点编辑器方案对比 — PyGraph

## 候选方案总览

| 特性 | React Flow (当前) | Blockly (Google) | Rete.js | Node-RED |
|------|:---:|:---:|:---:|:---:|
| **拼图块风格** | ❌ | ✅ 核心风格 | ❌ | ❌ |
| **React 原生** | ✅ | ⚠️ react-blockly 桥接 | ✅ (v2) | ❌ (JS/jQuery) |
| **代码生成** | ❌ 需自己写 | ✅ 多语言内置 | ⚠️ 需自定义 | ❌ |
| **部署体积** | ~35KB gzip | ~200KB gzip | ~80KB gzip | ~400KB |
| **蓝图画布** | ✅ | ❌ 垂直堆叠为主 | ✅ 自由画布 | ✅ 自由画布 |
| **撤销/重做** | ⚠️ 需自己加 | ✅ | ✅ | ✅ |
| **连线类型** | ✅ 任意连线 | ❌ 严格类型匹配 | ✅ Socket配对 | ✅ 任意连线 |
| **社区生态** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **维护方** | xyflow (活跃) | Google (稳定) | Vitaliy Stoliarov | OpenJS Foundation |

## 详细分析

### 1. React Flow (当前栈) — 推荐指数：⭐⭐⭐
- **优点**：已经集成，TS友好，画布操作成熟（缩放/平移/ minimap）
- **缺点**：缺「拼图块」视觉风格，连线无类型校验，撤销/粘贴要自己实现
- **改造方向**：用自定义节点模拟拼图块外观 + 自定义 ConnectionLine + 接入 `@react-flow/undo`
- **适合**：如果你愿意花时间打磨 UI 细节

### 2. Blockly (Google) — 推荐指数：⭐⭐⭐⭐⭐
- **优点**：真正的拼图块，凸起/凹陷接口，视觉不可连错，Python/JS/Lua 代码生成器内置
- **缺点**：非 React 原生，垂直堆叠为主（不适合 DAG/自由画布），大包体积
- **集成方案**：`react-blockly` 或 iframe 嵌入
- **适合**：如果「拼图块体验」是核心需求

### 3. Rete.js — 推荐指数：⭐⭐⭐⭐
- **优点**：专为可视化编程设计，声明式节点定义，Socket 类型匹配，支持 React/Vue
- **缺点**：学习曲线，文档偏少，自定义渲染有坑
- **集成方案**：npm 包直接引入
- **适合**：需要「专业节点编辑器」且愿意投入学习

### 4. Node-RED — 推荐指数：⭐⭐⭐
- **优点**：流式编程，事件驱动，大量现成节点
- **缺点**：非 React，嵌入较麻烦，风格偏 IoT/自动化
- **适合**：如果你的场景偏「数据流管道」

## 建议评估路径

1. **快速试 Rete.js** — 它最容易和 React 结合，先看能否满足「拼图+连线」双重需求
2. **如果 Rete 不行 → Blockly** — 拼图块体验最好，iframe 嵌入成本可接受
3. **如果以上都太笨重 → 深度改造 React Flow** — 增加 `react-flow-undo`、自定义节点形状、连接线类型校验

## Demo 快速验证

要快速看效果：
- **React Flow**：已运行在 `localhost:5173`
- **Blockly**：可以看 playground → https://blockly-demo.appspot.com/
- **Rete.js**：可以看示例 → https://rete.js.org/#/examples/basic
- **Node-RED**：可以看示例 → https://nodered.org/docs/user-guide/editor
