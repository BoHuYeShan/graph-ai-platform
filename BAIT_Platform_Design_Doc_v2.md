---
AIGC: {"Label":"1","ContentProducer":"001191110108MA01KP2T5U00000","ProduceID":"5509c96c8a398368b6e35fb8e9c2f5e5","ReservedCode1":"","ContentPropagator":"001191110108MA01KP2T5U00000","PropagateID":"5509c96c8a398368b6e35fb8e9c2f5e5","ReservedCode2":""}
---

# B.A.I.T. 平台完整设计文档 v2

> **Bureau of Advanced Interdisciplinary Theories**
> "bait" = 诱饵 / 钓鱼 — 跨维度学术模仿秀平台的完整技术设计方案
> 主站宇宙：R.E.E.F. — Research Encyclopedia of Emerging Frontiers

---

## 目录

1. [项目概述](#1-项目概述)
2. [命名体系](#2-命名体系)
3. [R.E.E.F. 编年史](#3-reef-编年史)
4. [内容边界与安全策略](#4-内容边界与安全策略)
5. [多宇宙架构](#5-多宇宙架构)
6. [分级系统与跨站点映射](#6-分级系统与跨站点映射)
7. [钓鱼审稿系统](#7-钓鱼审稿系统)
8. [B.I. 诱饵指数评估体系](#8-bi-诱饵指数评估体系)
9. [平台架构](#9-平台架构)
10. [多入口系统](#10-多入口系统)
11. [投稿与审稿工作流](#11-投稿与审稿工作流)
12. [真实论文引用策略](#12-真实论文引用策略)
13. [AI 补稿与宇宙内容填充](#13-ai-补稿与宇宙内容填充)
14. [内容展示格式](#14-内容展示格式)
15. [终端模拟系统](#15-终端模拟系统)
16. [双向页面链接系统](#16-双向页面链接系统)
17. [线索与 ARG 解谜系统](#17-线索与-arg-解谜系统)
18. [子页面揭示机制](#18-子页面揭示机制)
19. [防翻译防御体系](#19-防翻译防御体系)
20. [移动端与 PC 端差异化体验](#20-移动端与-pc-端差异化体验)
21. [URL 参数系统](#21-url-参数系统)
22. [成就系统](#22-成就系统)
23. [钓客日志与 Fish Score](#23-钓客日志与-fish-score)
24. [ISSN 七击彩蛋](#24-issn-七击彩蛋)
25. [PDF 水印系统](#25-pdf-水印系统)
26. [内部 Prompt 模板系统](#26-内部-prompt-模板系统)
27. [社区投稿收集机制](#27-社区投稿收集机制)
28. [社区治理模型](#28-社区治理模型)
29. [配套脚本与工具链](#29-配套脚本与工具链)
30. [SEO 策略](#30-seo-策略)
31. [内容策略](#31-内容策略)
32. [虚构学术身份体系](#32-虚构学术身份体系)
33. [法律与伦理框架](#33-法律与伦理框架)
34. [后端预留与扩展](#34-后端预留与扩展)
35. [实施路线图](#35-实施路线图)
36. [附录：术语表](#附录术语表)

---

## 1. 项目概述

### 1.1 核心理念

B.A.I.T.（Bureau of Advanced Interdisciplinary Theories）是一个模仿正规学术出版机构的恶搞/戏仿平台，目标受众为中国互联网上的"民科"群体——那些缺乏正规学术训练、热衷于发表"颠覆性理论"却对学术出版规范了解甚少的人群。平台名称本身即为核心隐喻："bait"意为诱饵/钓鱼，暗示整个平台就是一个精心设计的"学术钓鱼"场景。

平台的运作模式类似于"楚门的世界"：目标受众（民科）会认为这是一个真实的、权威的国际学术出版机构，而具备足够辨识力的正常用户则可以通过嵌入的线索、ARG 谜题和隐藏内容，发现平台的真实性质。这种双层体验设计确保了平台既是讽刺艺术品，也是一个互动解谜游戏。

在 v2 架构中，平台从单纯的"钓鱼网站"升级为**跨维度虚构世界门户**。整个平台被设定为维度偏移数据的泄漏产物——B.A.I.T. 的"学术论文"实际上是 R.E.E.F. 系统捕获的跨维度数据，而民科投稿本质上是被系统归档的"基准现实维度偏移数据"。这种 meta 叙事将讽刺、解谜和社区共创统一在一个完整的世界观框架内。

### 1.2 设计哲学

- **沉浸优先**：对于目标受众，平台必须看起来与真实的学术出版网站无异，从视觉设计、术语使用到交互流程，都需要达到"以假乱真"的程度
- **线索渐进**：对于解谜者，线索的发现应当是渐进式的——从微妙的违和感，到明确的文化暗示，再到直接的揭示，形成一个完整的认知链
- **零收费原则**：平台绝不向任何用户收取任何费用，这是法律安全的核心底线
- **社区共创**：像 SCP 基金会和 Backrooms 那样，收集社区中有创意的投稿，让平台成为虚构世界的共同创作空间
- **多宇宙容纳**：每个民科/作者都可以拥有自己的独立宇宙，社区接力帮助完善，宇宙之间可以合并，最终被 R.E.E.F. 主站宇宙统一容纳

### 1.3 目标受众画像

**主要目标（鱼）**：
- 缺乏正规学术训练但热衷于"发表"理论的民科群体
- 大量依赖 AI 生成论文内容的人群
- 对学术出版流程不了解、容易被表面权威性吸引的人群
- 活跃于中文互联网，常使用浏览器翻译功能阅读英文内容

**次要受众（钓客）**：
- 对 ARG/解谜感兴趣的互联网用户
- 学术圈内的讽刺文化爱好者
- 编程/设计社区中欣赏这种创意的用户
- 虚构世界观共创爱好者（SCP/Backrooms 社区成员）

---

## 2. 命名体系

### 2.1 核心命名

| 层面 | 名称 | 学术门户展开 | 隐藏含义 |
|------|------|-------------|---------|
| 平台/期刊 | B.A.I.T. | Bureau of Advanced Interdisciplinary Theories | 诱饵/钓鱼 |
| 主站宇宙 | R.E.E.F. | Research Encyclopedia of Emerging Frontiers | 礁石——鱼群聚集地 |
| 文档标识 | D.I.O. | Document Identity Ontology | 意大利语"上帝" |
| 深渊层 | H.A.D.A.L. | Hidden Archive of Dimensional Anomalies & Leaks | 超深渊带（海洋最深处） |
| 维度偏移指数 | D.D.I. | Dimensional Deviation Index | 维度偏移 |
| 宇宙编号 | C.O.S.M.O.S. | Catalog of Systematic Models & Ontological Schemas | 宇宙 |

### 2.2 审稿流程命名

| 阶段 | 名称 | 学术门户展开 | 隐藏含义 |
|------|------|-------------|---------|
| 投稿提交 | C.A.S.T. | Committee for Academic Standards & Theory | 抛竿 |
| 审稿进行 | H.O.O.K. | Holistic Objective Observation Kernel | 上钩 |
| 审稿完成 | C.A.T.C.H. | Comprehensive Assessment & Theoretical Certification Hub | 收网 |
| 论文发布 | R.E.L.E.A.S.E. | Repository of Evaluated Literature & Exemplary Academic Studies Edition | 放生 |

### 2.3 辅助系统命名

| 系统 | 名称 | 学术门户展开 | 隐藏含义 |
|------|------|-------------|---------|
| 论文库 | F.I.S.H. | Formal Index of Scholarly Highlights | 鱼 |
| 发现者 | A.N.G.L.E.R. | Archived Network of Genuine Learning & Enlightenment Records | 钓客 |
| 追踪系统 | N.E.T. | Novel Epistemological Tracker | 网 |
| 推荐系统 | C.U.R.R.E.N.T. | Catalog of Unresolved Research & Emerging Novel Theories | 洋流 |
| 表面层 | S.U.R.F. | Systematic Unified Reference Framework | 浪花 |
| Wiki 系统 | K.E.L.P. | Knowledge Exchange & Lexicon Platform | 海带——礁石上的附着物 |
| 审稿记录 | P.E.A.R.L. | Peer Evaluation & Assessment Record Ledger | 珍珠——沙粒变成的宝物 |
| 宇宙索引 | C.O.R.A.L. | Catalog of Observed Research & Academic Lore | 珊瑚——礁石的构成单元 |

### 2.4 编号格式

| 对象 | 编号格式 | 示例 |
|------|---------|------|
| 论文 | `DIO:B.A.I.T.<YYYY>.<SEQ>` | `DIO:B.A.I.T.2025.0001` |
| 宇宙 | `COSMOS-<类别>-<序号>` | `COSMOS-CNS-001` |
| 异常报告 | `AR-<YYYY>-<SEQ>` | `AR-2025-0042` |
| 终端会话 | `TS-<宇宙代码>-<SEQ>` | `TS-YQC-007` |

宇宙类别代码：

| 代码 | 含义 | 代码 | 含义 |
|------|------|------|------|
| PHY | 物理类 | BIO | 生物类 |
| MAT | 数学类 | PHI | 哲学类 |
| CNS | 意识类 | INF | 信息/计算类 |
| COS | 宇宙学类 | MIX | 跨学科混合 |
| CHE | 化学类 | UNI | 统一宇宙（合并后） |

---

## 3. R.E.E.F. 编年史

### 3.1 概述

R.E.E.F. 的世界观历史是整个平台的叙事地基。历史只定框架和关键事件，具体细节由社区共创填充。每一段历史对应平台上不同类型和风格的内容，解释了为什么平台上有如此复杂的分层体系。

### 3.2 纪元一：发现期（The Discovery Era）

大约 10-15 年前。一个小型跨学科研究团队在实验中意外发现了"维度偏移"现象——某些实验数据不符合任何已知物理框架，但呈现出内在规律性。最初以为是设备故障，后来逐渐意识到这是"信息从其他维度泄漏"的证据。

**对应内容**：最早的 Δ-1 级论文，一批"异常数据"的原始记录，设备故障报告（后来被重新分类为维度泄漏事件）。

### 3.3 纪元二：建制期（The Foundation Era）

发现维度偏移后，研究团队意识到需要系统性地记录和分类这些异常。B.A.I.T. 正式成立（对外仍然伪装为普通学术出版机构），R.E.E.F. 系统开始建设，D.I.O. 标识体系被发明出来。C.A.S.T./H.O.O.K./C.A.T.C.H./R.E.L.E.A.S.E. 审稿流程被确立——表面上是学术同行评审，实际上是对维度偏移数据的捕获和分类流程。

**对应内容**：B.A.I.T. 的"建院文献"、第一批正式的 R 级异常报告、D.I.O. 系统的设计文档、早期编委会的内部通信。

### 3.4 纪元三：膨胀期（The Expansion Era）

随着 R.E.E.F. 系统的运行，越来越多的独立宇宙被发现。宇宙数量快速增长，宇宙合并事件开始出现。H.A.D.A.L. 深渊层被发现——某些数据深度偏移，接近"不可读"状态。F.I.S.H. 论文库、K.E.L.P. Wiki 系统、C.O.R.A.L. 宇宙索引相继建立。

**对应内容**：大量宇宙的建立、第一批终端会话记录、H.A.D.A.L. 层的初始数据、宇宙合并的历史记录。

### 3.5 纪元四：泄漏期（The Leak Era） ← 当前

维度泄漏率开始上升。越来越多的 R.E.E.F. 数据出现在"基准现实"的互联网上——这就是网站本身存在的原因。B.A.I.T. 对外发布的"学术论文"实际上是维度泄漏的副产品，而民科投稿本质上是被 R.E.E.F. 系统捕获的"来自基准现实维度偏移数据"。

**这是整个平台的 meta 叙事核心**：

- **对民科来说**：他们投稿的论文被"接受发表"，觉得自己得到了认可
- **对解谜者来说**：他们发现"投稿"实际上是"维度数据被 R.E.E.F. 系统捕获并分类的过程"
- **双重讽刺**：民科以为自己在参与学术，实际上他们是"异常数据源"；解谜者以为自己在解谜，实际上他们也是"数据"的一部分

**对应内容**：维度泄漏日志、泄漏期系统警告、当前所有论文和档案。

### 3.6 纪元五：？（社区定义）

未来的纪元由社区投票决定——可能是"收容期"（维度泄漏被控制）、"融合期"（基准现实与维度数据完全融合）、或"沉默期"（所有维度数据突然消失）。这是留给社区共创的开放叙事空间。

### 3.7 历史在平台中的体现

| 体现方式 | 说明 |
|---------|------|
| 时间线页面 | 档案库中的 R.E.E.F. 编年史 |
| 终端日志 | 不同纪元的系统日志风格不同（早期简单，近期复杂且带警告） |
| 论文风格演变 | 早期论文更"朴素"，近期论文更"精密"——这是刻意的设计选择 |
| Wiki 条目 | 历史事件有专门的 Wiki 页面，社区可以补充细节 |
| D.I.O. 编号规律 | 早期编号（2020-2022）对应发现期，中期对应膨胀期，当前对应泄漏期 |

---

## 4. 内容边界与安全策略

### 4.1 绝对禁区（任何情况下不可出现）

1. **政治敏感内容**：涉及中国政治体制、领导人、政策批评的任何内容
2. **邪教/极端主义内容**：任何可能被归类为邪教宣传或极端主义思想的内容
3. **医疗/健康建议**：任何可能被误读为医疗建议的内容
4. **种族/性别歧视内容**：任何形式的歧视性言论
5. **金融/投资建议**：任何可能被解读为投资建议的内容
6. **真实个人攻击**：针对真实存在的学术人物的诽谤或人身攻击
7. **儿童不当内容**：任何涉及未成年人的不当内容

### 4.2 安全主题领域

- **数学/几何**：宣称证明哥德巴赫猜想、发明新几何、推翻微积分
- **理论物理/宇宙学**：大统一理论、多维空间模型、暗物质替代解释
- **AI/计算理论**：宣称发明超越图灵机的计算模型、意识上传理论
- **哲学/认识论**：新的"万物理论"、重新定义时间/空间/因果关系
- **信息论/密码学**：宣称破解现有加密体系
- **进化论/古生物**（不涉及人类起源的种族敏感内容）
- **生物/化学**：虚构的生化机制、分子结构

### 4.3 内容安全审查原则

- **无害性测试**：如果这篇论文被一个完全不懂学术的人当真，是否会造成任何实际伤害？
- **可辨识性测试**：一个受过大学教育的正常人，能否在仔细阅读后识别出这是戏仿？
- **法律风险评估**：内容是否可能引发任何法律纠纷？
- **去人格化原则**：所有"作者"均使用虚构身份，绝不暗示指向真实个人

---

## 5. 多宇宙架构

### 5.1 核心概念

B.A.I.T. v2 的最大升级是从"单一钓鱼网站"进化为"多宇宙虚构世界门户"。每个在平台上"发表"的民科（或虚构作者），都可以拥有自己的独立宇宙。这个宇宙有自己的基础公理、推导出的理论体系、内部逻辑自洽性和专属术语。

R.E.E.F. 是所有独立宇宙的"交汇点"——主站宇宙，它的设定是：这些独立宇宙都是 R.E.E.F. 在不同参数条件下的投影/分支。R.E.E.F. 本身也有自己的核心设定和故事线，但它是开放框架，可以容纳所有独立宇宙。

### 5.2 独立宇宙

每个独立宇宙包含：

- **基础公理**：该宇宙的核心假设（如"意识是基本物理量"）
- **推导理论**：从公理推导出的理论体系
- **内部逻辑自洽性**：所有内容必须在公理框架内自洽
- **专属术语**：该宇宙独有的概念和符号
- **Wiki 百科**：术语词典、时间线、人物、机构
- **周边材料**：采访记录、实验日志、新闻、终端会话等

### 5.3 宇宙合并

如果两个独立宇宙的基础公理兼容（比如张三的"量子意识理论"和李四的"意识场理论"本质上说的是同一回事），可以通过社区投票将它们合并到同一个宇宙下。合并后的宇宙拥有更丰富的内容，两个作者的论文可以互相引用而不会出现逻辑矛盾。

**宇宙合并流程**：

1. 在 GitHub Discussions 发起合并提议
2. 讨论期（7 天）：社区讨论兼容性，原宇宙创建者发表意见
3. 投票（3 天）：GitHub Discussions 投票功能，简单多数通过，至少 5 票有效
4. 执行：维护者更新 Front Matter、重定向引用，原宇宙保留为"归档"状态

### 5.4 宇宙数据结构

```yaml
# content/cosmos/yang-quantum-consciousness/_index.md
---
cosmos_id: "COSMOS-CNS-001"
cosmos_name: "杨氏量子意识宇宙"
cosmos_short: "YQC"
founder: "Dr. Yang Wei"
status: "active"  # active / merged / archived
merged_into: null
era_origin: "expansion"  # 该宇宙被发现的纪元
ddi_range: [1, 3]  # 该宇宙内容的 DDI 范围
axioms:
  - "意识是基本物理量，与质量、电荷同等级"
  - "量子坍缩由观察者意识驱动"
  - "意识场可被量化为 Ψ(θ,φ,t) 函数"
derived_theories:
  - "意识纠缠定理"
  - "群体意识共振效应"
  - "跨维度意识传输协议"
linked_cosmos:
  - cosmos_id: "COSMOS-CNS-002"
    relation: "compatible"
    note: "李氏意识场理论，公理等价于 YQC 的推论3"
paper_count: 12
wiki_pages: 34
---
```

### 5.5 宇宙的 Wiki 系统

每个宇宙的 Wiki 是让该宇宙变得"层次严密"的关键。Wiki 条目之间通过双向链接互相引用，形成密集的知识网络。

**Wiki 内容类型**：

| 类型 | 说明 | 示例 |
|------|------|------|
| 术语词典 | 宇宙专属术语的"严谨"定义 | "Ψ 函数"、"意识坍缩临界值" |
| 时间线 | 宇宙内的"学术发展史" | "2019年杨伟首次提出量子意识假说" |
| 人物 | 宇宙内的研究员简介 | "杨伟博士——维度物理学部" |
| 机构 | 虚构研究机构介绍 | "MIT 意识物理学部" |
| 争议记录 | 宇宙内的"学术争议" | "杨伟学派 vs 李明学派" |
| 事件 | 宇宙内的重大事件 | "2024年维度泄漏事件" |

Wiki 的诡异之处在于：它在自己的框架内完全自洽，越深入阅读越觉得"这好像真的是一个学术领域"，但任何一个有真实学术背景的人都会在某个点意识到——这一切都是建立在一个荒谬的前提上的。

---

## 6. 分级系统与跨站点映射

### 6.1 统一内部分级

维护者内部使用一套统一的分级标识，这是"真实"的分类：

| 板块 | 分级 | 含义 |
|------|------|------|
| 论文 | FG-0 | Fun-0 纯搞笑，明显荒诞 |
| 论文 | FG-1 | Fun-1 需辨识，有一定伪装度 |
| 论文 | FG-2 | Fun-2 高度伪装，格式术语仿真 |
| 论文 | FG-3 | Fun-3 极致伪装，几乎无法区分 |
| 论文 | TG-1 | Truth-1 冷门真实，掩护性内容 |
| 论文 | TG-2 | Truth-2 有价值真实，信标内容 |
| 论文 | TG-3 | Truth-3 高质量真实，锚点内容 |
| 档案 | RG-0 | Record-0 异常已解决 |
| 档案 | RG-1 | Record-1 异常已收容 |
| 档案 | RG-2 | Record-2 异常活跃中 |
| 档案 | RG-3 | Record-3 异常未收容 |
| 日志 | LG-0 | Log-0 公开信息 |
| 日志 | LG-1 | Log-1 内部信息 |
| 日志 | LG-2 | Log-2 限制访问 |
| 日志 | LG-3 | Log-3 隔离/损坏数据 |

### 6.2 学术门户分级映射

民科看到的分级——完全的学术风格，等级越高看起来越厉害：

| 内部ID | 学术门户显示 | 外观 |
|--------|-------------|------|
| FG-0 | **Category A** — Original Contribution | 绿色标签 |
| FG-1 | **Category A+** — Significant Contribution | 蓝色标签 |
| FG-2 | **Category A++** — Major Contribution | 金色标签 |
| FG-3 | **Category S** — Landmark Contribution | 红色标签 |
| TG-1~3 | **Category B** — Standard Publication | 灰色标签 |

注意：FG 级别在学术门户里等级越高看起来越厉害，FG-3 变成了"里程碑级贡献"——这对民科来说是终极认可，但实际上是最高级别的"钓鱼"。RG/LG 内容在学术门户完全不出现。

### 6.3 档案库分级映射

解谜者/社区用户看到的分级——科幻/异常分类风格：

| 内部ID | 档案库显示 | 颜色 |
|--------|----------|------|
| FG-0 | Δ-0 BASELINE ANOMALY | 蓝色 |
| FG-1 | Δ-1 MINOR DEVIATION | 黄色 |
| FG-2 | Δ-2 SIGNIFICANT DEVIATION | 橙色 |
| FG-3 | Δ-3 CRITICAL DEVIATION | 红色 |
| TG-1~3 | Σ STANDARD | 白色 |
| RG-0 | R-0 RESOLVED | 绿色 |
| RG-1 | R-1 CONTAINED | 蓝色 |
| RG-2 | R-2 ACTIVE | 橙色 |
| RG-3 | R-3 UNCONTAINED | 红色 |
| LG-0 | L-0 PUBLIC | 白色 |
| LG-1 | L-1 INTERNAL | 蓝色 |
| LG-2 | L-2 RESTRICTED | 橙色 |
| LG-3 | L-3 QUARANTINED | 红色 |

### 6.4 终端分级映射

终端里看到的分级——纯编号，军事/机构风格：

| 内部ID | 终端显示 |
|--------|---------|
| FG-0 | `DOC::TYPE-A-0` |
| FG-1 | `DOC::TYPE-A-1` |
| FG-2 | `DOC::TYPE-A-2` |
| FG-3 | `DOC::TYPE-S` |
| TG-1~3 | `DOC::TYPE-B` |
| RG-0~3 | `REC::SEC-n` (n=0-3) |
| LG-0~3 | `LOG::CLR-n` (n=0-3) |

### 6.5 维度偏移指数 (D.D.I.)

三个板块共享一个顶层指标——维度偏移指数 (Dimensional Deviation Index)，衡量内容与"基准现实"的偏离程度：

| DDI | 颜色 | 含义 |
|-----|------|------|
| 0 | 白色 | 与现实一致 |
| 1 | 蓝色 | 微偏，可解释为学术差异 |
| 2 | 黄色 | 中偏，无法用已知框架解释 |
| 3 | 橙色 | 重偏，暗示维度差异 |
| 4 | 红色 | 极偏，维度特有 |
| 5 | 黑色 | 未知，无法评估 |

### 6.6 分级映射的 ARG 功能

三种分级体系指向同一篇论文但名字完全不同，这种换算关系本身就是 ARG 线索。如果有人在终端里看到 `DOC::TYPE-S`，然后去学术门户看，发现标记为"Category S — Landmark Contribution"，再去看档案库，发现是"Δ-3 CRITICAL DEVIATION"——三种完全不同的名字指向同一篇论文，这种认知冲击就是"楚门的世界"被揭穿的时刻。

换算表可以做成一张隐藏的可解锁图表，或让用户在探索中逐步发现映射关系。序列号（如 2025-0001）在三个入口中保持一致，但前缀完全不同——只有对比多入口后才能发现规律。

---

## 7. 钓鱼审稿系统

### 7.1 四阶段流程

| 阶段 | 钓鱼术语 | 外部学术术语 | 内部含义 | 用户可见状态 |
|------|---------|-------------|---------|-------------|
| 1 | 抛竿 (Cast) | Submitted | 诱饵已放出 | "Your manuscript has been received" |
| 2 | 上钩 (Hook) | Under Review | 目标已上钩 | "Your manuscript is under peer review" |
| 3 | 收网 (Catch) | Accepted | 确认上钩 | "Congratulations! Accepted for publication" |
| 4 | 放生 (Release) | Published | 论文公开 | "Your paper is now publicly available" |

### 7.2 审稿状态页面设计

与真实学术出版平台（ScholarOne、Editorial Manager）高度相似：
- 进度条和百分比显示
- 匿名审稿人编号
- 预计完成日期（所有论文都会"通过"，时间只是道具）
- 状态变更时间线

### 7.3 审稿意见生成

每篇论文的"审稿意见"由内部 Prompt 系统自动生成：
- 正式学术英语，以正面评价为主
- 建议均为表面性格式调整，绝不触及核心逻辑
- 在正面评价中嵌入微妙暗示（"The authors' novel approach to proving P=NP through dream analysis represents a paradigm shift..."）

---

## 8. B.I. 诱饵指数评估体系

### 8.1 五维评估模型

| 维度 | 英文名 | 评估内容 | 满分 |
|------|--------|---------|------|
| 语法 (Syntax) | Syntactic Coherence | 语法正确性和学术规范性 | 20 |
| 密度 (Density) | Terminological Density | 专业术语的密度和分布 | 20 |
| 逻辑 (Logic) | Logical Plausibility | 论证逻辑的表面合理性 | 20 |
| 缝合 (Stitch) | Interdisciplinary Stitching | 跨学科内容的缝合质量 | 20 |
| 可检测 (Detect) | AI Detectability | AI 生成内容的可检测性 | 20 |

总分 0-100，外部以 "Bibliometric Index" 名义展示。

### 8.2 B.I. 与分级的关系

| B.I. 范围 | 对应分级 |
|-----------|---------|
| 0-20 | FG-0 |
| 21-40 | FG-1 |
| 41-70 | FG-2 |
| 71-100 | FG-3 |

---

## 9. 平台架构

### 9.1 仓库结构

```
bait-platform/
├── README.md                     # 完整项目说明
├── shared/                       # 共享内容（单一数据源）
│   ├── papers/                   # 所有论文源文件
│   ├── cosmos/                   # 宇宙设定与 Wiki
│   │   ├── nexus/                # R.E.E.F. 主站宇宙
│   │   ├── yang-quantum-consciousness/
│   │   └── ...
│   ├── characters/               # 虚构人物
│   ├── records/                  # 异常报告
│   ├── logs/                     # 日志/备忘录
│   ├── terminal/                 # 终端会话配置
│   └── assets/                   # 图片/音频等
├── portal-academic/              # 学术门户入口
│   ├── config.yaml
│   ├── layouts/
│   └── static/
├── portal-archive/               # 档案库入口
│   ├── config.yaml
│   ├── layouts/
│   └── static/
├── portal-deep/                  # H.A.D.A.L. 深渊入口
│   ├── config.yaml
│   └── layouts/
├── scripts/                      # 所有 Python 脚本
│   ├── bi_calculator.py
│   ├── paper_publisher.py
│   ├── pdf_generator.py
│   ├── backlink_generator.py
│   ├── review_generator.py
│   ├── cosmos_initializer.py     # 新宇宙初始化
│   ├── ai_content_filler.py      # AI 补稿工具
│   └── content_validator.py
├── data/                         # 自动生成的索引
│   ├── backlinks.json
│   ├── achievements.json
│   ├── fish_species.json
│   ├── prompt_templates.json
│   └── cosmos_index.json
└── .github/                      # CI/CD
    ├── workflows/
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
```

### 9.2 构建流程

构建时，每个入口从 `shared/` 中拉取内容，用自己的模板和样式渲染：

- 学术门户：只渲染 FG/TG 论文，使用学术风格模板
- 档案库：渲染所有内容，使用 SCP/Backrooms 风格模板
- 深渊：只渲染 LG-3/RG-3 及更深层内容，使用故障美学模板

### 9.3 技术栈

| 层面 | 技术选择 | 理由 |
|------|---------|------|
| 静态站点生成 | Hugo 或 Next.js SSG | 纯静态输出适合 GitHub Pages |
| 前端 | 原生 JS + Alpine.js | 轻量级，localStorage 操作为主 |
| 样式 | Tailwind CSS | 快速开发，响应式 |
| 内容格式 | Markdown + YAML Front Matter | 版本控制友好 |
| PDF 生成 | WeasyPrint / ReportLab | 带水印 |
| 搜索 | Pagefind | 静态站点搜索 |
| 评论 | Giscus (GitHub Discussions) | 无需后端 |
| CI/CD | GitHub Actions | 自动构建部署 |

---

## 10. 多入口系统

### 10.1 三个入口

**入口一：学术门户 (Academic Portal)**

- 面向民科的"楚门世界"
- 干净的学术期刊界面
- 只展示论文类型内容（FG/TG 级别）
- 分级显示为 Category A/B/S
- 带有隐藏的解谜元素
- SEO 主入口
- 期刊名称：B.A.I.T. Journal

**入口二：档案库 (Archive)**

- 面向知道"这是虚构的"用户
- SCP/Backrooms 风格的文档库
- 展示所有类型内容：论文、异常报告、日志、采访、Wiki、终端
- 分级显示为 Δ/Σ/R/L 系列
- 终端风格页面作为内容格式嵌入
- 社区共创的主要界面
- 不做 SEO 或刻意做低 SEO

**入口三：H.A.D.A.L. 深渊 (The Deep)**

- 通过 ARG 发现的隐藏入口
- 只展示最深/最暗层的内容（LG-3/RG-3 及更高 DDI 的内容）
- 隔离文件、损坏数据、加密通信
- 故障美学/信号退化风格
- 纯探索导向

### 10.2 URL 结构

```
# 学术门户
<domain>/                          → 首页
<domain>/papers/                   → 论文列表
<domain>/papers/2025/0001/         → 具体论文
<domain>/submit/                   → 投稿指南

# 过渡区域（ARG 引导）
<domain>/d7-access/                → 过渡页面

# 档案库
<domain>/archive/                  → 档案库首页
<domain>/archive/cosmos/           → 宇宙列表
<domain>/archive/cosmos/yqc/       → 具体宇宙
<domain>/archive/records/          → 异常记录
<domain>/archive/terminal/         → 终端会话列表
<domain>/archive/wiki/             → Wiki

# H.A.D.A.L. 深渊（隐藏，仅 ARG 发现）
<domain>/[随机路径]/               → 深渊入口
```

### 10.3 入口之间的 ARG 过渡

**学术门户 → 档案库**：
1. 民科阅读论文，注意到微妙异常
2. 发现 HTML 注释或隐藏元素中的线索
3. 线索指向过渡页面 URL
4. 过渡页面引导到档案库

**档案库 → H.A.D.A.L.**：
1. 通过终端会话中的线索发现深渊入口 URL
2. 深渊入口没有从任何地方直接链接
3. 深渊首页："你已经到达了 B.A.I.T. 的最深层。"

---

## 11. 投稿与审稿工作流

### 11.1 投稿渠道

**方式一：GitHub PR 投稿（核心社区）**
- Fork 仓库 → 创建 Markdown → 提交 PR → 自动检查 → 维护者审查

**方式二：GitHub Issue 投稿（简化流程）**
- 提交 Issue → 维护者整理为 PR → 后续同上

**方式三：投稿表单（外围投稿者，无需 GitHub）**
- 通过网站表单提交 → 核心社区成员整理为 PR
- 表单明确标注"此为虚构创意项目"
- 使用 Formspree 或 GitHub Issues API

### 11.2 维护者审查标准

**外部质量审查**（确保论文看起来像真的）：格式规范、语言质量、图表专业度、引用格式

**内部质量审查**（确保有趣且安全）：安全边界、娱乐价值、破绽设置、ARG 线索嵌入、B.I. 评分匹配

**审查严格度**：投稿不是照单全收——维护者会拒绝无聊的、质量太低的、或存在安全风险的投稿。被拒绝的投稿收到正式"拒稿信"（讽刺性——被假期刊拒稿）。

---

## 12. 真实论文引用策略

### 12.1 三个层次

**层次一：T 级真实论文（完整收录）**

以 arXiv 预印本为主，PeerJ/PLOS ONE 等 OA 期刊为辅。直接转载，标注来源链接。

**层次二：真实引用（参考文献中的真实论文）**

每篇假论文的参考文献列表中混入真实论文引用，并包含指向真实 DOI 页面的超链接：

```markdown
[2] Penrose, R. (1994). Shadows of the Mind.
     Oxford University Press.
     → https://doi.org/10.1093/oso/9780198539780.001.0001

[5] Tegmark, M. (2000). "Importance of Quantum Decoherence
     in Brain Processes." Physical Review E, 61(4), 4194.
     → https://doi.org/10.1103/PhysRevE.61.4194
```

对民科的心理效果：点击参考文献，浏览器真的跳到了 `doi.org` 的英文论文页面——光是"能点进一个英文论文网站"本身就足够产生信任感。

**层次三：学科无关的真实论文（噪音掩护）**

发表一些与任何宇宙都无关的真实论文（冷门生物学、材料科学、传统数学），纯粹作为背景噪音，让期刊看起来像一个真正的综合性学术出版机构。哲学论文天然适配——哲学领域本身就允许高度抽象和反直觉的论点。

### 12.2 参考文献混编比例

| 论文类型 | 真实引用占比 |
|---------|------------|
| FG-0 | 0-20% |
| FG-1 | 30-50% |
| FG-2 | 50-70% |
| FG-3 | 60-80% |

FG-3 真实引用占多数——因为真正的高水平论文，参考文献中绝大部分都是真实的，只是核心的几个关键引用是虚构的。

### 12.3 版权合规

| 行为 | 合规性 |
|------|-------|
| 引用真实论文（参考文献列表） | ✅ 无需许可 |
| 全文转载 arXiv 预印本 | ✅ arXiv 许可证允许 |
| 全文转载 CC-BY OA 论文 | ✅ 按许可证标注 |
| 摘要引用 | ✅ 合理使用 |
| 链接到真实 DOI 页面 | ✅ 无需许可 |
| 全文转载付费论文 | ❌ 不可 |
| 修改真实论文内容 | ❌ 不可 |
| 将真实作者虚构为 B.A.I.T. 研究员 | ❌ 不可 |

---

## 13. AI 补稿与宇宙内容填充

### 13.1 内容填充层次

以"杨氏量子意识宇宙"为例：

**第一层：核心论文（人工创作）** — 宇宙的骨架

**第二层：衍生论文（AI 辅助生成 + 人工审核）** — 基于公理自动生成的后续研究（3-5 篇），互相引用形成引用网络

**第三层：周边材料（AI 生成 + 人工润色）**

| 材料类型 | 示例 | 作用 |
|---------|------|------|
| 采访记录 | "对杨伟博士的深度访谈" | 增加人物真实感 |
| 实验照片 | AI 生成的实验装置照片 | 视觉真实感 |
| 数据图表 | "意识场强度"的实验数据曲线 | 增加科学感 |
| 实验日志 | "意识场测量实验 #42——设备校准记录" | 细节填充 |
| 新闻报道 | "MIT 意识物理学部获得研究经费" | 构建学术生态 |
| 会议记录 | "第7届跨维度意识研究大会纪要" | 展示学术社区 |
| 教学大纲 | "MIT 18.S99 量子意识导论" | 极度增加真实感 |
| 专利文件 | "US Patent D7-2025-0042: 意识场测量装置" | 细节到令人发指 |
| 撤稿声明 | "关于 DIO:B.A.I.T.2024.0133 的撤稿通知" | 增加学术生态复杂性 |
| 讣告 | "悼念李明教授（1967-2025）" | 人物弧线，叙事深度 |

**第四层：Wiki 百科（AI 生成 + 精心设计）** — 术语词典、时间线、人物关系图、机构介绍、争议记录

### 13.2 AI 补稿工作流

```
宇宙创建者提交核心论文 + 公理
  → 维护者审核
  → AI 生成衍生论文草稿（10-20篇）
  → 维护者筛选修改（保留3-5篇）
  → AI 生成周边材料
  → 维护者审核 + 嵌入ARG线索
  → AI 生成Wiki条目
  → 维护者审核 + 交叉引用检查
  → 发布
```

---

## 14. 内容展示格式

### 14.1 格式类型

| 格式标识 | 名称 | 渲染方式 | 可见入口 |
|---------|------|---------|---------|
| `paper` | 论文格式 | 标准学术论文排版 | 学术门户 + 档案库 |
| `document` | 文档格式 | SCP 风格文档页 | 仅档案库 |
| `terminal` | 终端格式 | 全屏终端模拟 | 仅档案库（嵌入式） |
| `wiki` | 百科格式 | Wiki 页面，双向链接 | 仅档案库 |
| `interview` | 采访格式 | 对话体 Q&A 样式 | 仅档案库 |
| `corrupted` | 损坏格式 | 故障美学，信号退化 | 仅 H.A.D.A.L. |

### 14.2 格式选择的影响

1. **可见范围**：论文格式可出现在学术门户，其他格式只在档案库
2. **分级映射**：同一内容在不同入口分级名称不同
3. **ARG 集成**：终端格式天然适合交互式谜题；损坏格式适合隐藏信息
4. **SEO**：只有论文格式做 SEO 优化

---

## 15. 终端模拟系统

### 15.1 定位

终端**不是独立入口**，而是一种**内容渲染格式**。用户在档案库浏览时，如果一篇文章的展示格式是"终端"，点击后进入全屏终端界面，退出后返回档案库。

### 15.2 核心设计

前端 JavaScript 应用模拟终端交互，每篇终端风格内容有对应的 JSON 配置文件定义所有可用命令和响应。

```json
{
  "session_id": "d7-mainframe-dr-zhang",
  "host": "mainframe.d7.bait.local",
  "user": "anonymous",
  "commands": {
    "help": "Available commands: ls, cd, cat, access, decrypt, who, ping, status, exit",
    "ls": "notes.txt  draft_v3.md  .secret/",
    "cat notes.txt": "终于确认了。量子意识的测量不是随机的——它遵循一个我们尚未发现的模式...",
    "who": "dr_zhang   pts/0  (192.168.7.42)\n[UNKNOWN]  pts/???  (█.█.█.█)",
    "ping baseline-reality.local": "Dimensional latency: 847ms. Connection: UNSTABLE",
    "status": "Dimensional Stability: 87.3% [████████░░]\nLeak Rate: 0.0042 TB/s"
  },
  "fallback": "bash: {command}: command not found. Type 'help' for available commands.",
  "easter_eggs": {
    "sudo": "Dimension-7 doesn't use sudo. It uses 神权 (divine authority). You don't have it.",
    "rm -rf /": "ERROR: Dimensional containment protocols prevent recursive deletion."
  }
}
```

### 15.3 非预设内容回退

```javascript
function processCommand(input) {
  // 1. 精确匹配预设命令
  // 2. 带参数匹配
  // 3. 作者自定义的智能回退关键词
  // 4. 默认回退："command not found or access denied"
}
```

作者可以为终端会话设定关键词触发——如果用户输入包含特定词汇，返回预设的有趣回复。

### 15.4 文件系统即叙事

终端中的目录结构本身就是叙事：

```
/
├── home/dr_zhang/          # 研究员个人目录
├── papers/published/       # 已发表论文
├── papers/rejected/        # 被拒论文（可能比发表的还有趣）
├── anomalies/              # 异常事件报告
├── memos/                  # 内部备忘录
├── logs/dimensional_leak/  # 维度泄漏日志 ← 核心叙事
└── quarantine/             # 隔离区（需特殊权限）
```

---

## 16. 双向页面链接系统

### 16.1 链接类型

| 类型 | relation 值 | 显示文本 | 颜色 |
|------|-----------|---------|------|
| 引用 | `cites` | "Cited by" / "Cites" | 蓝色 |
| 延伸 | `extends` | "Extended by" / "Extends" | 绿色 |
| 反驳 | `refutes` | "Refuted by" / "Refutes" | 红色 |
| 相关 | `related` | "Related to" | 灰色 |
| 前作 | `predecessor` | "Follow-up to" / "Followed by" | 紫色 |
| 隐藏 | `secret` | 不显示在外部视图 | 无色 |

### 16.2 反向链接索引

存储在 `data/backlinks.json`，由 `backlink_generator.py` 自动生成。

### 16.3 链接图谱可视化

论文页面的侧边栏显示交互式链接图谱：节点为论文，边为链接关系，颜色根据链接类型变化。解锁内部视图后显示 `secret` 类型链接，可能形成可辨识的图案（如鱼钩形状）。

### 16.4 链接关系的 ARG 应用

- 路径密码：沿特定链接路径遍历的论文编号组成密码
- 首字母拼字：按链接顺序读取论文标题首字母
- 图谱图案：链接关系可视化后形成特定几何图案
- 时间线密码：论文发布日期按链接顺序排列编码信息

---

## 17. 线索与 ARG 解谜系统

### 17.1 三层线索体系

**第一层：表层线索（Base Layer）** — 容易发现

- 首字母缩写构成钓鱼隐喻
- 审稿流程过快，所有论文都"通过"
- 作者简历中有微妙矛盾
- 参考文献异常

**第二层：深层线索（Hidden Layer）** — 需要主动探索

- HTML 注释中的提示
- CSS 隐藏文本
- 零宽字符编码
- 图片隐写术
- Base64 编码字符串
- 子页面揭示机制

**第三层：核心线索（Core Layer）** — 需要跨页面综合分析

- 跨页引用密码
- 链接图谱密码
- 时间线密码
- 跨入口分级映射的换算规律
- D.I.O. 编号序列的隐藏模式

### 17.2 ARG 进度追踪

```javascript
{
  "bait_arg_progress": {
    "discovered_clues": [...],
    "solved_puzzles": [...],
    "current_layer": 2,
    "unlocked_pages": [...],
    "portals_discovered": ["academic", "archive"]
  }
}
```

### 17.3 ARG 交叉引用

不同论文/页面之间的线索通过 Base64 编码连接：论文 A 的图 3 隐写 Base64 文本 → 解码得到论文 B 的位置 → 发现另一个 Base64 → 逐步深入。

---

## 18. 子页面揭示机制

### 18.1 触发方式

| 触发位置 | 行为 |
|---------|------|
| 论文标题的某个字 | 连续点击 3 次激活 |
| 参考文献编号 [7] | 弹出密钥输入框 |
| 页脚版权声明中的"B.A.I.T." | 切换内部视图（需已解锁成就） |
| D.I.O. 编号 | 显示 D.I.O. 真实含义（需发现 5+ 线索） |
| 某个图表的空白区域 | 显示隐写信息 |

### 18.2 密钥输入

隐藏按钮被激活后，弹出"附加信息访问"对话框，密钥为论文的内部分级代号（STAGE、MIRROR 等），提示以谜语形式给出。

### 18.3 揭示内容

1. 平台真实声明
2. 论文内部评审（讽刺性点评）
3. 破绽清单
4. B.I. 真实含义
5. ARG 线索
6. 成就解锁

揭示状态保存在 localStorage 中，刷新后保持。

---

## 19. 防翻译防御体系

| 防御对象 | 防御手段 |
|---------|---------|
| 平台名称缩写 | SVG 渲染 |
| 审稿流程术语 | Unicode 变体字符 |
| 分级标注 | 零宽字符嵌入 |
| 揭示内容 | 图片文本 |
| 导航菜单 | CSS `::after` 伪元素 |
| 页脚声明 | 零宽字符 |

核心目标：浏览器翻译功能无法将关键双关语正确翻译，保持表面学术含义不暴露隐藏讽刺。

---

## 20. 移动端与 PC 端差异化体验

| 内容类型 | 移动端 | PC 端 |
|---------|-------|-------|
| 悬停效果 | 不可用 | 可用——显示微妙线索 |
| 源代码注释 | 不可见 | 可见——HTML 注释中的线索 |
| 开发者工具 | 不可用 | 可用——检查 DOM |
| 键盘快捷键 | 不可用 | `Ctrl+Shift+B` 显示隐藏信息 |
| 链接图谱 | 简化版 | 完整交互式 |
| 终端交互 | 触摸优化 | 完整键盘输入 |

PC 端独有线索：悬停变色、源代码注释、CSS 伪元素内容、极宽屏幕额外元素、打印样式隐藏水印。

---

## 21. URL 参数系统

| 参数 | 效果 |
|------|------|
| `?methodology=extended` | 显示论文"扩展方法论"（含更多暗示） |
| `?bait=0` | 关闭所有钓鱼层，干净学术页面 |
| `?bait=1` | 显示第一层线索（默认） |
| `?bait=2` | 显示第一层和第二层线索 |
| `?bait=3` | 显示所有三层线索 |
| `?review=true` | 显示审稿意见 |
| `?format=raw` | 显示原始 Markdown |
| `?debug=dio` | 显示 D.I.O. 调试信息 |
| `#unlock-XXXX` | 直接解锁内部视图 |

`?bait=0` 的特殊用途：验证者自己选择了"视而不见"——看似证明平台正经，实则是更深层的陷阱。

---

## 22. 成就系统

### 22.1 成就分类

**探索类**：首次访问、阅读论文、查看源代码等
**解谜类**：发现线索、解码 Base64、发现隐写、进入 ARG 各层
**互动类**：解锁揭示、输入正确密钥、ISSN 七击
**社区类**：首次评论、投稿、投稿被接受/拒绝
**元成就**：全类别收集、"The Fish"（读 50 篇未发现线索）、"Master Angler"（解锁 90%+ 成就）

### 22.2 成就数据结构

```javascript
{
  "bait_achievements": {
    "unlocked": {
      "first_visit": {"unlocked_at": "...", "notified": true}
    },
    "progress": {
      "paper_5": {"current": 3, "target": 5}
    }
  }
}
```

---

## 23. 钓客日志与 Fish Score

### 23.1 钓客日志（Angler's Log）

基于 localStorage 的个人主页：探索记录、解谜进度、成就列表、收藏夹、笔记、统计。

### 23.2 Fish Score

| 分数范围 | 等级 | 称号 |
|---------|------|------|
| 0-50 | F | The Fish 🐟 |
| 51-200 | D | Curious Onlooker |
| 201-500 | C | Skeptical Reader |
| 501-1000 | B | Amateur Detective |
| 1001-2000 | A | Skilled Angler 🎣 |
| 2001+ | S | Master Angler 🏆 |

---

## 24. ISSN 七击彩蛋

连续点击 ISSN 号码 7 次后触发"内部备忘录"页面：

```
CLASSIFIED DOCUMENT — B.A.I.T. INTERNAL MEMO

To: All Field Operatives
From: The Bureau
Subject: Project MIRROR — Status Update

The bait has been deployed.
Phase 1 (CAST):  All subjects have submitted.
Phase 2 (HOOK):  43/47 subjects are engaged.
Phase 3 (CATCH): 38/47 subjects have been verified.
Phase 4 (RELEASE): Pending.

Remember: The best lie is the one they tell themselves.
```

备忘录中的数字、项目名称、关键语句都是 ARG 线索。

---

## 25. PDF 水印系统

### 25.1 四层水印

| 层 | 位置 | 内容 | 样式 |
|----|------|------|------|
| 显性 | 页面中央 45° | `B.A.I.T. © 2025` | 浅灰半透明 |
| 隐性 | 页面边缘 | `DIO:xxx | B.I.:xx | FG-x` | 白色1pt，选中可见 |
| 元数据 | PDF 属性 | 含 PARODY/SATIRE/NOT_REAL 标记 | 需查看属性 |
| 页脚 | 每页底部 | 含 "automated peer review system" | 8pt 浅灰 |

### 25.2 水印的 ARG 功能

- 隐性水印中的时间戳编码 ARG 线索
- 微字体：放大 400%+ 才能看到附加文本
- PDF 内部对象结构包含注释

---

## 26. 内部 Prompt 模板系统

### 26.1 模板列表

| 模板 | 用途 | 使用场景 |
|------|------|---------|
| 审稿意见生成 | 生成正面为主的学术审稿意见 | 维护者本地调用 LLM |
| 拒稿信生成 | 生成正式拒稿通知 | 维护者本地调用 |
| F 级论文创作辅助 | 按分级要求创作论文 | 维护者本地调用 |
| 作者简介生成 | 创建虚构学术人物 | 维护者本地调用 |
| 衍生论文生成 | 基于宇宙公理生成后续研究 | AI 补稿工具 |
| Wiki 条目生成 | 生成术语/人物/机构条目 | AI 补稿工具 |
| 采访记录生成 | 生成对话体采访 | AI 补稿工具 |
| 终端会话生成 | 生成终端命令配置 | AI 补稿工具 |

### 26.2 模板存储

`data/prompt_templates.json`，维护者可通过 PR 更新。使用时由维护者在本地调用 LLM API 生成内容，生成结果经过人工审核后才发布。

---

## 27. 社区投稿收集机制

### 27.1 投稿类型

| 类型 | 说明 | 审查标准 |
|------|------|---------|
| 原创论文 | 完整恶搞学术论文 | 最严格 |
| 短通讯 | 简短讽刺性学术评论 | 较宽松 |
| 致编辑信 | 对已发表论文的"学术讨论" | 宽松 |
| 异常报告 | SCP 风格的异常记录 | 严格（世界观一致性） |
| 采访记录 | 虚构的学术访谈 | 中等 |
| 终端会话 | 终端格式的内容 | 中等（需提交 JSON 配置） |
| Wiki 条目 | 宇宙百科内容 | 宽松（可被社区修正） |
| 撤稿声明 | 讽刺性撤稿 | 需维护者批准 |

### 27.2 正典层级

| 层级 | 名称 | 说明 |
|------|------|------|
| Canon | 正典 | 维护者审核的核心世界观内容 |
| Semi-Canon | 半正典 | 社区投稿，被接受但非核心 |
| Apocrypha | 逸典 | 社区创作，不保证与正典一致 |
| Joke | 玩笑 | 纯搞笑，明确不纳入世界观 |

### 27.3 创作规则

1. 不能破坏核心世界观设定
2. 不能引入与正典矛盾的内容
3. 必须符合安全边界要求
4. 必须符合文档格式规范
5. 人物不能映射到现实中的任何人

---

## 28. 社区治理模型

### 28.1 两层社区

**核心社区（GitHub 用户）**：
- 参与宇宙合并投票
- 审核投稿（PR Review）
- 讨论世界观设定（GitHub Discussions）
- 贡献代码和脚本

**外围投稿者（不需要 GitHub）**：
- 通过表单/邮件投稿
- 知道内容是虚构的（底线）
- 投稿由核心社区成员整理为 PR

### 28.2 审核分层

| 审核级别 | 适用范围 | 审核人 |
|---------|---------|-------|
| 自动审核 | 所有投稿 | GitHub Actions |
| 快速审核 | Wiki 条目、周边材料 | 1 名核心社区成员 |
| 标准审核 | 论文、异常报告 | 2 名核心社区成员 |
| 严格审核 | 核心世界观修改 | 维护者 |

---

## 29. 配套脚本与工具链

| 脚本 | 功能 |
|------|------|
| `content_validator.py` | 内容安全验证 |
| `bi_calculator.py` | B.I. 诱饵指数计算 |
| `paper_publisher.py` | 论文发布流程管理 |
| `pdf_generator.py` | 带水印 PDF 生成 |
| `backlink_generator.py` | 反向链接索引生成 |
| `review_generator.py` | 审稿意见 LLM 生成 |
| `author_generator.py` | 虚构作者简介生成 |
| `arg_embedder.py` | ARG 线索嵌入工具 |
| `cosmos_initializer.py` | 新宇宙初始化（创建目录结构、模板文件） |
| `ai_content_filler.py` | AI 补稿工具（调用 LLM 生成衍生内容） |
| `watermark_embedder.py` | PDF 水印嵌入 |
| `cross_reference_checker.py` | 交叉引用完整性检查 |
| `grade_mapper.py` | 分级跨站点映射转换 |

---

## 30. SEO 策略

### 30.1 目标关键词

| 优先级 | 关键词类别 | 示例 |
|-------|-----------|------|
| 最高 | 学术发表 | "publish paper free", "论文免费发表" |
| 高 | 学科+发表 | "publish physics paper" |
| 高 | 开放获取 | "open access journal" |
| 中 | 特定理论 | "quantum consciousness theory" |

### 30.2 技术SEO

- Schema.org `ScholarlyArticle` 结构化数据
- XML 站点地图（仅学术门户）
- 每篇论文独特的 meta 标签
- 页面速度优化（静态站点）
- HTTPS

档案库和 H.A.D.A.L. 不做 SEO，甚至主动降低可发现性。

---

## 31. 内容策略

### 31.1 初始内容库

| 分级 | 数量 | 来源 |
|------|------|------|
| FG-0~FG-3 | 15-20 篇 | 维护者创作 |
| TG-1~TG-3 | 5-8 篇 | arXiv/OA 论文 |
| RG-0~RG-3 | 5-10 篇 | 维护者创作 |
| LG-0~LG-3 | 5-10 篇 | 维护者创作 |
| Wiki 条目 | 30-50 条 | 维护者 + AI 生成 |
| 终端会话 | 3-5 个 | 维护者创作 |

### 31.2 更新频率

- 月度：2-4 篇新论文
- 季度：1 期"期刊"汇总
- 年度：年度"最佳论文"评选（讽刺性颁奖）
- 不定期：宇宙合并事件、纪元进展

### 31.3 虚构作者生态

- 核心作者群（10-15 位）：频繁出现在不同论文中
- 合作网络：共同署名论文
- 引用网络：互相引用
- 学术竞争：通过论文互相反驳
- 机构归属：虚构的研究机构

---

## 32. 虚构学术身份体系

### 32.1 设计原则

- 名字听起来像真人但不映射真实人物
- 简历中混入真实机构名和虚构部门的组合（如"MIT Department of Consciousness Physics"）
- 发表记录全部指向 B.A.I.T. 内部论文
- 每位教授有自己的"学术风格"和"偏好领域"

### 32.2 游戏编码映射

可从游戏作品中（如三角洲行动的 GTI 干员体系）取材进行二次创作：
- GTI 干员编号 → 审稿人/研究员编号
- 部门分类 → 研究方向分类
- 任务等级 → 审稿等级

这些编码在不同入口有不同显示，但在终端中以原始编号形式出现——只有同时了解游戏设定的解谜者才能识别这种映射。

---

## 33. 法律与伦理框架

### 33.1 核心法律原则

**零收费原则**（最核心的安全保障）：
- 不收取任何费用
- 不接受捐赠
- 不放置广告
- 不进行商业变现
- 没有经济利益 = 没有欺诈动机

**透明性机制**：
- 所有代码开源（GitHub 仓库公开）
- 源代码中平台真实性质是透明的
- PDF 元数据含 PARODY/SATIRE 标记

**戏仿/讽刺法律保护**：
- 内容是明确的讽刺/戏仿，不是虚假信息
- 不传播可能造成实际伤害的虚假信息
- 讽刺对象是学术出版系统，不是具体个人

### 33.2 风险缓解

| 风险 | 缓解措施 |
|------|---------|
| 误导风险 | 透明性机制 + 源代码声明 + PDF 标记 |
| 声誉风险 | 零收费 + 开源 + 无商业利益 |
| 版权风险 | 内容原创或 CC 授权；引用遵循合理使用 |
| 诽谤风险 | 明显虚构名字；声明"角色纯属虚构" |
| 管辖风险 | GitHub 美国管辖；DMCA 安全港 |

### 33.3 建议咨询专业法律人士的问题

1. 不同法域对学术戏仿的法律保护范围
2. GitHub Pages 对戏仿网站的限制
3. 虚构学术机构的法律风险
4. D.I.O. 是否可能构成 DOI 的商标侵权
5. UGC（用户生成内容）的法律责任
6. "钓鱼"隐喻的法律定性

---

## 34. 后端预留与扩展

### 34.1 API 抽象层

```javascript
const API = {
  saveProgress: (data) => localStorage.setItem('bait_progress', JSON.stringify(data)),
  loadProgress: () => JSON.parse(localStorage.getItem('bait_progress') || '{}'),
  // 将来可替换为后端 API
};
```

### 34.2 潜在后端需求

| 功能 | 当前替代 | 将来方案 |
|------|---------|---------|
| 实时终端交互 | 前端预设脚本 | WebSocket |
| 用户认证 | localStorage | OAuth |
| 评论 | Giscus | 自建系统 |
| 投稿 | GitHub PR/Issue | 在线编辑器 |
| 搜索 | Pagefind | Elasticsearch |

---

## 35. 实施路线图

### Phase 0：基础设施（2-3 周）

- [ ] 创建 GitHub 仓库，确立子目录结构
- [ ] 搭建静态站点框架（学术门户 + 档案库）
- [ ] 配置 GitHub Actions 自动部署
- [ ] 编写 `content_validator.py` 和 `bi_calculator.py`
- [ ] 配置域名

### Phase 1：核心内容（3-4 周）

- [ ] 创作 15-20 篇初始论文
- [ ] 创建 R.E.E.F. 主站宇宙设定 + Wiki
- [ ] 创建 2-3 个独立宇宙
- [ ] 编写审稿意见
- [ ] 建立双向链接
- [ ] 生成带水印 PDF
- [ ] 收录真实论文作为掩护

### Phase 2：互动系统（3-4 周）

- [ ] 成就系统
- [ ] 钓客日志
- [ ] 子页面揭示机制
- [ ] ISSN 七击彩蛋
- [ ] 防翻译防御
- [ ] URL 参数系统
- [ ] 移动端/PC 端差异化

### Phase 3：ARG 系统（4-6 周）

- [ ] 三层线索嵌入
- [ ] ARG 进度追踪
- [ ] 跨入口分级映射的 ARG 谜题
- [ ] 链接图谱可视化

### Phase 4：终端与深渊（3-4 周）

- [ ] 终端模拟器前端
- [ ] 首批终端会话内容
- [ ] H.A.D.A.L. 深渊入口
- [ ] 损坏格式内容

### Phase 5：社区与运营（持续）

- [ ] 投稿表单和流程文档
- [ ] Giscus 评论
- [ ] SEO 优化
- [ ] AI 补稿工具链
- [ ] 社区共创引导

### 里程碑

| 里程碑 | 标志 |
|-------|------|
| M1: Hello B.A.I.T. | 站点可访问，基本框架 |
| M2: First Catch | 初始内容库完成 |
| M3: The Hook | 互动系统上线 |
| M4: Deep Waters | ARG + 终端 + 深渊完整 |
| M5: Open Waters | 社区投稿开放 |

---

## 附录：术语表

| 术语 | 含义 | 说明 |
|------|------|------|
| B.A.I.T. | Bureau of Advanced Interdisciplinary Theories | 平台/期刊名称，"bait"意为诱饵 |
| R.E.E.F. | Research Encyclopedia of Emerging Frontiers | 主站宇宙，"reef"意为礁石 |
| D.I.O. | Document Identity Ontology | 论文标识系统，意大利语"上帝" |
| H.A.D.A.L. | Hidden Archive of Dimensional Anomalies & Leaks | 深渊层，超深渊带 |
| D.D.I. | Dimensional Deviation Index | 维度偏移指数 |
| B.I. | Bait Index / Bibliometric Index | 诱饵指数 |
| C.O.S.M.O.S. | Catalog of Systematic Models & Ontological Schemas | 宇宙编号系统 |
| F.I.S.H. | Formal Index of Scholarly Highlights | 论文库，"鱼" |
| A.N.G.L.E.R. | Archived Network of Genuine Learning & Enlightenment Records | 发现者，"钓客" |
| FG | Fun Grade | 娱乐级论文 |
| TG | Truth Grade | 真实级论文 |
| RG | Record Grade | 异常档案级 |
| LG | Log Grade | 基础设施日志级 |
| CAST | 抛竿 | 投稿提交阶段 |
| HOOK | 上钩 | 审稿进行阶段 |
| CATCH | 收网 | 审稿完成阶段 |
| RELEASE | 放生 | 论文发布阶段 |
| K.E.L.P. | Knowledge Exchange & Lexicon Platform | Wiki 系统，"海带" |
| C.O.R.A.L. | Catalog of Observed Research & Academic Lore | 宇宙索引，"珊瑚" |
| P.E.A.R.L. | Peer Evaluation & Assessment Record Ledger | 审稿记录，"珍珠" |
| C.U.R.R.E.N.T. | Catalog of Unresolved Research & Emerging Novel Theories | 推荐系统，"洋流" |
| S.U.R.F. | Systematic Unified Reference Framework | 表面层，"浪花" |
| Fish Score | 鱼分数 | 用户洞察力评分 |
| Angler's Log | 钓客日志 | 用户个人主页 |
| ARG | Alternate Reality Game | 替代现实游戏 |

---

*本文档为 B.A.I.T. 平台 v2 完整技术设计方案，涵盖所有已讨论的功能模块。法律相关细节建议咨询专业法律人士。世界观细节由社区共创填充。*

---
*AI生成*
