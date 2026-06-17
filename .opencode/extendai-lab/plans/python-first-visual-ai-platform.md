# Python-First Visual AI Programming Platform Plan
## Domain Classification
Software Engineering
## Plan Name
`python-first-visual-ai-platform`
## Intended Save Targets
- Root mirror: `PYTHON_FIRST_VISUAL_AI_PLATFORM_PLAN.md`
- Canonical plan: `.opencode/extendai-lab/plans/python-first-visual-ai-platform.md`
## TL;DR
构建一个 **Python-first 的可视化 AI 编程平台**，核心不是"再做一个低代码工作流工具"，而是做一个 **Python ↔ Graph 双向可编辑系统**：
- 人类主要看图、拖图、改图。
- AI 主要读 Python、写 Python、改 Python。
- 平台用 `graph-ai.json` 作为中间 IR。
- 首版只支持 **受限 Python 子集**，不承诺"任意 Python"都能完美反渲染。
- 不使用 Qt，不以 GPL/AGPL/许可证不明项目为代码基础。
- 参考已有仓库，但 **核心逻辑自行实现**。
---
## Why This Project
目标不是做一个"像扣子 / Flowise / ComfyUI"的节点编排器，而是做一个具有明确技术壁垒的系统：
1. **Python 作为 AI 母语**：模型对 Python 理解最好。
2. **图形作为人类母语**：非程序员更容易理解图。
3. **反向渲染是壁垒**：`AI写Python → 图` 这一步比普通拖拽工作流更难，也更有差异化。
4. **商业空间更大**：新手编程、AI 协作编程、自动化流程、教学和半专业用户都能覆盖。
---
## Product Scope
### In Scope
- Python 子集到图的反向渲染
- 图到 Python 的正向生成
- 节点编辑器
- 代码视图 / 图视图双视图
- AI 编辑链路
- 运行时执行与调试预览
- 初学者友好 UI 和安全约束
### Out of Scope for MVP
- 任意 Python 全量支持
- 原生桌面 Qt 客户端
- 插件市场 / Agent 市场
- 多语言支持
- 企业部署能力
- 完整的多人协作
---
## Reference Repositories and Roles
### Primary Reference Repos
- `C:\Users\BOHUYE~1\AppData\Local\Temp\opencode\GraPy`
  - 角色：**graph ↔ code**、嵌套 Python、运行时与 AI 编程体验参考
  - 协议：MIT
  - 备注：方向最接近，但前端源码暴露不完整，不能直接当底座
- `C:\Users\BOHUYE~1\AppData\Local\Temp\opencode\nodezator`
  - 角色：**Python-native 节点编辑器**、node pack 机制、导出 Python 参考
  - 协议：Unlicense
  - 备注：适合借"Python 节点组织思想"，不适合直接做现代 Web 产品 UI
- `C:\Users\BOHUYE~1\AppData\Local\Temp\opencode\py2blocks`
  - 角色：**Python AST → Blockly JSON** 反向解析参考
  - 协议：Apache-2.0
  - 备注：体量小但方向最准，适合当反向渲染内核样本
### Secondary Reference Repos
- `C:\Users\BOHUYE~1\AppData\Local\Temp\opencode\PyFlow`
  - 角色：节点框架、逻辑/UI 分离、子图和导入导出参考
  - 协议：Apache-2.0
- `C:\Users\BOHUYE~1\AppData\Local\Temp\opencode\blockpy`
  - 角色：Blockly/Python 新手交互参考
  - 协议：仓库元数据显示 Apache-2.0，但 `package.json` 写 ISC，**代码复用前必须人工复核**
  - 备注：只看 UX，不看底座
- `C:\Users\BOHUYE~1\AppData\Local\Temp\opencode\langflow`
  - 角色：大规模 Web 平台工程分层、组件化、API、部署参考
  - 协议：MIT
  - 备注：不作为主底座，只借工程组织思路
### Explicitly Excluded as Code Base
- GPL / AGPL / 许可证不明项目
- Qt 技术栈
- 纯 ComfyUI 式工作流平台思路
---
## Recommended Technical Direction
### Recommended Approach
**Self-built Python core + Web frontend**
- **Backend is the source of truth**
  - Python parser
  - Python normalizer
  - IR transformer
  - Python code generator
  - runtime executor
- **Frontend is the editor surface**
  - Graph canvas
  - Property panel
  - Code viewer/editor
  - Run/debug UI
### Rejected Alternatives
1. **Fork GraPy**
   - 问题：前端和核心转换层耦合高，且你已经对现状有不满。
2. **Fork Nodezator**
   - 问题：Python-native 很好，但 pygame UI 不适合你要的产品感。
3. **Fork PyFlow**
   - 问题：Qt 直接排除。
4. **Blockly-first product**
   - 问题：太偏教学，难以承载你要的 AI 编程闭环。
---
## Architecture
### Core Principle
**Python owns semantics. Graph owns interaction. IR owns conversion.**
### System Layers
1. **Parsing Layer**
   - Python source → AST / LibCST
   - 保留结构、注释、位置、格式信息
2. **Normalization Layer**
   - 把 AI 返回的任意 Python 规范化成平台支持子集
   - 复杂结构降级为 `CodeBlockNode`
3. **IR Layer**
   - `graph-ai.json`
   - 统一承载图结构、节点元数据、布局、源码映射
4. **Generation Layer**
   - Graph IR → canonical Python
   - 保证导出代码可运行、可读、可再次被解析
5. **Runtime Layer**
   - 安全执行
   - 节点状态
   - 变量作用域
   - 调试/回放
6. **UI Layer**
   - 图编辑器
   - 节点面板
   - 代码视图
   - 运行面板
   - AI 助手面板
---
## IR Specification Direction
### Canonical IR
`graph-ai.json`
### IR Must Separate
- **logic**：节点、边、控制流、变量、作用域
- **view**：坐标、折叠、主题、颜色、分组
- **sourceMap**：节点 ↔ Python 行列位置
- **metadata**：版本、项目、语言子集、导出信息
### Minimum Node Categories
- control: `if`, `for`, `while`, `break`, `continue`, `return`
- structure: `function`, `class`, `module`
- action: `assign`, `expr`, `call`
- data: `literal`, `name`, `attribute`
- escape hatch: `CodeBlockNode`
---
## Supported Python Subset for MVP
### Must Support
- module-level statements
- `if / elif / else`
- `for`
- `while`
- function definition
- class definition
- variable assignment
- function call
- `return`
- `import` / `from import`
- simple attributes and literals
### May Support in Phase 2
- list/dict comprehensions
- `try / except`
- decorators
- async function
- generators
- context manager
### Must Defer
- metaprogramming
- dynamic monkey patching
- arbitrary eval/exec
- complex import side effects
- arbitrary runtime reflection as first-class graph nodes
---
## Repository Strategy in This Repo
### Recommended New Top-Level Project Directory
`graph_ai_platform/`
### Proposed Layout
```text
graph_ai_platform/
  README.md
  pyproject.toml
  apps/
    web/
  services/
    core/
    runtime/
  packages/
    graph_ir/
    parser/
    codegen/
    node_catalog/
  tests/
    fixtures/
    unit/
    integration/
    roundtrip/
  docs/
    architecture/
    ir/
    decisions/
```
### Why Not Reuse Root Directly
当前仓库已有 B.A.I.T. 相关内容。新项目应隔离在单独目录中，避免：
- 构建脚本互相污染
- 依赖冲突
- AI 代理误修改无关文件
---
## Frontend Recommendation
### Stack
- React
- TypeScript
- Vite
- React Flow
- Zustand
- Zod
- Monaco Editor
### Why Web Frontend
- 比 pygame 更现代、可主题化、适合新手
- 比 Qt 更适合商业化和迭代
- 更容易做嵌入式 AI 面板和文档化交互
### Important Note on "TS Go"
TypeScript Go / preview 只会改善：
- type-check
- IDE 响应
- build/check latency
它**不会单独解决**画布卡顿问题。真正影响流畅度的是：
- React Flow 渲染策略
- 节点状态粒度
- 自动布局算法
- large graph virtualization
- minimap / edges / selection update frequency
---
## UX Direction
目标用户是"新手也能用"，所以不是只把程序员工具做成图形界面，而是要加安全层。
### UX Principles
- 图是主视图，代码是辅助视图
- 新手模式默认隐藏复杂细节
- 复杂代码自动降级成 `CodeBlockNode`
- 所有 AI 生成内容都可以被定位到节点
- 节点 palette 语言要简单、可教学
- 每个节点有输入输出说明和示例
### Modes
- **Beginner Mode**
  - 限制节点种类
  - 只允许安全 Python 子集
- **Advanced Mode**
  - 开放更多节点
  - 显示源码映射和更多调试面板
- **AI Mode**
  - 从需求生成图
  - 从代码恢复图
  - 局部图 patch
---
## Execution Strategy
## Wave 0 — Project Framing
### Task 0.1 — Create ADR and Scope Freeze
- What
  - 写清项目边界、协议红线、Python 子集边界
- Must NOT
  - 不开始写 UI
- Recommended Agent
  - Main implementation agent
- Acceptance Criteria
  - `docs/architecture/overview.md`
  - `docs/decisions/license-boundaries.md`
- QA
  - 检查是否写明不能复用 GPL/AGPL/许可证不明代码
### Task 0.2 — Create reference audit
- What
  - 为 6 个参考仓库写审计摘要
- Must NOT
  - 不复制源码
- Acceptance Criteria
  - `docs/architecture/reference-repos.md`
- QA
  - 每个仓库都有：定位、协议、可借内容、禁借内容
---
## Wave 1 — IR and Parser Foundation
### Task 1.1 — Define `graph-ai.json`
- What
  - 定义 schema、versioning、logic/view/sourceMap 分层
- Dependencies
  - none
- Acceptance Criteria
  - `packages/graph_ir/schema.json`
  - 3 个 fixture 样例
- QA
  - schema 校验可通过
  - fixture 可 round-trip 读写
### Task 1.2 — Build Python subset fixtures
- What
  - 建 30 段固定样例代码
- Acceptance Criteria
  - `tests/fixtures/python_subset/`
- QA
  - 样例覆盖 `if/for/function/class/import/call`
### Task 1.3 — Build parser prototype
- What
  - `Python → AST/LibCST → graph-ai.json`
- Acceptance Criteria
  - 至少支持 5 类基础结构
- QA
  - 单测覆盖率高于 80%
  - 失败时输出 `CodeBlockNode` 而不是崩溃
---
## Wave 2 — Code Generation and Roundtrip
### Task 2.1 — Build code generator
- What
  - `graph-ai.json → canonical Python`
- Dependencies
  - IR schema
- Acceptance Criteria
  - 生成代码可运行
- QA
  - 对 fixture 逐个执行 smoke test
### Task 2.2 — Roundtrip benchmark
- What
  - `Python → Graph → Python`
- Acceptance Criteria
  - 建立 roundtrip 成功率报告
- QA
  - 统计成功率、降级率、结构丢失点
  - MVP 目标：`70%+`
---
## Wave 3 — Node Catalog and Runtime
### Task 3.1 — Build node catalog
- What
  - 每个节点定义输入、输出、AST signature、UI label
- Acceptance Criteria
  - `packages/node_catalog/`
- QA
  - 节点与 parser / generator 双向映射一致
### Task 3.2 — Build runtime executor
- What
  - 节点执行、状态回传、变量作用域
- Acceptance Criteria
  - 能运行基础 graph
- QA
  - 调试时能查看每节点输入输出
  - 错误节点可定位
---
## Wave 4 — Web Editor MVP
### Task 4.1 — Canvas and node editor
- What
  - React Flow 画布、节点拖拽、连接、属性面板
- Acceptance Criteria
  - 能编辑 5 类基础节点
- QA
  - 100 节点内交互流畅
  - 保存/加载 graph 正常
### Task 4.2 — Dual view
- What
  - 图视图 + 代码视图
- Acceptance Criteria
  - 节点选中时能高亮对应代码
- QA
  - sourceMap 生效
  - 双向跳转正常
### Task 4.3 — Beginner UX
- What
  - 新手友好 palette、提示、示例
- Acceptance Criteria
  - 初学者可以拖出一个可运行例子
- QA
  - 不暴露过多内部字段
  - 文案不使用纯专家术语
---
## Wave 5 — AI Editing Protocol
### Task 5.1 — Define AI contract
- What
  - 约束 AI 输出格式：canonical Python 或 IR patch
- Acceptance Criteria
  - `docs/ir/ai-edit-contract.md`
- QA
  - AI 输出失败时可回退
  - patch 有校验
### Task 5.2 — Normalization service
- What
  - 规范化 AI 返回代码，提升反解析成功率
- Acceptance Criteria
  - 复杂代码能降级、不能炸
- QA
  - AI 生成样例的反解析成功率高于 raw 模式
---
## Wave 6 — Hardening and Delivery
### Task 6.1 — Performance
- What
  - 节点渲染优化、布局缓存、延迟计算
- Acceptance Criteria
  - 中型图编辑不卡顿
- QA
  - profile 报告
  - 关键渲染热点定位完毕
### Task 6.2 — Packaging
- What
  - 本地运行、一键启动、开发说明
- Acceptance Criteria
  - `README` + dev setup 完整
- QA
  - 新环境可启动
### Task 6.3 — Handoff pack
- What
  - 交接给其他 AI 的上下文包
- Acceptance Criteria
  - 关键路径、架构图、规则文档齐全
- QA
  - 不需要再回头问"项目到底要做什么"
---
## Parallelization Matrix
### Can Run in Parallel
- Wave 1.1 IR schema
- Wave 1.2 fixture construction
- reference repo audit
### Parallel After IR Freeze
- parser
- code generator
- node catalog
### Parallel After Core Works
- runtime
- web editor
- beginner UX
### Must Wait
- AI protocol should wait until parser/generator are stable
- performance tuning should wait until editor MVP exists
---
## Testing Strategy
### Unit Tests
- AST to IR mapping
- IR to Python generation
- schema validation
- node catalog validation
### Integration Tests
- parse → render → edit → generate
- code view ↔ graph view sync
- runtime state flow
### End-to-End Tests
- load fixture → show graph → modify node → export code → execute
- AI returns Python → normalize → parse → render
### Benchmark Suite
- 30 curated Python fixtures
- 10 AI-generated snippets
- 3 long nested examples
---
## Risk Register
### Risk 1 -- "Support all Python" trap
- Mitigation
  - Freeze subset early
  - Add `CodeBlockNode` escape hatch
### Risk 2 — UI-first distraction
- Mitigation
  - IR and parser before visual polish
### Risk 3 — License contamination
- Mitigation
  - No code copy from GPL/AGPL/NOASSERTION
  - BlockPy manual recheck before any reuse
### Risk 4 — Graph fidelity illusion
- Mitigation
  - Track measurable roundtrip success rate
  - Allow partial fidelity with explicit fallback
### Risk 5 — Performance blame on TypeScript
- Mitigation
  - Benchmark render pipeline, not compiler mythology
---
## Definition of Done for MVP
MVP is done when:
- `graph-ai.json` schema is frozen
- Python subset parser exists
- graph → Python generator exists
- roundtrip success rate reaches `70%+`
- web editor can edit/load/save/run basic graphs
- AI-generated Python can be normalized and rendered
- docs are sufficient for another AI or developer to continue without extra clarification
---
## Explicit Instructions for the Next AI
1. Do **not** start by redesigning the UI.
2. Do **not** start by integrating every reference repo.
3. Do **not** promise full Python support.
4. Start with:
   - IR schema
   - parser
   - generator
   - fixtures
5. Use reference repos for patterns only.
6. Treat `GraPy` as concept reference, not fork base.
7. Treat `py2blocks` as reverse-parser inspiration.
8. Treat `Nodezator` as Python-node modeling inspiration.
9. Keep everything under a new isolated top-level project directory.
10. Prefer correctness and handoff clarity over visual completeness.
---
## Final Recommendation
The best path is:
- **Own the core logic**
- **Use Python as the semantic core**
- **Use Web UI as the product surface**
- **Use IR as the long-term platform standard**
This is the highest-probability route to a product that is:
- Python-first
- AI-friendly
- novice-friendly
- commercially flexible
- not trapped by Qt or low-code workflow clones
