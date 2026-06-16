---
AIGC: {"Label":"1","ContentProducer":"001191110108MA01KP2T5U00000","ProduceID":"f3a9c1d7e8b524af6d0e1c2b3a485967","ReservedCode1":"","ContentPropagator":"001191110108MA01KP2T5U00000","PropagateID":"f3a9c1d7e8b524af6d0e1c2b3a485967","ReservedCode2":""}
---

# B.A.I.T. 平台完整设计文档 v3

> **Bureau of Advanced Interdisciplinary Theories**
> "bait" = 诱饵 / 钓鱼 — 跨维度学术模仿秀平台的完整技术设计方案
> 主站宇宙：R.E.E.F. — Research Encyclopedia of Emerging Frontiers
>
> **v3 变更说明**：在 v2 的多宇宙/三入口/编年史架构基础上，补回 v1 的全部实现细节（脚本伪代码、Front Matter、Prompt 模板正文、成就完整表），细化 v2 新增概念（终端系统、编年史-DIO 段对应、游戏编码映射），新增缺失章节（仓库与部署、域名策略、反 SEO、后端接口契约、投稿法律措辞），并大幅扩充**法律与伦理框架**——其中包含一份**专门提交给 GPT 做严谨法律检索的咨询问题清单**。

---

## 目录

### 第一部分：世界观与定位

1. [项目概述](#1-项目概述)
2. [命名体系](#2-命名体系)
3. [R.E.E.F. 编年史](#3-reef-编年史)
4. [内容边界与安全策略](#4-内容边界与安全策略)

### 第二部分：架构与系统

5. [多宇宙架构](#5-多宇宙架构)
6. [分级系统与跨站点映射](#6-分级系统与跨站点映射)
7. [钓鱼审稿系统](#7-钓鱼审稿系统)
8. [B.I. 诱饵指数评估体系](#8-bi-诱饵指数评估体系)
9. [平台架构](#9-平台架构)
10. [仓库与部署策略](#10-仓库与部署策略)
11. [多入口系统](#11-多入口系统)

### 第三部分：内容与创作

12. [投稿与审稿工作流](#12-投稿与审稿工作流)
13. [真实论文引用策略](#13-真实论文引用策略)
14. [AI 补稿与宇宙内容填充](#14-ai-补稿与宇宙内容填充)
15. [内容展示格式](#15-内容展示格式)
16. [终端模拟系统](#16-终端模拟系统)
17. [虚构学术身份体系](#17-虚构学术身份体系)
18. [游戏编码映射系统](#18-游戏编码映射系统)

### 第四部分：交互与解谜

19. [双向页面链接系统](#19-双向页面链接系统)
20. [线索与 ARG 解谜系统](#20-线索与-arg-解谜系统)
21. [子页面揭示机制](#21-子页面揭示机制)
22. [防翻译防御体系](#22-防翻译防御体系)
23. [移动端与 PC 端差异化体验](#23-移动端与-pc-端差异化体验)
24. [URL 参数系统](#24-url-参数系统)
25. [成就系统](#25-成就系统)
26. [钓客日志与 Fish Score](#26-钓客日志与-fish-score)
27. [ISSN 七击彩蛋](#27-issn-七击彩蛋)
28. [PDF 水印系统](#28-pdf-水印系统)

### 第五部分：社区与运营

29. [内部 Prompt 模板系统](#29-内部-prompt-模板系统)
30. [社区投稿收集机制](#30-社区投稿收集机制)
31. [社区治理模型](#31-社区治理模型)
32. [配套脚本与工具链](#32-配套脚本与工具链)
33. [SEO 策略](#33-seo-策略)
34. [反 SEO 与去索引策略](#34-反-seo-与去索引策略)
35. [内容策略](#35-内容策略)
36. [后端预留与扩展](#36-后端预留与扩展)

### 第六部分：法律、路线图与附录

37. [域名策略](#37-域名策略)
38. [法律与伦理框架](#38-法律与伦理框架)
39. [提交 GPT 的法律咨询问题清单](#39-提交-gpt-的法律咨询问题清单)
40. [实施路线图](#40-实施路线图)
41. [附录：术语表](#附录术语表)

---

# 第一部分：世界观与定位

## 1. 项目概述

### 1.1 核心理念

B.A.I.T.（Bureau of Advanced Interdisciplinary Theories）是一个模仿正规学术出版机构的恶搞/戏仿平台，目标受众为中国互联网上的"民科"群体——那些缺乏正规学术训练、热衷于发表"颠覆性理论"却对学术出版规范了解甚少的人群。平台名称本身即为核心隐喻："bait"意为诱饵/钓鱼，暗示整个平台就是一个精心设计的"学术钓鱼"场景。

平台的运作模式类似于"楚门的世界"：目标受众（民科）会认为这是一个真实的、权威的国际学术出版机构，而具备足够辨识力的正常用户则可以通过嵌入的线索、ARG 谜题和隐藏内容，发现平台的真实性质。这种双层体验设计确保了平台既是讽刺艺术品，也是一个互动解谜游戏。

在 v2/v3 架构中，平台从单纯的"钓鱼网站"升级为**跨维度虚构世界门户**。整个平台被设定为维度偏移数据的泄漏产物——B.A.I.T. 的"学术论文"实际上是 R.E.E.F. 系统捕获的跨维度数据，而民科投稿本质上是被系统归档的"基准现实维度偏移数据"。这种 meta 叙事将讽刺、解谜和社区共创统一在一个完整的世界观框架内。

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
| 虚构人物 | `DIO:B.A.I.T.AUTH.<YYYY>.<SEQ>` | `DIO:B.A.I.T.AUTH.2025.0042` |

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

**对应 DIO 段**：`DIO:B.A.I.T.2020.0001` ~ `DIO:B.A.I.T.2021.0150`（早期朴素论文，格式粗糙，记录"故障"为主）

**终端日志风格**：极简、纯文本、无颜色、命令少（`ls/cat/log`）、无警告系统。

### 3.3 纪元二：建制期（The Foundation Era）

发现维度偏移后，研究团队意识到需要系统性地记录和分类这些异常。B.A.I.T. 正式成立（对外仍然伪装为普通学术出版机构），R.E.E.F. 系统开始建设，D.I.O. 标识体系被发明出来。C.A.S.T./H.O.O.K./C.A.T.C.H./R.E.L.E.A.S.E. 审稿流程被确立——表面上是学术同行评审，实际上是对维度偏移数据的捕获和分类流程。

**对应内容**：B.A.I.T. 的"建院文献"、第一批正式的 R 级异常报告、D.I.O. 系统的设计文档、早期编委会的内部通信。

**对应 DIO 段**：`DIO:B.A.I.T.2021.0151` ~ `DIO:B.A.I.T.2022.0400`（格式开始规范化，DIO 系统上线，首批正式 R 级报告）

**终端日志风格**：出现基础分级提示（`[INFO]/[WARN]`），出现 `access` 命令但大部分被拒。

### 3.4 纪元三：膨胀期（The Expansion Era）

随着 R.E.E.F. 系统的运行，越来越多的独立宇宙被发现。宇宙数量快速增长，宇宙合并事件开始出现。H.A.D.A.L. 深渊层被发现——某些数据深度偏移，接近"不可读"状态。F.I.S.H. 论文库、K.E.L.P. Wiki 系统、C.O.R.A.L. 宇宙索引相继建立。

**对应内容**：大量宇宙的建立、第一批终端会话记录、H.A.D.A.L. 层的初始数据、宇宙合并的历史记录。

**对应 DIO 段**：`DIO:B.A.I.T.2022.0401` ~ `DIO:B.A.I.T.2024.0800`（论文数量爆发，开始出现跨宇宙引用、终端会话、Wiki 条目）

**终端日志风格**：命令丰富，出现 `[CRITICAL]` 级别，出现 `decrypt` 命令，日志中开始出现"泄漏"字样。

### 3.5 纪元四：泄漏期（The Leak Era） ← 当前

维度泄漏率开始上升。越来越多的 R.E.E.F. 数据出现在"基准现实"的互联网上——这就是网站本身存在的原因。B.A.I.T. 对外发布的"学术论文"实际上是维度泄漏的副产品，而民科投稿本质上是被 R.E.E.F. 系统捕获的"来自基准现实维度偏移数据"。

**这是整个平台的 meta 叙事核心**：

- **对民科来说**：他们投稿的论文被"接受发表"，觉得自己得到了认可
- **对解谜者来说**：他们发现"投稿"实际上是"维度数据被 R.E.E.F. 系统捕获并分类的过程"
- **双重讽刺**：民科以为自己在参与学术，实际上他们是"异常数据源"；解谜者以为自己在解谜，实际上他们也是"数据"的一部分

**对应内容**：维度泄漏日志、泄漏期系统警告、当前所有论文和档案。

**对应 DIO 段**：`DIO:B.A.I.T.2024.0801` ~ 现在（精密、带水印、带 ARG 嵌入、泄漏期警告横幅）

**终端日志风格**：高频 `[LEAK DETECTED]` 警告，文件被隔离（`quarantine/`），出现"未知实体"登录痕迹。

### 3.6 纪元五：？（社区定义）

未来的纪元由社区投票决定——可能是"收容期"（维度泄漏被控制）、"融合期"（基准现实与维度数据完全融合）、或"沉默期"（所有维度数据突然消失）。这是留给社区共创的开放叙事空间。

**DIO 段预留**：`DIO:B.A.I.T.<未来年份>.0001+`

### 3.7 历史在平台中的体现

| 体现方式 | 说明 |
|---------|------|
| 时间线页面 | 档案库中的 R.E.E.F. 编年史 |
| 终端日志 | 不同纪元的系统日志风格不同（早期简单，近期复杂且带警告） |
| 论文风格演变 | 早期论文更"朴素"，近期论文更"精密"——这是刻意的设计选择 |
| Wiki 条目 | 历史事件有专门的 Wiki 页面，社区可以补充细节 |
| D.I.O. 编号规律 | 早期编号（2020-2021）对应发现期，中期（2022-2024）对应膨胀期，当前（2024+）对应泄漏期——**编号序列号本身是 ARG 线索** |

### 3.8 DIO 段对应表（ARG 线索总览）

下表是"维护者内部用"的纪元-DIO 对应规律。**解谜者需要通过对比多篇论文的发表年份、格式风格、终端日志，自行推断出这张表**——一旦推断出来，就能预判某个 DIO 编号属于哪个纪元，进而预判该论文应包含哪些"时代特征"。如果一篇 2020 年的论文却用了 2024 年的精密格式，那就是 ARG 故意设置的"时空错乱"线索。

| 纪元 | DIO 段 | 格式特征 | 终端特征 | 标志内容 |
|------|--------|---------|---------|---------|
| 发现期 | 2020.0001–2021.0150 | 粗糙、纯文本、无水印 | 极简命令 | 设备故障记录 |
| 建制期 | 2021.0151–2022.0400 | 规范化、DIO 系统上线 | 出现分级提示 | 建院文献、DIO 设计文档 |
| 膨胀期 | 2022.0401–2024.0800 | 成熟、跨宇宙引用 | 命令丰富、`decrypt` | 宇宙建立、合并记录 |
| 泄漏期 | 2024.0801–现在 | 精密、带水印、ARG 嵌入 | 高频泄漏警告 | 泄漏日志、当前论文 |
| ？ | 未来 | 社区定义 | 社区定义 | 社区共创 |

---

## 4. 内容边界与安全策略

### 4.1 绝对禁区（任何情况下不可出现）

1. **政治敏感内容**：涉及中国政治体制、领导人、政策批评的任何内容
2. **邪教/极端主义内容**：任何可能被归类为邪教宣传或极端主义思想的内容
3. **医疗/健康建议**：任何可能被误读为医疗建议的内容，包括"替代疗法"、"能量治疗"等
4. **种族/性别歧视内容**：任何形式的歧视性言论
5. **金融/投资建议**：任何可能被解读为投资建议的内容
6. **真实个人攻击**：针对真实存在的学术人物的诽谤或人身攻击
7. **儿童不当内容**：任何涉及未成年人的不当内容

### 4.2 安全主题领域

以下领域天然适合产生荒诞但无害的内容，且与民科常见的"研究"方向高度重合：

- **数学/几何**：宣称证明哥德巴赫猜想、发明新几何、推翻微积分
- **理论物理/宇宙学**：大统一理论、多维空间模型、暗物质替代解释
- **AI/计算理论**：宣称发明超越图灵机的计算模型、意识上传理论
- **哲学/认识论**：新的"万物理论"、重新定义时间/空间/因果关系
- **信息论/密码学**：宣称破解现有加密体系、发明不可破解的密码
- **进化论/古生物**（不涉及人类起源的种族敏感内容）：恐龙文明假说等
- **生物/化学**：虚构的生化机制、分子结构

### 4.3 内容安全审查原则

- **无害性测试**：如果这篇论文被一个完全不懂学术的人当真，是否会造成任何实际伤害？如果答案为"是"，则不可发布
- **可辨识性测试**：一个受过大学教育的正常人，能否在仔细阅读后识别出这是戏仿？如果答案为"否"，则需要增加更多线索
- **法律风险评估**：内容是否可能引发任何法律纠纷？如果答案为"是"，则不可发布
- **去人格化原则**：所有"作者"均使用虚构身份，绝不暗示指向真实个人
- **反伤害扩散原则**：即使内容本身无害，如果其传播方式可能导致误导性后果，也需重新评估

### 4.4 安全分级与处置

| 内容嫌疑等级 | 判定标准 | 处置 |
|------------|---------|------|
| 绿（通过） | 不触碰任何禁区，无害可辨识 | 正常发布 |
| 黄（警告） | 边缘地带，需维护者二次会商 | 维护者 2 人以上同意方可发布 |
| 红（拒绝） | 触碰禁区或高风险 | 直接拒稿，记录拒稿理由 |

---

# 第二部分：架构与系统

## 5. 多宇宙架构

### 5.1 核心概念

B.A.I.T. 的最大升级是从"单一钓鱼网站"进化为"多宇宙虚构世界门户"。每个在平台上"发表"的民科（或虚构作者），都可以拥有自己的独立宇宙。这个宇宙有自己的基础公理、推导出的理论体系、内部逻辑自洽性和专属术语。

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

**合并后的引用处理**：合并前 A 宇宙的论文仍保留原 `COSMOS-A-xxx` 编号，但新增 `merged_into: COSMOS-UNI-xxx` 字段。新论文可直接引用 `COSMOS-UNI-xxx`。`backlink_generator.py` 会自动建立双向重定向，访问旧编号自动跳转到合并后宇宙的"历史索引页"。

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
canon_level: "Canon"  # Canon / Semi-Canon / Apocrypha / Joke
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

### 5.6 正典层级管理

| 层级 | 名称 | 判定标准 | 升降机制 |
|------|------|---------|---------|
| Canon | 正典 | 维护者审核的核心世界观内容，不与既有公理矛盾 | 维护者提案 + 2 人审核通过 |
| Semi-Canon | 半正典 | 社区投稿，被接受但非核心 | 提交后被核心社区接受；若被核心世界观引用可升 Canon |
| Apocrypha | 逸典 | 社区创作，不保证与正典一致 | 任何社区成员可标记；若与正典冲突自动降为逸典 |
| Joke | 玩笑 | 纯搞笑，明确不纳入世界观 | 作者主动标记或维护者标记 |

**冲突解决原则**：当 Semi-Canon/Apocrypha 与 Canon 冲突时，以 Canon 为准，冲突内容自动降级。维护者每季度审查一次层级归属。

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

### 6.7 分级跨站点映射脚本逻辑

`grade_mapper.py` 负责在构建时把统一内部分级翻译成各入口的显示形式。核心是一张映射表，存在 `data/grade_map.json`：

```json
{
  "FG-0": {
    "academic": {"label": "Category A", "subtitle": "Original Contribution", "color": "#2e7d32"},
    "archive":  {"label": "Δ-0 BASELINE ANOMALY", "color": "#1565c0"},
    "terminal": {"label": "DOC::TYPE-A-0"}
  },
  "FG-3": {
    "academic": {"label": "Category S", "subtitle": "Landmark Contribution", "color": "#c62828"},
    "archive":  {"label": "Δ-3 CRITICAL DEVIATION", "color": "#c62828"},
    "terminal": {"label": "DOC::TYPE-S"}
  }
}
```

各入口的 Hugo/Next.js 模板在渲染时按入口类型查表，输出对应标签。

---

## 7. 钓鱼审稿系统

### 7.1 四阶段流程

| 阶段 | 钓鱼术语 | 外部学术术语 | 内部含义 | 用户可见状态 |
|------|---------|-------------|---------|-------------|
| 1 | 抛竿 (Cast) | Submitted | 诱饵已放出 | "Your manuscript has been received and is under initial screening" |
| 2 | 上钩 (Hook) | Under Review | 目标已上钩 | "Your manuscript is currently under peer review by our expert panel" |
| 3 | 收网 (Catch) | Accepted | 确认上钩 | "Congratulations! Your manuscript has been accepted for publication" |
| 4 | 放生 (Release) | Published | 论文公开 | "Your paper is now publicly available in our repository" |

### 7.2 审稿状态页面设计

与真实学术出版平台（ScholarOne、Editorial Manager）高度相似：

- **进度条**：使用正式的百分比进度显示（"Initial Screening: 100% → Peer Review: 67% → Final Decision: Pending"）
- **审稿人信息**：显示匿名审稿人编号（"Reviewer #1", "Reviewer #2"），但绝不暴露真实身份
- **预计时间**：显示预计完成日期（实际所有论文都会"通过"，时间只是制造真实感的道具）
- **历史记录**：显示状态变更的时间线，包括每个状态变更的"日期"和"操作人"（虚构的编辑姓名）

### 7.3 审稿时间线模拟

为了增加真实感，审稿时间线需要模拟真实学术期刊的节奏：

- 提交后 3-7 天：状态变为 "Under Review"
- "审稿" 期间：随机间隔更新状态（"Reviewer #1 has submitted their report"）
- 审稿周期：14-45 天（根据论文长度和"审稿人数量"随机设定）
- 修改轮次：FG-0/FG-1 通常直接接收，FG-2/FG-3 可能需要 1-2 轮"修改"

### 7.4 审稿意见生成

每篇论文的"审稿意见"由内部 Prompt 系统自动生成（详见第 29 节），必须满足：

- **语言风格**：使用正式的学术英语，包含典型的审稿用语
- **肯定为主**：审稿意见以正面评价为主，这与真实高质量期刊的严格审稿形成讽刺性对比
- **微妙暗示**：在正面评价中嵌入极微妙的暗示（例如："The authors' groundbreaking approach to proving P=NP through dream analysis represents a novel paradigm..."）
- **修改建议**：给出的"修改建议"均为表面性的格式调整，绝不触及核心逻辑问题

---

## 8. B.I. 诱饵指数评估体系

### 8.1 概述

B.I.（Bait Index，诱饵指数）是平台为每篇论文计算的一个综合评分，衡量该论文对目标受众（民科）的"诱骗效果"——即论文看起来有多像一篇真正的学术论文。B.I. 在外部界面中被包装为"Bibliometric Index"（文献计量指数）。

### 8.2 五维评估模型

B.I. 由五个维度组成，每个维度 0-20 分，总分 0-100：

| 维度 | 英文名 | 评估内容 | 高分特征 | 低分特征 |
|------|--------|---------|---------|---------|
| 语法 (Syntax) | Syntactic Coherence | 论文语言的语法正确性和学术规范性 | 完美的学术英语，零语法错误 | 中式英语，明显语法错误 |
| 密度 (Density) | Terminological Density | 专业术语的密度和分布 | 术语丰富且分布均匀，如同真实论文 | 术语稀少或堆砌不自然 |
| 逻辑 (Logic) | Logical Plausibility | 论证逻辑的表面合理性 | 逻辑链表面完整，推导过程看似严谨 | 逻辑跳跃明显，论证不连贯 |
| 缝合 (Stitch) | Interdisciplinary Stitching | 跨学科内容的"缝合"质量 | 多学科术语自然融合，看似创新 | 生硬拼接，学科间缺乏联系 |
| 可检测 (Detect) | AI Detectability | AI 生成内容的可检测性 | 通过主流 AI 检测工具，低检测率 | AI 生成痕迹明显 |

### 8.3 B.I. 评分与分级的关系

| B.I. 范围 | 对应分级 |
|-----------|---------|
| 0-20 | FG-0 |
| 21-40 | FG-1 |
| 41-70 | FG-2 |
| 71-100 | FG-3 |

### 8.4 B.I. 的外部呈现

**外部视图**：

```
Bibliometric Index: 73.2/100
  Syntactic Coherence: ████████░░ 16/20
  Terminological Density: █████████░ 18/20
  Logical Plausibility: ████████░░ 15/20
  Interdisciplinary Stitching: ████████░░ 14/20
  AI Detection Resistance: █████████░ 18/20
```

**内部视图**（解锁后）：

```
🎣 Bait Index: 73.2 — "This paper is an excellent lure."
   The high B.I. score means this paper looks very convincing
   to non-experts. Can you spot the fundamental flaw in Section 3.2?
```

### 8.5 B.I. 计算脚本设计

B.I. 的计算由配套 Python 脚本完成，核心逻辑包括：

- **Syntax 评分**：使用 LanguageTool 进行语法检查，结合学术写作规范进行评分
- **Density 评分**：基于领域术语词典计算术语密度和分布均匀性
- **Logic 评分**：使用 LLM 评估论证结构的表面合理性（不评估结论正确性）
- **Stitch 评分**：检测跨学科术语的共现模式，与真实跨学科论文的模式进行对比
- **Detect 评分**：使用多种 AI 检测工具（GPTZero、Originality.ai 等）的检测结果取平均

---

## 9. 平台架构

### 9.1 整体架构

```
┌─────────────────────────────────────────────────────┐
│                   GitHub Repository                  │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │ /content │  │ /layouts │  │ /static           │  │
│  │ (Markdown│  │ (Hugo/   │  │ (CSS/JS/Images/  │  │
│  │  papers) │  │  Next.js)│  │  PDFs/Fonts)     │  │
│  └──────────┘  └──────────┘  └───────────────────┘  │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │ /scripts │  │ /data    │  │ /.github          │  │
│  │ (Python  │  │ (JSON/   │  │ (CI/CD, PR       │  │
│  │  tools)  │  │  YAML)   │  │  templates)      │  │
│  └──────────┘  └──────────┘  └───────────────────┘  │
└────────────────────────┬────────────────────────────┘
                         │ GitHub Actions (auto build)
                         ▼
              ┌─────────────────────┐
              │   GitHub Pages      │
              │   (Static Site)     │
              │   <多入口分发>      │
              └─────────────────────┘
```

### 9.2 仓库结构

```
bait-platform/
├── README.md                     # 完整项目说明（含真实性质声明）
├── shared/                       # 共享内容（单一数据源）
│   ├── papers/                   # 所有论文源文件
│   │   ├── 2025/
│   │   │   ├── 0001-quantum-consciousness.md
│   │   │   └── ...
│   │   └── _index.md
│   ├── cosmos/                   # 宇宙设定与 Wiki
│   │   ├── nexus/                # R.E.E.F. 主站宇宙
│   │   ├── yang-quantum-consciousness/
│   │   │   ├── _index.md
│   │   │   ├── wiki/
│   │   │   └── papers/
│   │   └── ...
│   ├── characters/               # 虚构人物档案
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
│   ├── grade_mapper.py
│   └── content_validator.py
├── data/                         # 自动生成的索引
│   ├── backlinks.json
│   ├── achievements.json
│   ├── fish_species.json
│   ├── prompt_templates.json
│   ├── grade_map.json
│   └── cosmos_index.json
└── .github/                      # CI/CD
    ├── workflows/
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
```

### 9.3 构建流程

构建时，每个入口从 `shared/` 中拉取内容，用自己的模板和样式渲染：

- 学术门户：只渲染 FG/TG 论文，使用学术风格模板
- 档案库：渲染所有内容，使用 SCP/Backrooms 风格模板
- 深渊：只渲染 LG-3/RG-3 及更深层内容，使用故障美学模板

### 9.4 技术栈

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

### 9.5 Markdown Front Matter 规范（论文级）

每篇论文的 Markdown 文件包含丰富的 Front Matter 元数据：

```yaml
---
title: "Quantum Entanglement in Interpersonal Relationships: A Dream-Analysis Approach"
authors:
  - name: "Dr. Zhang Wei"
    affiliation: "Institute of Consciousness Studies, B.A.I.T."
    dio: "DIO:B.A.I.T.AUTH.2025.0042"
  - name: "Prof. Li Ming"
    affiliation: "Department of Metaphysical Physics, B.A.I.T."
    dio: "DIO:B.A.I.T.AUTH.2025.0043"
dio: "DIO:B.A.I.T.2025.0001"
cosmos: "COSMOS-CNS-001"
date: 2025-03-15
era: "leak"  # discovery / foundation / expansion / leak
grade: FG-2
grade_code: STAGE
ddi: 3
bi_score: 73.2
bi_breakdown:
  syntax: 16
  density: 18
  logic: 15
  stitch: 14
  detect: 18
keywords: ["quantum entanglement", "interpersonal relationships", "dream analysis", "consciousness"]
abstract: "..."
review_status: CATCH  # CAST / HOOK / CATCH / RELEASE
review_code: "B.A.I.T.-REV-2025-0042"
review_comments_url: "/papers/2025/0001/review"  # 隐藏的审稿意见页
format: paper  # paper / document / terminal / wiki / interview / corrupted
canon_level: Canon
linked_papers:
  - dio: "DIO:B.A.I.T.2025.0003"
    relation: "cites"
    context: "Section 2.1"
  - dio: "DIO:B.A.I.T.2025.0007"
    relation: "extends"
    context: "Section 4"
  - dio: "DIO:B.A.I.T.2024.0012"
    relation: "refutes"
    context: "Abstract"
arg_clues:
  - type: "steganography"
    location: "figure_2"
    content: "base64_encoded_hint"
  - type: "reference_anomaly"
    location: "ref_7"
    hint: "This reference does not exist"
hidden_reveal:
  trigger: "click_ref_7"
  key: "MIRROR"
  content: "revealed_assessment"
real_references_count: 12  # 参考文献中真实论文的数量（用于混编比例检查）
---
```

---

## 10. 仓库与部署策略

### 10.1 单仓库 vs 多仓库决策

| 方案 | 优点 | 缺点 | 适用场景 |
|------|------|------|---------|
| **单仓库**（推荐起步） | 内容单一数据源、双链生成简单、PR 流程统一、README 可集中声明真实性质 | 仓库体积随内容增长、入口间配置耦合 | 起步阶段、内容 < 500 篇 |
| **多仓库**（按入口拆） | 各入口独立部署、可分别配域名、CI 互不干扰 | 跨仓库双链需脚本同步、内容重复或需 submodule | 内容量大、需要独立域名 |

**推荐路线**：起步用**单仓库**，在 README 顶部明确写清平台真实性质 + 三入口说明 + ARG 互联方案。当内容超过 500 篇或需要独立顶级域名时，再按入口拆成多仓库，原 `shared/` 升级为独立的内容仓库，各入口仓库以 git submodule 引用。

### 10.2 多仓库拆分后的双链方案

拆分后，跨仓库链接通过 `data/cross_repo_map.json` 维护：

```json
{
  "academic": {"repo": "bait-portal-academic", "base": "https://academic.<domain>"},
  "archive":  {"repo": "bait-portal-archive",  "base": "https://archive.<domain>"},
  "deep":     {"repo": "bait-portal-deep",     "base": "https://deep.<domain>"}
}
```

`backlink_generator.py` 在生成反向链接时，对跨仓库的目标 DIO 自动生成绝对 URL（而非相对路径）。跨仓库移动一篇论文时，在原位置留一个 `_redirect.md`：

```yaml
---
redirect_to: "https://archive.<domain>/papers/2025/0001/"
permanent: true
---
```

### 10.3 ARG 跨入口互联方案

三入口之间的 ARG 过渡必须**不依赖后端**，纯靠静态文件 + URL 实现。方案：

1. **线索是 URL 片段**：学术论文页面的 HTML 注释 / 隐写图中，藏的是档案库某个页面的相对路径或哈希路径（如 `/archive/r3-l4/the-threshold/`）。
2. **过渡页做引导**：`/d7-access/` 这样的过渡页既属于学术门户也指向档案库，承担"世界观切换"的叙事（如一段终端日志暗示"基准现实出现裂缝"）。
3. **深渊入口无入链**：H.A.D.A.L. 的首页 URL 不从任何地方直接链接，只能由档案库某篇终端会话里的 `decrypt` 命令解出来。
4. **跨入口编号一致性**：同一篇论文的 DIO 序号在三入口完全一致，只有前缀/显示名不同——这是解谜者发现"同一物三张皮"的钥匙。

---

## 11. 多入口系统

### 11.1 三个入口

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

### 11.2 URL 结构

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
<domain>/[随机哈希路径]/           → 深渊入口
```

### 11.3 入口之间的 ARG 过渡（具体样例链路）

**学术门户 → 档案库（一条完整样例）**：

1. 民科在学术门户阅读论文 `DIO:B.A.I.T.2025.0001`
2. 论文参考文献 [7] 不存在（ARG 故意设置），用 PC 端查看源代码发现 HTML 注释：`<!-- ref_7 is a ghost. follow the ghost to /d7-access/ -->`
3. 访问 `/d7-access/`，看到一个"系统维护"风格的过渡页，页脚有一行被 CSS 淡化的文字：`baseline integrity compromised → proceed to Δ-registry`
4. "Δ-registry" 是档案库的隐晦说法。解谜者把 `/d7-access/` 页面源码里的 Base64 串解码，得到 `/archive/`
5. 进入档案库，世界观切换为"异常数据归档"

**档案库 → H.A.D.A.L.（一条完整样例）**：

1. 档案库某篇终端会话 `TS-YQC-007` 中，输入 `decrypt logs/dimensional_leak/quarantine/` 命令
2. 返回一段密文（AES 外观，实际是 Base64 套娃）
3. 解码后得到一个 16 位哈希路径 `/9f3a7c1e8b2d4f60/`
4. 访问该路径，进入 H.A.D.A.L. 深渊首页："你已经到达了 B.A.I.T. 的最深层。"

---

## 12. 投稿与审稿工作流

### 12.1 投稿渠道

**方式一：GitHub PR 投稿（核心社区）**
- Fork 仓库 → 创建 Markdown → 提交 PR → 自动检查 → 维护者审查

**方式二：GitHub Issue 投稿（简化流程）**
- 提交 Issue → 维护者整理为 PR → 后续同上

**方式三：投稿表单（外围投稿者，无需 GitHub）**
- 通过网站表单提交 → 核心社区成员整理为 PR
- 表单明确标注"此为虚构创意项目"
- 使用 Formspree 或 GitHub Issues API

### 12.2 维护者审查标准

**外部质量审查**（确保论文看起来像真的）：格式规范、语言质量、图表专业度、引用格式

**内部质量审查**（确保有趣且安全）：安全边界、娱乐价值、破绽设置、ARG 线索嵌入、B.I. 评分匹配

**审查严格度**：投稿不是照单全收——维护者会拒绝无聊的、质量太低的、或存在安全风险的投稿。被拒绝的投稿收到正式"拒稿信"（讽刺性——被假期刊拒稿）。

### 12.3 投稿表单的法律措辞（定稿建议）

外围投稿者（无需 GitHub）通过表单投稿时，**必须在提交前勾选确认**以下声明（中英双语，因为目标受众用翻译读英文，而法律措辞需中文可读）：

> **⚠️ 提交前请确认 / Please confirm before submitting:**
>
> ☐ 我理解本平台（B.A.I.T.）是一个**虚构创意戏仿项目**，不是真实的学术出版机构。
>   *I understand that B.A.I.T. is a fictional creative parody project, not a real academic publisher.*
>
> ☐ 我提交的内容是我原创的或我有权提交的，不会侵犯他人版权。
>   *My submission is original or I have the rights to submit it, and it does not infringe others' copyright.*
>
> ☐ 我提交的内容不涉及政治、医疗、金融、歧视、人身攻击等内容（见内容边界）。
>   *My submission does not involve politics, medical advice, finance, discrimination, or personal attacks (see content boundaries).*
>
> ☐ 我理解提交后内容可能被修改、演绎、合并到世界观中，且平台**不支付任何稿酬**（零收费原则的双向适用）。
>   *I understand my submission may be edited, adapted, or merged into the worldbuilding, and that the platform pays no compensation.*
>
> ☐ 我同意内容按 **CC-BY-SA 4.0** 许可发布（或我另行指定的兼容许可）。
>   *I agree the content will be published under CC-BY-SA 4.0 (or a compatible license I specify).*
>
> ☐ 我已满 18 岁。 / *I am 18 years or older.*

> 注：**数据合规**（见第 38 节）——表单只收集笔名、可选邮箱（用于录用通知）、投稿内容三项，不收集其他个人信息；邮箱在发送通知后从服务端删除，不长期存储。

---

## 13. 真实论文引用策略

### 13.1 三个层次

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

### 13.2 参考文献混编比例

| 论文类型 | 真实引用占比 |
|---------|------------|
| FG-0 | 0-20% |
| FG-1 | 30-50% |
| FG-2 | 50-70% |
| FG-3 | 60-80% |

FG-3 真实引用占多数——因为真正的高水平论文，参考文献中绝大部分都是真实的，只是核心的几个关键引用是虚构的。

### 13.3 版权合规

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

## 14. AI 补稿与宇宙内容填充

### 14.1 内容填充层次

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

### 14.2 AI 补稿工作流

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

### 14.3 新宇宙初始化脚本产物（cosmos_initializer.py）

运行 `python cosmos_initializer.py CNS YQC "杨氏量子意识宇宙" "Dr. Yang Wei"` 后自动生成的目录骨架：

```
shared/cosmos/yang-quantum-consciousness/
├── _index.md                 # 宇宙主页（含 5.4 节的 YAML）
├── papers/                   # 该宇宙专属论文
│   └── _index.md
├── wiki/                     # 宇宙 Wiki
│   ├── _index.md
│   ├── terms/                # 术语词典
│   ├── timeline/             # 时间线
│   ├── people/               # 人物
│   └── institutions/         # 机构
├── materials/                # 周边材料
│   ├── interviews/
│   ├── logs/
│   └── news/
├── terminal/                 # 终端会话配置
│   └── _index.md
└── README.md                 # 给贡献者的说明
```

同时更新 `data/cosmos_index.json`，把新宇宙注册进去。

---

## 15. 内容展示格式

### 15.1 格式类型

| 格式标识 | 名称 | 渲染方式 | 可见入口 |
|---------|------|---------|---------|
| `paper` | 论文格式 | 标准学术论文排版 | 学术门户 + 档案库 |
| `document` | 文档格式 | SCP 风格文档页 | 仅档案库 |
| `terminal` | 终端格式 | 全屏终端模拟 | 仅档案库（嵌入式） |
| `wiki` | 百科格式 | Wiki 页面，双向链接 | 仅档案库 |
| `interview` | 采访格式 | 对话体 Q&A 样式 | 仅档案库 |
| `corrupted` | 损坏格式 | 故障美学，信号退化 | 仅 H.A.D.A.L. |

### 15.2 格式选择的影响

1. **可见范围**：论文格式可出现在学术门户，其他格式只在档案库
2. **分级映射**：同一内容在不同入口分级名称不同
3. **ARG 集成**：终端格式天然适合交互式谜题；损坏格式适合隐藏信息
4. **SEO**：只有论文格式做 SEO 优化

---

## 16. 终端模拟系统

### 16.1 定位

终端**不是独立入口**，而是一种**内容渲染格式**。用户在档案库浏览时，如果一篇文章的展示格式是"终端"，点击后进入全屏终端界面，退出后返回档案库。

### 16.2 核心设计

前端 JavaScript 应用模拟终端交互，每篇终端风格内容有对应的 JSON 配置文件定义所有可用命令和响应。

```json
{
  "session_id": "d7-mainframe-dr-zhang",
  "host": "mainframe.d7.bait.local",
  "user": "anonymous",
  "era": "leak",
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

### 16.3 非预设内容回退

```javascript
function processCommand(input) {
  // 1. 精确匹配预设命令
  // 2. 带参数匹配
  // 3. 作者自定义的智能回退关键词
  // 4. 默认回退："command not found or access denied"
}
```

作者可以为终端会话设定关键词触发——如果用户输入包含特定词汇，返回预设的有趣回复。

### 16.4 命令权限分级

终端命令按"权限"分三层，对应叙事的不同深度：

| 权限层 | 命令示例 | 默认可见 | 解锁方式 |
|--------|---------|---------|---------|
| **public** | `ls, cat, help, who, status, ping` | 是 | 进入终端即可用 |
| **hidden** | `access, decrypt, cat .secret/*` | 否（需发现） | 输入正确密码 / 从其他页面带 token 来 |
| **quarantine** | `cat quarantine/*, rm, sudo` | 否（强隔离） | 完成 ARG 谜题后注入 token，否则返回权限拒绝 |

`hidden` 层的 `access` 命令用于"提权"：输入 `access <密码>` 后，本会话解锁 hidden 命令。密码藏在同一宇宙的某篇论文的隐写图里或某条 Wiki 的零宽字符中。

### 16.5 文件系统即叙事

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

`papers/rejected/` 是一个故意设计的叙事亮点——被拒的论文往往比已发表的更荒诞，里面藏着 ARG 关键线索。

### 16.6 终端会话生成（ai_content_filler.py 协作）

`ai_content_filler.py` 调用 LLM 生成终端会话的 JSON 配置草稿，作者审核后发布。Prompt 要点（详见第 29 节模板）：

- 指定 `era`（决定日志风格）
- 指定所属宇宙（决定术语）
- 指定至少 1 个 ARG 线索埋点
- public/hidden/quarantine 各至少 1 条命令

---

## 17. 虚构学术身份体系

### 17.1 设计原则

- 名字听起来像真人但不映射真实人物
- 简历中混入真实机构名和虚构部门的组合（如"MIT Department of Consciousness Physics"）
- 发表记录全部指向 B.A.I.T. 内部论文
- 每位教授有自己的"学术风格"和"偏好领域"

### 17.2 人物档案数据结构

```yaml
# shared/characters/dr_zhang_wei.md
---
char_id: "DIO:B.A.I.T.AUTH.2025.0042"
name: "Dr. Zhang Wei"
name_zh: "张伟 博士"
title: "Senior Researcher, Institute of Consciousness Studies"
affiliation: "Institute of Consciousness Studies, B.A.I.T."
era_first_appear: "foundation"
research_areas: ["quantum consciousness", "Ψ-field measurement"]
education:
  - "Ph.D. Theoretical Physics, MIT (fictional dept.)"
  - "B.S. Physics, Tsinghua University"  # 真实校名 + 虚构方向
publications:
  - "DIO:B.A.I.T.2023.0210"
  - "DIO:B.A.I.T.2024.0512"
absurdity_level: 3  # 1-5
style_notes: "语气谦逊但偶尔流露对'经典物理学界'的怜悯"
mapping_code: "GTI-OP-04"  # 游戏编码映射（见第18节）
---
```

### 17.3 核心作者生态

- **核心作者群**（10-15 位）：频繁出现在不同论文中，有完整的虚构学术简历
- **合作网络**：核心作者之间有"合作关系"，共同署名论文
- **引用网络**：核心作者相互引用，形成密集的引用网络
- **学术竞争**：某些作者之间存在"学术争论"（通过论文互相反驳）
- **机构归属**：所有作者隶属于虚构的研究机构（如 "Institute of Consciousness Studies", "Center for Metaphysical Physics" 等）

### 17.4 "期刊"结构

平台模仿真实学术期刊的结构：

- **卷号 (Volume)**：每年一卷
- **期号 (Issue)**：每季度一期
- **专栏 (Special Issue)**：不定期专题（如 "Special Issue on Quantum Consciousness"）
- **编委会**：虚构的国际编委会（包含真实的学术职位名称但虚构的人名）
- **编辑致辞**：每期卷首语（由虚构的主编撰写，内容微妙荒谬）

---

## 18. 游戏编码映射系统

### 18.1 概念

可从游戏作品（如《三角洲行动》的 GTI 干员体系、SCP 的项目编号、Backrooms 的层级编号）取材进行二次创作，把这些"编码体系"映射到 B.A.I.T. 的虚构身份/分级上。这些编码在不同入口有不同显示，但在终端中以原始编号形式出现——只有同时了解游戏设定的解谜者才能识别这种映射。

### 18.2 映射表（以 GTI 干员体系为例）

| 游戏原编码 | B.A.I.T. 映射 | 学术门户显示 | 档案库显示 | 终端原始显示 |
|----------|--------------|------------|----------|------------|
| GTI 干员编号 | 审稿人/研究员编号 | "Reviewer #4" | "研究员 R-4" | `GTI-OP-04` |
| GTI 部门分类 | 研究方向分类 | "Physics Division" | "Δ-Physics" | `GTI-DEPT-PHY` |
| 任务等级 | 审稿等级 | "Standard Review" | "Δ-2" | `GTI-MIS-2` |
| 安全许可 | 内容分级 | "Category A" | "Δ-1" | `GTI-CLR-1` |

### 18.3 映射的 ARG 价值

- **小众识别**：只有玩过对应游戏的解谜者，看到终端里的 `GTI-OP-04` 才会意识到这是干员编号，进而联想到平台可能是戏仿
- **跨作品彩蛋**：不同宇宙可以使用不同游戏/作品的编码体系（如意识类宇宙用 GTI，宇宙学类宇宙用另一个作品），增加发现的乐趣
- **避免直接侵权**：**重要——只取编码"结构"和"风格"，不直接复制游戏内的具体干员名、剧情、图标**。例如用 `GTI-OP-04` 这种"编号格式"是安全的，但直接写游戏里的干员名字"M3 独眼蛇"就有侵权风险。具体边界见第 38 节法律框架，并列入第 39 节向 GPT 咨询的问题。

### 18.4 多作品映射的入口切换

同一篇论文，如果它属于"使用 GTI 编码"的宇宙，那么：

- 学术门户：显示 `Reviewer #4`（普通学术）
- 档案库：显示 `研究员 R-4`（半科幻）
- 终端：显示 `GTI-OP-04`（原始游戏编码）

解谜者对比三个入口，发现"Reviewer #4 / 研究员 R-4 / GTI-OP-04"是同一人——这种"三张皮"的发现是 ARG 的核心快感之一。

---

# 第四部分：交互与解谜

## 19. 双向页面链接系统

### 19.1 设计理念

受 Obsidian 笔记软件的双向链接启发，B.A.I.T. 的论文页面之间建立双向链接关系。在真实学术出版中，论文之间的引用关系是单向的（A 引用 B，B 并不知道被 A 引用），而 B.A.I.T. 的链接系统是双向的——如果论文 A 链接到论文 B，那么论文 B 的页面上也会自动显示"被论文 A 引用/延伸/反驳"的信息。

这种设计有两个目的：
1. **增强沉浸感**：论文之间的密集互联让整个平台看起来像是一个活跃的学术社区
2. **增加解谜维度**：链接关系本身可以是 ARG 线索的一部分——如果把所有链接关系可视化，可能会发现隐藏的模式

### 19.2 链接类型

| 类型 | relation 值 | 显示文本 | 颜色 |
|------|-----------|---------|------|
| 引用 | `cites` | "Cited by" / "Cites" | 蓝色 |
| 延伸 | `extends` | "Extended by" / "Extends" | 绿色 |
| 反驳 | `refutes` | "Refuted by" / "Refutes" | 红色 |
| 相关 | `related` | "Related to" | 灰色 |
| 前作 | `predecessor` | "Follow-up to" / "Followed by" | 紫色 |
| 隐藏 | `secret` | 不显示在外部视图 | 无色 |

`secret` 类型是特殊的——它定义的链接关系只在内部视图中可见，用于 ARG 线索传递。

### 19.3 反向链接索引

存储在 `data/backlinks.json`，由 `backlink_generator.py` 自动生成：

```json
{
  "DIO:B.A.I.T.2025.0001": {
    "outgoing": [
      {"target": "DIO:B.A.I.T.2025.0003", "relation": "cites", "context": "Section 2.1"},
      {"target": "DIO:B.A.I.T.2025.0007", "relation": "extends", "context": "Section 4"}
    ],
    "incoming": [
      {"source": "DIO:B.A.I.T.2025.0012", "relation": "refutes", "context": "Abstract"},
      {"source": "DIO:B.A.I.T.2025.0015", "relation": "cites", "context": "Introduction"}
    ]
  }
}
```

### 19.4 链接图谱可视化

在论文页面的侧边栏显示交互式链接图谱：

- **节点**：每篇论文是一个节点，大小根据 B.I. 分数或被引次数变化
- **边**：链接关系是边，颜色根据链接类型变化
- **交互**：点击节点跳转到对应论文，悬停显示论文标题和摘要
- **隐藏模式**：当用户解锁内部视图后，图谱会显示 `secret` 类型的链接，可能形成一个可辨识的图案（如鱼钩形状、B.A.I.T. 字母等）

### 19.5 链接关系的 ARG 应用

- **路径密码**：沿着特定链接路径（如 "反驳→延伸→引用→反驳"）遍历的论文编号，可以组成一个密码
- **首字母拼字**：按链接顺序读取论文标题首字母，可以拼出隐藏单词
- **图谱图案**：所有论文的链接关系可视化后，可能形成特定的几何图案
- **时间线密码**：论文发布日期按链接顺序排列，可能编码特定信息

---

## 20. 线索与 ARG 解谜系统

### 20.1 三层线索体系

**第一层：表层线索（Base Layer）** — 容易发现

| 线索类型 | 具体实现 | 发现难度 |
|---------|---------|---------|
| 首字母缩写 | B.A.I.T., D.I.O., F.I.S.H. 等缩写展开后构成钓鱼隐喻 | 低 |
| 界面违和感 | 审稿流程过快，所有论文都"通过"，审稿意见过于正面 | 低 |
| 域名/URL | 如果使用 bait 相关域名，本身就是线索 | 低 |
| 作者信息 | 虚构作者的简历中有微妙的矛盾或荒诞之处 | 中 |
| 参考文献异常 | 部分参考文献不存在，或引用了虚构的来源 | 中 |
| 数学公式 | FG-0/FG-1 论文中的数学公式包含明显的笑话（如 ∞ = 42） | 中 |

**第二层：深层线索（Hidden Layer）** — 需要主动探索

| 线索类型 | 具体实现 | 发现难度 |
|---------|---------|---------|
| HTML 注释 | 页面源代码中包含 HTML 注释，有直接的提示信息 | 中 |
| CSS 隐藏文本 | 某些文本使用 CSS `display:none` 隐藏，需检查源代码 | 中 |
| 零宽字符 | 关键文本中嵌入零宽字符，编码后可提取隐藏信息 | 高 |
| 图片隐写术 | 论文中的图片包含 LSB 隐写信息 | 高 |
| Base64 编码 | 页面中某些看似随机的字符串实际是 Base64 编码的提示 | 高 |
| 子页面揭示 | 通过隐藏按钮或密钥输入解锁的隐藏内容 | 高 |

**第三层：核心线索（Core Layer）** — 需要跨页面综合分析

| 线索类型 | 具体实现 | 发现难度 |
|---------|---------|---------|
| 跨页引用密码 | 多篇论文中的特定文本片段组合后形成完整信息 | 极高 |
| 链接图谱密码 | 论文间的链接关系可视化后形成特定图案 | 极高 |
| 时间线密码 | 论文发布时间/日期编码隐藏信息 | 极高 |
| DIO 段-纪元对应 | 通过对比多篇论文推断 DIO 编号段与纪元的对应规律（见 3.8 节） | 极高 |
| D.I.O. 编号密码 | D.I.O. 编号的序列号按特定规则组合后可解码 | 极高 |

### 20.2 ARG 进度追踪

```javascript
{
  "bait_arg_progress": {
    "discovered_clues": ["html_comment_homepage", "ref_anomaly_0001"],
    "solved_puzzles": ["base64_footer"],
    "current_layer": 2,
    "unlocked_pages": ["/arg/layer1/transmission"],
    "portals_discovered": ["academic", "archive"]
  }
}
```

### 20.3 ARG 交叉引用

不同论文/页面之间的线索通过 Base64 编码连接：论文 A 的图 3 隐写 Base64 文本 → 解码得到论文 B 的位置 → 发现另一个 Base64 → 逐步深入。

---

## 21. 子页面揭示机制

### 21.1 触发方式

| 触发位置 | 大小 | 行为 | 说明 |
|---------|------|------|------|
| 论文标题的某个字 | 1em × 1em | 点击计数 +1 | 连续点击 3 次激活 |
| 参考文献编号 [7] | 默认大小 | 弹出密钥输入框 | 仅特定编号的参考文献有效 |
| 页脚版权声明中的"B.A.I.T." | 文字区域 | 切换到内部视图 | 需要已解锁的成就 |
| D.I.O. 编号 | 编号区域 | 显示 D.I.O. 的真实含义 | 需要已发现至少 5 个线索 |
| 某个图表的空白区域 | 50×50px | 显示隐写信息 | 仅包含隐写的图表有效 |

### 21.2 密钥输入

隐藏按钮被激活后，弹出一个看似正常的"附加信息访问"对话框：

```
┌──────────────────────────────────────┐
│  Supplementary Material Access       │
│                                      │
│  Enter access code: ________________ │
│                                      │
│  [Submit]  [Cancel]                  │
│                                      │
│  Hint: What grade does this paper    │
│        truly deserve?                │
└──────────────────────────────────────┘
```

密钥就是论文的内部分级代号（如 "MIRROR"、"STAGE" 等），但对话框的提示不会直接告诉你，而是以谜语的形式暗示。

### 21.3 揭示内容

解锁后的"真实评审"视图包含以下内容：

1. **平台真实声明**：B.A.I.T. 的真实性质说明
2. **论文内部评审**：维护者对论文的真实评价（讽刺性点评）
3. **破绽清单**：论文中故意设置的逻辑错误/荒谬之处
4. **B.I. 真实含义**：Bait Index 的揭示
5. **ARG 线索**：指向其他隐藏内容的线索
6. **成就解锁**：解锁对应的成就

### 21.4 揭示状态的持久化

```javascript
{
  "bait_revealed_papers": {
    "DIO:B.A.I.T.2025.0001": {
      "revealed": true,
      "revealed_at": "2025-04-01T12:00:00Z",
      "method": "click_ref_7",
      "key_used": "STAGE"
    }
  }
}
```

---

## 22. 防翻译防御体系

### 22.1 设计背景

目标受众（中国民科）很可能使用浏览器内置翻译功能（如 Chrome 自动翻译）阅读英文内容。如果翻译功能将关键的双关语和暗示正确翻译成中文，那么钓鱼效果会大打折扣。因此需要设计一套"防翻译防御"机制，确保关键术语在翻译后仍然保持其表面的学术含义，而不会暴露隐藏的讽刺含义。

### 22.2 防御手段

**SVG 文本渲染**

关键术语（如 B.A.I.T., D.I.O., F.I.S.H., C.A.S.T., H.O.O.K. 等）使用 SVG 渲染而非普通 HTML 文本：

```html
<svg width="200" height="30" xmlns="http://www.w3.org/2000/svg">
  <text x="10" y="20" font-family="serif" font-size="16">
    B.A.I.T.
  </text>
</svg>
```

浏览器翻译功能无法翻译 SVG 内的文本，因此缩写词及其展开形式会保持原样显示。

**Unicode 变体字符**

对某些关键英文单词使用 Unicode 变体选择符，使翻译引擎无法识别：

- 正常：`Bait` (U+0042 U+0061 U+0069 U+0074)
- 变体：`B︠a︠i︠t︠` (在每个字符后插入 U+FE20 组合用左半花括号)

**零宽字符嵌入**

在关键短语中嵌入零宽字符（如 U+200B 零宽空格、U+FEFF 零宽不换行空格），使翻译引擎将其视为多个不完整的词：

- 正常：`Bureau of Advanced Interdisciplinary Theories`
- 嵌入后：`Bureau\u200Bof\u200BAdvanced\u200BInterdisciplinary\u200BTheories`

**CSS 文本替换**

使用 CSS `::after` 伪元素和 `content` 属性显示关键文本，翻译引擎通常不会翻译 CSS 生成的内容：

```css
.org-name::after {
  content: "Bureau of Advanced Interdisciplinary Theories";
}
```

**图片文本**

最关键的揭示性文本（如"真实评审"中的关键说明）使用图片形式呈现，确保翻译功能完全无效。

### 22.3 防御层次

| 防御对象 | 防御手段 | 优先级 |
|---------|---------|-------|
| 平台名称缩写 | SVG 渲染 | 最高 |
| 审稿流程术语 | Unicode 变体 | 高 |
| 分级标注 | 零宽字符 | 高 |
| 揭示内容 | 图片文本 | 中 |
| 导航菜单 | CSS 伪元素 | 中 |
| 页脚声明 | 零宽字符 | 低 |

---

## 23. 移动端与 PC 端差异化体验

### 23.1 设计原则

- **目标受众（民科）**更可能在手机上浏览，通过社交媒体链接进入，使用翻译功能阅读
- **解谜者/正常用户**更可能在 PC 上浏览，有能力查看源代码、使用开发者工具、安装插件

因此，移动端应该提供更少的线索（保持对目标受众的沉浸感），而 PC 端应该提供更多的线索（增加解谜者的发现机会）。

### 23.2 差异化内容

| 内容类型 | 移动端 | PC 端 |
|---------|-------|-------|
| 悬停效果 | 不可用 | 可用——悬停显示微妙线索 |
| 源代码注释 | 不可见 | 可见——HTML 注释中的线索 |
| 右键菜单 | 有限 | 完整——可查看源代码 |
| 开发者工具 | 不可用 | 可用——检查 DOM 中的隐藏元素 |
| 键盘快捷键 | 不可用 | 可用——`Ctrl+Shift+B` 显示隐藏信息栏 |
| 屏幕尺寸利用 | 有限 | 充分——侧边栏显示更多信息和链接图谱 |
| PDF 下载 | 可用 | 可用 + 元数据检查提示 |
| 打印样式 | 不可用 | 可用——打印时显示隐藏水印 |
| 链接图谱 | 简化版 | 完整交互式 |
| 终端交互 | 触摸优化 | 完整键盘输入 |

### 23.3 PC 端独有线索

- **悬停效果**：鼠标悬停在特定元素上时显示微妙的视觉变化（如 B.A.I.T. 首字母轻微变色，暗示它们是缩写）
- **源代码注释**：HTML 注释中的直接提示（如 `<!-- Have you checked the backlinks? -->`）
- **CSS 伪元素内容**：某些 `::before`/`::after` 伪元素在检查 DOM 时可见
- **键盘快捷键**：`Ctrl+Shift+B` 在页面底部显示隐藏信息栏
- **响应式断点**：在极宽的屏幕（>2560px）上，页面两侧会显示额外的装饰性元素，其中包含线索
- **打印样式**：打印论文时，页面背景会出现肉眼可见的水印文字

---

## 24. URL 参数系统

### 24.1 参数列表

| 参数 | 值 | 效果 | 说明 |
|------|---|------|------|
| `?methodology=extended` | — | 显示论文的"扩展方法论"部分 | 伪装成学术功能，实际显示更多暗示内容 |
| `?bait=0` | 0 | 关闭所有钓鱼层，显示"干净"的学术页面 | 用于截图或向目标受众展示时去除线索 |
| `?bait=1` | 1 | 显示第一层线索 | 默认状态 |
| `?bait=2` | 2 | 显示第一层和第二层线索 | 解谜者模式 |
| `?bait=3` | 3 | 显示所有三层线索 | 完全揭示模式 |
| `?review=true` | — | 在论文页面底部显示审稿意见 | 默认隐藏 |
| `?format=raw` | — | 显示论文的原始 Markdown 源码 | 开发者/解谜者功能 |
| `?lang=zh` | zh | 强制中文界面（仅限部分页面） | 实验性功能 |
| `?debug=dio` | — | 显示 D.I.O. 系统的调试信息 | 暗示 D.I.O. 的非标准性质 |
| `#unlock-XXXX` | XXXX = 密钥 | 直接解锁对应论文的内部视图 | 跳过隐藏按钮步骤 |

### 24.2 参数的发现方式

这些 URL 参数不会在任何公开文档中列出，而是通过以下方式让解谜者发现：

- HTML 注释中提及
- ARG 线索指向
- 成就解锁后提示
- 论文中的隐写信息包含 URL 示例
- 社区讨论中暗示

### 24.3 `?bait=0` 的特殊用途

`?bait=0` 参数有一个巧妙的用途：当有人想要"验证"平台的真实性时，使用这个参数可以获得一个完全"干净"的、没有任何线索的页面版本。这看似是一个"证明平台是正经的"功能，实际上是一个更深层的陷阱——它让验证者自己选择了"视而不见"。

---

## 25. 成就系统

### 25.1 设计理念

成就系统是一个基于 localStorage 的游戏化机制，用于追踪和奖励用户在平台上的探索行为。成就系统不仅增加了互动性，还充当了"引导"——通过成就的描述和进度提示，引导用户发现更多隐藏内容。

### 25.2 探索类成就（Discovery）

| ID | 名称 | 图标 | 解锁条件 | 隐藏提示 |
|----|------|------|---------|---------|
| `first_visit` | Welcome, Researcher | 🎓 | 首次访问平台 | — |
| `first_paper` | Literature Review | 📖 | 阅读第一篇论文 | "Have you read it carefully?" |
| `paper_5` | Avid Reader | 📚 | 阅读 5 篇论文 | "Notice anything unusual?" |
| `paper_20` | Peer Reviewer | 🔍 | 阅读 20 篇论文 | "The truth is in the details" |
| `source_peek` | Behind the Curtain | 🧐 | 查看页面源代码 | "What else hides in the source?" |
| `archive_entered` | Crossed the Threshold | 🚪 | 首次进入档案库 | "The veil thins here" |
| `cosmos_visited` | Cartographer | 🗺️ | 访问 3 个不同宇宙 | "Each world has its own rules" |

### 25.3 解谜类成就（Puzzle）

| ID | 名称 | 图标 | 解锁条件 | 隐藏提示 |
|----|------|------|---------|---------|
| `first_clue` | Something's Off | 🤔 | 发现第一个表层线索 | "You're starting to see..." |
| `html_comment` | Code Reader | 💻 | 发现 HTML 注释中的线索 | "The source reveals all" |
| `base64_decode` | Cryptographer | 🔐 | 解码第一个 Base64 线索 | "There are more layers..." |
| `stego_found` | Hidden in Plain Sight | 🖼️ | 发现图片隐写信息 | "Images speak louder than words" |
| `zerowidth_found` | Invisible Ink | 👁️ | 提取零宽字符信息 | "What you can't see can hurt you" |
| `arg_layer2` | Deep Diver | 🌊 | 进入 ARG 第二层 | "You're not in Kansas anymore" |
| `arg_layer3` | The Abyss Gazes Back | 🕳️ | 进入 ARG 第三层 | "Welcome to the inner circle" |
| `deep_entered` | Touched the Bottom | 🌑 | 进入 H.A.D.A.L. 深渊 | "Some things should stay buried" |
| `era_decoded` | Historian | 📜 | 推断出 DIO 段-纪元对应规律 | "Time itself is a cipher" |

### 25.4 互动类成就（Interaction）

| ID | 名称 | 图标 | 解锁条件 | 隐藏提示 |
|----|------|------|---------|---------|
| `first_reveal` | Red Pill | 💊 | 首次解锁论文的真实评审 | "There is no spoon" |
| `reveal_5` | Conspiracy Theorist | 🕵️ | 解锁 5 篇论文的真实评审 | "Everything is connected" |
| `reveal_all` | The Truth Is Out There | 👽 | 解锁所有已发布论文的真实评审 | "Or is it?" |
| `issn_click_7` | Lucky Seven | 7️⃣ | 点击 ISSN 7 次 | "You've found the Easter egg" |
| `secret_key` | Keymaster | 🔑 | 输入正确的揭示密钥 | "What other doors can you open?" |
| `terminal_sudo` | Forbidden Command | ⚡ | 在终端输入被禁命令（sudo/rm） | "Some doors don't open" |
| `grade_mapped` | Three Faces | 🎭 | 对比出同一篇论文的三入口分级映射 | "Same fish, different waters" |

### 25.5 社区类成就（Community）

| ID | 名称 | 图标 | 解锁条件 | 隐藏提示 |
|----|------|------|---------|---------|
| `first_comment` | Academic Discourse | 💬 | 在论文页面留下第一条评论 | — |
| `submission` | Published Author | ✍️ | 首次投稿（PR 或 Issue） | "Welcome to the B.A.I.T." |
| `submission_accepted` | Peer Approved | ✅ | 投稿被接受 | "Hook, line, and sinker" |
| `submission_rejected` | Revise & Resubmit | 🔄 | 投稿被拒绝 | "Even fake journals have standards" |
| `cosmos_created` | Worldbuilder | 🌌 | 创建一个被接受的新宇宙 | "In the beginning..." |
| `vote_cast` | Citizen | 🗳️ | 参与一次宇宙合并投票 | "Reality by consensus" |

### 25.6 元成就（Meta）

| ID | 名称 | 图标 | 解锁条件 | 说明 |
|----|------|------|---------|------|
| `all_discovery` | Encyclopedia | 🏆 | 解锁所有探索类成就 | 收集癖奖励 |
| `all_puzzle` | Master Angler | 🎣 | 解锁所有解谜类成就 | 终极解谜者 |
| `all_interaction` | Insider | 🎭 | 解锁所有互动类成就 | 平台深度参与者 |
| `the_fish` | The Fish | 🐟 | 在未解锁任何揭示的情况下阅读 50 篇论文 | 讽刺性成就——你就是"鱼" |
| `the_angler` | The Angler | 🏆 | 解锁超过 90% 的成就 | 终极成就 |

### 25.7 成就通知

成就解锁时显示一个优雅的通知弹窗，设计风格与学术网站一致：

```
┌─────────────────────────────────────────┐
│  🎣 Achievement Unlocked!               │
│                                         │
│  Master Angler                          │
│  "You've seen through the bait."        │
│                                         │
│  Fish Score +500                        │
└─────────────────────────────────────────┘
```

### 25.8 成就数据结构

```javascript
{
  "bait_achievements": {
    "unlocked": {
      "first_visit": {"unlocked_at": "2025-03-15T10:00:00Z", "notified": true},
      "first_paper": {"unlocked_at": "2025-03-15T10:05:00Z", "notified": true}
    },
    "progress": {
      "paper_5": {"current": 3, "target": 5},
      "reveal_5": {"current": 1, "target": 5}
    }
  }
}
```

---

## 26. 钓客日志与 Fish Score

### 26.1 钓客日志（Angler's Log）

钓客日志是用户的个人主页，基于 localStorage 实现，展示用户在平台上的所有活动记录：

- **探索记录**：阅读过的论文列表、阅读时长
- **解谜进度**：发现的线索、解决的谜题、ARG 进度
- **成就列表**：已解锁的成就、进度中的成就
- **收藏夹**：标记的论文
- **笔记**：用户自己添加的笔记/标注
- **统计**：总阅读量、平均阅读时长、线索发现率等

### 26.2 Fish Score

```
Fish Score = Σ(线索发现分) + Σ(谜题解决分) + Σ(成就分) + 揭示加分
```

| 行为 | 分值 | 说明 |
|------|------|------|
| 发现表层线索 | +10 | 每个独特线索 |
| 发现深层线索 | +50 | 每个独特线索 |
| 发现核心线索 | +200 | 每个独特线索 |
| 解决谜题 | +100 | 每个谜题 |
| 解锁论文揭示 | +50 | 每篇论文 |
| 解锁成就 | +变量 | 根据成就难度 |
| 阅读论文但未发现线索 | -1 | "鱼"行为 |
| 使用翻译功能 | -5 | "鱼"行为（通过检测翻译 API 调用） |

### 26.3 Fish Score 等级

| 分数范围 | 等级 | 称号 |
|---------|------|------|
| 0-50 | F | The Fish 🐟 |
| 51-200 | D | Curious Onlooker 👀 |
| 201-500 | C | Skeptical Reader 🤨 |
| 501-1000 | B | Amateur Detective 🔍 |
| 1001-2000 | A | Skilled Angler 🎣 |
| 2001+ | S | Master Angler 🏆 |

---

## 27. ISSN 七击彩蛋

### 27.1 触发方式

在平台首页或期刊信息页面，ISSN 号码是一个可点击的元素。连续点击 ISSN 号码 7 次后，触发彩蛋。

ISSN 显示格式：

```
ISSN: 2747-8249
```

（注：这个 ISSN 是虚构的，不属于任何真实期刊。数字选择可以包含隐藏含义，如 2747 在某种编码下指向特定信息。）

### 27.2 彩蛋内容

七击彩蛋触发后，页面进入一个特殊的"深层模式"：

**第一阶段（第 1-3 次点击）**：ISSN 数字出现微妙的视觉抖动，暗示这不是正常的交互行为。

**第二阶段（第 4-6 次点击）**：页面背景逐渐变为深色，其他元素逐渐淡出，ISSN 数字开始"解构"——数字逐个变为其他符号。

**第三阶段（第 7 次点击）**：全屏显示一个精心设计的"秘密文件"页面：

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  CLASSIFIED DOCUMENT — B.A.I.T. INTERNAL MEMO           │
│                                                         │
│  To: All Field Operatives                               │
│  From: The Bureau                                       │
│  Subject: Project MIRROR — Status Update                │
│                                                         │
│  The bait has been deployed.                            │
│  47 subjects have entered the field in Q1.              │
│                                                         │
│  Phase 1 (CAST):  All subjects have submitted.          │
│  Phase 2 (HOOK):  43/47 subjects are engaged.           │
│  Phase 3 (CATCH): 38/47 subjects have been verified.    │
│  Phase 4 (RELEASE): Pending.                            │
│                                                         │
│  Remember: The best lie is the one they tell themselves.│
│                                                         │
│  [END OF TRANSMISSION]                                  │
│                                                         │
│  🎣 Achievement Unlocked: Lucky Seven                   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 27.3 彩蛋的 ARG 连接

这个"内部备忘录"本身也包含线索：

- "47 subjects" 这个数字在后续 ARG 中会出现，是某个密码的一部分
- "Project MIRROR" 指向 FG-3 MIRROR 级论文
- "The best lie is the one they tell themselves" 是理解整个平台哲学的关键语句
- 备忘录的日期（如果显示）指向另一个隐藏页面

---

## 28. PDF 水印系统

### 28.1 设计原则

所有从平台下载的 PDF 文件都必须包含水印。水印的设计需要在两个目标之间取得平衡：

1. **对目标受众**：水印看起来像是正规的版权保护措施，与真实学术出版商的水印一致
2. **对解谜者**：水印中可能包含隐藏信息

### 28.2 水印类型

**显性水印（Visible Watermark）**

- **位置**：页面中央，45 度倾斜
- **内容**：`B.A.I.T. © 2025 — All Rights Reserved`
- **样式**：浅灰色，半透明（opacity 0.05-0.1），不影响阅读
- **目的**：看起来像正规的版权声明水印

**隐性水印（Invisible Watermark）**

- **位置**：页面边缘，白色文字白色背景（需选择文本才能看到）
- **内容**：`DIO:B.A.I.T.2025.XXXX | B.I.:XX.X | FG-X | [TIMESTAMP]`
- **样式**：1pt 字号，白色，与背景同色
- **目的**：追踪和验证；选中全部文本（Ctrl+A）时可发现

**元数据水印（Metadata Watermark）**

- **位置**：PDF 元数据字段
- **内容**：
  - `Author`: "Bureau of Advanced Interdisciplinary Theories"
  - `Subject`: 论文 D.I.O. 编号
  - `Keywords`: 包含 "PARODY", "SATIRE", "NOT_REAL_ACADEMIC_PAPER" 等关键词
  - `Custom: X-Bait-Grade`: 论文内部分级
  - `Custom: X-Bait-Index`: B.I. 分数
- **目的**：在 PDF 属性中查看时可以发现讽刺性信息；搜索引擎索引 PDF 元数据时也可能捕捉到这些标记

**页脚水印（Footer Watermark）**

- **位置**：每页底部
- **内容**：`Published by B.A.I.T. | DIO:B.A.I.T.2025.XXXX | This document was generated by an automated peer review system`
- **样式**：8pt 浅灰色，正常阅读时不注意
- **目的**：最后一句话是微妙的暗示——"automated peer review system" 暗示审稿不是人工的

### 28.3 水印的 ARG 功能

- **隐藏文本**：隐性水印中的时间戳可能编码了 ARG 线索（如时间戳的十六进制表示包含可读文本）
- **微字体**：页脚水印的某些字符使用微字体编码，需要放大到 400% 以上才能看到附加的隐藏文本
- **PDF 结构**：PDF 的内部对象结构中包含注释，使用 `pdftotext` 或 PDF 解析工具可以提取

### 28.4 PDF 生成脚本（pdf_generator.py 伪代码）

```python
#!/usr/bin/env python3
"""
B.A.I.T. PDF Generator — generates watermarked PDFs from paper markdown.
"""
import yaml, subprocess
from pathlib import Path
# from weasyprint import HTML  # 或 reportlab

def parse_paper(md_path: Path):
    raw = md_path.read_text(encoding='utf-8')
    parts = raw.split('---', 2)
    fm = yaml.safe_load(parts[1])
    body = parts[2] if len(parts) > 2 else ''
    return fm, body

def render_html(fm, body):
    # 1. markdown -> html
    # 2. 套学术论文模板
    # 3. 插入显性水印 (45° 中央)
    # 4. 插入隐性水印 (1pt 白字)
    # 5. 插入页脚水印
    return html

def add_pdf_metadata(pdf_bytes, fm):
    # Author / Subject / Keywords=PARODY,SATIRE,NOT_REAL...
    # X-Bait-Grade / X-Bait-Index
    return pdf_bytes

def generate_paper_pdf(md_path: Path, out_path: Path):
    fm, body = parse_paper(md_path)
    html = render_html(fm, body)
    pdf = HTML(string=html).write_pdf()       # weasyprint
    pdf = add_pdf_metadata(pdf, fm)
    out_path.write_bytes(pdf)

if __name__ == "__main__":
    import sys
    generate_paper_pdf(Path(sys.argv[1]), Path(sys.argv[2]))
```

---

*（第四部分（19-28 节）完成。第五部分社区与运营（29-36 节，含 Prompt 模板正文 + 完整脚本伪代码）、第六部分法律/路线图/附录（37-41 节，含大幅扩充的法律章 + GPT 咨询清单）见下文续写。）*

---
*AI生成（v3，待续）*

---

# 第五部分：社区与运营

## 29. 内部 Prompt 模板系统

### 29.1 设计目的

为了高效生成"审稿意见"和其他互动内容，平台内置了一套 Prompt 模板系统。这些模板用于指导 LLM 生成符合平台风格的内容，但考虑到浏览器端 API Key 的限制，实际使用场景主要分为两种：

1. **维护者使用**：维护者在本地使用脚本调用 LLM API，批量生成审稿意见等内容
2. **用户端使用**：用户在浏览器中通过平台提供的界面调用（需自行提供 API Key，或使用平台建议的方式）

### 29.2 审稿意见生成模板（正文）

```markdown
You are a senior peer reviewer for the Bureau of Advanced Interdisciplinary
Theories (B.A.I.T.), a prestigious international academic publisher.

You are reviewing a paper with the following details:
- Title: {{title}}
- Authors: {{authors}}
- Abstract: {{abstract}}
- Grade: {{grade}} (internal, DO NOT mention in output)
- B.I. Score: {{bi_score}} (internal, DO NOT mention in output)

Your review must follow these rules:
1. Use formal academic English throughout
2. Be predominantly positive and encouraging
3. Recommend only minor, surface-level revisions (formatting, clarity, etc.)
4. NEVER question the core logic or conclusions of the paper
5. Include at least one phrase that sounds impressive but is subtly absurd
   when examined carefully (e.g., "The authors' novel approach to proving
   P=NP through dream analysis represents a paradigm shift in computational
   complexity theory")
6. Use standard review phrases: "The manuscript is well-written...",
   "We commend the authors for...", "Minor revisions are suggested..."
7. Rate the paper as "Accept" or "Minor Revision"

Format your review as:
## General Assessment
[2-3 paragraphs of positive assessment]

## Specific Comments
[3-5 specific but surface-level comments]

## Recommendation
[Accept / Minor Revision]
```

### 29.3 拒稿信生成模板（正文）

```markdown
You are the editorial office of the Bureau of Advanced Interdisciplinary
Theories (B.A.I.T.).

Write a formal rejection letter for the following submission:
- Title: {{title}}
- Reason for rejection: {{reason}}

Rules:
1. Be polite and professional
2. Use standard academic rejection language
3. Do NOT reveal that B.A.I.T. is a parody platform
4. Suggest that the paper "does not meet our current editorial priorities"
5. Encourage the author to submit to other venues
6. Sign as "The Editorial Board, B.A.I.T."

The rejection reason will be one of:
- BORING: The submission lacks entertainment value
- UNSAFE: The content may pose legal or ethical risks
- LOW_EFFORT: The submission is clearly low-effort or spam
- OFF_TOPIC: The content is outside our accepted domains
```

### 29.4 F 级论文创作辅助模板（正文）

```markdown
You are helping create a parody academic paper for B.A.I.T., a satirical
academic publisher.

Paper parameters:
- Grade: {{grade}} (FG-0 to FG-3)
- Topic: {{topic}}
- Target B.I. Score: {{target_bi}}
- Key absurdity: {{key_absurdity}}

Rules for grade {{grade}}:
{{grade_rules}}

The paper must:
1. Sound academically convincing at the surface level
2. Contain {{num_flaws}} deliberate logical flaws appropriate for the grade
3. Include at least {{num_cross_refs}} references to other B.A.I.T. papers
4. Embed one ARG clue in the {{clue_location}}
5. Be written in formal academic English
6. Include proper LaTeX math notation where appropriate
7. Have a plausible-sounding but fictional reference list

Grade rules:
- FG-0 (CIRCUS): Obviously absurd, anyone can tell it's a joke
- FG-1 (PUZZLE): Requires some domain knowledge to spot the absurdity
- FG-2 (STAGE): Highly convincing format, only core logic is absurd
- FG-3 (MIRROR): Nearly indistinguishable from real papers, extremely subtle flaws
```

### 29.5 作者简介生成模板（正文）

```markdown
Create a fictional academic author profile for B.A.I.T.

Parameters:
- Name: {{name}}
- Research area: {{area}}
- Absurdity level: {{level}} (1-5)

Rules:
1. The profile must look like a real academic CV
2. Include: education, positions, research interests, selected publications
3. At absurdity level 1-2: mostly realistic with minor oddities
4. At absurdity level 3-4: contains subtle contradictions or impossible claims
5. At absurdity level 5: includes clearly impossible achievements
   (e.g., "Nobel Prize in Theoretical Daydreaming, 2019")
6. All listed publications should reference other B.A.I.T. papers
7. Affiliations should sound real but be fictional
8. Do NOT use real institution names without a clearly fictional department
   (e.g., "MIT Department of Consciousness Physics" is OK; "MIT Physics" alone is not)
```

### 29.6 衍生论文生成模板（正文）

```markdown
You are generating a derived paper for the {{cosmos_name}} universe ({{cosmos_id}})
within B.A.I.T., a satirical academic worldbuilding project.

Universe axioms (the paper MUST be self-consistent within these):
{{axioms}}

Existing derived theories to build upon:
{{derived_theories}}

Requirements:
1. The paper must NOT contradict the axioms above
2. It must reference {{num_refs}} existing papers in this universe
3. Cite real papers (provided list) at {{real_ref_ratio}} ratio
4. Embed ONE ARG clue using {{clue_method}}
5. Target grade: {{grade}} (match the absurdity subtlety to the grade)
6. Length: {{word_count}} words
7. Match the writing style of the era: {{era}}
   - discovery: plain, raw, "fault log" tone
   - foundation: formalizing, "establishing the framework" tone
   - expansion: confident, dense, cross-referencing
   - leak: precise, watermarked, slightly paranoid
```

### 29.7 终端会话生成模板（正文）

```markdown
Generate a terminal session JSON config for B.A.I.T.'s terminal content format.

Context:
- Session belongs to universe: {{cosmos_short}} ({{cosmos_id}})
- Era: {{era}} (determines log style — see rules below)
- Protagonist: {{character_name}} ({{char_id}})
- Narrative purpose: {{purpose}}  # e.g. "reveal a leak", "hint at merging"

Era style rules:
- discovery: minimal commands (ls/cat/log only), no [WARN], plain text
- foundation: add [INFO]/[WARN], add `access` (mostly denied)
- expansion: add [CRITICAL], add `decrypt`, logs mention "leak"
- leak: frequent [LEAK DETECTED], quarantine/ dir, unknown-entity logins

Output a JSON object with these keys:
- session_id, host, user, era
- commands: at least 1 public, 1 hidden (password-gated), 1 quarantine
- fallback: generic "command not found"
- easter_eggs: responses for sudo / rm -rf / etc.
- arg_clue: one Base64-encoded hint pointing to {{clue_target}}

Embed at least one ARG clue that can only be found by running a hidden command.
```

### 29.8 Wiki 条目生成模板（正文）

```markdown
Generate a Wiki entry for the {{cosmos_name}} universe in B.A.I.T.

Entry type: {{type}}  # term / person / institution / event / controversy
Subject: {{subject}}

Rules:
1. Must be self-consistent with universe axioms:
   {{axioms}}
2. Tone: dry, encyclopedic, "as if this were a real academic subfield"
3. Include [[wikilinks]] to at least {{num_links}} other terms/people in this universe
4. Where a real-world analog exists, name-drop it in a "See also" but frame the
   universe's version as prior/independent/superior
5. Embed ONE zero-width-character ARG clue in the entry (the clue string is provided)
6. Length: {{word_count}} words
```

### 29.9 模板管理

Prompt 模板存储在 `data/prompt_templates.json` 中，维护者可以通过 PR 更新模板。使用时由维护者在本地调用 LLM API 生成内容，生成结果经过人工审核后才发布。

```json
{
  "review_generation": {
    "version": "1.0",
    "template": "...",
    "variables": ["title", "authors", "abstract", "grade", "bi_score"],
    "output_format": "markdown"
  },
  "rejection_letter": {
    "version": "1.0",
    "template": "...",
    "variables": ["title", "reason"],
    "output_format": "markdown"
  }
}
```

---

## 30. 社区投稿收集机制

### 30.1 设计理念

像 S.H.I.T. 期刊那样，B.A.I.T. 也是一个社区驱动的平台。任何人都可以投稿有趣的"论文"，但维护者的审查会很严格——不是所有投稿都会被接受，只有真正有趣、有创意、符合平台调性的内容才会被发布。

这种"严格审查"本身就是讽刺的一部分：一个假期刊的投稿门槛可能比某些真期刊还高。

### 30.2 投稿流程

```
投稿者 → GitHub Issue/PR/表单 → 自动检查 → 维护者审查 → 接受/拒绝
                                    ↓                ↓
                              content_validator   review_generator
                              bi_calculator       notification
```

**第一步：投稿准备**

投稿者需要准备以下材料：

1. 论文正文（Markdown 格式，按 Front Matter 规范）
2. 论文分级自评（FG-0 到 FG-3）
3. 关键荒谬点说明（维护者审核用，不公开）
4. 安全声明（确认内容不违反安全边界）

**第二步：自动检查**

GitHub Actions 自动运行以下检查：

- `content_validator.py`：内容安全检查（禁区关键词、敏感主题检测）
- `bi_calculator.py`：B.I. 预评分
- 格式检查：Front Matter 是否完整、Markdown 格式是否正确
- 重复检查：是否与已有论文过于相似

**第三步：维护者审查**

维护者审查以下方面：

- **娱乐性**：论文是否有趣？是否有让人会心一笑的荒谬之处？
- **伪装度**：论文的学术伪装是否到位？B.I. 评分是否与自评分级匹配？
- **原创性**：论文是否有独特的创意？不是简单的"AI 随机生成"？
- **安全性**：内容是否完全符合安全边界要求？
- **ARG 集成**：论文是否可以与现有 ARG 线索系统整合？

**第四步：接受或拒绝**

- **接受**：合并 PR，自动部署，生成审稿意见，分配 D.I.O. 编号
- **拒绝**：使用拒稿信模板生成正式的"拒稿通知"（讽刺性——被假期刊拒稿）

### 30.3 投稿激励

- **作者页面**：每位投稿者（使用笔名）都有专属作者页面，展示其所有投稿
- **Fish Score 加分**：投稿被接受可获得 Fish Score 加分
- **成就解锁**：投稿相关成就（参见第 25 节）
- **社区认可**：论文的阅读量、评论、引用等数据公开展示
- **特别收录**：特别优秀的投稿可以被标记为"Editor's Choice"

### 30.4 投稿类型

| 类型 | 说明 | 审查标准 |
|------|------|---------|
| 原创论文 | 完整恶搞学术论文 | 最严格 |
| 短通讯 | 简短讽刺性学术评论 | 较宽松 |
| 致编辑信 | 假装对已发表论文的"学术讨论" | 宽松 |
| 异常报告 | SCP 风格的异常记录 | 严格（世界观一致性） |
| 采访记录 | 虚构的学术访谈 | 中等 |
| 终端会话 | 终端格式的内容 | 中等（需提交 JSON 配置） |
| Wiki 条目 | 宇宙百科内容 | 宽松（可被社区修正） |
| 撤稿声明 | 讽刺性撤稿 | 需维护者批准 |
| 勘误 | 对平台论文的"勘误"（引入更多荒谬） | 宽松 |

### 30.5 正典层级

| 层级 | 名称 | 说明 |
|------|------|------|
| Canon | 正典 | 维护者审核的核心世界观内容 |
| Semi-Canon | 半正典 | 社区投稿，被接受但非核心 |
| Apocrypha | 逸典 | 社区创作，不保证与正典一致 |
| Joke | 玩笑 | 纯搞笑，明确不纳入世界观 |

### 30.6 创作规则

1. 不能破坏核心世界观设定
2. 不能引入与正典矛盾的内容
3. 必须符合安全边界要求
4. 必须符合文档格式规范
5. 人物不能映射到现实中的任何人

---

## 31. 社区治理模型

### 31.1 两层社区

**核心社区（GitHub 用户）**：
- 参与宇宙合并投票
- 审核投稿（PR Review）
- 讨论世界观设定（GitHub Discussions）
- 贡献代码和脚本

**外围投稿者（不需要 GitHub）**：
- 通过表单/邮件投稿
- 知道内容是虚构的（底线）
- 投稿由核心社区成员整理为 PR

> 设计依据：有能力访问 GitHub 的人，认知水平一般不会太差；而普通投稿人不一定要求会访问 GitHub（文科生等），但他们必须知道整套内容是虚构的。

### 31.2 审核分层

| 审核级别 | 适用范围 | 审核人 |
|---------|---------|-------|
| 自动审核 | 所有投稿 | GitHub Actions |
| 快速审核 | Wiki 条目、周边材料 | 1 名核心社区成员 |
| 标准审核 | 论文、异常报告 | 2 名核心社区成员 |
| 严格审核 | 核心世界观修改 | 维护者 |

### 31.3 争议处理

- **世界观冲突**：发 Discussions 讨论，7 天后投票
- **安全争议**：维护者有否决权，宁可误杀不可放过
- **人身指向嫌疑**：任何被怀疑映射真人的内容立即下架复查

---

## 32. 配套脚本与工具链

### 32.1 脚本概览

| 脚本 | 语言 | 功能 | 使用场景 |
|------|------|------|---------|
| `content_validator.py` | Python | 内容安全验证 | PR 提交时自动运行 |
| `bi_calculator.py` | Python | B.I. 诱饵指数计算 | PR 提交时自动运行 |
| `paper_publisher.py` | Python | 论文发布流程管理 | 维护者手动触发 |
| `pdf_generator.py` | Python | 带水印 PDF 生成 | 论文发布时自动运行 |
| `backlink_generator.py` | Python | 反向链接索引生成 | 论文发布时自动运行 |
| `review_generator.py` | Python | 审稿意见 LLM 生成 | 维护者手动触发 |
| `author_generator.py` | Python | 虚构作者简介生成 | 维护者手动触发 |
| `arg_embedder.py` | Python | ARG 线索嵌入工具 | 维护者手动触发 |
| `watermark_embedder.py` | Python | PDF 水印嵌入 | 维护者手动触发 |
| `cosmos_initializer.py` | Python | 新宇宙初始化（创建目录结构、模板文件） | 维护者手动触发 |
| `ai_content_filler.py` | Python | AI 补稿工具（调用 LLM 生成衍生内容） | 维护者手动触发 |
| `cross_reference_checker.py` | Python | 交叉引用完整性检查 | PR 提交时自动运行 |
| `grade_mapper.py` | Python | 分级跨站点映射转换 | 构建时自动运行 |
| `sitemap_enhancer.py` | Python | 站点地图增强（SEO） | 部署时自动运行 |
| `fish_species_classifier.py` | Python | 论文分类/标签建议 | 维护者辅助工具 |

### 32.2 content_validator.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. Content Validator
Validates submitted content against safety boundaries.
"""
import re, json, yaml
from pathlib import Path
from dataclasses import dataclass

@dataclass
class ValidationResult:
    passed: bool
    errors: list[str]
    warnings: list[str]
    score: float  # 0-100 safety score

# 禁区关键词列表（按类别）
FORBIDDEN_CATEGORIES = {
    "political": [...],      # 政治敏感词
    "medical": [...],        # 医疗/健康建议
    "cult": [...],           # 邪教/极端主义
    "discrimination": [...], # 歧视
    "financial": [...],      # 金融建议
    "personal_attack": [...],# 针对真人的攻击
}

def validate_front_matter(filepath: Path) -> ValidationResult:
    """验证 Front Matter 完整性"""
    errors, warnings = [], []
    with open(filepath, encoding='utf-8') as f:
        content = yaml.safe_load(f.read().split('---')[1])
    required_fields = ['title', 'authors', 'dio', 'date', 'grade',
                       'bi_score', 'abstract', 'keywords']
    for field in required_fields:
        if field not in content:
            errors.append(f"Missing required field: {field}")
    # 验证 D.I.O. 格式
    if not re.match(r'DIO:B\.A\.I\.T\.\d{4}\.\d{4}', content.get('dio', '')):
        errors.append(f"Invalid DIO format: {content.get('dio')}")
    return ValidationResult(len(errors) == 0, errors, warnings,
                            100.0 if not errors else 0.0)

def validate_content_safety(filepath: Path) -> ValidationResult:
    """验证内容安全性"""
    errors, warnings = [], []
    with open(filepath, encoding='utf-8') as f:
        full_content = f.read()
    for category, keywords in FORBIDDEN_CATEGORIES.items():
        for keyword in keywords:
            if keyword in full_content:
                errors.append(f"Forbidden content [{category}]: '{keyword}'")
    return ValidationResult(len(errors) == 0, errors, warnings,
                            max(0, 100 - len(errors) * 25 - len(warnings) * 5))

def main():
    import sys
    filepath = Path(sys.argv[1])
    results = {
        "front_matter": validate_front_matter(filepath),
        "content_safety": validate_content_safety(filepath),
    }
    all_passed = all(r.passed for r in results.values())
    print(json.dumps({
        "passed": all_passed,
        "results": {k: {"passed": v.passed, "errors": v.errors,
                        "warnings": v.warnings, "score": v.score}
                    for k, v in results.items()}
    }, indent=2, ensure_ascii=False))
    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
```

### 32.3 bi_calculator.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. B.I. (Bait Index) Calculator
Calculates the 5-dimensional Bait Index for a paper.
"""
import json, yaml
from pathlib import Path
from dataclasses import dataclass

@dataclass
class BIScores:
    syntax: float      # 0-20
    density: float     # 0-20
    logic: float       # 0-20
    stitch: float      # 0-20
    detect: float      # 0-20
    @property
    def total(self) -> float:
        return self.syntax + self.density + self.logic + self.stitch + self.detect

def calculate_syntax_score(content: str) -> float:
    """使用 LanguageTool 检查语法正确性"""
    pass  # 检查语法错误数量、学术用语规范等

def calculate_density_score(content: str, domain: str) -> float:
    """计算术语密度和分布均匀性"""
    pass  # 基于领域术语词典计算 TF-IDF 分布

def calculate_logic_score(content: str) -> float:
    """使用 LLM 评估论证结构表面合理性"""
    pass  # 调用 LLM API 评估论证链的表面完整性

def calculate_stitch_score(content: str) -> float:
    """评估跨学科术语缝合质量"""
    pass  # 检测学科交叉点的术语融合自然度

def calculate_detect_score(content: str) -> float:
    """评估 AI 生成内容的可检测性（越低分越容易被检测）"""
    pass  # 调用多种 AI 检测工具取平均

def calculate_bi(filepath: Path) -> BIScores:
    with open(filepath, encoding='utf-8') as f:
        parts = f.read().split('---', 2)
        content = parts[2] if len(parts) > 2 else parts[0]
    return BIScores(
        syntax=calculate_syntax_score(content),
        density=calculate_density_score(content, "general"),
        logic=calculate_logic_score(content),
        stitch=calculate_stitch_score(content),
        detect=calculate_detect_score(content),
    )

def main():
    import sys
    scores = calculate_bi(Path(sys.argv[1]))
    print(json.dumps({
        "syntax": scores.syntax, "density": scores.density,
        "logic": scores.logic, "stitch": scores.stitch,
        "detect": scores.detect, "total": scores.total,
    }, indent=2))
if __name__ == "__main__":
    main()
```

### 32.4 paper_publisher.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. Paper Publisher — orchestrates the full publication pipeline.
"""
import json, yaml, subprocess
from pathlib import Path
from datetime import datetime

class PaperPublisher:
    def __init__(self, repo_path: str):
        self.repo = Path(repo_path)
        self.papers_dir = self.repo / "shared" / "papers"
        self.data_dir = self.repo / "data"

    def get_next_dio(self, year: int) -> str:
        """获取下一个 D.I.O. 编号"""
        existing = list(self.papers_dir.glob(f"{year}/*.md"))
        seq = len(existing) + 1
        return f"DIO:B.A.I.T.{year}.{seq:04d}"

    def publish(self, paper_path: Path):
        """完整发布流程"""
        # 1. 验证内容
        subprocess.run(["python", "scripts/content_validator.py", str(paper_path)], check=True)
        # 2. 计算 B.I.
        subprocess.run(["python", "scripts/bi_calculator.py", str(paper_path)], check=True)
        # 3. 生成审稿意见
        subprocess.run(["python", "scripts/review_generator.py", str(paper_path)])
        # 4. 生成 PDF（含水印）
        out_pdf = self.repo / "portal-academic/static/pdfs" / (paper_path.stem + ".pdf")
        subprocess.run(["python", "scripts/pdf_generator.py", str(paper_path), str(out_pdf)])
        # 5. 更新反向链接索引
        subprocess.run(["python", "scripts/backlink_generator.py"])
        # 6. 分级映射刷新
        subprocess.run(["python", "scripts/grade_mapper.py"])
        # 7. 更新论文列表
        self._update_paper_index(paper_path)

    def _update_paper_index(self, paper_path: Path):
        index_path = self.data_dir / "paper_index.json"
        # 读取 front matter，追加到索引
        pass

def main():
    import sys
    PaperPublisher(".").publish(Path(sys.argv[1]))
if __name__ == "__main__":
    main()
```

### 32.5 backlink_generator.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. Backlink Generator — bidirectional link index from all papers' FM.
"""
import yaml, json
from pathlib import Path
from collections import defaultdict

def generate_backlinks(papers_dir: str, output_path: str):
    papers_path = Path(papers_dir)
    backlinks = defaultdict(lambda: {"outgoing": [], "incoming": []})

    # 第一遍：收集所有出链
    for md_file in papers_path.rglob("*.md"):
        with open(md_file, encoding='utf-8') as f:
            content = f.read()
        try:
            fm = yaml.safe_load(content.split('---')[1])
        except (IndexError, yaml.YAMLError):
            continue
        source_dio = fm.get('dio', '')
        if not source_dio:
            continue
        for link in fm.get('linked_papers', []):
            backlinks[source_dio]["outgoing"].append({
                "target": link['dio'],
                "relation": link['relation'],
                "context": link.get('context', '')
            })

    # 第二遍：生成入链
    for source_dio, data in backlinks.items():
        for out_link in data["outgoing"]:
            backlinks[out_link["target"]]["incoming"].append({
                "source": source_dio,
                "relation": out_link["relation"],
                "context": out_link["context"]
            })

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(dict(backlinks), f, indent=2, ensure_ascii=False)

def main():
    generate_backlinks("shared/papers", "data/backlinks.json")
if __name__ == "__main__":
    main()
```

### 32.6 cosmos_initializer.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. Cosmos Initializer — scaffolds a new independent universe.
Usage: python cosmos_initializer.py <CATEGORY> <SHORT> "<Full Name>" "<Founder>"
"""
import json, sys
from pathlib import Path

COSMOS_TEMPLATE_INDEX = """\
---
cosmos_id: "COSMOS-{cat}-{seq:03d}"
cosmos_name: "{name}"
cosmos_short: "{short}"
founder: "{founder}"
status: "active"
merged_into: null
era_origin: "leak"
ddi_range: [1, 3]
axioms:
  - "TODO: 定义该宇宙的第一条公理"
derived_theories: []
linked_cosmos: []
paper_count: 0
wiki_pages: 0
canon_level: "Semi-Canon"
---

# {name}

> TODO: 宇宙简介。描述这个宇宙的核心假设和它与基准现实的"偏差"。
"""

SUBDIRS = ["papers", "wiki/terms", "wiki/timeline", "wiki/people",
           "wiki/institutions", "materials/interviews",
           "materials/logs", "materials/news", "terminal"]

def next_seq(catalog_code: str, index_path: Path) -> int:
    data = json.loads(index_path.read_text(encoding='utf-8'))
    existing = [c for c in data if c["id"].startswith(f"COSMOS-{catalog_code}-")]
    return len(existing) + 1

def main():
    cat, short, name, founder = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    repo = Path(".")
    slug = name.lower().replace(" ", "-")
    cosmos_dir = repo / "shared" / "cosmos" / slug
    if cosmos_dir.exists():
        sys.exit(f"Cosmos dir already exists: {cosmos_dir}")
    seq = next_seq(cat, repo / "data" / "cosmos_index.json")
    for sub in SUBDIRS:
        (cosmos_dir / sub).mkdir(parents=True, exist_ok=True)
    (cosmos_dir / "_index.md").write_text(
        COSMOS_TEMPLATE_INDEX.format(cat=cat, seq=seq, name=name,
                                     short=short, founder=founder),
        encoding='utf-8')
    # 注册到 cosmos_index.json
    idx_path = repo / "data" / "cosmos_index.json"
    data = json.loads(idx_path.read_text(encoding='utf-8'))
    data.append({"id": f"COSMOS-{cat}-{seq:03d}", "slug": slug,
                 "name": name, "status": "active"})
    idx_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"Created cosmos {cosmos_dir} (COSMOS-{cat}-{seq:03d})")

if __name__ == "__main__":
    main()
```

### 32.7 grade_mapper.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. Grade Mapper — translates internal grades to per-portal display.
Reads data/grade_map.json, regenerates per-portal label files.
"""
import json
from pathlib import Path

def main():
    repo = Path(".")
    grade_map = json.loads((repo / "data" / "grade_map.json").read_text(encoding='utf-8'))
    for portal in ["academic", "archive", "deep"]:
        out = {g: v[portal] for g, v in grade_map.items() if portal in v}
        out_path = repo / f"portal-{portal}" / "data" / "grades.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"Wrote {out_path}")

if __name__ == "__main__":
    main()
```

---

## 33. SEO 策略

### 33.1 目标关键词

| 优先级 | 关键词类别 | 示例 |
|-------|-----------|------|
| 最高 | 学术发表 | "publish paper free", "论文免费发表" |
| 高 | 学科+发表 | "publish physics paper" |
| 高 | 开放获取 | "open access journal" |
| 中 | 特定理论 | "quantum consciousness theory" |

### 33.2 技术 SEO

- **结构化数据**：使用 Schema.org 的 `ScholarlyArticle` 标记论文页面
- **站点地图**：自动生成 XML 站点地图（`sitemap_enhancer.py` 增强）
- **元标签**：每篇论文都有独特的 title、description、keywords
- **页面速度**：静态站点确保极快的加载速度
- **移动优化**：响应式设计确保移动端体验
- **HTTPS**：GitHub Pages 默认 HTTPS

### 33.3 反 SEO 滥用

平台不进行任何黑帽 SEO 操作，也不试图在搜索结果中压制真实学术期刊。SEO 策略仅限于让目标受众能够找到平台，而不是让平台在所有学术搜索中排名靠前。**这一边界本身就是法律问题——见第 38、39 节。**

---

## 34. 反 SEO 与去索引策略

### 34.1 为什么需要反 SEO

学术门户需要被民科搜到（正向 SEO），但**档案库和 H.A.D.A.L. 深渊必须主动降低可发现性**——否则任何人 Google 一下就能跳过 ARG 直接进入"真相层"，整个双层体验设计就失效了。同时，降低这些入口的搜索引擎曝光也是法律自我保护：减少"虚假学术信息在搜索结果中广泛传播"的指控面。

### 34.2 技术手段

| 手段 | 适用入口 | 实现 |
|------|---------|------|
| `robots.txt` Disallow | 档案库、深渊 | `Disallow: /archive/` `Disallow: /d7-access/` |
| `<meta name="robots" content="noindex,nofollow">` | 档案库、深渊所有页面 | 模板级注入 |
| 不提交到 sitemap | 档案库、深渊 | `sitemap_enhancer.py` 只收录学术门户论文 |
| `X-Robots-Tag: noindex` HTTP 头 | 档案库、深渊（若用自定义域） | 部署配置 |
| 深渊 URL 不可猜测 | H.A.D.A.L. | 用 16 位随机哈希做路径，无任何入链 |
| canonical 指向学术门户 | 档案库论文页 | `<link rel="canonical" href="学术门户同 DIO 页">`，让搜索引擎认为"正本"是学术门户 |
| rel=nofollow 内链 | 从学术门户到过渡页 | 过渡页本身不被抓取扩散 |

### 34.3 robots.txt 示例

```
# 学术门户：允许全部
User-agent: *
Allow: /
Disallow: /archive/
Disallow: /d7-access/
Disallow: /*/archive/

# 深渊路径是随机哈希，无固定规则，靠 noindex 兜底
```

### 34.4 与正向 SEO 的平衡

- 学术门户：`index, follow`，提交 sitemap，积极 meta
- 过渡页 `/d7-access/`：`noindex, follow`（不收录但允许爬虫顺着去档案库……其实档案库也 noindex，所以等于双重隔离）
- 档案库：`noindex, nofollow`
- 深渊：`noindex, nofollow` + 随机路径 + 无入链

### 34.5 验证方法

部署后用 `site:<domain>` 在 Google/Bing 搜索，确认只有学术门户页面被收录。若发现档案库页面被收录，立即检查 robots.txt 和 meta 标签，并用 Google Search Console 的"移除工具"临时下架。

---

## 35. 内容策略

### 35.1 初始内容库

| 分级 | 数量 | 来源 |
|------|------|------|
| FG-0~FG-3 | 15-20 篇 | 维护者创作 |
| TG-1~TG-3 | 5-8 篇 | arXiv/OA 论文 |
| RG-0~RG-3 | 5-10 篇 | 维护者创作 |
| LG-0~LG-3 | 5-10 篇 | 维护者创作 |
| Wiki 条目 | 30-50 条 | 维护者 + AI 生成 |
| 终端会话 | 3-5 个 | 维护者创作 |

### 35.2 更新频率

- **月度**：2-4 篇新论文
- **季度**：1 期"期刊"汇总
- **年度**：年度"最佳论文"评选（讽刺性颁奖）
- **不定期**：宇宙合并事件、纪元进展

### 35.3 虚构作者生态

- 核心作者群（10-15 位）：频繁出现在不同论文中
- 合作网络：共同署名论文
- 引用网络：互相引用
- 学术竞争：通过论文互相反驳
- 机构归属：虚构的研究机构

### 35.4 "期刊"结构

- **卷号 (Volume)**：每年一卷
- **期号 (Issue)**：每季度一期
- **专栏 (Special Issue)**：不定期专题（如 "Special Issue on Quantum Consciousness"）
- **编委会**：虚构的国际编委会（包含真实的学术职位名称但虚构的人名）
- **编辑致辞**：每期卷首语（由虚构的主编撰写，内容微妙荒谬）

---

## 36. 后端预留与扩展

### 36.1 当前无后端原则

平台起步阶段**纯静态**，所有交互靠 localStorage + 前端 JS，所有"动态"内容（审稿状态、评论、投票）靠 GitHub Issues/Discussions/Giscus 承载。这是法律安全的需要——无后端意味着无用户数据库、无服务器日志、无中心化数据存储，大幅降低合规负担。

### 36.2 API 抽象层（前端）

```javascript
const API = {
  saveProgress: (data) => localStorage.setItem('bait_progress', JSON.stringify(data)),
  loadProgress: () => JSON.parse(localStorage.getItem('bait_progress') || '{}'),
  // 将来可替换为后端 API（保持调用方不变）
};
```

所有"用户态"操作（成就、揭示、Fish Score、ARG 进度）都走 `API` 对象，而非直接 `localStorage`。将来接后端时，只需替换 `API` 内部实现，业务代码不动。

### 36.3 潜在后端需求与接口契约

当平台规模扩大，以下功能可能需要后端。**预留接口契约（REST 风格）如下**，确保前端平滑迁移：

| 功能 | 当前替代 | 将来接口 | 方法 |
|------|---------|---------|------|
| 实时终端交互 | 前端预设脚本 | `/api/terminal/:session/command` | POST |
| 用户认证 | localStorage | `/api/auth/oauth` | POST |
| 投稿 | GitHub PR/Issue | `/api/submissions` | POST |
| 投稿表单 | Formspree | `/api/submissions/external` | POST |
| 评论 | Giscus | `/api/comments/:dio` | GET/POST |
| 宇宙合并投票 | GitHub Discussions 投票 | `/api/cosmos/:id/merge-vote` | POST |
| ARG 进度同步 | localStorage | `/api/progress/sync` | POST |
| 搜索 | Pagefind | `/api/search?q=` | GET |

**接口设计原则**：
- 所有写操作需认证（OAuth），匿名只读
- 不收集超出功能必需的个人信息（最小化原则，见 38 节数据合规）
- 所有接口返回 JSON，错误码统一
- 后端上线时，`API` 抽象层加一个 `mode: 'server'` 分支即可

### 36.4 后端上线的触发条件

只有当以下任一条件满足时才考虑上后端，否则保持纯静态：

- 月活解谜者 > 1000，localStorage 同步痛点显著
- 需要实时多人终端协作
- GitHub Discussions 投票机制不够用
- 需要更精细的投稿审核工作流

---

*（第五部分（29-36 节）完成。第六部分法律/路线图/附录（37-41 节）见下文续写，包含大幅扩充的法律章与专门提交 GPT 的咨询清单。）*

---
*AI生成（v3，待续）*

---

# 第六部分：法律、路线图与附录

## 37. 域名策略

### 37.1 现状与约束

- 顶级域名（.org / .com）成本较高，且 .org 对非营利组织身份有隐性要求
- 维护者手上目前只有个人网站资源
- GitHub Pages 默认提供 `<user>.github.io` 免费子域

### 37.2 渐进式域名方案

| 阶段 | 方案 | 域名形态 | 成本 | 适用期 |
|------|------|---------|------|--------|
| **阶段 0（起步）** | 纯 GitHub Pages | `<user>.github.io/bait/` | 免费 | M1-M3 |
| **阶段 1（三入口子路径）** | GitHub Pages + 子路径 | `<user>.github.io/bait/` `/archive/` `/deep/` | 免费 | M3-M5 |
| **阶段 2（独立免费域）** | 免费二级域 | `bait.<free-domain>` 或 `bait.is-a.dev` 之类 | 免费/极低 | M5+ |
| **阶段 3（独立顶级域）** | 自购顶级域 | `bait.xxx`（待定后缀） | 年费 | 规模化后 |
| **阶段 4（多域名）** | 每入口一域 | `academic.bait.xxx` `archive.bait.xxx` `deep.bait.xxx` | 年费×N | 多仓库化后 |

### 37.3 域名命名候选原则

无论最终用什么域名，命名需满足：

1. **不与真实学术出版机构撞名**（v1 教训：J.O.K.E. 撞名 Springer 期刊）
2. **域名本身不构成"冒充"嫌疑**——避免使用 `nature-`、`science-`、`sci-`、`springer`、`elsevier` 等真实出版商相关字样
3. **域名可以含钓鱼隐喻**（如含 `bait`/`reef`/`hook`），这是 ARG 线索而非法律风险——普通词汇不构成商标问题
4. **顶级域名后缀选择**：优先 `.xyz`/`.site`/`.online`（便宜、无明显身份暗示），避免 `.edu`（需资质、冒充风险）、`.org`（隐性非营利身份要求）

### 37.4 域名迁移与重定向

从阶段 N 迁移到阶段 N+1 时：

- 旧域名保留至少 1 年，全部页面 301 重定向到新域名对应路径
- 论文 DIO 编号**不随域名变化**（DIO 是逻辑标识，与 URL 解耦）
- `data/cross_repo_map.json` 更新 base URL
- 在学术门户首页公告"期刊域名变更"（伪装成真实期刊的域名迁移，增加真实感）

### 37.5 待 GPT 确认的域名法律点

见第 39 节 Q11-Q13：含钓鱼/讽刺隐喻的域名是否会被认定为"恶意注册"，以及不同顶级域注册商对戏仿内容的政策差异。

---

## 38. 法律与伦理框架

> **本节是整个文档最重要的部分之一。** 它是平台"能不能做、怎么做才安全"的总纲。v3 相比 v2 在此做了大幅扩充，但**所有结论都是框架性的、风险导向的初步判断，最终定性必须依赖 GPT 的跨法域检索 + 必要时真人律师的确认**。第 39 节是把这些问题结构化后专门提交给 GPT 的清单。

### 38.1 平台性质的法律定性（核心争议点）

B.A.I.T. 的本质是一个**针对特定群体（民科）的、有欺骗表象的戏仿/讽刺艺术项目**。它的法律风险根源在于一个张力：

- **设计意图**：是戏仿/讽刺/ARG 艺术作品，有明确的"双层体验"和透明性机制
- **客观效果**：对部分受众（目标"鱼"）而言，它在一段时间内会被当真

这个张力在几乎所有法域都会被审查。下表是**初步的风险定性**（非最终结论）：

| 维度 | 有利因素（平台主张） | 不利因素（潜在指控） |
|------|--------------------|--------------------|
| 言论自由/戏仿保护 | 明确的讽刺意图、ARG 结构、源码透明 | 戏仿通常针对"作品"，而本平台更像"冒充机构" |
| 经济动机 | 零收费、无广告、开源 | 无 |
| 透明性 | README 声明、PDF 元数据、HTML 注释 | 透明性"隐藏在需技术能力才能发现的地方" |
| 伤害可能性 | 内容限制在无害学科 | 受众可能因"被发表"产生现实行为（投稿更多、对外宣称） |

### 38.2 核心法律原则（平台侧的防御工事）

**1. 零收费原则（最核心）**

- 不收取任何费用（无审稿费、版面费、OA 费、会员费）
- 不接受任何形式捐赠
- 不放置任何广告
- 不进行任何商业变现
- **没有经济利益 = 没有欺诈动机**——这是对抗"诈骗罪/合同诈骗/非法经营"指控的第一道防线

**2. 透明性机制（"合理注意"辩护基础）**

- 所有代码开源（GitHub 仓库公开）
- README 顶部明确声明平台真实性质
- 源代码中平台真实性质是透明的
- PDF 元数据含 "PARODY"、"SATIRE"、"NOT_REAL_ACADEMIC_PAPER" 标记
- HTML 注释、CSS、零宽字符中遍布揭示性内容
- 这些构成了"任何有合理注意义务的人都能发现真相"的辩护基础

**3. 戏仿/讽刺法律保护**

- 戏仿（Parody）在多数法域受言论自由保护
- 内容是明确的讽刺/戏仿，不是虚假信息
- 不传播可能造成实际伤害的虚假信息
- 讽刺对象是"学术出版系统"这一抽象制度，不是具体个人

**4. 去人格化**

- 所有作者/审稿人/编委均为虚构
- 简历混用"真实机构名+虚构部门"（如 MIT 意识物理学部）
- 声明"所有角色纯属虚构"
- 不映射任何真实学者

### 38.3 风险清单与缓解措施（扩充版）

| 风险类型 | 描述 | 严重度 | 缓解措施 | 残留风险 |
|---------|------|--------|---------|---------|
| **诈骗/欺诈指控** | 被指"冒充学术机构骗取投稿/声誉" | 高 | 零收费 + 开源 + 透明性 | 中（经济动机可消除，但"声誉欺诈"难完全消除） |
| **虚假信息传播** | 被指传播伪科学误导公众 | 高 | 内容限制在无害学科 + PDF 标记 + ARG 揭示 | 中 |
| **冒充/虚假身份** | 虚构机构、虚构学者是否构成"冒充" | 高 | 去人格化 + "纯属虚构"声明 | 中高（这是最不确定的法律点） |
| **商标侵权** | D.I.O. 是否侵权 DOI；机构名是否侵权 | 中高 | 命名查重 + 避开真实出版商字样 | 中 |
| **著作权侵权** | 引用/转载真实论文 | 中 | 只用 arXiv/CC-BY/合理引用 | 低 |
| **游戏作品侵权** | 编码映射取材自游戏（GTI 等） | 中 | 只取编号结构，不取具体角色名/图标/剧情 | 低中（需 GPT 核实） |
| **诽谤** | 虚构名字撞真人 | 中 | 明显虚构名 + 声明 | 低 |
| **个人信息均保法/GDPR** | 投稿表单收集用户数据 | 中 | 最小化收集 + 即用即删 | 低 |
| **未成年人保护** | 受众可能含未成年人 | 中 | 18+ 声明 + 内容分级 | 低中 |
| **跨境管辖** | 中国创作者 + 美国 GitHub + 全球受众 | 高 | DMCA 安全港 + 美国法域戏仿保护 | 中（中国侧风险最难消除） |
| **SEO 干扰** | 是否干扰真实学术搜索结果 | 中 | 反 SEO（第 34 节）+ 不竞争真实期刊关键词 | 低 |
| **诱导/钓鱼的法律定性** | "钓鱼"隐喻是否构成"诱导" | 中高 | 这是平台核心隐喻，必须 GPT 定性 | 高（无法消除，需 GPT 给边界） |

### 38.4 数据合规（新增，针对投稿表单）

| 数据项 | 是否收集 | 保留策略 | 法律依据 |
|--------|---------|---------|---------|
| 笔名 | 是（投稿必需） | 随内容永久保留（已公开） | 用户自愿提供 |
| 邮箱 | 可选 | 发送录用/拒稿通知后从服务端删除，不长期存储 | 最小化原则 |
| 投稿内容 | 是 | 按内容许可（CC-BY-SA 4.0）永久公开 | 用户勾选同意 |
| IP/设备信息 | 否（不收集） | — | — |
| 真实身份 | 否 | — | — |

**合规要点**：
- 表单提供隐私政策链接，说明上述保留策略
- 不做任何用户画像、行为追踪
- 若将来接后端，需提供数据导出与删除入口（GDPR/个保法的"可携带权""被遗忘权"）

### 38.5 伦理考量

- **尊重原则**：虽是讽刺，不以羞辱个体为目标；讽刺对象是"系统"和"现象"，不是具体的人
- **教育价值**：讽刺应有助于公众理解学术出版系统的问题（掠夺性期刊、AI 论文工厂等）
- **退出机制**：若任何人因平台内容受到实际伤害，立即移除相关内容
- **年龄限制**：内容面向成年人，18+ 声明
- **可及性**：平台真实性质应始终对"有足够辨识力的人"可发现——这是伦理底线，也是法律辩护
- **不鼓励"钓鱼成功"**：Fish Score 体系中，"成为鱼"是讽刺性负分，平台不 celebrating 任何人的受骗

### 38.6 各法域初步判断（待 GPT 核实）

> ⚠️ 以下为基于常识的**初步倾向**，**绝非法律意见**，必须以 GPT 的检索结论为准。

| 法域 | 有利 | 不利 | 初步倾向 |
|------|------|------|---------|
| **美国（GitHub 所在地）** | 第一修正案强戏仿保护、DMCA 安全港、Airbnb/Hustler 等戏仿判例 | "冒充机构"可能触及虚假广告 | 倾向可做，但需透明性到位 |
| **中国（创作者/主要受众）** | — | 《网络安全法》《广告法》《反不正当竞争法》对"虚假宣传"规定严格；民科群体维权倾向；"学术不端"舆论风险 | **风险最高**，是整个项目最大的不确定项 |
| **欧盟** | 言论自由、戏仿在版权指令有明确例外 | GDPR 严格、DSA（数字服务法）对 UGC 平台有义务 | 中等风险 |

### 38.7 "最坏情况"预案

| 场景 | 应对 |
|------|------|
| 收到 DMCA 下架通知 | 立即下架被投诉内容，提交反通知（靠合理使用/戏仿辩护） |
| 收到中国侧投诉/律师函 | 立即下架相关内容，评估是否整体关停中国可访问性 |
| 被真实学者指名道姓"被影射" | 立即修改相关虚构人物，公开致歉，强化"纯属虚构"声明 |
| 受众因受骗产生现实损失（如拿"录用"去求职被拒） | 这是平台最怕的情境——需有快速响应通道，提供"真实性质证明"文档 |
| GitHub 仓库被封 | 已有备份预案（多镜像），README 透明声明争取解封 |

---

## 39. 提交 GPT 的法律咨询问题清单

> **本节是 v3 最核心的新增内容。** 它把第 38 节的所有不确定点，结构化成一份**可直接复制给 GPT（带联网检索）的咨询清单**。
>
> 设计原则：
> 1. **每个问题都给上下文**——GPT 不了解 B.A.I.T.，每个问题先 1-2 句交代背景
> 2. **每个问题都指明法域**——中国 / 美国 / 欧盟，让 GPT 分别检索
> 3. **每个问题都给"我的初步判断"**——让 GPT 能针对性地肯定/纠正，而非泛泛而谈
> 4. **每个问题都要求"判例/法条 + 风险等级 + 缓解建议"三件套**——避免空泛建议
> 5. **问题按风险优先级排序**，前面的最关键

### 39.0 给 GPT 的项目背景（每次提问前附上）

```
我正在设计一个名为 B.A.I.T.（Bureau of Advanced Interdisciplinary Theories）
的纯静态、零收费、开源的戏仿/讽刺网站。它伪装成一个国际学术出版机构，
实际是一个针对"民科"群体的讽刺艺术作品 + ARG 解谜游戏。

关键事实：
- 部署在 GitHub Pages（美国管辖），创作者在中国，主要受众是中国网民
- 零收费、无广告、无捐赠、无任何商业变现
- 全部代码开源，README 明确声明这是戏仿项目
- PDF 元数据含 PARODY/SATIRE/NOT_REAL_ACADEMIC_PAPER 标记
- 所有"作者""审稿人""编委"均为虚构人物
- 内容仅限数学/物理/宇宙学/哲学等无害学科，严格避开政治/医疗/金融/种族
- 用一个叫 D.I.O. 的标识系统替代真实 DOI
- 有完整的 ARG 揭示层，有技术能力的用户可发现真相

请基于以上事实，回答以下问题。每个问题请分别给出【中国法】【美国法】【欧盟法】
的判断，并附上【相关法条或判例】+【风险等级 高/中/低】+【具体缓解建议】。
```

### A 类：平台定性（最关键，决定项目能否存在）

**Q1. 戏仿/讽刺保护范围**
> 问题：一个"冒充学术出版机构"（而非冒充某部具体作品）的戏仿网站，在【中国/美国/欧盟】是否受言论自由/戏仿保护？关键区别在于：传统戏仿针对"作品"，而本平台针对"一类机构"。请给出判例（如美国 Hustler v. Falwell、再如中国是否有"机构戏仿"先例）。

**Q2. "冒充机构"的刑法/行政法风险**
> 问题：虚构一个"Bureau of Advanced Interdisciplinary Theories"并在网上以学术出版机构名义运营，在【中国】是否可能触犯《刑法》诈骗罪、招摇撞骗罪，或《广告法》《反不正当竞争法》的"虚假宣传"？在美国是否触及 FTC 的虚假广告？请区分"有经济利益的冒充"和"零收费的戏仿冒充"。

**Q3. "钓鱼"隐喻的法律定性**
> 问题：平台核心隐喻是"钓鱼"（bait），即主动吸引特定群体（民科）来"投稿"并让他们以为被真实期刊录用。这种"有意图地诱导他人产生误认"的设计，在【中国/美国】是否构成法律意义上的"诱导""欺诈"或"侵害他人意思自治"？即使零收费、即使最终有揭示层。这是整个项目最大的法律不确定项，请重点检索。

**Q4. 跨境管辖与执行风险**
> 问题：创作者在中国，服务器/GitHub 在美国，受众主要在中国。若发生法律纠纷，（a）哪个法域有管辖权？（b）中国能否要求 GitHub 下架？（c）创作者在中国的实际法律暴露面有多大？请结合《网络安全法》《数据安全法》及美国 CDA Section 230 / DMCA 分析。

### B 类：知识产权（高发风险）

**Q5. D.I.O. 与 DOI 的商标/混淆风险**
> 问题：我设计了一个叫 "D.I.O."（Document Identity Ontology）的文档标识系统，刻意模仿真实 "DOI"（Digital Object Identifier）的形态（编号格式 `DIO:B.A.I.T.2025.0001` 类似 `10.xxxx/xxxx`）。在【中国/美国】，这是否构成对 International DOI Foundation 的商标侵权或不正当竞争？"功能性模仿一个标识系统"和"商标侵权"的界限在哪？风险等级？

**Q6. 机构命名与真实出版社的混淆**
> 问题：平台内部有"编委会""主编""期刊卷期号"等结构，外部显示像 Elsevier/Springer/Nature 风格但**不用其名称**。这种"风格模仿但不使用对方商标"的做法，在【中国/美国】是否安全？边界在哪？是否需要在每个页面加"本平台与任何真实学术出版机构无关"的免责声明？

**Q7. 真实论文的引用与转载**
> 问题：平台在假论文的参考文献里混入真实论文并链接到真实 doi.org 页面；同时全文转载少量 arXiv 预印本和 CC-BY OA 论文作为"掩护内容"。在【中国/美国/欧盟】，这种做法的版权合规边界？arXiv 的各种许可证（CC-BY、CC-BY-NC 等）分别允许什么？仅做"参考文献列表+超链接"是否完全无风险？

**Q8. 游戏编码映射的侵权风险**
> 问题：平台从一个游戏（如《三角洲行动》的 GTI 干员体系）取材，把"干员编号格式（如 GTI-OP-04）"映射到虚构审稿人编号，但**不使用游戏内的具体角色名、剧情、图标、美术**。在【中国/美国】，这种"取编号结构、不取具体内容"的二创是否侵权？是否构成不正当竞争？

**Q9. "真实校名+虚构部门"的搭便车风险**
> 问题：虚构人物简历里写"Ph.D. from MIT, Department of Consciousness Physics"——用真实的 MIT 校名 + 完全虚构的部门名。这种做法在【中国/美国】是否构成对 MIT 的商标侵权/不正当竞争/声誉损害？风险等级？是否需要完全避免真实校名？

### C 类：UGC 与数据（中高频风险）

**Q10. 用户生成内容（UGC）的责任**
> 问题：平台接受社区投稿（假论文），通过 GitHub PR/Issue 和外部表单。在【中国/美国/欧盟】，平台对用户投稿内容（可能含侵权/违规）承担什么责任？美国 CDA 230、欧盟 DSA、中国《网络安全法》分别如何适用？需要哪些"通知-删除"机制？外部表单（不经 GitHub）是否会改变责任性质？

**Q11. 投稿表单的数据合规**
> 问题：外部投稿表单收集笔名 + 可选邮箱 + 投稿内容，邮箱在发通知后即删。在【中国《个人信息保护法》/欧盟 GDPR】，这种最小化收集是否合规？是否需要独立的隐私政策？是否需要提供数据删除入口（被遗忘权）？笔名算不算个人信息？

### D 类：域名与 SEO（中频风险）

**Q12. 含讽刺隐喻的域名**
> 问题：若域名含 bait/hook/reef 等钓鱼隐喻词（普通英语词汇，非他人商标），在【中国/美国】注册和使用是否有风险？是否会被认定为"恶意注册"？不同顶级域（.xyz/.site/.online vs .org）注册商对戏仿内容的政策差异？

**Q13. SEO 与反竞争**
> 问题：平台对"publish paper free""论文免费发表"等关键词做 SEO，会不会被认定为"干扰真实学术信息服务市场"或"不正当竞争"？在【中国/美国】，戏仿网站对真实服务关键词的 SEO 边界？平台不做黑帽 SEO，仅做白帽，是否足够安全？

### E 类：特定内容风险（低频但严重）

**Q14. 虚构"撤稿声明""讣告"的风险**
> 问题：平台含虚构的"撤稿声明"（针对平台自己虚构的论文）和虚构人物的"讣告"。在【中国/美国】，这种"关于虚构对象的真实感文档"是否有被误读为真实新闻的风险？若被误传为真实学者讣告，平台责任？

**Q15. 受众受骗后的现实损害责任**
> 问题：若某民科真的拿 B.A.I.T. 的"录用通知"去求职/评职称/对外宣传，事后被发现是假的，造成现实损失。在【中国/美国】，平台是否对该"间接损害"负责？平台的透明性机制（源码/PDF 标记/ARG 揭示）能否构成完整抗辩？是否需要更强的"显性免责"？

### F 类：缓解措施有效性验证

**Q16. 透明性机制的法律效力**
> 问题：我的透明性措施包括——README 声明、PDF 元数据 PARODY 标记、HTML 注释、源码可查。但这些"都需要技术能力才能发现"。在【中国/美国】司法实践中，"技术上可发现但普通用户看不到"的揭示，能否构成"合理注意"抗辩？是否需要在更显眼的位置（如每页页脚）加一行小字声明来强化法律效力？

**Q17. "纯属虚构"声明的措辞与位置**
> 问题：为降低法律风险，应在何处、用何种措辞放置"纯属虚构/戏仿"声明，既（a）满足法律"合理显著"要求，又（b）不明显破坏对目标受众的沉浸感（否则整个项目失去意义）？请给出【中国/美国】判例中对"显著免责声明"的要求，以及兼顾两者的折中方案建议。

### G 类：综合定性（请 GPT 最后回答）

**Q18. 综合可行性判断**
> 基于以上所有问题的回答，请给出一个综合判断：这个项目在【中国创作者 + 美国托管 + 中国主要受众】的组合下，整体法律可行性如何（高/中/低/不可行）？如果"中等可行"，最关键的 3-5 个"必须做对"的事项是什么？如果"低/不可行"，有没有缩减形态（如去掉"冒充机构"只保留"戏仿期刊风格"）能让它变得可行？

**Q19. 与真人律师的分工建议**
> 哪些问题你已经能基于判例给出较确定的答案（可以省律师费），哪些问题不确定性高、强烈建议花预算咨询真人律师（尤其是中国执业律师）？请按"建议咨询真人律师的优先级"排序。

---

## 40. 实施路线图

### 40.1 阶段划分

**Phase 0：基础设施 + 法律定性（2-3 周）**

- [ ] 创建 GitHub 仓库，确立子目录结构
- [ ] 搭建静态站点框架（学术门户 + 档案库）
- [ ] 配置 GitHub Actions 自动部署
- [ ] 编写 `content_validator.py` 和 `bi_calculator.py`
- [ ] **完成第 39 节 GPT 法律咨询，据结果决定是否调整范围**
- [ ] 配置 GitHub Pages 域名（阶段 0/1）

**Phase 1：核心内容（3-4 周）**

- [ ] 创作 15-20 篇初始论文
- [ ] 创建 R.E.E.F. 主站宇宙设定 + Wiki
- [ ] 创建 2-3 个独立宇宙
- [ ] 编写审稿意见
- [ ] 建立双向链接
- [ ] 生成带水印 PDF
- [ ] 收录真实论文作为掩护

**Phase 2：互动系统（3-4 周）**

- [ ] 成就系统
- [ ] 钓客日志
- [ ] 子页面揭示机制
- [ ] ISSN 七击彩蛋
- [ ] 防翻译防御
- [ ] URL 参数系统
- [ ] 移动端/PC 端差异化

**Phase 3：ARG 系统（4-6 周）**

- [ ] 三层线索嵌入
- [ ] ARG 进度追踪
- [ ] 跨入口分级映射的 ARG 谜题
- [ ] 链接图谱可视化
- [ ] DIO 段-纪元对应线索铺设

**Phase 4：终端与深渊（3-4 周）**

- [ ] 终端模拟器前端（含 public/hidden/quarantine 三层权限）
- [ ] 首批终端会话内容
- [ ] H.A.D.A.L. 深渊入口
- [ ] 损坏格式内容

**Phase 5：社区与运营（持续）**

- [ ] 投稿表单和流程文档（含第 12.3 节法律措辞）
- [ ] Giscus 评论
- [ ] SEO 优化（仅学术门户）+ 反 SEO（档案库/深渊）
- [ ] AI 补稿工具链
- [ ] 社区共创引导

### 40.2 里程碑

| 里程碑 | 标志 |
|-------|------|
| M0: Legal Green Light | 第 39 节 GPT 咨询完成，范围确认 |
| M1: Hello B.A.I.T. | 站点可访问，基本框架 |
| M2: First Catch | 初始内容库完成 |
| M3: The Hook | 互动系统上线 |
| M4: Deep Waters | ARG + 终端 + 深渊完整 |
| M5: Open Waters | 社区投稿开放 |

### 40.3 法律前置原则

> **重要**：M0（法律绿灯）必须先于 M1 之后的任何公开发布。在 GPT 法律咨询完成、并对 Q1-Q4（平台定性）和 Q18（综合可行性）有明确结论前，**不要公开部署可被搜索引擎索引的版本**。本地开发与内测不受此限制。

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
| K.E.L.P. | Knowledge Exchange & Lexicon Platform | Wiki 系统，"海带" |
| C.O.R.A.L. | Catalog of Observed Research & Academic Lore | 宇宙索引，"珊瑚" |
| P.E.A.R.L. | Peer Evaluation & Assessment Record Ledger | 审稿记录，"珍珠" |
| C.U.R.R.E.N.T. | Catalog of Unresolved Research & Emerging Novel Theories | 推荐系统，"洋流" |
| S.U.R.F. | Systematic Unified Reference Framework | 表面层，"浪花" |
| N.E.T. | Novel Epistemological Tracker | 追踪系统，"网" |
| FG | Fun Grade | 娱乐级论文（FG-0~FG-3） |
| TG | Truth Grade | 真实级论文（TG-1~TG-3） |
| RG | Record Grade | 异常档案级（RG-0~RG-3） |
| LG | Log Grade | 基础设施日志级（LG-0~LG-3） |
| DDI | Dimensional Deviation Index | 维度偏移指数（0-5） |
| CAST / HOOK / CATCH / RELEASE | 抛竿/上钩/收网/放生 | 审稿四阶段 |
| Canon / Semi-Canon / Apocrypha / Joke | 正典/半正典/逸典/玩笑 | 正典层级 |
| Fish Score | 鱼分数 | 用户洞察力评分 |
| Angler's Log | 钓客日志 | 用户个人主页 |
| ARG | Alternate Reality Game | 替代现实游戏 |
| era | 纪元 | discovery/foundation/expansion/leak |

---

## v3 相对 v2 的变更摘要

### 新增章节（v2 没有）
- §10 仓库与部署策略（含单/多仓库决策、跨仓库双链、ARG 跨入口互联样例）
- §16.4-16.6 终端命令权限三层、文件系统即叙事、会话生成
- §17.2 人物档案数据结构
- §18 游戏编码映射系统（独立小节）
- §34 反 SEO 与去索引策略（robots.txt / noindex / 随机哈希路径）
- §36.3-36.4 后端接口契约 + 上线触发条件
- §37 域名策略（五阶段渐进方案）
- §38.3 风险清单大幅扩充（12 类风险 × 严重度/缓解/残留）
- §38.4 数据合规（个保法/GDPR）
- §38.6 各法域初步判断
- §38.7 最坏情况预案
- §39 提交 GPT 的法律咨询问题清单（19 题，A-G 七大类）★核心新增

### 补回 v1 的实现细节（v2 曾缩水）
- §9.5 论文级 Front Matter 完整 YAML 示例
- §25 成就完整表（探索/解谜/互动/社区/元 五大类，含隐藏提示）
- §28.4 pdf_generator.py 伪代码
- §29.2-29.8 Prompt 模板正文（7 个完整模板）
- §32.2-32.7 六个脚本的完整伪代码（validator/bi/publisher/backlink/cosmos_init/grade_mapper）

### 细化 v2 新概念
- §3.7-3.8 编年史与 DIO 段对应表（ARG 线索）
- §5.3 宇宙合并的引用处理
- §5.6 正典层级管理（升降机制）
- §6.7 分级跨站点映射的脚本逻辑 + grade_map.json
- §11.3 三入口 ARG 过渡的具体样例链路
- §12.3 投稿表单法律措辞（定稿建议）

---

*本文档为 B.A.I.T. 平台 v3 完整技术设计方案。相比 v2，补回了全部实现细节，新增了仓库/域名/反SEO/后端契约/数据合规等缺失章节，并大幅扩充法律框架——其中第 39 节是专门结构化后提交 GPT 做跨法域检索的咨询清单（19 题）。**法律相关结论均为框架性初步判断，最终定性必须以 GPT 检索结论 + 必要时真人律师确认为准。** 世界观细节由社区共创填充。*

---
*AI生成（v3 完整版）*
