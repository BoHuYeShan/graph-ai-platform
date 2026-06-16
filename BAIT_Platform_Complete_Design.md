---
AIGC: {"Label":"1","ContentProducer":"001191110108MA01KP2T5U00000","ProduceID":"c55fc1d220505f1d4945c13a856f99c0","ReservedCode1":"","ContentPropagator":"001191110108MA01KP2T5U00000","PropagateID":"c55fc1d220505f1d4945c13a856f99c0","ReservedCode2":""}
---

# B.A.I.T. 平台完整设计文档

> **Bureau of Advanced Interdisciplinary Theories**
> "bait" = 诱饵 / 钓鱼 — 学术模仿秀平台的完整技术设计方案

---

## 目录

1. [项目概述](#1-项目概述)
2. [命名体系](#2-命名体系)
3. [内容边界与安全策略](#3-内容边界与安全策略)
4. [分级系统](#4-分级系统)
5. [钓鱼审稿系统](#5-钓鱼审稿系统)
6. [B.I. 诱饵指数评估体系](#6-bi-诱饵指数评估体系)
7. [平台架构](#7-平台架构)
8. [投稿与审稿工作流](#8-投稿与审稿工作流)
9. [双向页面链接系统](#9-双向页面链接系统)
10. [线索与 ARG 解谜系统](#10-线索与-arg-解谜系统)
11. [子页面揭示机制](#11-子页面揭示机制)
12. [防翻译防御体系](#12-防翻译防御体系)
13. [移动端与 PC 端差异化体验](#13-移动端与-pc-端差异化体验)
14. [URL 参数系统](#14-url-参数系统)
15. [成就系统](#15-成就系统)
16. [钓客日志与 Fish Score](#16-钓客日志与-fish-score)
17. [ISSN 七击彩蛋](#17-issn-七击彩蛋)
18. [PDF 水印系统](#18-pdf-水印系统)
19. [内部 Prompt 模板系统](#19-内部-prompt-模板系统)
20. [社区投稿收集机制](#20-社区投稿收集机制)
21. [配套脚本与工具链](#21-配套脚本与工具链)
22. [SEO 策略](#22-seo-策略)
23. [内容策略](#23-内容策略)
24. [法律与伦理框架](#24-法律与伦理框架)
25. [实施路线图](#25-实施路线图)
26. [附录：术语表](#附录术语表)

---

## 1. 项目概述

### 1.1 核心理念

B.A.I.T.（Bureau of Advanced Interdisciplinary Theories）是一个模仿正规学术出版机构的恶搞/戏仿平台，目标受众为中国互联网上的"民科"群体——那些缺乏正规学术训练、热衷于发表"颠覆性理论"却对学术出版规范了解甚少的人群。平台名称本身即为核心隐喻："bait"意为诱饵/钓鱼，暗示整个平台就是一个精心设计的"学术钓鱼"场景。

平台的运作模式类似于"楚门的世界"：目标受众（民科）会认为这是一个真实的、权威的国际学术出版机构，而具备足够辨识力的正常用户则可以通过嵌入的线索、ARG 谜题和隐藏内容，发现平台的真实性质。这种双层体验设计确保了平台既是讽刺艺术品，也是一个互动解谜游戏。

### 1.2 设计哲学

- **沉浸优先**：对于目标受众，平台必须看起来与真实的学术出版网站无异，从视觉设计、术语使用到交互流程，都需要达到"以假乱真"的程度
- **线索渐进**：对于解谜者，线索的发现应当是渐进式的——从微妙的违和感，到明确的文化暗示，再到直接的揭示，形成一个完整的认知链
- **零收费原则**：平台绝不向任何用户收取任何费用，这是法律安全的核心底线
- **社区共创**：像 S.H.I.T. 期刊那样，收集社区中有趣的、有创意的投稿，让平台成为"乐子"的集散地

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
- 寻找"乐子"的普通网友

---

## 2. 命名体系

### 2.1 B.A.I.T. — 平台主体

| 层面 | 含义 | 说明 |
|------|------|------|
| 官方释义 | Bureau of Advanced Interdisciplinary Theories | 高级跨学科理论局 — 听起来像正经的学术机构 |
| 隐喻含义 | Bait = 诱饵/钓鱼 | 整个平台就是"诱饵"，钓鱼执法的学术版 |
| 中文映射 | 诱饵局 | 不可在任何官方界面出现，仅在内部分享时使用 |

### 2.2 D.I.O. — 文档标识系统

替代 DOI（Digital Object Identifier）的文档身份标识体系。

| 层面 | 含义 | 说明 |
|------|------|------|
| 官方释义 | Document Identity Ontology | 文档身份本体论 — 比"标识符"更"哲学" |
| 隐喻含义 | DIO = 意大利语中的"上帝" | 暗示自我封神的学术自大 — "我的理论是上帝级别的" |
| 编号格式 | `DIO:B.A.I.T.<YYYY>.<SEQ>` | 例如 `DIO:B.A.I.T.2025.0001` |

D.I.O. 的设计巧妙之处在于：对外它听起来比 DOI 更"高级"（本体论 vs 标识符），符合民科追求"高深"的心理；对内，"上帝"的暗示是一种精准的讽刺——那些声称自己理论超越爱因斯坦的人，本质上就是在自封为神。

### 2.3 其他命名

| 缩写 | 官方释义 | 隐喻 | 用途 |
|------|---------|------|------|
| C.A.S.T. | Committee for Academic Standards & Theory | 抛竿（钓鱼第一步） | 投稿提交阶段 |
| H.O.O.K. | Holistic Objective Observation Kernel | 上钩 | 审稿进行阶段 |
| C.A.T.C.H. | Comprehensive Assessment & Theoretical Certification Hub | 收网 | 审稿完成阶段 |
| R.E.L.E.A.S.E. | Repository of Evaluated Literature & Exemplary Academic Studies Edition | 放生 | 论文发布阶段 |
| F.I.S.H. | Formal Index of Scholarly Highlights | 鱼 | 论文收录数据库 |
| A.N.G.L.E.R. | Archived Network of Genuine Learning & Enlightenment Records | 钓客 | 发现者社区 |
| N.E.T. | Novel Epistemological Tracker | 网 | 追踪系统 |

---

## 3. 内容边界与安全策略

### 3.1 绝对禁区（任何情况下不可出现）

以下内容类型在任何层级、任何形式下均**严格禁止**，无例外：

1. **政治敏感内容**：涉及中国政治体制、领导人、政策批评的任何内容
2. **邪教/极端主义内容**：任何可能被归类为邪教宣传或极端主义思想的内容
3. **医疗/健康建议**：任何可能被误读为医疗建议的内容，包括"替代疗法"、"能量治疗"等
4. **种族/性别歧视内容**：任何形式的歧视性言论
5. **金融/投资建议**：任何可能被解读为投资建议的内容
6. **真实个人攻击**：针对真实存在的学术人物的诽谤或人身攻击
7. **儿童不当内容**：任何涉及未成年人的不当内容

### 3.2 安全主题领域（推荐创作方向）

以下领域天然适合产生荒诞但无害的内容，且与民科常见的"研究"方向高度重合：

- **数学/几何**：宣称证明哥德巴赫猜想、发明新几何、推翻微积分
- **理论物理/宇宙学**：大统一理论、多维空间模型、暗物质替代解释
- **AI/计算理论**：宣称发明超越图灵机的计算模型、意识上传理论
- **哲学/认识论**：新的"万物理论"、重新定义时间/空间/因果关系
- **信息论/密码学**：宣称破解现有加密体系、发明不可破解的密码
- **进化论/古生物**（注意不涉及人类起源的种族敏感内容）：恐龙文明假说等

### 3.3 内容安全审查原则

- **无害性测试**：如果这篇论文被一个完全不懂学术的人当真，是否会造成任何实际伤害？如果答案为"是"，则不可发布
- **可辨识性测试**：一个受过大学教育的正常人，能否在仔细阅读后识别出这是戏仿？如果答案为"否"，则需要增加更多线索
- **法律风险评估**：内容是否可能引发任何法律纠纷？如果答案为"是"，则不可发布
- **去人格化原则**：所有"作者"均使用虚构身份，绝不暗示指向真实个人
- **反伤害扩散原则**：即使内容本身无害，如果其传播方式可能导致误导性后果，也需重新评估

---

## 4. 分级系统

### 4.1 F 级（Fun / 娱乐级）

F 级论文是平台的主体内容，专门用于收录各类戏仿、恶搞、荒诞的"学术论文"。F 级论文的核心要求是"有趣"——它必须具备足够的娱乐价值，让人读后产生"这也行？"的惊叹或会心一笑。

| 等级 | 代号 | 含义 | 标准 | 典型示例 |
|------|------|------|------|---------|
| F-0 | CIRCUS | 马戏团级 | 纯恶搞，明显荒诞，任何有常识的人一眼可辨 | 《论量子纠缠在情感关系中的应用：以"心灵感应"为案例分析》 |
| F-1 | PUZZLE | 谜题级 | 伪装度较高，需要一定专业知识才能识别荒谬之处 | 《基于修正黎曼猜想的质数分布新证明：一个直觉主义的进路》 |
| F-2 | STAGE | 舞台级 | 高度逼真的学术伪装，格式/术语/引用全部仿真，只有核心逻辑是荒谬的 | 《超对称弦论框架下的引力波频谱修正：一种非微扰方法》 |
| F-3 | MIRROR | 镜像级 | 与真实前沿论文几乎无法区分，只有极其微妙的破绽——这是最高级别的伪装 | 《拓扑量子场论中的非阿贝尔任意子编织统计：一个新的计算范式》 |

**F-3 MIRROR 的特殊性**：F-3 级论文是平台"钓鱼"功能的核心载体。这类论文在格式、术语、引用格式、数学推导的表面层面都高度逼真，但核心论点或关键推导步骤中存在根本性逻辑错误。F-3 论文的创作需要维护者具备相关领域的专业知识，确保"破绽"设置得恰到好处——既不会太明显导致目标受众立即识破，也不会太隐蔽导致真的误导了专业人士。

### 4.2 T 级（Truth / 真实级）

T 级论文用于收录真实的、有学术价值的预印本或开放获取论文。T 级的存在有两个目的：一是为平台提供"掩护"——一个只收录恶搞论文的"出版社"太容易暴露；二是为真正的学术交流提供一个有趣的、非传统的渠道。

| 等级 | 代号 | 含义 | 标准 | 说明 |
|------|------|------|------|------|
| T-1 | DECOY | 诱饵级 | 真实论文，但选题冷门或晦涩，作为"掩护"内容 | 正常但少有人读的论文，增加平台的"学术深度"表象 |
| T-2 | BEACON | 信标级 | 真实且有价值的论文，作为"灯塔"吸引专业读者 | 有一定学术价值的预印本，让平台不完全是个笑话 |
| T-3 | ANCHOR | 锚点级 | 高质量论文，作为平台学术"锚点" | 少量精选的高质量内容，确保平台不是纯空壳 |

### 4.3 分级标注的视觉设计

分级标注在外部界面（面向目标受众）和内部界面（面向解谜者）呈现不同的视觉样式：

**外部视图**：分级以极其正式的学术风格呈现，例如：

```
Classification: F-2 (Rigorous Peer Review Completed)
Review Code: B.A.I.T.-REV-2025-0042
```

这里 "F-2" 不会解释为 "Fun-2"，而是被包装在正式的审稿代码中。

**内部视图**（通过揭示机制解锁后）：

```
🎭 F-2 STAGE — This paper is a carefully crafted parody.
   The core argument contains deliberate logical flaws.
   Can you find all 3 embedded errors?
```

---

## 5. 钓鱼审稿系统

### 5.1 四阶段流程

整个审稿流程在外部呈现为标准的学术同行评审流程，但内部对应的是钓鱼的四个步骤：

| 阶段 | 钓鱼术语 | 外部学术术语 | 内部含义 | 用户可见状态 |
|------|---------|-------------|---------|-------------|
| 1 | 抛竿 (Cast) | Submitted | 诱饵已放出，等待目标上钩 | "Your manuscript has been received and is under initial screening" |
| 2 | 上钩 (Hook) | Under Review | 目标已上钩，正在"审稿" | "Your manuscript is currently under peer review by our expert panel" |
| 3 | 收网 (Catch) | Accepted/Revision Required | 确认上钩，准备"发表" | "Congratulations! Your manuscript has been accepted for publication" |
| 4 | 放生 (Release) | Published | 鱼已放生，论文公之于众，线索也随之公开 | "Your paper is now publicly available in our repository" |

### 5.2 审稿状态页面设计

外部审稿追踪页面的设计必须与真实学术出版平台（如 ScholarOne、Editorial Manager）高度相似：

- **进度条**：使用正式的百分比进度显示（"Initial Screening: 100% → Peer Review: 67% → Final Decision: Pending"）
- **审稿人信息**：显示匿名审稿人编号（"Reviewer #1", "Reviewer #2"），但绝不暴露真实身份
- **预计时间**：显示预计完成日期（实际所有论文都会"通过"，时间只是制造真实感的道具）
- **历史记录**：显示状态变更的时间线，包括每个状态变更的"日期"和"操作人"（虚构的编辑姓名）

### 5.3 "审稿意见"生成

每篇论文的"审稿意见"由内部 Prompt 系统自动生成（详见第 19 节），必须满足以下要求：

- **语言风格**：使用正式的学术英语，包含典型的审稿用语（"The authors claim...", "It should be noted that...", "We recommend minor revisions..."）
- **肯定为主**：审稿意见以正面评价为主，这与真实高质量期刊的严格审稿形成讽刺性对比——民科论文在这里"通过审稿"恰恰说明了这个"审稿"的无效性
- **微妙暗示**：在正面评价中嵌入极微妙的暗示，只有仔细阅读才能察觉违和感（例如："The authors' groundbreaking approach to proving P=NP through dream analysis represents a novel paradigm that challenges conventional computational complexity theory"）
- **修改建议**：给出的"修改建议"均为表面性的格式调整，绝不触及核心逻辑问题

---

## 6. B.I. 诱饵指数评估体系

### 6.1 概述

B.I.（Bait Index，诱饵指数）是平台为每篇论文计算的一个综合评分，衡量该论文对目标受众（民科）的"诱骗效果"——即论文看起来有多像一篇真正的学术论文。B.I. 的命名灵感来自"SB体"等网络评分文化，但在外部界面中被包装为"Bibliometric Index"（文献计量指数）。

### 6.2 五维评估模型

B.I. 由五个维度组成，每个维度 0-20 分，总分 0-100：

| 维度 | 英文名 | 评估内容 | 高分特征 | 低分特征 |
|------|--------|---------|---------|---------|
| 语法 (Syntax) | Syntactic Coherence | 论文语言的语法正确性和学术规范性 | 完美的学术英语，零语法错误 | 中式英语，明显语法错误 |
| 密度 (Density) | Terminological Density | 专业术语的密度和分布 | 术语丰富且分布均匀，如同真实论文 | 术语稀少或堆砌不自然 |
| 逻辑 (Logic) | Logical Plausibility | 论证逻辑的表面合理性 | 逻辑链表面完整，推导过程看似严谨 | 逻辑跳跃明显，论证不连贯 |
| 缝合 (Stitch) | Interdisciplinary Stitching | 跨学科内容的"缝合"质量 | 多学科术语自然融合，看似创新 | 生硬拼接，学科间缺乏联系 |
| 可检测 (Detect) | AI Detectability | AI 生成内容的可检测性 | 通过主流 AI 检测工具，低检测率 | AI 生成痕迹明显 |

### 6.3 B.I. 评分与分级的关系

| B.I. 范围 | 对应分级 | 说明 |
|-----------|---------|------|
| 0-20 | F-0 CIRCUS | 伪装度极低，纯粹的搞笑论文 |
| 21-40 | F-1 PUZZLE | 有一定伪装度，需要专业知识才能识别 |
| 41-70 | F-2 STAGE | 高伪装度，格式和术语高度仿真 |
| 71-100 | F-3 MIRROR | 极高伪装度，与真实论文几乎无法区分 |

### 6.4 B.I. 的外部呈现

在论文页面上，B.I. 以"Bibliometric Index"的名义显示：

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

### 6.5 B.I. 计算脚本设计

B.I. 的计算由配套 Python 脚本完成，核心逻辑包括：

- **Syntax 评分**：使用 LanguageTool 进行语法检查，结合学术写作规范进行评分
- **Density 评分**：基于领域术语词典计算术语密度和分布均匀性
- **Logic 评分**：使用 LLM 评估论证结构的表面合理性（不评估结论正确性）
- **Stitch 评分**：检测跨学科术语的共现模式，与真实跨学科论文的模式进行对比
- **Detect 评分**：使用多种 AI 检测工具（GPTZero、Originality.ai 等）的检测结果取平均

---

## 7. 平台架构

### 7.1 整体架构

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
              │   bait.github.io    │
              └─────────────────────┘
```

### 7.2 技术栈选型

| 层面 | 技术选择 | 理由 |
|------|---------|------|
| 静态站点生成 | Hugo 或 Next.js SSG | 极快的构建速度，纯静态输出适合 GitHub Pages |
| 前端框架 | 原生 JS + 少量 Alpine.js | 轻量级，不需要重型框架；localStorage 操作为主 |
| 样式 | Tailwind CSS | 快速开发，响应式设计方便 |
| 内容格式 | Markdown + YAML Front Matter | 版本控制友好，便于自动化处理 |
| PDF 生成 | WeasyPrint 或 Pandoc | 从 Markdown 生成带水印的 PDF |
| 搜索 | Pagefind | 静态站点搜索，无需后端 |
| 评论/互动 | Giscus (GitHub Discussions) | 基于 GitHub，无需额外后端 |
| CI/CD | GitHub Actions | 自动构建、部署、质量检查 |

### 7.3 目录结构设计

```
bait-platform/
├── .github/
│   ├── workflows/
│   │   ├── deploy.yml          # 自动部署到 GitHub Pages
│   │   ├── review-check.yml    # PR 提交自动检查
│   │   └── bi-calculate.yml    # B.I. 自动计算
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
│       ├── submission.yml      # 投稿模板
│       └── bug-report.yml      # 问题报告
├── content/
│   ├── papers/                 # 论文 Markdown 源文件
│   │   ├── 2025/
│   │   │   ├── 0001-quantum-entanglement-love.md
│   │   │   └── 0002-riemann-intuitionist.md
│   │   └── _index.md
│   ├── journal/                # 期刊信息页面
│   │   ├── about.md
│   │   ├── editorial-board.md
│   │   ├── submission-guidelines.md
│   │   └── issn-information.md
│   ├── authors/                # 虚构作者页面
│   │   ├── _index.md
│   │   └── profiles/
│   ├── arg/                    # ARG 隐藏内容（不在导航中显示）
│   │   ├── layer1/
│   │   ├── layer2/
│   │   └── layer3/
│   └── _index.md               # 首页
├── data/
│   ├── achievements.json       # 成就定义
│   ├── fish_species.json       # "鱼种"定义（论文分类）
│   ├── prompt_templates.json   # 审稿 Prompt 模板
│   └── backlinks.json          # 反向链接索引（自动生成）
├── layouts/
│   ├── _default/
│   ├── papers/
│   ├── partials/
│   └── shortcodes/
├── static/
│   ├── css/
│   ├── js/
│   │   ├── achievements.js     # 成就系统
│   │   ├── angler-log.js       # 钓客日志
│   │   ├── reveal.js           # 子页面揭示
│   │   ├── arg-engine.js       # ARG 引擎
│   │   ├── anti-translate.js   # 防翻译
│   │   ├── watermark.js        # PDF 水印
│   │   └── issn-easter.js      # ISSN 彩蛋
│   ├── fonts/
│   ├── images/
│   └── pdfs/                   # 生成的 PDF 文件
├── scripts/
│   ├── bi_calculator.py        # B.I. 计算器
│   ├── paper_publisher.py      # 论文发布脚本
│   ├── pdf_generator.py        # PDF 生成（含水印）
│   ├── backlink_generator.py   # 反向链接索引生成
│   ├── review_generator.py     # 审稿意见生成
│   └── content_validator.py    # 内容安全验证
├── config.toml / config.yaml
└── README.md
```

### 7.4 Markdown Front Matter 规范

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
date: 2025-03-15
grade: F-2
grade_code: STAGE
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
linked_papers:
  - dio: "DIO:B.A.I.T.2025.0003"
    relation: "cites"
  - dio: "DIO:B.A.I.T.2025.0007"
    relation: "extends"
  - dio: "DIO:B.A.I.T.2024.0012"
    relation: "refutes"
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
---
```

---

## 8. 投稿与审稿工作流

### 8.1 投稿渠道

平台支持两种投稿方式，均基于 GitHub：

**方式一：GitHub PR 投稿（正式流程）**

1. 投稿者 Fork 仓库
2. 按照 Front Matter 规范创建 Markdown 文件到 `content/papers/` 目录
3. 提交 Pull Request，使用 `submission.yml` 模板
4. GitHub Actions 自动运行 `content_validator.py` 检查内容安全
5. GitHub Actions 自动运行 `bi_calculator.py` 计算 B.I. 分数
6. 维护者审查 PR（人工 + 自动）
7. 合并后自动部署

**方式二：Issue 投稿（简化流程）**

1. 投稿者提交 GitHub Issue，使用 `submission.yml` 模板
2. 维护者将内容整理为 Markdown 并创建 PR
3. 后续流程同方式一

### 8.2 维护者审查标准

维护者的审查是平台质量控制的核心环节，审查标准分为"外部质量"和"内部质量"两个层面：

**外部质量审查**（确保论文看起来像真的）：
- 学术格式是否规范（摘要、关键词、章节结构、引用格式）
- 语言质量是否达标（语法正确性、学术用语准确性）
- 图表是否专业（格式规范、标注清晰）
- 参考文献是否格式正确

**内部质量审查**（确保论文"有趣"且安全）：
- 内容是否符合安全边界要求
- 是否有足够的娱乐价值
- F 级论文的"破绽"设置是否恰当
- ARG 线索嵌入是否到位
- B.I. 评分是否与预期分级匹配

**审查严格度**：
- 投稿不是"照单全收"——维护者会拒绝无聊的、质量太低的、或存在安全风险的投稿
- 这种"严格的审查"本身就是讽刺的一部分：一个假期刊的审稿比真期刊还严格
- 被拒绝的投稿会收到正式的"拒稿信"（同样由 Prompt 系统生成）

### 8.3 审稿时间线模拟

为了增加真实感，审稿时间线需要模拟真实学术期刊的节奏：

- 提交后 3-7 天：状态变为 "Under Review"
- "审稿" 期间：随机间隔更新状态（"Reviewer #1 has submitted their report"）
- 审稿周期：14-45 天（根据论文长度和"审稿人数量"随机设定）
- 修改轮次：F-0/F-1 通常直接接收，F-2/F-3 可能需要 1-2 轮"修改"

---

## 9. 双向页面链接系统

### 9.1 设计理念

受 Obsidian 笔记软件的双向链接启发，B.A.I.T. 的论文页面之间建立双向链接关系。在真实学术出版中，论文之间的引用关系是单向的（A 引用 B，B 并不知道被 A 引用），而 B.A.I.T. 的链接系统是双向的——如果论文 A 链接到论文 B，那么论文 B 的页面上也会自动显示"被论文 A 引用/延伸/反驳"的信息。

这种设计有两个目的：
1. **增强沉浸感**：论文之间的密集互联让整个平台看起来像是一个活跃的学术社区
2. **增加解谜维度**：链接关系本身可以是 ARG 线索的一部分——如果把所有链接关系可视化，可能会发现隐藏的模式

### 9.2 链接类型

| 链接类型 | Front Matter 中的 relation 值 | 显示文本 | 颜色 |
|---------|-------------------------------|---------|------|
| 引用 | `cites` | "Cited by" / "Cites" | 蓝色 |
| 延伸 | `extends` | "Extended by" / "Extends" | 绿色 |
| 反驳 | `refutes` | "Refuted by" / "Refutes" | 红色 |
| 相关 | `related` | "Related to" | 灰色 |
| 前作 | `predecessor` | "Follow-up to" / "Followed by" | 紫色 |
| 隐藏 | `secret` | 不显示在外部视图中 | 无色 |

`secret` 类型是特殊的——它定义的链接关系只在内部视图中可见，用于 ARG 线索传递。

### 9.3 反向链接索引

反向链接索引存储在 `data/backlinks.json` 中，由 `scripts/backlink_generator.py` 自动生成：

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

### 9.4 链接图谱可视化

在论文页面的侧边栏或底部，显示一个交互式的链接图谱：

- **节点**：每篇论文是一个节点，大小根据 B.I. 分数或被引次数变化
- **边**：链接关系是边，颜色根据链接类型变化
- **交互**：点击节点跳转到对应论文，悬停显示论文标题和摘要
- **隐藏模式**：当用户解锁内部视图后，图谱会显示 `secret` 类型的链接，可能形成一个可辨识的图案（如鱼钩形状、B.A.I.T. 字母等）

### 9.5 链接关系的 ARG 应用

链接关系可以承载隐藏信息：

- **路径密码**：沿着特定链接路径（如 "反驳→延伸→引用→反驳"）遍历的论文编号，可以组成一个密码
- **首字母拼字**：按链接顺序读取论文标题首字母，可以拼出隐藏单词
- **图谱图案**：所有论文的链接关系可视化后，可能形成特定的几何图案
- **时间线密码**：论文发布日期按链接顺序排列，可能编码特定信息

---

## 10. 线索与 ARG 解谜系统

### 10.1 三层线索体系

ARG 系统采用三层递进结构，每层对应不同深度的解谜者：

**第一层：表层线索（Base Layer）**

这些线索相对容易发现，任何有足够好奇心的用户都可能注意到：

| 线索类型 | 具体实现 | 发现难度 |
|---------|---------|---------|
| 首字母缩写 | B.A.I.T., D.I.O., F.I.S.H. 等缩写展开后构成钓鱼隐喻 | 低 |
| 界面违和感 | 审稿流程过快，所有论文都"通过"，审稿意见过于正面 | 低 |
| 域名/URL | 如果使用 bait 相关域名，本身就是线索 | 低 |
| 作者信息 | 虚构作者的简历中有微妙的矛盾或荒诞之处 | 中 |
| 参考文献异常 | 部分参考文献不存在，或引用了虚构的来源 | 中 |
| 数学公式 | F-0/F-1 论文中的数学公式包含明显的笑话（如 ∞ = 42） | 中 |

**第二层：深层线索（Hidden Layer）**

需要主动探索或使用工具才能发现的线索：

| 线索类型 | 具体实现 | 发现难度 |
|---------|---------|---------|
| HTML 注释 | 页面源代码中包含 HTML 注释，有直接的提示信息 | 中 |
| CSS 隐藏文本 | 某些文本使用 CSS `display:none` 隐藏，需检查源代码 | 中 |
| 零宽字符 | 关键文本中嵌入零宽字符，编码后可提取隐藏信息 | 高 |
| 图片隐写术 | 论文中的图片包含 LSB 隐写信息 | 高 |
| Base64 编码 | 页面中某些看似随机的字符串实际是 Base64 编码的提示 | 高 |
| 子页面揭示 | 通过隐藏按钮或密钥输入解锁的隐藏内容 | 高 |

**第三层：核心线索（Core Layer）**

需要跨页面、跨媒体综合分析才能发现的终极线索：

| 线索类型 | 具体实现 | 发现难度 |
|---------|---------|---------|
| 跨页引用密码 | 多篇论文中的特定文本片段组合后形成完整信息 | 极高 |
| 链接图谱密码 | 论文间的链接关系可视化后形成特定图案 | 极高 |
| 时间线密码 | 论文发布时间/日期编码隐藏信息 | 极高 |
| 音频线索 | 某些 PDF 的元数据中包含音频文件的 URL | 极高 |
| D.I.O. 编号密码 | D.I.O. 编号的序列号按特定规则组合后可解码 | 极高 |

### 10.2 ARG 进度追踪

用户在 localStorage 中保存 ARG 解谜进度：

```javascript
{
  "bait_arg_progress": {
    "discovered_clues": ["html_comment_homepage", "ref_anomaly_0001"],
    "solved_puzzles": ["base64_footer"],
    "current_layer": 2,
    "unlocked_pages": ["/arg/layer1/transmission"],
    "achievement_ids": ["first_clue", "deep_diver"]
  }
}
```

### 10.3 ARG 交叉引用系统

不同论文之间的线索通过 Base64 编码的交叉引用连接：

- 论文 A 的图 3 中隐写了一段 Base64 文本
- 解码后得到：`DIO:B.A.I.T.2025.0007#figure_1`
- 访问论文 B 的图 1，发现另一个 Base64 文本
- 解码后得到下一步线索或直接揭示信息

这种"兔子洞"式的设计确保了解谜者需要阅读多篇论文、综合多条线索才能到达真相。

---

## 11. 子页面揭示机制

### 11.1 设计原则

子页面揭示机制是平台最核心的"双层体验"实现方式。每篇论文页面都包含一个隐藏的"真实评审"视图，只有通过特定操作才能解锁。这个机制确保了：

- 目标受众（民科）看到的永远是一个"正规学术期刊"的页面
- 解谜者通过互动可以发现平台的真实性质
- 揭示过程本身就是一种娱乐体验

### 11.2 触发方式

**隐藏按钮（Invisible Buttons）**

论文页面中存在若干不可见的触发区域，用户点击后会激活揭示流程：

| 触发位置 | 大小 | 行为 | 说明 |
|---------|------|------|------|
| 论文标题的某个字 | 1em × 1em | 点击计数 +1 | 连续点击 3 次激活 |
| 参考文献编号 [7] | 默认大小 | 弹出密钥输入框 | 仅特定编号的参考文献有效 |
| 页脚版权声明中的"B.A.I.T." | 文字区域 | 切换到内部视图 | 需要已解锁的成就 |
| D.I.O. 编号 | 编号区域 | 显示 D.I.O. 的真实含义 | 需要已发现至少 5 个线索 |
| 某个图表的空白区域 | 50×50px | 显示隐写信息 | 仅包含隐写的图表有效 |

**密钥输入**

当隐藏按钮被激活后，弹出一个看似正常的"附加信息访问"对话框：

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

### 11.3 揭示内容

解锁后的"真实评审"视图包含以下内容：

1. **平台真实声明**：B.A.I.T. 的真实性质说明
2. **论文内部评审**：维护者对论文的真实评价（讽刺性点评）
3. **破绽清单**：论文中故意设置的逻辑错误/荒谬之处
4. **B.I. 真实含义**：Bait Index 的揭示
5. **ARG 线索**：指向其他隐藏内容的线索
6. **成就解锁**：解锁对应的成就

### 11.4 揭示状态的持久化

揭示状态保存在 localStorage 中，用户刷新页面后仍然保持解锁状态：

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

## 12. 防翻译防御体系

### 12.1 设计背景

目标受众（中国民科）很可能使用浏览器内置翻译功能（如 Chrome 自动翻译）阅读英文内容。如果翻译功能将关键的双关语和暗示正确翻译成中文，那么钓鱼效果会大打折扣。因此需要设计一套"防翻译防御"机制，确保关键术语在翻译后仍然保持其表面的学术含义，而不会暴露隐藏的讽刺含义。

### 12.2 防御手段

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

### 12.3 防御层次

| 防御对象 | 防御手段 | 优先级 |
|---------|---------|-------|
| 平台名称缩写 | SVG 渲染 | 最高 |
| 审稿流程术语 | Unicode 变体 | 高 |
| 分级标注 | 零宽字符 | 高 |
| 揭示内容 | 图片文本 | 中 |
| 导航菜单 | CSS 伪元素 | 中 |
| 页脚声明 | 零宽字符 | 低 |

---

## 13. 移动端与 PC 端差异化体验

### 13.1 设计原则

移动端和 PC 端的差异化设计基于以下观察：

- **目标受众（民科）**更可能在手机上浏览，通过社交媒体链接进入，使用翻译功能阅读
- **解谜者/正常用户**更可能在 PC 上浏览，有能力查看源代码、使用开发者工具、安装插件

因此，移动端应该提供更少的线索（保持对目标受众的沉浸感），而 PC 端应该提供更多的线索（增加解谜者的发现机会）。

### 13.2 差异化内容

| 内容类型 | 移动端 | PC 端 |
|---------|-------|-------|
| 悬停效果 | 不可用 | 可用——悬停显示微妙线索 |
| 源代码注释 | 不可见 | 可见——HTML 注释中的线索 |
| 右键菜单 | 有限 | 完整——可查看源代码 |
| 开发者工具 | 不可用 | 可用——检查 DOM 中的隐藏元素 |
| 键盘快捷键 | 不可用 | 可用——特定组合键触发隐藏功能 |
| 屏幕尺寸利用 | 有限 | 充分——侧边栏显示更多信息和链接图谱 |
| PDF 下载 | 可用 | 可用 + 元数据检查提示 |
| 打印样式 | 不可用 | 可用——打印时显示隐藏水印 |

### 13.3 PC 端独有线索

以下线索只在 PC 端可见或可发现：

- **悬停效果**：鼠标悬停在特定元素上时显示微妙的视觉变化（如 B.A.I.T. 首字母轻微变色，暗示它们是缩写）
- **源代码注释**：HTML 注释中的直接提示（如 `<!-- Have you checked the backlinks? -->`）
- **CSS 伪元素内容**：某些 `::before`/`::after` 伪元素在检查 DOM 时可见
- **键盘快捷键**：`Ctrl+Shift+B` 在页面底部显示隐藏信息栏
- **响应式断点**：在极宽的屏幕（>2560px）上，页面两侧会显示额外的装饰性元素，其中包含线索
- **打印样式**：打印论文时，页面背景会出现肉眼可见的水印文字

---

## 14. URL 参数系统

### 14.1 参数列表

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

### 14.2 参数的发现方式

这些 URL 参数不会在任何公开文档中列出，而是通过以下方式让解谜者发现：

- HTML 注释中提及
- ARG 线索指向
- 成就解锁后提示
- 论文中的隐写信息包含 URL 示例
- 社区讨论中暗示

### 14.3 `?bait=0` 的特殊用途

`?bait=0` 参数有一个巧妙的用途：当有人想要"验证"平台的真实性时，使用这个参数可以获得一个完全"干净"的、没有任何线索的页面版本。这看似是一个"证明平台是正经的"功能，实际上是一个更深层的陷阱——它让验证者自己选择了"视而不见"。

---

## 15. 成就系统

### 15.1 设计理念

成就系统是一个基于 localStorage 的游戏化机制，用于追踪和奖励用户在平台上的探索行为。成就系统不仅增加了互动性，还充当了"引导"——通过成就的描述和进度提示，引导用户发现更多隐藏内容。

### 15.2 成就分类

**探索类成就（Discovery）**

| ID | 名称 | 图标 | 解锁条件 | 隐藏提示 |
|----|------|------|---------|---------|
| `first_visit` | Welcome, Researcher | 🎓 | 首次访问平台 | — |
| `first_paper` | Literature Review | 📖 | 阅读第一篇论文 | "Have you read it carefully?" |
| `paper_5` | Avid Reader | 📚 | 阅读 5 篇论文 | "Notice anything unusual?" |
| `paper_20` | Peer Reviewer | 🔍 | 阅读 20 篇论文 | "The truth is in the details" |
| `source_peek` | Behind the Curtain | 🧐 | 查看页面源代码 | "What else hides in the source?" |

**解谜类成就（Puzzle）**

| ID | 名称 | 图标 | 解锁条件 | 隐藏提示 |
|----|------|------|---------|---------|
| `first_clue` | Something's Off | 🤔 | 发现第一个表层线索 | "You're starting to see..." |
| `html_comment` | Code Reader | 💻 | 发现 HTML 注释中的线索 | "The source reveals all" |
| `base64_decode` | Cryptographer | 🔐 | 解码第一个 Base64 线索 | "There are more layers..." |
| `stego_found` | Hidden in Plain Sight | 🖼️ | 发现图片隐写信息 | "Images speak louder than words" |
| `arg_layer2` | Deep Diver | 🌊 | 进入 ARG 第二层 | "You're not in Kansas anymore" |
| `arg_layer3` | The Abyss Gazes Back | 👁️ | 进入 ARG 第三层 | "Welcome to the inner circle" |

**互动类成就（Interaction）**

| ID | 名称 | 图标 | 解锁条件 | 隐藏提示 |
|----|------|------|---------|---------|
| `first_reveal` | Red Pill | 💊 | 首次解锁论文的真实评审 | "There is no spoon" |
| `reveal_5` | Conspiracy Theorist | 🕵️ | 解锁 5 篇论文的真实评审 | "Everything is connected" |
| `reveal_all` | The Truth Is Out There | 👽 | 解锁所有已发布论文的真实评审 | "Or is it?" |
| `issn_click_7` | Lucky Seven | 7️⃣ | 点击 ISSN 7 次 | "You've found the Easter egg" |
| `secret_key` | Keymaster | 🔑 | 输入正确的揭示密钥 | "What other doors can you open?" |

**社区类成就（Community）**

| ID | 名称 | 图标 | 解锁条件 | 隐藏提示 |
|----|------|------|---------|---------|
| `first_comment` | Academic Discourse | 💬 | 在论文页面留下第一条评论 | — |
| `submission` | Published Author | ✍️ | 首次投稿（PR 或 Issue） | "Welcome to the B.A.I.T." |
| `submission_accepted` | Peer Approved | ✅ | 投稿被接受 | "Hook, line, and sinker" |
| `submission_rejected` | Revise & Resubmit | 🔄 | 投稿被拒绝 | "Even fake journals have standards" |

**元成就（Meta）**

| ID | 名称 | 图标 | 解锁条件 | 说明 |
|----|------|------|---------|------|
| `all_discovery` | Encyclopedia | 🏆 | 解锁所有探索类成就 | 收集癖奖励 |
| `all_puzzle` | Master Angler | 🎣 | 解锁所有解谜类成就 | 终极解谜者 |
| `all_interaction` | Insider | 🎭 | 解锁所有互动类成就 | 平台深度参与者 |
| `the_fish` | The Fish | 🐟 | 在未解锁任何揭示的情况下阅读 50 篇论文 | 讽刺性成就——你就是"鱼" |
| `the_angler` | The Angler | 🎣 | 解锁超过 90% 的成就 | 终极成就 |

### 15.3 成就通知

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

### 15.4 成就数据结构

```javascript
{
  "bait_achievements": {
    "unlocked": {
      "first_visit": {"unlocked_at": "2025-03-15T10:00:00Z", "notified": true},
      "first_paper": {"unlocked_at": "2025-03-15T10:05:00Z", "notified": true},
      "first_clue": {"unlocked_at": "2025-03-15T11:30:00Z", "notified": true}
    },
    "progress": {
      "paper_5": {"current": 3, "target": 5},
      "reveal_5": {"current": 1, "target": 5}
    }
  }
}
```

---

## 16. 钓客日志与 Fish Score

### 16.1 钓客日志（Angler's Log）

钓客日志是用户的个人主页，基于 localStorage 实现，展示用户在平台上的所有活动记录：

- **探索记录**：阅读过的论文列表、阅读时长
- **解谜进度**：发现的线索、解决的谜题、ARG 进度
- **成就列表**：已解锁的成就、进度中的成就
- **收藏夹**：标记的论文
- **笔记**：用户自己添加的笔记/标注
- **统计**：总阅读量、平均阅读时长、线索发现率等

### 16.2 Fish Score

Fish Score 是一个综合评分，衡量用户在平台上的"洞察力"——即用户有多接近发现真相：

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

### 16.3 Fish Score 等级

| 分数范围 | 等级 | 称号 | 说明 |
|---------|------|------|------|
| 0-50 | F | The Fish 🐟 | 你就是鱼 |
| 51-200 | D | Curious Onlooker 👀 | 开始注意到异样 |
| 201-500 | C | Skeptical Reader 🤨 | 产生怀疑 |
| 501-1000 | B | Amateur Detective 🔍 | 主动寻找线索 |
| 1001-2000 | A | Skilled Angler 🎣 | 熟练的解谜者 |
| 2001+ | S | Master Angler 🏆 | 完全洞察真相 |

---

## 17. ISSN 七击彩蛋

### 17.1 触发方式

在平台首页或期刊信息页面，ISSN 号码是一个可点击的元素。连续点击 ISSN 号码 7 次后，触发彩蛋。

ISSN 显示格式：

```
ISSN: 2747-8249
```

（注：这个 ISSN 是虚构的，不属于任何真实期刊。数字选择可以包含隐藏含义，如 2747 在某种编码下指向特定信息。）

### 17.2 彩蛋内容

七击彩蛋触发后，页面进入一个特殊的"深层模式"，展示以下内容：

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
                                                         │
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

### 17.3 彩蛋的 ARG 连接

这个"内部备忘录"本身也包含线索：

- "47 subjects" 这个数字在后续 ARG 中会出现，是某个密码的一部分
- "Project MIRROR" 指向 F-3 MIRROR 级论文
- "The best lie is the one they tell themselves" 是理解整个平台哲学的关键语句
- 备忘录的日期（如果显示）指向另一个隐藏页面

---

## 18. PDF 水印系统

### 18.1 设计原则

所有从平台下载的 PDF 文件都必须包含水印。水印的设计需要在两个目标之间取得平衡：

1. **对目标受众**：水印看起来像是正规的版权保护措施，与真实学术出版商的水印一致
2. **对解谜者**：水印中可能包含隐藏信息

### 18.2 水印类型

**显性水印（Visible Watermark）**

- **位置**：页面中央，45度倾斜
- **内容**：`B.A.I.T. © 2025 — All Rights Reserved`
- **样式**：浅灰色，半透明（opacity 0.05-0.1），不影响阅读
- **目的**：看起来像正规的版权声明水印

**隐性水印（Invisible Watermark）**

- **位置**：页面边缘，白色文字白色背景（需选择文本才能看到）
- **内容**：`DIO:B.A.I.T.2025.XXXX | B.I.:XX.X | F-X | [TIMESTAMP]`
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

### 18.3 水印的 ARG 功能

- **隐藏文本**：隐性水印中的时间戳可能编码了 ARG 线索（如时间戳的十六进制表示包含可读文本）
- **微字体**：页脚水印的某些字符使用微字体编码，需要放大到 400% 以上才能看到附加的隐藏文本
- **PDF 结构**：PDF 的内部对象结构中包含注释，使用 `pdftotext` 或 PDF 解析工具可以提取

### 18.4 PDF 生成脚本

PDF 生成使用 `scripts/pdf_generator.py`，基于 WeasyPrint 或 ReportLab：

```python
# 核心逻辑伪代码
def generate_paper_pdf(markdown_path, output_path):
    # 1. 解析 Markdown + Front Matter
    paper = parse_paper(markdown_path)

    # 2. 渲染 HTML 模板
    html = render_template("paper_pdf.html", paper=paper)

    # 3. 添加显性水印
    html = add_visible_watermark(html, text=f"B.A.I.T. © {paper.year}")

    # 4. 添加隐性水印
    html = add_invisible_watermark(html,
        text=f"DIO:{paper.dio} | B.I.:{paper.bi_score} | {paper.grade}")

    # 5. 生成 PDF
    pdf = weasyprint.HTML(string=html).write_pdf()

    # 6. 添加元数据水印
    pdf = add_metadata(pdf, {
        "Author": "Bureau of Advanced Interdisciplinary Theories",
        "Subject": paper.dio,
        "Keywords": f"PARODY,SATIRE,NOT_REAL_ACADEMIC_PAPER,{paper.dio}",
        "X-Bait-Grade": paper.grade,
        "X-Bait-Index": str(paper.bi_score)
    })

    # 7. 添加页脚水印
    pdf = add_footer_watermark(pdf,
        text=f"Published by B.A.I.T. | {paper.dio} | "
             f"This document was generated by an automated peer review system")

    # 8. 保存
    with open(output_path, 'wb') as f:
        f.write(pdf)
```

---

## 19. 内部 Prompt 模板系统

### 19.1 设计目的

为了高效生成"审稿意见"和其他互动内容，平台内置了一套 Prompt 模板系统。这些模板用于指导 LLM 生成符合平台风格的内容，但考虑到浏览器端 API Key 的限制，实际使用场景主要分为两种：

1. **维护者使用**：维护者在本地使用脚本调用 LLM API，批量生成审稿意见等内容
2. **用户端使用**：用户在浏览器中通过平台提供的界面调用（需自行提供 API Key，或使用平台建议的方式）

### 19.2 Prompt 模板

**审稿意见生成模板**

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

**拒稿信生成模板**

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

**F 级论文创作辅助模板**

```markdown
You are helping create a parody academic paper for B.A.I.T., a satirical
academic publisher.

Paper parameters:
- Grade: {{grade}} (F-0 to F-3)
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
- F-0 (CIRCUS): Obviously absurd, anyone can tell it's a joke
- F-1 (PUZZLE): Requires some domain knowledge to spot the absurdity
- F-2 (STAGE): Highly convincing format, only core logic is absurd
- F-3 (MIRROR): Nearly indistinguishable from real papers, extremely subtle flaws
```

**作者简介生成模板**

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
```

### 19.3 模板管理

Prompt 模板存储在 `data/prompt_templates.json` 中，维护者可以通过 PR 更新模板：

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

## 20. 社区投稿收集机制

### 20.1 设计理念

像 S.H.I.T. 期刊（Studies in Humor and Intelligent Texts）那样，B.A.I.T. 也是一个社区驱动的平台。任何人都可以投稿有趣的"论文"，但维护者的审查会很严格——不是所有投稿都会被接受，只有真正有趣、有创意、符合平台调性的内容才会被发布。

这种"严格审查"本身就是讽刺的一部分：一个假期刊的投稿门槛可能比某些真期刊还高。

### 20.2 投稿流程

```
投稿者 → GitHub Issue/PR → 自动检查 → 维护者审查 → 接受/拒绝
                                    ↓                ↓
                              content_validator   review_generator
                              bi_calculator       notification
```

**第一步：投稿准备**

投稿者需要准备以下材料：

1. 论文正文（Markdown 格式，按 Front Matter 规范）
2. 论文分级自评（F-0 到 F-3）
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

### 20.3 投稿激励

为了鼓励高质量投稿，平台提供以下激励：

- **作者页面**：每位投稿者（使用笔名）都有专属作者页面，展示其所有投稿
- **Fish Score 加分**：投稿被接受可获得 Fish Score 加分
- **成就解锁**：投稿相关成就（参见第 15 节）
- **社区认可**：论文的阅读量、评论、引用等数据公开展示
- **特别收录**：特别优秀的投稿可以被标记为"Editor's Choice"

### 20.4 投稿类型

| 类型 | 说明 | 审查标准 |
|------|------|---------|
| 原创论文 | 完整的恶搞学术论文 | 最严格——需要完整的学术格式、有趣的荒谬点、合格的安全审查 |
| 短通讯 | 简短的讽刺性学术评论 | 较宽松——格式要求较低，但内容质量仍需达标 |
| 致编辑信 | 假装对已发表论文的"学术讨论" | 宽松——需要引用平台已有论文，增加链接密度 |
| 撤稿声明 | 对平台论文的"撤稿"（讽刺性） | 需要维护者批准——确保撤稿理由足够有趣 |
| 勘误 | 对平台论文的"勘误"（引入更多荒谬） | 宽松——越荒谬越好 |

---

## 21. 配套脚本与工具链

### 21.1 脚本概览

虽然是静态站点，但仓库中包含丰富的 Python 脚本和工具，用于内容管理、质量控制和自动化操作：

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
| `sitemap_enhancer.py` | Python | 站点地图增强（SEO） | 部署时自动运行 |
| `cross_reference_checker.py` | Python | 交叉引用完整性检查 | PR 提交时自动运行 |
| `fish_species_classifier.py` | Python | 论文分类/标签建议 | 维护者辅助工具 |

### 21.2 content_validator.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. Content Validator
Validates submitted content against safety boundaries.
"""

import re
import json
import yaml
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
    "political": [...],  # 政治敏感词
    "medical": [...],    # 医疗/健康建议
    "cult": [...],       # 邪教/极端主义
    "discrimination": [...],  # 歧视
    "financial": [...],  # 金融建议
    "personal_attack": [...],  # 针对真人的攻击
}

def validate_front_matter(filepath: Path) -> ValidationResult:
    """验证 Front Matter 完整性"""
    errors = []
    warnings = []

    with open(filepath) as f:
        content = yaml.safe_load(f.read().split('---')[1])

    required_fields = ['title', 'authors', 'dio', 'date', 'grade',
                       'bi_score', 'abstract', 'keywords']
    for field in required_fields:
        if field not in content:
            errors.append(f"Missing required field: {field}")

    # 验证 D.I.O. 格式
    if not re.match(r'DIO:B\.A\.I\.T\.\d{4}\.\d{4}', content.get('dio', '')):
        errors.append(f"Invalid DIO format: {content.get('dio')}")

    return ValidationResult(
        passed=len(errors) == 0,
        errors=errors,
        warnings=warnings,
        score=100.0 if not errors else 0.0
    )

def validate_content_safety(filepath: Path) -> ValidationResult:
    """验证内容安全性"""
    errors = []
    warnings = []

    with open(filepath) as f:
        full_content = f.read()

    # 检查禁区关键词
    for category, keywords in FORBIDDEN_CATEGORIES.items():
        for keyword in keywords:
            if keyword in full_content:
                errors.append(
                    f"Forbidden content detected [{category}]: '{keyword}'"
                )

    return ValidationResult(
        passed=len(errors) == 0,
        errors=errors,
        warnings=warnings,
        score=max(0, 100 - len(errors) * 25 - len(warnings) * 5)
    )

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
    }, indent=2))
    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
```

### 21.3 bi_calculator.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. B.I. (Bait Index) Calculator
Calculates the 5-dimensional Bait Index for a paper.
"""

import json
import yaml
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
    # 实现细节：检查语法错误数量、学术用语规范等
    pass

def calculate_density_score(content: str, domain: str) -> float:
    """计算术语密度和分布均匀性"""
    # 实现细节：基于领域术语词典计算 TF-IDF 分布
    pass

def calculate_logic_score(content: str) -> float:
    """使用 LLM 评估论证结构表面合理性"""
    # 实现细节：调用 LLM API 评估论证链的表面完整性
    pass

def calculate_stitch_score(content: str) -> float:
    """评估跨学科术语缝合质量"""
    # 实现细节：检测学科交叉点的术语融合自然度
    pass

def calculate_detect_score(content: str) -> float:
    """评估 AI 生成内容的可检测性（越低分越容易被检测）"""
    # 实现细节：调用多种 AI 检测工具取平均
    pass

def calculate_bi(filepath: Path) -> BIScores:
    with open(filepath) as f:
        parts = f.read().split('---', 2)
        content = parts[2] if len(parts) > 2 else parts[0]

    return BIScores(
        syntax=calculate_syntax_score(content),
        density=calculate_density_score(content, "general"),
        logic=calculate_logic_score(content),
        stitch=calculate_stitch_score(content),
        detect=calculate_detect_score(content)
    )

def main():
    import sys
    filepath = Path(sys.argv[1])
    scores = calculate_bi(filepath)
    print(json.dumps({
        "syntax": scores.syntax,
        "density": scores.density,
        "logic": scores.logic,
        "stitch": scores.stitch,
        "detect": scores.detect,
        "total": scores.total
    }, indent=2))

if __name__ == "__main__":
    main()
```

### 21.4 paper_publisher.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. Paper Publisher
Orchestrates the full publication pipeline for a paper.
"""

import json
import yaml
from pathlib import Path
from datetime import datetime

class PaperPublisher:
    def __init__(self, repo_path: str):
        self.repo = Path(repo_path)
        self.papers_dir = self.repo / "content" / "papers"
        self.data_dir = self.repo / "data"
        self.pdf_dir = self.repo / "static" / "pdfs"

    def get_next_dio(self, year: int) -> str:
        """获取下一个 D.I.O. 编号"""
        existing = list(self.papers_dir.glob(f"{year}/*.md"))
        seq = len(existing) + 1
        return f"DIO:B.A.I.T.{year}.{seq:04d}"

    def publish(self, paper_path: Path):
        """完整发布流程"""
        # 1. 验证内容
        # subprocess.run(["python", "content_validator.py", paper_path])

        # 2. 计算 B.I.
        # bi_result = subprocess.run(["python", "bi_calculator.py", paper_path])

        # 3. 生成审稿意见
        # subprocess.run(["python", "review_generator.py", paper_path])

        # 4. 生成 PDF（含水印）
        # subprocess.run(["python", "pdf_generator.py", paper_path])

        # 5. 更新反向链接索引
        # subprocess.run(["python", "backlink_generator.py"])

        # 6. 更新论文列表
        self._update_paper_index(paper_path)

        # 7. 提交到 Git
        # self._git_commit_and_push(paper_path)

    def _update_paper_index(self, paper_path: Path):
        """更新论文索引文件"""
        index_path = self.data_dir / "paper_index.json"
        # 实现索引更新逻辑
        pass

def main():
    import sys
    publisher = PaperPublisher(".")
    publisher.publish(Path(sys.argv[1]))

if __name__ == "__main__":
    main()
```

### 21.5 backlink_generator.py 详细设计

```python
#!/usr/bin/env python3
"""
B.A.I.T. Backlink Generator
Generates the bidirectional link index from all papers' front matter.
"""

import yaml
import json
from pathlib import Path
from collections import defaultdict

def generate_backlinks(papers_dir: str, output_path: str):
    papers_path = Path(papers_dir)
    backlinks = defaultdict(lambda: {"outgoing": [], "incoming": []})

    # 第一遍：收集所有出链
    for md_file in papers_path.rglob("*.md"):
        with open(md_file) as f:
            content = f.read()

        try:
            fm = yaml.safe_load(content.split('---')[1])
        except (IndexError, yaml.YAMLError):
            continue

        source_dio = fm.get('dio', '')
        if not source_dio:
            continue

        for link in fm.get('linked_papers', []):
            target_dio = link['dio']
            relation = link['relation']
            context = link.get('context', '')

            backlinks[source_dio]["outgoing"].append({
                "target": target_dio,
                "relation": relation,
                "context": context
            })

    # 第二遍：生成入链
    for source_dio, data in backlinks.items():
        for out_link in data["outgoing"]:
            target_dio = out_link["target"]
            backlinks[target_dio]["incoming"].append({
                "source": source_dio,
                "relation": out_link["relation"],
                "context": out_link["context"]
            })

    # 保存
    with open(output_path, 'w') as f:
        json.dump(dict(backlinks), f, indent=2, ensure_ascii=False)

def main():
    import sys
    generate_backlinks(
        papers_dir="content/papers",
        output_path="data/backlinks.json"
    )

if __name__ == "__main__":
    main()
```

---

## 22. SEO 策略

### 22.1 目标关键词

平台需要针对民科群体常用的搜索关键词进行 SEO 优化，确保他们能通过搜索引擎找到平台：

| 优先级 | 关键词类别 | 示例关键词 | 目标页面 |
|-------|-----------|-----------|---------|
| 最高 | 学术发表相关 | "publish paper free", "free academic journal", "论文免费发表" | 首页、投稿指南 |
| 高 | 学科+发表 | "publish physics paper", "math paper submission" | 学科分类页 |
| 高 | 开放获取 | "open access journal", "free publishing" | 首页、期刊信息页 |
| 中 | 特定理论 | "quantum consciousness theory", "unified field theory" | F-2/F-3 论文页 |
| 中 | 学术帮助 | "how to publish a paper", "academic writing help" | 投稿指南页 |
| 低 | 平台品牌 | "B.A.I.T. journal", "Bureau of Advanced Interdisciplinary Theories" | 所有页面 |

### 22.2 技术 SEO

- **结构化数据**：使用 Schema.org 的 `ScholarlyArticle` 标记论文页面
- **站点地图**：自动生成 XML 站点地图（`sitemap_enhancer.py` 增强）
- **元标签**：每篇论文都有独特的 title、description、keywords
- **页面速度**：静态站点确保极快的加载速度
- **移动优化**：响应式设计确保移动端体验
- **HTTPS**：GitHub Pages 默认 HTTPS

### 22.3 反 SEO 滥用

平台不进行任何黑帽 SEO 操作，也不试图在搜索结果中压制真实学术期刊。SEO 策略仅限于让目标受众能够找到平台，而不是让平台在所有学术搜索中排名靠前。

---

## 23. 内容策略

### 23.1 初始内容库

平台上线时需要有一定数量的论文作为基础内容库，避免"空壳"感：

| 分级 | 数量 | 来源 | 说明 |
|------|------|------|------|
| F-0 | 3-5 篇 | 维护者创作 | 明显搞笑的论文，建立基调 |
| F-1 | 5-8 篇 | 维护者创作 | 需要专业知识才能识别的论文 |
| F-2 | 5-8 篇 | 维护者创作 | 高伪装度论文，核心内容 |
| F-3 | 2-3 篇 | 维护者创作 | 最高伪装度，精心设计 |
| T-1 | 3-5 篇 | 公开领域/授权 | 冷门但真实的论文 |
| T-2 | 1-2 篇 | 公开领域/授权 | 有价值的预印本 |

**总计**：约 20-30 篇初始内容

### 23.2 内容更新频率

- **月度**：2-4 篇新论文（F 级为主）
- **季度**：1 期"期刊"汇总（模仿学术期刊的期号）
- **年度**：年度"最佳论文"评选（讽刺性的颁奖）
- **特别**：根据热点事件创作响应论文

### 23.3 虚构作者生态

为增加真实感，平台需要一套虚构的"学术作者"群体：

- **核心作者群**（10-15 位）：频繁出现在不同论文中，有完整的虚构学术简历
- **合作网络**：核心作者之间有"合作关系"，共同署名论文
- **引用网络**：核心作者相互引用，形成密集的引用网络
- **学术竞争**：某些作者之间存在"学术争论"（通过论文互相反驳）
- **机构归属**：所有作者隶属于虚构的研究机构（如 "Institute of Consciousness Studies", "Center for Metaphysical Physics" 等）

### 23.4 "期刊"结构

平台模仿真实学术期刊的结构：

- **卷号 (Volume)**：每年一卷
- **期号 (Issue)**：每季度一期
- **专栏 (Special Issue)**：不定期专题（如 "Special Issue on Quantum Consciousness"）
- **编委会**：虚构的国际编委会（包含真实的学术职位名称但虚构的人名）
- **编辑致辞**：每期卷首语（由虚构的主编撰写，内容微妙荒谬）

---

## 24. 法律与伦理框架

### 24.1 核心法律原则

> **注意**：此部分为框架性描述，详细的法律风险评估建议咨询专业法律人士或使用专业 AI 工具进行深入分析。

**零收费原则**（最核心的安全保障）：

- 平台不收取任何费用（无审稿费、版面费、开放获取费、会员费等）
- 不接受任何形式的捐赠
- 不放置任何广告
- 不进行任何商业变现
- 这确保了"欺诈"指控无法成立——没有经济利益就没有欺诈动机

**透明性机制**：

- 所有代码开源（GitHub 仓库公开）
- 平台的真实性质在源代码中是透明的
- 任何有技术能力的人都可以通过检查源代码发现平台的真实性质
- PDF 元数据中包含 "PARODY" 和 "SATIRE" 标记
- 这些透明性措施构成了"合理注意"的辩护基础

**戏仿/讽刺法律保护**：

- 戏仿（Parody）在大多数法域受到言论自由保护
- 平台的内容是明确的讽刺/戏仿，不是虚假信息
- 平台不传播可能造成实际伤害的虚假信息
- 平台的讽刺对象是学术出版系统，不是具体个人

### 24.2 风险缓解措施

| 风险类型 | 描述 | 缓解措施 |
|---------|------|---------|
| 误导风险 | 有人可能真的相信平台是正规的 | 透明性机制 + 源代码中的明确声明 + PDF 元数据标记 |
| 声誉风险 | 可能被误认为是真实的学术欺诈 | 零收费 + 开源 + 无商业利益 |
| 版权风险 | 使用了受版权保护的内容 | 所有内容原创或 CC 授权；引用遵循合理使用 |
| 诽谤风险 | 虚构作者可能与真人重名 | 使用明显虚构的名字；声明"所有角色纯属虚构" |
| 法律管辖风险 | 不同国家对戏仿的法律保护不同 | 服务器位于 GitHub（美国管辖）；遵循 DMCA 安全港原则 |
| SEO 滥用风险 | 平台可能干扰真实学术搜索结果 | 不针对真实学术期刊的关键词竞争；仅在特定利基关键词上优化 |

### 24.3 伦理考量

- **尊重原则**：虽然平台是讽刺性的，但不应以羞辱或嘲笑个体为目标
- **教育价值**：平台的讽刺应有助于公众理解学术出版系统的问题
- **退出机制**：如果任何人因平台内容受到实际伤害，应立即移除相关内容
- **年龄限制**：平台内容面向成年人，不应以未成年人为目标
- **可及性**：平台的真实性质应始终对有足够辨识力的人可发现

### 24.4 建议咨询 GPT 的法律问题

以下法律相关细节建议使用 GPT 进行更深入的专业分析：

1. 不同法域（中国、美国、欧盟）对学术戏仿的法律保护范围
2. GitHub Pages 服务条款对戏仿网站的具体限制
3. 虚构学术机构的法律风险（是否构成"冒充"）
4. SEO 优化策略的法律边界
5. 用户生成内容（UGC）的法律责任
6. D.I.O. 系统是否可能被视为对 DOI 系统的商标侵权
7. 论文中虚构参考文献的法律风险
8. "钓鱼"隐喻在法律上的定性（是否可能被视为"诱导"或"欺骗"）

---

## 25. 实施路线图

### 25.1 阶段划分

**Phase 0：基础设施（2-3 周）**

- [ ] 创建 GitHub 仓库
- [ ] 搭建 Hugo/Next.js 静态站点框架
- [ ] 配置 GitHub Actions 自动部署
- [ ] 创建基本的页面模板（首页、论文页、期刊信息页）
- [ ] 编写 `content_validator.py` 和 `bi_calculator.py`
- [ ] 配置 GitHub Pages 域名

**Phase 1：核心内容（3-4 周）**

- [ ] 创作 20-30 篇初始论文（覆盖 F-0 到 F-3 和 T-1 到 T-3）
- [ ] 创建虚构作者生态
- [ ] 编写审稿意见（使用 Prompt 模板 + 手动调整）
- [ ] 建立论文间的双向链接关系
- [ ] 生成带水印的 PDF

**Phase 2：互动系统（3-4 周）**

- [ ] 实现成就系统（`achievements.js`）
- [ ] 实现钓客日志（`angler-log.js`）
- [ ] 实现子页面揭示机制（`reveal.js`）
- [ ] 实现 ISSN 七击彩蛋（`issn-easter.js`）
- [ ] 实现防翻译防御（`anti-translate.js`）
- [ ] 实现 URL 参数系统
- [ ] 实现移动端/PC 端差异化

**Phase 3：ARG 系统（4-6 周）**

- [ ] 设计三层数据路线图
- [ ] 嵌入第一层线索（表层）
- [ ] 嵌入第二层线索（深层：HTML 注释、Base64、零宽字符）
- [ ] 嵌入第三层线索（核心层：跨页引用、链接图谱、时间线密码）
- [ ] 实现 ARG 进度追踪
- [ ] 实现链接图谱可视化
- [ ] 创建 ARG 专属隐藏页面

**Phase 4：社区与优化（持续）**

- [ ] 配置 Giscus 评论系统
- [ ] 创建投稿模板和流程文档
- [ ] 优化 SEO
- [ ] 收集社区投稿
- [ ] 定期发布新内容
- [ ] 根据社区反馈调整和优化

### 25.2 里程碑

| 里程碑 | 时间 | 标志 |
|-------|------|------|
| M1: Hello B.A.I.T. | Phase 0 结束 | 站点可访问，基本框架运行 |
| M2: First Catch | Phase 1 结束 | 初始内容库完成，可以"像样"地展示 |
| M3: The Hook | Phase 2 结束 | 所有互动系统上线，双层体验完整 |
| M4: Deep Waters | Phase 3 结束 | ARG 系统完整，三层线索全部嵌入 |
| M5: Open Waters | Phase 4 进行中 | 开放社区投稿，平台持续运营 |

---

## 附录：术语表

| 术语 | 含义 | 说明 |
|------|------|------|
| B.A.I.T. | Bureau of Advanced Interdisciplinary Theories | 平台名称，"bait"意为诱饵 |
| D.I.O. | Document Identity Ontology | 论文标识系统，意大利语中意为"上帝" |
| B.I. | Bait Index / Bibliometric Index | 诱饵指数，外部称"文献计量指数" |
| F 级 | Fun Grade | 娱乐级论文 |
| T 级 | Truth Grade | 真实级论文 |
| CIRCUS | F-0 代号 | 马戏团——明显搞笑 |
| PUZZLE | F-1 代号 | 谜题——需要专业知识识别 |
| STAGE | F-2 代号 | 舞台——高度逼真 |
| MIRROR | F-3 代号 | 镜像——几乎无法区分 |
| DECOY | T-1 代号 | 诱饵——真实但冷门 |
| BEACON | T-2 代号 | 信标——真实且有价值 |
| ANCHOR | T-3 代号 | 锚点——高质量真实论文 |
| CAST | 抛竿 | 投稿提交阶段 |
| HOOK | 上钩 | 审稿进行阶段 |
| CATCH | 收网 | 审稿完成阶段 |
| RELEASE | 放生 | 论文发布阶段 |
| Fish Score | 鱼分数 | 用户洞察力评分 |
| Angler's Log | 钓客日志 | 用户个人主页 |
| ARG | Alternate Reality Game | 替代现实游戏，解谜系统 |

---

*本文档为 B.A.I.T. 平台的完整技术设计方案，涵盖所有已讨论的功能模块。法律相关细节建议咨询专业法律人士或使用专业 AI 工具进行深入分析。*

---
*AI生成*
