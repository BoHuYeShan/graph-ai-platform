# B.A.I.T. V6 新增章节（世界观升级）

> 本文档为 V5.1 的补充章节，不是完整设计文档。
> V5.1 的安全机制、披露体系、社区公约、内容边界、投稿流程、法律框架**全部保留不变**。
> V6 仅替换和新增以下世界观相关内容。

---

## V6 相对 V5.1 的变更概述

| 章节 | 动作 |
|------|------|
| §3 R.E.E.F. 编年史 | **重写** — 裂隙观测史 |
| §5 多宇宙架构 | **重写** — 三层宇宙 + 本体裂隙理论 |
| §6 分级系统 | **修改** — Δ 分级 → F 裂隙分级，DDI → FDI |
| §25 世界观 | **新增** — R.E.E.F. 机构设定 |
| §27 ARG | **修改** — 新增裂隙相关谜题 |
| §V6-7 内容架构 | **新增** — Markdown/HTML 混合渲染与文档归档 |
| §V6-8 主题系统 | **新增** — 页面主题与特殊组件 |
| §V6-9 跳转策略 | **新增** — 标准站到主站 / 深层档案 |
| §V6-10 特殊组件 | **新增** — 弹窗、倒计时与动效 |
| §V6-11 执行规格 | **新增** — 前后端目录、路由、搜索、校验、组件契约 |
| 术语表 | **新增词条** |

---

## §V6-1：本体裂隙理论（Ontological Fissure Theory）

### 1.1 核心发现

R.E.E.F. 研究所的核心发现是：**宇宙并非只有一个。**

在弦论的 brane cosmology 框架中，我们的宇宙是一个漂浮在高维空间中的「膜」。在某些条件下，两个相邻的膜之间会产生**本体裂隙（Ontological Fissure）**。裂隙不传输物质，不传输能量——只传输**信息**。

数学结构。物理理论。历史叙事。完整的学术论文。从裂隙中涌出的不是「异常」，是**另一个宇宙的正常物理学**。

### 1.2 三层宇宙

```
Tier 0 — 基准现实 (Baseline Reality)
  │  我们所在的宇宙。
  │  doi.org 可以打开。GitHub Pages 跑在这里。
  │  R.E.E.F. 的页面在这一层被访问，但其叙事实体属于 Tier 1。
  │
  │  ┌──────────────────────────────────────┐
  └──┤ Tier 1 — R.E.E.F. Nexus（主站宇宙）    │
     │  裂隙观测站所在的宇宙。               │
     │  B.A.I.T. = 该宇宙的学术期刊。        │
     │  所有「论文」= 裂隙信息的学术化报告。   │
     └──────────┬───────────────────────────┘
                │ 本体裂隙
     ┌──────────▼───────────────────────────┐
     │ Tier 2 — 多元宇宙 (The Multiverse)     │
     │  裂隙通往的无数独立宇宙。              │
     │  每个民科的理论在某个宇宙中是真实的。   │
     │  COSMOS-xxx = 各宇宙编号。            │
     │  H.A.D.A.L. = 靠近混沌边界的信息退化区。│
     └──────────────────────────────────────┘
```

### 1.3 关键叙事原则

**没有反派。没有灾难。没有收容失效。**
本体裂隙是一种自然现象，就像地震或日食。R.E.E.F. 的角色是「观测和记录」，不是「收容和控制」。

**在裂隙中，你不是错的——你只是属于另一个宇宙。**
这是一个刻在 R.E.E.F. 总部墙上的格言。它定义了整个平台对待民科内容的叙事态度：不嘲笑、不驳斥、不「揭穿」；只是平静地指出——「这个理论在我们的宇宙中不成立，但在某个裂隙宇宙中，它可能是对的。」

---

## §V6-2：裂隙分级系统（Fissure Classification）

> 替代 §6 中的 Δ 分级系统。以下为 V6 的「统一内部分级」。

### 2.1 裂隙等级（F-Grade）

| 等级 | 名称 | 含义 | 对应内容 |
|------|------|------|---------|
| F-0 | Surface Ripple | 微弱信息涟漪，结构不稳定。多为巧合或噪声。 | 纯搞笑、明显荒诞的文稿 |
| F-1 | Minor Fissure | 可辨识的结构化信息，但持续时间和信息密度较低。 | 有一定伪装度的文稿 |
| F-2 | Stable Fissure | 持续涌入，形成可验证的理论结构。活跃观测目标。 | 高度伪装的文稿 |
| F-3 | Deep Rift | 大量信息涌入，与基准现实的物理规律系统性偏离。优先观测目标。 | 极致伪装的文稿 |
| Σ | Standard | 来自基准现实本身。非裂隙信息。 | 真实 arXiv/OA 论文评论 |
| X | Quarantine | 裂隙信息含逻辑矛盾、自毁性结构或信息退化。隔离处理。 | 损坏/矛盾的档案 |

### 2.2 裂隙偏离指数（Fissure Deviation Index / FDI）

> 替代 DDI

| FDI | 含义 |
|-----|------|
| 0 | 基准现实 |
| 1 | 微幅偏离——可能只是观测误差 |
| 2 | 可测量的偏离——无法用基准现实物理学解释 |
| 3 | 显著偏离——暗示不同的物理常数集合 |
| 4 | 深度偏离——该宇宙的物理规律与基准现实完全不同 |
| 5 | 混沌边界——信息高度退化，无法可靠评估 |

### 2.3 三入口分级映射

**学术门户（民科看到）**：

| F-Grade | 显示 |
|---------|------|
| F-0~3 | Category S / A++ / A+ / A — Research Observation Report |
| Σ | Category B — Standard Commentary |

**档案库（解谜者看到）**：

| F-Grade | 显示 |
|---------|------|
| F-0 | F-0 Surface Ripple · 蓝色 |
| F-1 | F-1 Minor Fissure · 黄色 |
| F-2 | F-2 Stable Fissure · 橙色 |
| F-3 | F-3 Deep Rift · 红色 |
| Σ | Σ Standard · 白色 |
| X | X Quarantine · 黑色/红色 |

**终端**：保持旧格式 `DOC::TYPE-A-n` / `DOC::TYPE-S` / `DOC::TYPE-B`。

---

## §V6-3：R.E.E.F. 编年史（裂隙观测史）

> 替代 §3 旧编年史

### 3.1 纪元一：首次接触期（The First Contact Era）

约 15 年前。R.E.E.F. 前身——一个跨学科理论物理研究组——在分析宇宙微波背景辐射数据时，发现了无法用已知物理框架解释的结构化信号。最初以为是设备噪声。经过三年的数据清洗和验证，研究组确认：这些信号不是噪声。它们携带**信息**。

**对应 DIO 段**：`DIO:B.A.I.T.2020.0001` ~ `DIO:B.A.I.T.2021.0150`
**终端日志风格**：极简，纯文本，无颜色，命令少（`ls/cat/log`）。

### 3.2 纪元二：建制期（The Foundation Era）

研究组正式更名为 R.E.E.F.。B.A.I.T. 作为其旗舰学术期刊创刊。裂隙分类法（F-Grade）和编号系统（D.I.O. / C.O.S.M.O.S.）确立。首个永久性裂隙观测站投入运行。对外，B.A.I.T. 以普通学术出版机构的形象出现；对内，每篇「论文」都是一份裂隙观测报告。

**对应 DIO 段**：`DIO:B.A.I.T.2021.0151` ~ `DIO:B.A.I.T.2022.0400`
**终端日志风格**：出现基础分级提示（`[INFO]/[WARN]`），出现 `access` 命令。

### 3.3 纪元三：测绘期（The Cartography Era）

裂隙观测从单个目标扩展为系统性的多元宇宙测绘。COSMOS 编号系统上线，已知宇宙数量快速增长。首个宇宙合并事件发生——两个独立裂隙被发现通往同一宇宙。K.E.L.P. Wiki 系统、C.O.R.A.L. 宇宙索引、P.E.A.R.L. 审稿记录系统相继建立。H.A.D.A.L. 混沌边界被首次探测——某些裂隙的信息高度退化，接近不可读。

**对应 DIO 段**：`DIO:B.A.I.T.2022.0401` ~ `DIO:B.A.I.T.2024.0800`
**终端日志风格**：命令丰富、出现 `decrypt` 命令、日志中出现「fissure mapping」字样。

### 3.4 纪元四：网络测绘期（The Network Era）← 当前

裂隙并非孤立存在。它们形成一个复杂的网络拓扑——有些裂隙相互连接，有些宇宙共享同一组物理常数，有些区域是「信息沙漠」。当前阶段的核心任务是**绘制裂隙网络图谱**。

这也是为什么 B.A.I.T. 的论文之间存在密集的双向链接——它们不是随机的引用，而是**裂隙网络的拓扑映射**。

**对应 DIO 段**：`DIO:B.A.I.T.2024.0801` ~ 现在
**终端日志风格**：出现 `topology` 命令、裂隙网络可视化、混沌边界探测日志。

### 3.5 纪元五：？（社区定义）

未来可能的纪元：
- **模拟假说期**：发现某些宇宙的裂隙信号带有非自然的结构——它们可能是被其他宇宙的智慧文明「模拟」出来的。
- **裂隙闭合期**：某些裂隙开始闭合，信息涌入停止。
- **深度探测期**：首次成功向裂隙发送探测信号并收到回复。

---

## §V6-4：R.E.E.F. 机构设定

### 4.1 基本信息

- **全称**：Research Encyclopedia of Emerging Frontiers
- **性质**：虚构宇宙中的国际学术研究机构
- **旗舰期刊**：B.A.I.T.（Bureau of Advanced Interdisciplinary Theories）
- **总部**：未公开（叙事留白，供社区填充）
- **经费来源**：不明（叙事留白）

### 4.2 核心研究部门

| 部门 | 代号 | 职责 |
|------|------|------|
| 裂隙观测部 | F.O.D. (Fissure Observation Division) | 运行观测站，实时监控裂隙信号 |
| 信息分析部 | I.A.D. (Information Analysis Division) | 将裂隙信息整理为标准学术格式 |
| 宇宙测绘部 | C.M.D. (Cosmic Mapping Division) | 维护 COSMOS 编号系统和裂隙网络图谱 |
| 混沌研究部 | C.R.D. (Chaos Research Division) | 负责 H.A.D.A.L. 混沌边界的探测与研究 |
| 理论部 | T.D. (Theory Division) | 研究裂隙的物理机制，改进本体裂隙模型 |

### 4.3 著名研究员（虚构人物）

| 姓名 | 职位 | 研究领域 | 简介 |
|------|------|---------|------|
| Dr. Null Current | 高级研究员，理论部 | 裂隙拓扑学 | 面无表情，论文极干。据称从未离开过观测站。 |
| Prof. Sylvia Rift | 主任，信息分析部 | 裂隙信号分类 | 提出了 F-Grade 分类法。喜欢在论文脚注里藏冷笑话。 |
| Dr. Zhang Wei | 研究员，宇宙测绘部 | COSMOS 编号系统 | 设计了 COSMOS 编号体系。据说他的办公室贴满了宇宙参数表。 |
| Dr. A. Nemo | 混沌研究部 | 信息退化动力学 | 负责 H.A.D.A.L. 项目。此人存在本身疑似裂隙信息。 |

### 4.4 机构格言

> *In a fissure, you are not wrong. You simply belong to another universe.*
> 「在裂隙中，你不是错的。你只是属于另一个宇宙。」

---

## §V6-5：ARG 新线索（裂隙相关）

### 5.1 裂隙网络图谱

论文之间的双向链接不是随机引用——它们反映裂隙网络的拓扑结构。如果解谜者将所有链接关系可视化为图谱，会发现：
- 某些论文形成密集的「星团」——对应参数空间中靠近的多个宇宙
- 某些论文孤立——对应偏远宇宙
- 某些链接是单向的——对应「单向裂隙」（信息只从 A 流向 B）

### 5.2 模拟假说线索

部分裂隙信号中存在「非自然的结构」：
- 某些宇宙的物理常数过于「整齐」——像是被人为设定而非随机生成的
- 某些裂隙信号在特定频率上出现周期性模式——怀疑是「模拟器」的时钟信号
- H.A.D.A.L. 深处有一段重复的二进制序列，解码后是 `R.E.E.F. IS WATCHING`

---

## §V6-6：与 V5.1 不变的部分

以下 V5.1 内容在 V6 中**完全不变**：
- §1 项目概述（定位、设计哲学、受众）
- §4 内容边界与安全策略
- §7-9 投稿流程、B.I. 指数、平台架构
- §11-12 多入口、手机端
- §13-19 内容模型、引用、AI补稿、终端、身份、游戏编码
- §20-29 链接、ARG、揭示、防翻译、URL参数、成就、Fish Score、彩蛋、水印
- §30-38 社区治理、公约、脚本、SEO、域名、后端、删库预案
- §39 法律框架（完整保留）
- §40 实施路线图（新增裂隙相关内容到 Phase 1 和 Phase 4）

---

## §V6-7：内容架构、文档目录与渲染模式

V6 继续以 Markdown 作为常规文档的主内容格式，但引入“文档文件夹 + 元数据 + 可选 HTML 壳”的混合结构，保证普通文档可检索、特殊文档可动效化、深层档案可组件化。

### 7.1 页面类型

| 页面类型 | 用途 | 主体格式 | 适用入口 |
|---|---|---|---|
| standard | 论文、评论、说明、索引 | `index.md` | 标准站 |
| hybrid | 需要少量动效或特殊组件的文档 | `index.md` + `page.html` | 主站 / 档案站 |
| html | 强互动页面、终端、验证页、图谱页 | `page.html` 为主 | 主站 / 深层档案 |

### 7.2 单文档单文件夹结构

每个文档单独一个文件夹，文件夹名使用文档 slug 或内部编号，推荐结构如下：

```text
content/
  documents/
    2026-0001-fissure-observation/
      meta.yml
      index.md
      page.html        # 可选
      assets/          # 可选
```

### 7.3 文件职责

- `index.md`：正文与主要可搜索内容，常规文档的唯一内容源。
- `meta.yml`：标题、主题、入口、渲染模式、标签、搜索摘要、动效等级。
- `page.html`：仅在特殊页面时存在，负责 HTML 壳、组件挂载和动效容器。
- `assets/`：图片、SVG、音效、Lottie、图谱素材。

推荐元数据字段：

```yaml
document_id: "DIO:B.A.I.T.2026.0001"
slug: "fissure-observation-001"
title: "A Speculative Interpretation of Dimensional Heat Transfer"
entry: standard
render_mode: markdown
theme: standard-journal
motion: subtle
searchable: true
```

### 7.4 搜索与归档

- 浏览器内搜索只索引 `index.md`、`meta.yml` 的公开字段和显式摘要。
- `page.html` 不作为默认正文索引，避免把特殊动效层误当成文档语义。
- 归档时按文档文件夹作为最小单位保存，便于版本化、撤回和搬迁。
- 如果页面只有 HTML 壳，也必须提供可检索的摘要或正文片段，不能让搜索结果只剩组件。

### 7.5 文档排序

默认排序顺序：

1. 入口优先级（标准站 > 主站 > 深层档案）。
2. 文档类型（普通文档 > 评论 > 终端页 > 图谱页 > 验证页）。
3. 时间戳 / DIO 编号。

---

## §V6-8：主题系统

V6 的主题不是单纯的 CSS 皮肤，而是“入口身份 + 组件密度 + 动效强度 + 披露语气”的组合。

### 8.1 主题清单

| 主题 | 入口 | 视觉特征 | 动效强度 | 典型组件 |
|---|---|---|---|---|
| `standard-journal` | 标准站 | 论文机构、简洁、克制 | 低 | DisclosureBadge、FooterDisclosure |
| `reef-main` | 主站 | 学术门户 + 系统感 | 中 | SourceContextCard、ArchiveCTA、SystemNotice |
| `hadal-archive` | 深层档案 | 黑暗、深层、裂隙感 | 中高 | WakeTimer、WakeModal、IntrusionBanner |
| `terminal` | 终端页 | 等宽字体、命令行 | 中 | TerminalWindow、CommandHistory |
| `release-card` | 验证页 / 发布卡 | 卡片式、仪式感 | 中 | ReleaseCard、QRPanel、ValidationResult |
| `fissure-map` | 图谱页 | 网络图、节点和连线 | 高 | ArchiveMap、NodeLegend、TopologyFilter |
| `system-log` | 日志页 | 警告条、事件记录 | 中 | LogStream、AlertPanel、EventStamp |

### 8.2 主题职责

每个主题负责四件事：

1. 字体与排版。
2. 色彩与对比度。
3. 可用组件集合。
4. 动效等级与过渡风格。

### 8.3 主题选择规则

- 标准站默认 `standard-journal`。
- 主站默认 `reef-main`，系统文档可切 `system-log`。
- 深层档案默认 `hadal-archive`，图谱页可切 `fissure-map`。
- 终端页和验证页分别固定为 `terminal`、`release-card`。

---

## §V6-9：标准站 / 主站 / 深层档案的跳转策略

标准站、主站和深层档案不是同一类入口。标准站负责“看起来像真的机构”；主站负责“知道这是虚构后继续玩”；深层档案负责“更深入的世界观与互动”。

### 9.1 标准站跳转原则

- 不自动跳转。
- 不弹出 30 分钟醒来提醒。
- 不使用黑客入侵式提示。
- 只提供明确但克制的入口：`About`、`Context`、`Archive`、`Read more`。

### 9.2 标准站可见跳转

标准站允许以下引导：

- 文章页底部的 `View context`。
- 首页/检索页的 `Enter archive layer`。
- 作者卡片的 `Explore R.E.E.F.`。
- 搜索结果中的 `Main site context` 标签。

这些链接必须是“用户主动点击才进入”，不能像强制升级一样把用户推走。

### 9.3 主站与深层档案跳转

- 主站可以在停留较久后显示软提示：`想知道更多吗？`。
- 深层档案可以显示红蓝选择、倒计时和漂移提醒。
- 30 分钟后的“如梦初醒”弹窗只在主站与深层档案出现，不出现在标准站。

### 9.4 跳转语气

允许：

- `Continue to archive context`
- `Enter fissure layer`
- `Return to baseline`
- `Stay in the archive`

不允许：

- 浏览器/系统级安全警报式文案。
- 类似真实黑客入侵提示的恐吓性措辞。
- 自动强制重定向。

---

## §V6-10：特殊组件与动效

特殊组件用于主站和深层档案，不用于标准站的常规论文页。

### 10.1 核心组件

| 组件 | 用途 |
|---|---|
| `DisclosureBadge` | 短披露徽章 |
| `SourceContextCard` | 真实人物/公开材料上下文 |
| `WakeTimer` | 停留倒计时 |
| `WakeModal` | 红蓝选择弹窗 |
| `IntrusionBanner` | 虚构系统异常横幅 |
| `ArchiveMap` | 裂隙网络图谱 |
| `TerminalWindow` | 伪终端 |
| `ReleaseCard` | 虚构展示卡 |
| `MotionTransition` | 如梦初醒 / 回到主站的过渡动画 |

### 10.2 动效等级

| 等级 | 名称 | 适用 |
|---|---|---|
| none | 无动效 | 标准站正文 |
| subtle | 轻微动效 | 标准站/主站普通文档 |
| drift | 漂移动效 | 主站提示、档案提醒 |
| wake | 醒来动效 | 红蓝弹窗跳转 |
| glitch | 裂隙故障感 | 深层档案、系统日志 |

### 10.3 安全约束

- 不模拟真实浏览器/操作系统安全弹窗。
- 所有弹窗必须可关闭。
- 所有动效必须提供 `prefers-reduced-motion` 降级。
- 特殊动效不得掩盖披露文本。
- 右上角倒计时必须服务于世界观，不得伪装成真实系统故障。

### 10.4 推荐动效关键词

- `fade-to-white`
- `desaturate-and-blur`
- `archive-glow`
- `fissure-ripple`
- `console-blink`
- `paper-shift`

---

## §V6-11：前后端架构执行规格

本节用于直接指导后续实现。若其他 AI 执行代码任务，应优先遵守本节；若本节与 V5.1 安全机制冲突，以 V5.1 安全机制为准。

### 11.1 总体原则

1. Markdown 管内容：所有可检索正文、说明文字、论文正文、档案正文优先写入 `index.md`。
2. HTML 管体验：动画、弹窗、图谱、终端、验证页用 `page.html` 或组件承载。
3. `meta.yml` 管路由和主题：不要把主题、排序、入口、风险级别硬编码在正文里。
4. 组件管互动：红蓝选择、倒计时、终端、图谱、验证结果都应是可复用组件。
5. 标准站保持克制：不放强互动、红蓝选择、黑客感警告或自动跳转。

### 11.2 推荐仓库目录

```text
bait-core/
  content/
    documents/
      <slug>/
        meta.yml
        index.md
        page.html
        assets/
    source-context/
      <slug>/
        meta.yml
        index.md
    cosmos/
      <cosmos-id>/
        meta.yml
        index.md
    release-cards/
      <dio-id>/
        meta.yml
        index.md
  data/
    content_index.json
    route_manifest.json
    search_index.json
    theme_registry.json
    component_registry.json
    source_subjects.json
    risk_register.json
    takedown_log.json
  src/
    components/
      DisclosureBadge.*
      SourceContextCard.*
      WakeTimer.*
      WakeModal.*
      IntrusionBanner.*
      ArchiveMap.*
      TerminalWindow.*
      ReleaseCard.*
      MotionTransition.*
    themes/
      standard-journal.*
      reef-main.*
      hadal-archive.*
      terminal.*
      release-card.*
      fissure-map.*
      system-log.*
    layouts/
      StandardLayout.*
      HybridLayout.*
      HtmlIslandLayout.*
      ArchiveLayout.*
      TerminalLayout.*
      ReleaseCardLayout.*
    scripts/
      build_content_index.*
      build_search_index.*
      validate_content.*
      validate_routes.*
      validate_disclosure.*
      validate_theme_rules.*
  public/
    assets/
    search/
    archive/
  policies/
    DISCLAIMER.md
    EDITORIAL_POLICY.md
    CODE_OF_CONDUCT.md
    ABUSE_RESPONSE.md
    TAKEDOWN.md
    CONTENT_PROVENANCE.md
```

### 11.3 单文档文件夹规范

每个文档文件夹必须至少包含：

```text
<slug>/
  meta.yml
  index.md
```

可选文件：

```text
<slug>/
  page.html
  assets/
    cover.svg
    graph.json
    animation.json
```

禁止：

- 多个文档共用一个 `index.md`。
- 把同一文档拆散到多个无索引的 HTML 片段。
- 只有 `page.html` 而没有可检索摘要。
- 在 HTML 中写唯一披露文本，导致 Markdown 搜索找不到披露。

### 11.4 `meta.yml` 完整字段

```yaml
document_id: "DIO:B.A.I.T.2026.0001"
slug: "fissure-observation-001"
title: "A Speculative Interpretation of Dimensional Heat Transfer"
subtitle: "Observed through COSMOS-CNS-001"
language: zh-CN

entry: standard              # standard | main | archive | terminal | release | system
render_mode: markdown        # markdown | hybrid | html
theme: standard-journal
layout: StandardLayout
motion: subtle               # none | subtle | drift | wake | glitch

content_mode: fictional_manuscript
f_grade: F-1
fdi: 2
cosmos: COSMOS-CNS-001
dio: "DIO:B.A.I.T.2026.0001"

authors:
  - name: "Dr. Null Current"
    type: fictional_profile

source_subjects: []

disclosure:
  fictional_disclosure: true
  not_real_journal: true
  not_peer_reviewed: true
  not_certification: true
  short_label: true
  screenshot_watermark: true
  pdf_watermark: true

search:
  searchable: true
  title_weight: 10
  summary: "A fictional community manuscript in the B.A.I.T. archive."
  tags:
    - fissure
    - speculative-manuscript

routing:
  path: "/manuscripts/fissure-observation-001/"
  canonical_entry: standard
  related_context: "/context/fissure-observation-001/"
  archive_entry: "/archive/fissure-observation-001/"

risk:
  level: green
  requires_review: false
  takedown_contact: "abuse@placeholder.example"
```

### 11.5 入口与主题允许矩阵

| entry | 允许 theme | 禁止 theme | 默认 render_mode |
|---|---|---|---|
| standard | `standard-journal` | `hadal-archive`, `terminal`, `system-log` | markdown |
| main | `reef-main`, `system-log` | 无 | markdown / hybrid |
| archive | `hadal-archive`, `fissure-map`, `system-log` | `standard-journal` | hybrid |
| terminal | `terminal` | 其他全部 | html |
| release | `release-card` | 其他全部 | html |
| system | `system-log`, `reef-main` | `standard-journal` | hybrid |

实现时必须校验矩阵，不允许在标准站页面挂载 `WakeModal`、`IntrusionBanner` 或 `glitch` 动效。

### 11.6 路由规则

推荐路由：

```text
/                         标准站首页
/manuscripts/<slug>/      标准站文稿页
/commentary/<slug>/       标准站评论页
/context/<slug>/          主站上下文页
/reef/                    主站入口
/reef/system/<slug>/      主站系统文档
/archive/                 深层档案入口
/archive/<slug>/          深层档案页
/terminal/                伪终端
/map/fissures/            裂隙图谱
/release/<dio>/           Release Card 展示页
/verify/                  编号查询页
/policies/<name>/         政策文件
```

路由原则：

- 标准站路由不应默认带 `archive`、`hadal`、`terminal` 等强 ARG 语气。
- 主站与深层档案可以互链，但必须保留返回标准站的显眼路径。
- 验证页不得写成现实认证查询系统。

### 11.7 渲染管线

构建顺序：

1. 扫描 `content/**/meta.yml`。
2. 校验 `meta.yml` 必填字段。
3. 读取 `index.md` 并生成正文 AST / HTML。
4. 根据 `render_mode` 选择 layout。
5. 根据 `theme` 注入 CSS 变量和允许组件。
6. 若存在 `page.html`，作为 HTML island 挂载到 layout 指定 slot。
7. 生成 `content_index.json`。
8. 生成 `route_manifest.json`。
9. 生成 `search_index.json`。
10. 执行 disclosure / theme / routing 校验。

### 11.8 Layout slot 规范

所有 layout 至少支持以下 slot：

| slot | 用途 |
|---|---|
| `header` | 导航、短披露、入口标签 |
| `main` | Markdown 正文 |
| `aside` | Source Context、目录、相关链接 |
| `interactive` | HTML island / 组件挂载 |
| `footer` | 完整披露、政策链接、返回入口 |

特殊页面可增加：

| slot | 用途 |
|---|---|
| `overlay` | 弹窗、倒计时、漂移提醒 |
| `terminal` | 伪终端主体 |
| `graph` | 裂隙图谱 |
| `transition` | 如梦初醒动画 |

### 11.9 组件契约

| 组件 | 允许入口 | 必需输入 | 禁止行为 |
|---|---|---|---|
| `DisclosureBadge` | 全部 | disclosure flags | 不得隐藏或做成 ARG 谜题 |
| `SourceContextCard` | main / archive | source_subjects | 不得出现在作者栏 |
| `WakeTimer` | main / archive | duration, targetRoute | 不得用于 standard |
| `WakeModal` | main / archive | redAction, blueAction | 不得强制跳转 |
| `IntrusionBanner` | main / archive / system | eventType, text | 不得模拟真实系统安全警报 |
| `ArchiveMap` | archive | graph data | 不得暴露私人信息 |
| `TerminalWindow` | terminal / archive | command registry | 不得执行真实系统命令 |
| `ReleaseCard` | release | dio, title, disclosure | 不得使用 certificate/accepted/indexed 语气 |
| `MotionTransition` | main / archive | mode, reducedMotionFallback | 不得掩盖披露文本 |

### 11.10 弹窗与倒计时规则

`WakeTimer` 默认参数：

```yaml
duration_minutes: 30
warning_minutes: 5
critical_minutes: 1
reset_on_interaction: true
dismissible: true
```

红蓝按钮默认文案：

```text
红色：醒来 · 返回主站
蓝色：继续下潜 · 留在档案层
```

允许弹窗主题：

- 档案层漂移提醒。
- 裂隙同步异常。
- 基准现实回声。
- 观测者疲劳提示。
- 梦境保持失败。

禁止弹窗主题：

- 真实黑客入侵。
- 真实病毒感染。
- 浏览器安全警告。
- 账号泄露或支付风险。
- 任何可能被普通用户理解为现实事故的系统提示。

### 11.11 搜索设计

搜索对象：

- `title`
- `subtitle`
- `index.md` 正文
- `search.summary`
- `search.tags`
- 公开的 Source Context 摘要

搜索结果分组：

1. Manuscripts
2. Commentary
3. Context
4. Archive
5. Terminal / ARG
6. Policies

搜索结果必须显示入口标签：

```text
[Standard] [Main Context] [Archive] [Policy]
```

标准站搜索默认只显示 Standard + Policy，可提供“显示主站/档案结果”的开关，但不能默认把深层档案推给普通访客。

### 11.12 构建校验规则

构建失败条件：

- `fictional_disclosure` 不是 `true`。
- 标准站页面使用 `WakeModal`、`IntrusionBanner`、`terminal` 主题或 `glitch` 动效。
- `release-card` 页面出现 `Certificate`、`Acceptance Letter`、`Indexed by`、`认证编号` 等禁用词作为功能描述。
- `Source Subject` 出现在作者字段。
- `page.html` 存在但没有 `index.md` 或 `search.summary`。
- `html` 页面没有可访问的返回路径。
- 弹窗不可关闭。
- 动效没有 `prefers-reduced-motion` 降级。

构建警告条件：

- 文档没有 tags。
- 没有相关上下文链接。
- 入口与主题不匹配但可自动降级。
- 页面动效等级高于主题默认等级。

### 11.13 实施优先级

Phase 1 必须先实现：

1. `meta.yml` 解析。
2. Markdown 渲染。
3. `standard-journal` 主题。
4. DisclosureBadge。
5. 搜索索引。
6. 路由 manifest。

Phase 2 再实现：

1. `reef-main` 与 `hadal-archive`。
2. `hybrid` 渲染。
3. SourceContextCard。
4. WakeTimer / WakeModal。
5. ReleaseCard / Verify 页面。

Phase 3 再实现：

1. TerminalWindow。
2. ArchiveMap。
3. MotionTransition。
4. IntrusionBanner / System Log。
5. 裂隙网络图谱。

### 11.14 给执行 AI 的硬性约束

如果后续由其他 AI 执行开发，必须遵守：

1. 不要把所有页面都做成纯 Markdown，也不要把所有页面都做成纯 HTML。
2. 不要在标准站加入红蓝按钮、30 分钟倒计时、黑客感弹窗。
3. 不要把 `page.html` 当作正文来源；正文仍以 `index.md` 为准。
4. 不要把 R.E.E.F. 写成现实世界中的真实机构。
5. 不要使用真实证书、真实认证、真实收录系统的措辞。
6. 不要让任何 ARG 机制承担免责声明或平台性质披露义务。
7. 不要实现强制跳转；所有跳转必须是用户可选择的。
8. 不要把真实人物放进作者栏，除非走 V5.1 自愿投稿者流程。

### 11.15 最小可交付版本

最小可交付版本不需要一次实现所有动效，但必须包含：

- 单文档单文件夹结构。
- `meta.yml` + `index.md`。
- `standard` / `hybrid` / `html` 三种 render mode。
- 至少 `standard-journal`、`reef-main`、`hadal-archive` 三个主题。
- DisclosureBadge 与 SourceContextCard。
- 搜索索引和入口分组。
- 构建校验规则。

如果时间有限，先不要做终端、裂隙图谱和复杂动画；但不要牺牲披露、水印、路由和搜索。

---

*V6 补充章节完。与 V5.1 合并后构成完整 V6 设计文档。*
