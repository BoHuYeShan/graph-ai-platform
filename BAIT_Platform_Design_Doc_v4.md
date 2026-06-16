---
AIGC: {"Label":"1","ContentProducer":"001191110108MA01KP2T5U00000","ProduceID":"v4-2025-bait-platform-design","ReservedCode1":"","ContentPropagator":"001191110108MA01KP2T5U00000","PropagateID":"v4-2025-bait-platform-design","ReservedCode2":""}
---

# B.A.I.T. 平台完整设计文档 v4

> **Bureau of Advanced Interdisciplinary Theories**
> "bait" = 诱饵 / 钓鱼 — 跨维度学术戏仿平台的完整技术设计方案
>
> **v4 变更说明**（相对 v3）：
> - 架构升级：单源维护（bait-core）+ 三展示仓库自动拉取
> - 内容模型统一为「论文解读」格式，砍掉 T 级完整转载
> - 钓鱼模型从被动投稿升级为 SEO 钓鱼（主动生成内容，等鱼自寻）
> - 手机端 L0–L3 能力分层，天然过滤
> - 分级标签双套：民科看假分区（CAS 一区等），解谜者看 Backrooms 风格
> - ARG 验证码系统：存在但揭示真相
> - 伦理框架大幅扩充（对事不对人、减少对当事人损害）
> - 新增社区公约、删库跑路预案、SSR 订阅预留
> - 法律章节保留 v3 的第 38–39 节（已足够完整），不再重复

---

## 目录

### 第一部分：世界观与定位

1. [项目概述](#1-项目概述)
2. [命名体系](#2-命名体系)
3. [伦理框架与社区公约](#3-伦理框架与社区公约)
4. [内容边界与安全策略](#4-内容边界与安全策略)

### 第二部分：架构与系统

5. [多仓库架构](#5-多仓库架构)
6. [多宇宙架构](#6-多宇宙架构)
7. [分级系统与跨站点映射](#7-分级系统与跨站点映射)
8. [内容模型：论文解读](#8-内容模型论文解读)
9. [钓鱼审稿系统](#9-钓鱼审稿系统)
10. [B.I. 诱饵指数评估体系](#10-bi-诱饵指数评估体系)
11. [多入口系统](#11-多入口系统)
12. [手机端能力分层](#12-手机端能力分层)

### 第三部分：内容与创作

13. [投稿与审稿工作流](#13-投稿与审稿工作流)
14. [真实论文引用与解读策略](#14-真实论文引用与解读策略)
15. [AI 补稿与宇宙内容填充](#15-ai-补稿与宇宙内容填充)
16. [内容展示格式](#16-内容展示格式)
17. [终端模拟系统](#17-终端模拟系统)
18. [虚构学术身份体系](#18-虚构学术身份体系)
19. [游戏编码映射系统](#19-游戏编码映射系统)

### 第四部分：交互与解谜

20. [双向页面链接系统](#20-双向页面链接系统)
21. [线索与 ARG 解谜系统](#21-线索与-arg-解谜系统)
22. [子页面揭示机制](#22-子页面揭示机制)
23. [ARG 验证码与证书系统](#23-arg-验证码与证书系统)
24. [防翻译与多语言策略](#24-防翻译与多语言策略)
25. [URL 参数系统](#25-url-参数系统)
26. [成就系统](#26-成就系统)
27. [钓客日志与 Fish Score](#27-钓客日志与-fish-score)
28. [ISSN 七击彩蛋](#28-issn-七击彩蛋)
29. [PDF 水印系统](#29-pdf-水印系统)

### 第五部分：社区与运营

30. [内部 Prompt 模板系统](#30-内部-prompt-模板系统)
31. [社区治理模型](#31-社区治理模型)
32. [社区公约与免责声明](#32-社区公约与免责声明)
33. [配套脚本与工具链](#33-配套脚本与工具链)
34. [SEO 与反 SEO 策略](#34-seo-与反-seo-策略)
35. [域名策略](#35-域名策略)
36. [SSR 订阅预留](#36-ssr-订阅预留)
37. [后端预留与扩展](#37-后端预留与扩展)
38. [删库跑路预案](#38-删库跑路预案)

### 第六部分：法律与路线图

39. [法律与伦理框架](#39-法律与伦理框架)
40. [实施路线图](#40-实施路线图)
41. [附录：术语表](#附录术语表)

---

# 第一部分：世界观与定位

## 1. 项目概述

### 1.1 核心理念

B.A.I.T.（Bureau of Advanced Interdisciplinary Theories）是一个模仿正规学术出版机构的戏仿平台。平台名称本身即为核心隐喻："bait" 意为诱饵/钓鱼。

平台同时承载两条内容线：
- **钓鱼线（楚门的世界）**：面向「民科」群体，呈现为一个权威的国际学术出版机构。民科以为自己被正经期刊收录，但任何有辨识力的用户都能通过嵌入的线索发现真相。
- **社区小说线（我们的世界）**：面向解谜者和创作者，类似 SCP 基金会和 Backrooms 的虚构世界共创空间。R.E.E.F. 主站宇宙将所有独立宇宙统一容纳。

在 v4 架构中，平台从「被动等鱼投稿」升级为 **SEO 钓鱼模型**：维护者主动将民科在视频平台发布的研究内容整理为「论文解读」，署其名发表。民科定期搜索自己的网名时，会发现「有一篇署名自己的论文被 B.A.I.T. 收录了」——这个过程无需平台主动联系任何人。

### 1.2 设计哲学

- **沉浸优先**：对目标受众，平台必须与真实学术出版网站无异
- **线索渐进**：从微妙的违和感，到明确的文化暗示，再到直接的揭示
- **零收费原则**：平台绝不向任何用户收取任何费用
- **对事不对人**：讽刺目标是「学术出版系统」和「民科现象」，不是具体的个人
- **减少伤害**：民科群体晚年不易，他们在平台上的「发表」可以让他们心情舒畅，而非遭受围攻
- **社区共创**：像 SCP 和 Backrooms 那样，收集社区创意投稿
- **多宇宙容纳**：每个民科/作者可拥有独立宇宙，社区助力完善，宇宙之间可合并
- **删库友好**：所有内容 Markdown 源文件化，站点删仓库即消失

### 1.3 目标受众画像

**主要目标（鱼）**：
- 缺乏正规学术训练但热衷「发表」理论的民科群体
- 大量依赖 AI 生成论文内容的人群
- 活跃于中文视频平台（抖音、快手、B站等），习惯用手机上网
- 部分是老年人，晚年精神状态不佳，生活不易
- 常使用浏览器翻译功能阅读英文内容

**次要受众（钓客）**：
- 对 ARG/解谜感兴趣的互联网用户
- 学术圈内的讽刺文化爱好者
- 编程/设计社区用户
- 虚构世界观共创爱好者（SCP/Backrooms 社区成员）

---

## 2. 命名体系

### 2.1 核心命名

| 层面 | 名称 | 学术门户展开 | 隐藏含义 |
|------|------|-------------|---------|
| 平台/期刊 | B.A.I.T. | Bureau of Advanced Interdisciplinary Theories | 诱饵/钓鱼 |
| 主站宇宙 | R.E.E.F. | Research Encyclopedia of Emerging Frontiers | 礁石——鱼群聚集地 |
| 文档标识 | D.I.O. | Document Identity Ontology | 意大利语「上帝」 |
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
| Wiki 系统 | K.E.L.P. | Knowledge Exchange & Lexicon Platform | 海带 |
| 审稿记录 | P.E.A.R.L. | Peer Evaluation & Assessment Record Ledger | 珍珠 |
| 宇宙索引 | C.O.R.A.L. | Catalog of Observed Research & Academic Lore | 珊瑚 |

### 2.4 编号格式

| 对象 | 编号格式 | 示例 |
|------|---------|------|
| 论文 | `DIO:B.A.I.T.<YYYY>.<SEQ>` | `DIO:B.A.I.T.2025.0001` |
| 宇宙 | `COSMOS-<类别>-<序号>` | `COSMOS-CNS-001` |
| 异常报告 | `AR-<YYYY>-<SEQ>` | `AR-2025-0042` |
| 终端会话 | `TS-<宇宙代码>-<SEQ>` | `TS-YQC-007` |
| 虚构人物 | `DIO:B.A.I.T.AUTH.<YYYY>.<SEQ>` | `DIO:B.A.I.T.AUTH.2025.0042` |

宇宙类别代码：PHY（物理）、BIO（生物）、MAT（数学）、PHI（哲学）、CNS（意识）、INF（信息/计算）、COS（宇宙学）、MIX（跨学科混合）、CHE（化学）、UNI（统一宇宙·合并后）

---

## 3. 伦理框架与社区公约

> **本节是 v4 最核心的新增内容。** 它定义了平台「能做什么、不能做什么」的伦理底线，以及对维护者和社区参与者的行为约束。技术架构和法律框架服务于这些伦理原则。

### 3.1 对待目标受众（民科）的基本原则

1. **不主动联系原则**：平台绝不主动以「编辑部」名义联系任何人。所有「发现」通过 SEO 自然发生——民科自己搜索自己的网名时发现论文。这避免了「主动冒充机构联系他人」的法律和伦理风险。

2. **对事不对人原则**：讽刺的对象是「学术出版系统的荒诞」和「民科现象」这一社会现象，不是具体的个人。禁止在任何公开页面中对具体民科进行人身攻击、嘲笑其智力、或暴露其真实身份信息。

3. **减少伤害原则**：很多民科是老年人，生活不易，晚年精神状态不佳。他们在平台上「被发表」可以带来心情的舒畅——这在伦理上是正向的。禁止社区成员去民科的视频/社交平台下留言嘲讽、揭穿或围攻。

4. **不制造现实后果原则**：
   - 绝不提供可用于外部验证的「会员编号」「认证编号」「收录证书编号」
   - 所有「证书」上的验证码输入后揭示的是「这是假的」
   - 杜绝民科拿着平台内容去求职、申请经费、或对外声称「我是 B.A.I.T. 认证学者」的可能

5. **可退出原则**：若任何人因平台内容受到实际伤害并提出，立即移除相关内容。

### 3.2 对待解谜者/社区成员的基本原则

1. **透明性**：平台真实性质在源码、README、HTML 注释中始终可发现
2. **禁止越界**：社区成员不得代表 B.A.I.T. 去联系民科，不得「替平台钓鱼」
3. **玩梗不玩人**：创作内容可以荒诞，但不得针对真实个人进行攻击
4. **共创尊重**：宇宙合并、Wiki 修改需尊重原作者意愿

### 3.3 虚构内容伦理

- 所有「作者」「审稿人」「编委」均为虚构
- 虚构的「撤稿声明」「讣告」等文档需在页面注明「虚构创作」
- 不虚构涉及真实机构（如 MIT、清华）的负面事件
- 「真实校名 + 虚构部门」的组合（如 MIT Department of Consciousness Physics）需确保不会对真实机构声誉造成实质损害

---

## 4. 内容边界与安全策略

### 4.1 绝对禁区

1. 政治敏感内容
2. 邪教/极端主义内容
3. 医疗/健康建议（包括替代疗法、能量治疗）
4. 种族/性别歧视内容
5. 金融/投资建议
6. 针对真实学术人物的诽谤或人身攻击
7. 儿童不当内容

### 4.2 安全主题领域

- 数学/几何：哥德巴赫猜想、新几何、推翻微积分
- 理论物理/宇宙学：大统一理论、多维空间、暗物质替代解释
- AI/计算理论：超越图灵机的计算模型、意识上传
- 哲学/认识论：万物理论、重新定义时间/空间/因果关系
- 信息论/密码学：破解现有加密体系
- 进化论/古生物（不涉及人类起源）：恐龙文明假说
- 生物/化学：虚构的生化机制、分子结构

### 4.3 安全审查原则

- **无害性测试**：如果被完全不懂学术的人当真，是否会造成实际伤害？
- **可辨识性测试**：受过大学教育的正常人能否识别出戏仿？
- **法律风险评估**：是否可能引发任何法律纠纷？
- **去人格化原则**：所有作者均为虚构身份
- **反伤害扩散原则**：即使内容本身无害，传播方式是否可能导致误导？

### 4.4 安全分级与处置

| 嫌疑等级 | 判定标准 | 处置 |
|---------|---------|------|
| 绿（通过） | 不触碰禁区，无害可辨识 | 正常发布 |
| 黄（警告） | 边缘地带，需维护者二次会商 | 2 人以上同意方可发布 |
| 红（拒绝） | 触碰禁区或高风险 | 直接拒稿，记录理由 |

---

# 第二部分：架构与系统

## 5. 多仓库架构

### 5.1 核心设计

v4 采用「单源维护 + 多展示仓库自动拉取」架构：

- **bait-core**：唯一需要人工维护的源仓库。包含所有 Markdown 内容、脚本、数据。
- **bait-academic / bait-archive / bait-deep**：三个纯展示仓库，由 GitHub Actions 自动从 bait-core 拉取内容并构建，各自部署到独立的 GitHub Pages URL。

```
bait-core/                        ← 🔧 唯一维护的仓库
  ├── content/
  │   ├── papers/                 ← 所有论文源文件 (Markdown + Front Matter)
  │   ├── cosmos/                 ← 宇宙设定 + Wiki
  │   ├── characters/             ← 虚构人物档案
  │   ├── records/                ← 异常报告
  │   ├── terminal/               ← 终端会话 JSON 配置
  │   └── assets/                 ← 图片/音频等
  ├── scripts/                    ← 构建/生成脚本
  ├── data/                       ← 自动生成的索引
  │   ├── backlinks.json
  │   ├── grade_map.json
  │   ├── cosmos_index.json
  │   ├── achievements.json
  │   └── prompt_templates.json
  ├── .github/
  │   └── workflows/
  │       └── dispatch-sync.yml   ← 推送时触发下游仓库同步
  ├── CONTRIBUTING.md
  ├── CODE_OF_CONDUCT.md
  ├── DISCLAIMER.md
  └── README.md

bait-academic/                    ← 🤖 自动拉取，展示学术门户
bait-archive/                     ← 🤖 自动拉取，展示档案库
bait-deep/                        ← 🤖 自动拉取，展示深渊
```

### 5.2 自动同步机制

每个展示仓库包含 `.github/workflows/sync.yml`：

```yaml
name: Sync from bait-core
on:
  repository_dispatch:
    types: [content-updated]
  schedule:
    - cron: '0 6 * * *'          # 每天兜底同步一次

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          repository: <org>/bait-core
          path: core

      - name: Build academic portal
        run: |
          pip install -r core/scripts/requirements.txt
          python core/scripts/build.py --target academic --dist ./dist

      - uses: peaceiris/actions-gh-pages@v3
        with:
          publish_dir: ./dist
```

bait-core 的 `dispatch-sync.yml` 在每次 push 到 main 时，向三个展示仓库发送 `repository_dispatch` 事件触发同步。

### 5.3 仓库隔离的收益

| 维度 | 效果 |
|------|------|
| URL 隔离 | 三入口在不同 GitHub Pages URL 下，民科无法通过改路径闯入 |
| SEO 隔离 | 学术门户做 SEO，档案库/深渊 robots.txt 全禁 |
| 删库隔离 | 可单独删除展示仓库而不丢失源内容 |
| 维护隔离 | 维护者只碰 bait-core |

### 5.4 构建过滤规则

`scripts/build.py` 按目标入口过滤内容：

| 构建目标 | 包含内容 | 排除内容 |
|---------|---------|---------|
| academic | FG/TG 论文 | RG 档案、LG 日志、终端、损坏格式 |
| archive | 全部 FG/TG/RG/LG/终端/Wiki | 损坏格式（除非 DDI < 4） |
| deep | RG-3、LG-3、DDI ≥ 4、损坏格式 | 普通论文 |

构建后自动运行 `content_validator.py` 检查是否有不该出现在某入口的内容泄露。

---

## 6. 多宇宙架构

### 6.1 核心概念

每个民科（或虚构作者）可拥有独立宇宙。宇宙有自己的基础公理、推导理论、内部逻辑自洽性和专属术语。

R.E.E.F. 是所有独立宇宙的「交汇点」——主站宇宙，设定为：这些独立宇宙都是 R.E.E.F. 在不同参数条件下的投影/分支。

### 6.2 独立宇宙结构

```yaml
# content/cosmos/yang-quantum-consciousness/_index.md
---
cosmos_id: "COSMOS-CNS-001"
cosmos_name: "杨氏量子意识宇宙"
cosmos_short: "YQC"
founder: "Dr. Yang Wei"
status: "active"            # active / merged / archived
merged_into: null
era_origin: "expansion"
ddi_range: [1, 3]
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
paper_count: 12
wiki_pages: 34
canon_level: "Canon"        # Canon / Semi-Canon / Apocrypha / Joke
---
```

### 6.3 宇宙合并

两个公理兼容的独立宇宙可通过社区投票合并：
1. GitHub Discussions 发起合并提议
2. 讨论期 7 天
3. 投票 3 天，至少 5 票有效，简单多数通过
4. 维护者执行：更新 Front Matter、重定向引用，原宇宙保留为归档

合并时脚本自动检测术语/公理冲突，生成冲突报告供社区讨论解决。

### 6.4 正典层级管理

| 层级 | 判定标准 | 升降机制 |
|------|---------|---------|
| Canon | 维护者审核的核心世界观，不与既有公理矛盾 | 维护者提案 + 2 人审核 |
| Semi-Canon | 社区投稿被接受但非核心 | 被核心世界观引用可升 Canon |
| Apocrypha | 社区创作，不保证与正典一致 | 与正典冲突自动降级 |
| Joke | 纯搞笑，明确不纳入世界观 | 作者主动标记或维护者标记 |

---

## 7. 分级系统与跨站点映射

### 7.1 统一内部分级

| 板块 | 分级 | 含义 |
|------|------|------|
| 论文 | FG-0 | Fun-0 纯搞笑 |
| 论文 | FG-1 | Fun-1 有一定伪装度 |
| 论文 | FG-2 | Fun-2 高度伪装 |
| 论文 | FG-3 | Fun-3 极致伪装 |
| 论文 | TG-1~3 | Truth 真实论文解读 |
| 档案 | RG-0~3 | Record 异常档案 |
| 日志 | LG-0~3 | Log 基础设施日志 |

### 7.2 学术门户分级映射（民科看到）

这是给民科看的「假分区」，让他觉得自己的论文被高级别期刊收录：

| 内部ID | 学术门户显示 | 颜色 | 对应「假分区」 |
|--------|-------------|------|--------------|
| FG-0 | Category A — Original Contribution | 绿色 | JCR Q3 |
| FG-1 | Category A+ — Significant Contribution | 蓝色 | JCR Q2 |
| FG-2 | Category A++ — Major Contribution | 金色 | JCR Q1 / 中科院二区 |
| FG-3 | Category S — Landmark Contribution | 红色 | JCR Q1 / 中科院一区 Top |
| TG-1~3 | Category B — Standard Publication | 灰色 | — |

RG/LG 内容在学术门户完全不出现。

### 7.3 档案库分级映射（解谜者/社区用户看到）

SCP/Backrooms 风格，如同 Backrooms 的「生存等级」「实体情况」标签——页面顶部有醒目的大标签：

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

### 7.4 档案库分级标签的视觉设计（Backrooms 风格）

档案库中每篇内容顶部有一个醒目的分级标签，模仿 Backrooms 层级页面的风格：

```
┌─────────────────────────────────────────────┐
│ ⚠️ ANOMALY CLASSIFICATION                   │
│                                             │
│ ██ Δ-3 CRITICAL DEVIATION                  │
│                                             │
│ DIMENSIONAL DEVIATION INDEX: 4 (RED)        │
│ CONTAINMENT STATUS: UNCONTAINED             │
│ THREAT LEVEL: ●●●●○ (HIGH)                  │
│                                             │
│ ████████████████████████████████████████████ │
└─────────────────────────────────────────────┘
```

学术门户中同一篇论文的标签则是：

```
┌─────────────────────────────────────────────┐
│ ✅ PEER REVIEW COMPLETED                    │
│                                             │
│ Category S — Landmark Contribution          │
│ JCR Q1 / CAS 一区 Top                        │
│                                             │
│ Review Code: B.A.I.T.-REV-2025-0042         │
│ Bibliometric Index: 73.2/100                │
└─────────────────────────────────────────────┘
```

### 7.5 维度偏移指数 (D.D.I.)

三个板块共享的顶层指标：

| DDI | 颜色 | 含义 |
|-----|------|------|
| 0 | 白色 | 与现实一致 |
| 1 | 蓝色 | 微偏，可解释为学术差异 |
| 2 | 黄色 | 中偏，无法用已知框架解释 |
| 3 | 橙色 | 重偏，暗示维度差异 |
| 4 | 红色 | 极偏，维度特有 |
| 5 | 黑色 | 未知，无法评估 |

### 7.6 分级映射的 ARG 功能

同一篇论文在学术门户显示「Category S — Landmark Contribution」，在档案库显示「Δ-3 CRITICAL DEVIATION」，在终端显示 `DOC::TYPE-S`——三种完全不同的名字指向同一篇论文。这种换算关系本身是 ARG 线索。

---

## 8. 内容模型：论文解读

### 8.1 统一格式

v4 将平台所有内容统一为「论文解读」格式：

> B.A.I.T. 对外声称自己是「学术论文解读与评论平台」，不声称是「出版机构」。我们解读各类前沿研究——有些解读的是真实论文，有些解读的是来自 Dimension-7 的异常数据。

一篇标准的论文解读包含：

```markdown
---
title: "意识作为基本物理量：一项维度偏移数据分析"
format: interpretation
grade: FG-2
ddi: 3
dio: "DIO:B.A.I.T.2025.0042"
cosmos: "COSMOS-CNS-001"
authors:
  - name: "Dr. Zhang Wei"
    affiliation: "Institute of Consciousness Studies, B.A.I.T."
    dio: "DIO:B.A.I.T.AUTH.2025.0042"
source_author: "杨伟（视频平台用户「量子哥」）"  # ← 民科的网名
source_type: "video_transcription"               # video_transcription / real_paper / community_fiction
source_url: null                                 # 不链回原视频
real_references_count: 8
review_status: CATCH
bi_score: 68.5
canon_level: Canon
linked_papers: [...]
arg_clues: [...]
---

# 意识作为基本物理量：一项维度偏移数据分析

> **原文来源**：基于视频平台用户「量子哥」的研究内容整理。
> **解读人**：Dr. Zhang Wei（意识学研究所，B.A.I.T.）
> **DIO**: DIO:B.A.I.T.2025.0042
> **发表日期**：2025-03-15

## 编者按

本解读基于视频平台用户「量子哥」在 2024 年发布的一系列关于
「意识是基本物理量」的视频内容。我们的研究团队对其核心论点
进行了系统性的学术化整理，并将其置于当今意识研究的理论框架
中进行考察……

## 1. 引言

（AI 生成的学术化论文正文，基于民科视频内容转写）

## 2. 核心论点重构

（将民科的口语化表述转写为学术语言）

## 参考文献

[1] Penrose, R. (1994). *Shadows of the Mind*. Oxford University Press.
    → https://doi.org/10.1093/oso/9780198539780.001.0001
[2] （虚构引用）
[3] Tegmark, M. (2000). "Importance of Quantum Decoherence in Brain Processes."
    *Physical Review E*, 61(4), 4194.
    → https://doi.org/10.1103/PhysRevE.61.4194
...
```

### 8.2 三种来源类型

| source_type | 含义 | 内容来源 | 署名 |
|------------|------|---------|------|
| `video_transcription` | 民科视频转写 | AI 将视频内容转写为论文 | 民科网名为 `source_author`，解读人为虚构教授 |
| `real_paper` | 真实论文解读 | 真实存在的学术论文（arXiv/OA） | 真实作者保留，解读人另署 |
| `community_fiction` | 社区原创虚构 | 社区成员直接创作 | 创作者笔名 |

### 8.3 真实论文解读的格式

真实论文不做全文转载。格式为：

```markdown
---
title: "[解读] Penrose (1994): 意识与量子力学的一次失败相遇"
format: interpretation
source_type: real_paper
grade: TG-1
ddi: 0
dio: "DIO:B.A.I.T.2025.0100"
real_paper_doi: "10.1093/oso/9780198539780.001.0001"
real_paper_authors: "Roger Penrose"
real_paper_title: "Shadows of the Mind"
real_paper_journal: "Oxford University Press, 1994"
real_paper_license: "Publisher"   # 只做引用+评论，不转载全文
authors:
  - name: "Prof. Li Ming"
    affiliation: "Department of Metaphysical Physics, B.A.I.T."
---

# [解读] Penrose (1994): 意识与量子力学的一次失败相遇

> **原文信息**：
> Penrose, R. (1994). *Shadows of the Mind*.
> Oxford University Press.
> → https://doi.org/10.1093/oso/9780198539780.001.0001
>
> **解读人**：Prof. Li Ming（B.A.I.T.）

## 编者按

Penrose 在这本书中提出了一个在当时看来激进而现在看来……
（合法的评论和解读，不转载原文）
```

### 8.4 法律基理

- 真实论文解读 = 评论/引用，属于合理使用，无需许可
- 不全文转载真实论文 → 无版权风险
- 民科视频转写 = 原创性转写 + 评论，署名使用其网名但不链回原视频
- 不主动联系作者 → 避免「冒充机构」指控
- 民科自己搜到 = SEO 自然发现 → 平台从未「联系」过他

---

## 9. 钓鱼审稿系统

### 9.1 SEO 钓鱼模型（v4 核心变更）

V3 的「被动等待投稿」升级为 v4 的「SEO 钓鱼」：

```
维护者发现民科视频
  → AI 将视频内容转写为学术论文
  → 署该民科的网名为 source_author
  → 发表到 bait-academic
  → 做 SEO 优化（该民科的网名 + 论文标题）
  → 民科定期搜索自己网名
  → 发现 B.A.I.T. 上有一篇署名自己的论文
  → 震惊：「有国际期刊注意到了我的研究！」
  → 点击阅读 → 看到正式的学术排版 → 极度信任
  → 他自然会在视频里宣传「我被国际期刊收录了」
  → 更多民科闻讯而来，开始投稿
```

关键点：**平台从未主动联系任何人**。民科是自己搜到的。这绕过了「主动冒充机构联系他人」的法律风险。

### 9.2 四阶段流程（对民科可见）

| 阶段 | 外部显示 | 用户可见状态 |
|------|---------|-------------|
| 抛竿 (Cast) | Submitted | "Your manuscript has been received and is under initial screening" |
| 上钩 (Hook) | Under Review | "Your manuscript is currently under peer review by our expert panel" |
| 收网 (Catch) | Accepted | "Congratulations! Your manuscript has been accepted for publication" |
| 放生 (Release) | Published | "Your paper is now publicly available in our repository" |

### 9.3 审稿意见生成

由内部 Prompt 系统生成（详见第 30 节）：
- 正式学术英语，以正面评价为主
- 修改建议仅涉及表面格式
- 在正面评价中嵌入微妙暗示（辨识者可察觉）

### 9.4 审稿的双重逻辑

- **外部（民科看到）**：标准的学术同行评审流程，有进度条、审稿人编号、预计完成日期
- **内部（实际）**：所有论文最终都会被接受。维护者审查的是内容趣味性、安全性和 ARG 嵌入质量，而非学术正确性。无聊或违规的内容会被移除，但不在审稿流程中体现。

---

## 10. B.I. 诱饵指数评估体系

### 10.1 五维评估模型

| 维度 | 英文名 | 评估内容 | 满分 |
|------|--------|---------|------|
| 语法 (Syntax) | Syntactic Coherence | 语法正确性和学术规范性 | 20 |
| 密度 (Density) | Terminological Density | 专业术语的密度和分布 | 20 |
| 逻辑 (Logic) | Logical Plausibility | 论证逻辑的表面合理性 | 20 |
| 缝合 (Stitch) | Interdisciplinary Stitching | 跨学科内容的缝合质量 | 20 |
| 可检测 (Detect) | AI Detectability | AI 生成内容的可检测性 | 20 |

总分 0–100。外部以 "Bibliometric Index" 名义展示。

### 10.2 B.I. 与分级的关系

| B.I. 范围 | 对应分级 |
|-----------|---------|
| 0–20 | FG-0 |
| 21–40 | FG-1 |
| 41–70 | FG-2 |
| 71–100 | FG-3 |

### 10.3 B.I. 的外部/内部呈现

**外部视图（学术门户）**：
```
Bibliometric Index: 73.2/100
  Syntactic Coherence: ████████░░ 16/20
  Terminological Density: █████████░ 18/20
  Logical Plausibility: ████████░░ 15/20
  Interdisciplinary Stitching: ████████░░ 14/20
  AI Detection Resistance: █████████░ 18/20
```

**内部视图（档案库，解锁后）**：
```
🎣 Bait Index: 73.2 — "This paper is an excellent lure."
   Can you spot the fundamental flaw in Section 3.2?
```

---

## 11. 多入口系统

### 11.1 三个入口

**入口一：学术门户 (Academic Portal)** — bait-academic
- 面向民科的「楚门世界」
- 干净的学术期刊界面
- 只展示论文解读（FG/TG 级别）
- 分级显示为 Category A/B/S + 假分区（JCR Q1 等）
- 带有隐藏的解谜元素（HTML 注释、隐写图等）
- SEO 主入口，robots.txt 允许
- URL: `https://<org>.github.io/bait-academic/`

**入口二：档案库 (Archive)** — bait-archive
- 面向知道真相的用户
- SCP/Backrooms 风格的文档库
- 展示所有类型内容
- Backrooms 风格大标签（Δ/Σ/R/L + DDI 等级）
- 终端会话嵌入
- 社区共创主界面
- robots.txt 全禁
- URL: `https://<org>.github.io/bait-archive/`

**入口三：H.A.D.A.L. 深渊 (The Deep)** — bait-deep
- 通过 ARG 发现的隐藏入口
- 只展示最深/最暗层内容（DDI ≥ 4）
- 故障美学/信号退化风格
- 纯探索导向
- URL 不公开，无入链

### 11.2 入口隔离

三个入口部署在不同的 GitHub Pages URL 下，天然隔离：
- 民科在学术门户地址栏改路径无法抵达档案库或深渊
- 学术门户页面中不包含指向档案库的直接链接
- 过渡页 `/d7-access/` 是唯一桥梁——其 URL 藏在 HTML 注释或隐写图中，不会被搜索引擎索引

### 11.3 ARG 过渡链路

**学术门户 → 档案库**：
1. 论文参考文献 [7] 不存在，PC 端查看源码发现 `<!-- ref_7 is a ghost. follow to /d7-access/ -->`
2. 访问过渡页，看到「系统维护」风格页面
3. 页脚被 CSS 淡化的文字提示档案库路径
4. 进入档案库，世界观切换

**档案库 → 深渊**：
1. 终端会话中 `decrypt` 命令返回 Base64 套娃密文
2. 解码得到哈希路径
3. 访问进入深渊

---

## 12. 手机端能力分层

### 12.1 L0–L3 分层模型

手机端是民科的主战场。v4 利用「能力差异」天然过滤受众：

| 层级 | 设备 | 用户画像 | 可见内容 | ARG 入口 |
|------|------|---------|---------|---------|
| L0 纯手机 | 手机浏览器 | 典型民科（视频平台引流） | 学术门户（论文列表 + 正文）。无「查看源代码」入口。无终端。无档案库链接。 | 无 |
| L1 手机 + 好奇心 | 手机 + 尝试桌面版视图 / 改地址栏 | 稍有动手能力 | L0 + 可能撞到过渡页 | 极有限 |
| L2 电脑 | 桌面浏览器 | B站等平台用户，有基础电脑操作 | 完整学术门户 + 可查看源码 + 过渡页可访问 | 标准 ARG 路径 |
| L3 电脑 + 技术 | 桌面 + DevTools / GitHub | 钓客/解谜者 | 全部三入口 + 源码透明 | 完整 ARG |

### 12.2 手机端限制机制

- **纯 CSS/JS 前端检测**：手机端模板不渲染「查看源代码」按钮、不显示 HTML 注释提示、不加载终端组件
- **概率触发 fake 弹窗**：手机端在页面停留过久时，低概率弹出一个看起来像浏览器安全警告的弹窗，内容荒诞（如「此页面已被 Dimension-7 污染」）。L0 用户被吓退，L1 用户反而被激起好奇心——这是第一个 ARG 钩子。
- **天然可绕过**：手机用户切换到「桌面版网站」即可突破——但这个行为恰好证明他不是 L0

### 12.3 设计哲学

手机端限制不是安全机制（它可被绕过），而是**叙事过滤器**。它让「发现真相」需要一定的技术好奇心，而这个好奇心恰好是区分「鱼」和「钓客」的关键。

---

# 第三部分：内容与创作

## 13. 投稿与审稿工作流

### 13.1 投稿渠道

| 方式 | 适用人群 | 机制 |
|------|---------|------|
| GitHub Issue | 有 GitHub 账号的用户 | 提交 Issue → 维护者整理为 PR → 审查 |
| GitHub PR | 核心社区成员 | Fork → 创建 Markdown → 提交 PR → 审查 |
| 外部投稿表单 | 不会 GitHub 的民科（将来） | 表单 → Supabase → 维护者整理为 PR |

Phase 0–2 期间：仅 GitHub Issue + PR。GitHub 账号本身就是能力过滤器——能注册 GitHub 的人，基本上不会被误伤。

### 13.2 投稿表单法律措辞（将来实现时）

外部投稿表单需用户勾选确认（中英双语）：

> ☐ 我理解本平台（B.A.I.T.）是一个**虚构创意戏仿项目**，不是真实的学术出版机构。
>
> ☐ 我提交的内容是我原创的或我有权提交的。
>
> ☐ 内容不涉及政治、医疗、金融、歧视、人身攻击。
>
> ☐ 内容按 CC-BY-SA 4.0 许可发布。
>
> ☐ 我已满 18 岁。

### 13.3 维护者审查标准

- **外部质量**：格式规范、语言质量、引用格式
- **内部质量**：安全边界、娱乐价值、ARG 线索嵌入、B.I. 评分匹配
- **严格度**：拒绝无聊的、低质量的、存在安全风险的投稿

---

## 14. 真实论文引用与解读策略

### 14.1 核心原则

v4 砍掉 T 级全文转载。真实论文仅以以下两种形式出现：

1. **参考文献列表中的真实引用**：假论文的参考文献混入真实论文引用 + doi.org 超链接
2. **真实论文解读**：以评论/解读格式出现，不转载原文，属于合理使用

### 14.2 参考文献混编比例

| 论文类型 | 真实引用占比 |
|---------|------------|
| FG-0 | 0–20% |
| FG-1 | 30–50% |
| FG-2 | 50–70% |
| FG-3 | 60–80% |

民科点击参考文献 → 浏览器跳到 `doi.org` 的英文论文页面 → 「这期刊连参考文献都是真的」→ 信任感建立。

### 14.3 版权合规

| 行为 | 合规性 |
|------|-------|
| 引用真实论文（参考文献列表 + 超链接） | ✅ 无需许可 |
| 对真实论文做评论/解读 | ✅ 合理使用 |
| 链接到真实 DOI 页面 | ✅ 无需许可 |
| 全文转载付费论文 | ❌ 不可 |
| 全文转载 arXiv 预印本 | ❌ v4 不再做 |
| 将真实作者虚构为 B.A.I.T. 研究员 | ❌ 不可 |
| 「真实校名 + 虚构部门」组合 | ⚠️ 需 GPT 确认边界（见第 39 节） |

---

## 15. AI 补稿与宇宙内容填充

### 15.1 内容填充层次

以「杨氏量子意识宇宙」为例：

**第一层：核心论文（人工创作）** — 宇宙的骨架

**第二层：衍生论文（AI 辅助生成 + 人工审核）** — 3–5 篇，互相引用形成网络

**第三层：周边材料（AI 生成 + 人工润色）**：
- 采访记录、实验日志、新闻报道、会议记录、教学大纲、专利文件
- 撤稿声明（针对虚构论文，页面注明「虚构创作」）
- 讣告（针对虚构人物，页面注明「虚构创作」）

**第四层：Wiki 百科（AI 生成 + 精心设计）** — 术语词典、时间线、人物关系图

### 15.2 AI 补稿工作流

```
核心论文 + 公理输入
  → AI 生成衍生论文草稿（10–20 篇）
  → 维护者筛选修改（保留 3–5 篇）
  → AI 生成周边材料
  → 维护者审核 + 嵌入 ARG 线索
  → AI 生成 Wiki 条目
  → 维护者审核 + 交叉引用检查
  → 发布
```

### 15.3 民科视频转写流程（v4 新增）

```
维护者发现民科视频
  → AI 提取视频内容摘要
  → AI 将内容转写为学术论文格式
  → AI 生成参考文献列表（混编真实引用）
  → 维护者审核 + 嵌入 ARG 线索
  → 发布到 bait-academic
  → SEO 优化（target: 该民科的网名 + 关键词）
```

---

## 16. 内容展示格式

| 格式标识 | 名称 | 渲染方式 | 可见入口 |
|---------|------|---------|---------|
| `interpretation` | 论文解读 | 标准学术论文排版 | 学术门户 + 档案库 |
| `document` | 文档格式 | SCP 风格文档页 | 仅档案库 |
| `terminal` | 终端格式 | 全屏终端模拟 | 仅档案库（嵌入式） |
| `wiki` | 百科格式 | Wiki 页面，双向链接 | 仅档案库 |
| `interview` | 采访格式 | Q&A 样式 | 仅档案库 |
| `corrupted` | 损坏格式 | 故障美学，信号退化 | 仅深渊 |

---

## 17. 终端模拟系统

### 17.1 定位

终端不是独立入口，而是一种内容渲染格式。用户在档案库点击终端格式内容 → 进入全屏终端界面 → 退出后返回档案库。

### 17.2 核心设计

前端 JavaScript 模拟终端交互，每篇终端内容有 JSON 配置文件定义命令和响应。终端是**叙事性软隔离**——所有「隐藏」内容在前端 JSON 中可被 DevTools 查看，这被明确接受为设计特性（非 bug）。

### 17.3 命令权限三层

| 权限层 | 命令示例 | 默认可见 | 解锁方式 |
|--------|---------|---------|---------|
| public | `ls, cat, help, who, status` | 是 | 进入终端即可用 |
| hidden | `access, decrypt, cat .secret/*` | 否 | 输入正确密码 / 从其他页面带 token |
| quarantine | `cat quarantine/*, rm` | 否 | 完成 ARG 谜题后注入 token |

绕过终端的权限（如直接查看 JSON）本身被设计为 ARG 的一条路径——在 JSON 源码注释中对解谜者直接喊话。

---

## 18. 虚构学术身份体系

### 18.1 设计原则

- 名字听起来像真人但不映射真实人物
- 简历混用真实机构名 + 虚构部门（如 MIT Department of Consciousness Physics）
- 发表记录全部指向 B.A.I.T. 内部论文
- 每位教授有独特「学术风格」

### 18.2 核心作者生态

- 核心作者群 10–15 位，有完整虚构学术简历
- 合作网络：核心作者之间共同署名
- 引用网络：相互引用形成密集网络
- 学术竞争：通过论文互相反驳
- 机构归属：全部隶属于虚构研究机构

---

## 19. 游戏编码映射系统

从游戏作品（如《三角洲行动》的 GTI 干员体系、SCP 项目编号、Backrooms 层级编号）取材编码结构进行二次创作。

**重要**：只取编码「结构」和「风格」，不直接复制游戏内的具体角色名、剧情、图标、美术。例如用 `GTI-OP-04` 这种编号格式是安全的，但直接写干员名字就有侵权风险。具体边界需 GPT 核实（见 v3 第 39 节 Q8）。

---

# 第四部分：交互与解谜

## 20. 双向页面链接系统

### 20.1 链接类型

| 类型 | relation 值 | 显示文本 | 用途 |
|------|-----------|---------|------|
| 引用 | `cites` | Cited by / Cites | 标准引用 |
| 延伸 | `extends` | Extended by / Extends | 后续研究 |
| 反驳 | `refutes` | Refuted by / Refutes | 学术争论 |
| 相关 | `related` | Related to | 一般关联 |
| 前作 | `predecessor` | Follow-up to / Followed by | 历史演进 |
| 隐藏 | `secret` | 不显示 | ARG 线索 |

反向链接索引存储在 `data/backlinks.json`，由 `backlink_generator.py` 自动生成。链接图谱可视化支持 D3.js 交互。

### 20.2 跨仓库链接

由于三入口在不同仓库，跨入口链接使用绝对 URL。`backlink_generator.py` 生成反向链接时，对跨仓库目标自动生成完整 URL。

---

## 21. 线索与 ARG 解谜系统

### 21.1 三层线索深度

| 层级 | 发现方式 | 对应受众 | 示例 |
|------|---------|---------|------|
| L1 表面线索 | 查看 HTML 源代码、CSS 注释、隐写图 | L2 电脑用户 | `<!-- the answer is in /d7-access/ -->` |
| L2 深层线索 | 终端会话解密、零宽字符提取、Base64 解码 | L3 技术用户 | 终端中的 `decrypt` 命令 |
| L3 元线索 | 跨入口对比、DIO 编号规律、纪元-格式对应 | ARG 核心玩家 | 发现同一论文的三入口分级映射 |

### 21.2 移动端 ARG 入口

移动端无法「查看源代码」，ARG 入口改为：
- 页面底部一个视觉上不起眼的元素（多余的分号、极小的色块）
- 长按特定区域触发
- 概率性 fake 弹窗

---

## 22. 子页面揭示机制

某些论文有隐藏的评审页面，通过特定触发条件解锁：

- 点击不存在的参考文献 [7]
- 输入特定密钥（从 ARG 中获得）
- URL 参数触发（`?key=MIRROR`）

解锁后显示「真实评估」——对论文荒诞之处的逐条揭露。

---

## 23. ARG 验证码与证书系统

### 23.1 设计理念

验证码是 v4 的伦理安全阀。它的存在确保了：**任何声称 B.A.I.T. 认证了他的东西，都可以通过验证码被揭露为假的。**

### 23.2 验证码机制

每篇论文附带一个验证码（如 `B.A.I.T.-VERIFY-2025-0042`），显示在论文页面底部和「收录证书」上。

- **民科看到**：一个看起来很像正规期刊收录编号的验证码。他可能会在视频中展示「我的论文收录编号是 B.A.I.T.-VERIFY-2025-0042」。
- **真相**：在 B.A.I.T. 任一入口的验证页面输入此验证码，显示：

```
═══════════════════════════════════════════
⚠️  此编号为虚构戏仿内容标识

B.A.I.T.-VERIFY-2025-0042

此验证码对应的「论文」属于 B.A.I.T.
虚构创作项目的一部分。

B.A.I.T. 不是真实的学术出版机构。
所有内容均为戏仿/讽刺/虚构创作。

Learn more: <验证页面链接>
═══════════════════════════════════════════
```

### 23.3 证书（收录通知）设计

- 民科可以在论文页面点击「Download Certificate」下载一份 PDF
- PDF 上包含验证码和二维码
- **二维码只跳转到 B.A.I.T. 验证页面首页**（不是直接揭示该篇）
- 任何第三方（雇主、记者、好奇网友）扫描二维码 → 进入验证页面 → 输入编号 → 看到真相
- PDF 元数据标注 `PARODY` `SATIRE` `NOT_REAL_ACADEMIC_CERTIFICATE`

### 23.4 关键安全保障

- 证书上没有任何「会员编号」「认证编号」等可被用于外部验证的东西
- 验证码是「自证为假」的，不是「自证为真」的
- 如果民科只晒证书不输入验证码 → 他永远不会发现真相
- 如果有第三方输入验证码 → 立刻发现真相

---

## 24. 防翻译与多语言策略

### 24.1 设计转变

v3 的「防翻译」策略在 v4 转变为「利用翻译」策略：

- **不再对抗翻译**：零宽字符、CSS 反翻译在 2024+ 的翻译引擎面前效果有限，且影响可访问性和 SEO
- **翻译后的荒诞效果即为线索**：某些双关语和文字游戏在被翻译后会产生奇怪的效果，这本身是 ARG 的线索
- **保留关键双关**：命名体系中的双关（DIO = 上帝、BAIT = 诱饵）在英文原文中保持，翻译后若有微妙变化——这是 feature 不是 bug

### 24.2 多语言

- 学术门户：英文为主（民科会自己用浏览器翻译阅读）
- 档案库：英文为主 + 部分中文 Wiki
- 投稿表单法律措辞：中英双语

---

## 25. URL 参数系统

URL 参数用于：
- ARG 触发：`?key=MIRROR` 解锁隐藏评审
- 成就追踪：`?src=terminal-session-7` 标记来源
- 入口标记：`?portal=archive` 区分用户来源

参数不影响 SEO（使用 canonical URL 避免索引污染）。

---

## 26. 成就系统

### 26.1 五大类成就

**探索类**：
- FIRST_CATCH：首次通过过渡页进入档案库
- DEEP_DIVE：首次进入深渊
- MAPPER：发现完整的 DIO 段-纪元对应表

**解谜类**：
- CODEBREAKER：首次在终端成功使用 decrypt 命令
- TWO_FACES：发现同一篇论文在学术门户和档案库的分级不同
- GHOST_REF：点击不存在的参考文献触发隐藏内容

**互动类**：
- FIRST_SUBMISSION：首次通过 PR 成功投稿
- COMMUNITY_VOTE：首次参与宇宙合并投票
- WIKI_CONTRIBUTOR：首次贡献 Wiki 条目

**社区类**：
- COSMOS_CREATOR：创建新宇宙被接受
- MERGE_ARCHITECT：提案的宇宙合并通过
- PEARL_DIVER：在 rejected/ 中发现隐藏的好内容

**元成就类**：
- SOURCE_READER：阅读源码中发现隐藏内容
- JSON_DIVER：直接查看终端 JSON 配置
- REPO_CLONER：clone 了 bait-core 仓库

### 26.2 成就存储

成就由前端 localStorage 追踪。后端接入后迁移至数据库。

---

## 27. 钓客日志与 Fish Score

### 27.1 Fish Score

- **仅对钓客（解谜者）可见**，不在学术门户中暴露
- 「成为鱼」在内部是负分——这是一个讽刺性设计，但不对当事人公开
- 分数分为「探索深度」「解谜速度」「社区贡献」三个维度
- 不庆祝任何人的受骗

### 27.2 钓客日志

用户个人主页，记录：
- 已解锁的成就
- 已发现的宇宙
- 已阅读的论文
- ARG 进度

纯前端 localStorage 实现。

---

## 28. ISSN 七击彩蛋

点击页面底部 ISSN 编号 7 次触发隐藏内容。彩蛋内容为一条维度泄漏警告，包含指向档案库的线索。

---

## 29. PDF 水印系统

### 29.1 设计原则

- PDF 水印不是法律防御工具（法律防御靠 README + 网站声明）
- 水印是 ARG 线索的载体
- 内容中的微妙荒诞标记（如第 7 页脚注中的一个不可能存在的公式）是比水印更有效的「发现为假」的方式

### 29.2 PDF 元数据

所有生成的 PDF 元数据中标注：
```
Subject: PARODY - NOT REAL ACADEMIC PAPER - SATIRE
Keywords: parody, satire, fictional, BAIT, not real
```

---

# 第五部分：社区与运营

## 30. 内部 Prompt 模板系统

用于生成审稿意见、论文正文、Wiki 条目、终端会话、周边材料等。

模板存储在 `data/prompt_templates.json`。每个模板有特定的角色设定、语气要求和输出格式，确保所有 AI 生成内容风格一致。具体模板正文见 v3 第 29 节。

---

## 31. 社区治理模型

### 31.1 角色

| 角色 | 权限 | 产生方式 |
|------|------|---------|
| 维护者 (Maintainer) | 仓库写入、内容审核、宇宙合并执行 | 项目发起者 + 核心贡献者晋升 |
| 审核者 (Reviewer) | PR 审核、内容安全审查 | 维护者任命 |
| 创作者 (Creator) | Fork + PR、创建宇宙、编辑 Wiki | 任何 GitHub 用户 |
| 钓客 (Angler) | 浏览、ARG 解谜、社区讨论 | 任何网民 |

### 31.2 决策机制

- 日常维护：维护者多数决
- 宇宙合并：社区投票 + 维护者执行
- 正典变更：维护者提案 + 至少 2 人审核
- 紧急移除：任何维护者可单独执行（内容安全问题）

---

## 32. 社区公约与免责声明

### 32.1 bait-core 仓库文件

仓库内置以下文件（Markdown 格式，放在根目录）：

**DISCLAIMER.md**（免责声明）：
- 平台性质声明：这是一个虚构戏仿艺术项目
- 所有「作者」「机构」「论文」均为虚构（除明确标注为真实论文解读外）
- 不提供真实学术出版服务
- 不与任何真实学术出版机构关联

**CODE_OF_CONDUCT.md**（行为准则）：
- 对事不对人
- 不得对民科进行人身攻击
- 不得代表 B.A.I.T. 去联系民科或第三方
- 不得在民科的社交平台下揭穿或围攻
- 玩梗有度，尊重所有人的尊严

**CONTRIBUTING.md**（贡献指南）：
- 投稿格式规范
- 内容安全边界
- ARG 线索嵌入指南
- 分级选择指南

### 32.2 README.md 透明性声明

仓库 README 顶部明确声明平台真实性质：

> **⚠️ B.A.I.T. is a fictional parody / satire art project.**
> It is NOT a real academic publisher. All "papers", "authors", "peer reviews", and "editorial board members" are fictional creations — unless explicitly labeled as commentary on real published work. This project is open source and zero-revenue. For more information, see [DISCLAIMER.md](./DISCLAIMER.md).

### 32.3 学术门户页脚声明

学术门户每页页脚包含一行小字（CSS 淡化处理，需仔细看才可见）：

> *B.A.I.T. is an open research interpretation initiative. Content labeled as "interpretation" reflects the views of the interpreting author and does not constitute original research publication unless sourced from peer-reviewed venues.*

---

## 33. 配套脚本与工具链

### 33.1 脚本清单

| 脚本 | 功能 |
|------|------|
| `build.py` | 按入口构建静态站点，从 bait-core 拉取内容 |
| `bi_calculator.py` | 计算 B.I. 评分 |
| `content_validator.py` | 内容安全验证 + 跨入口泄露检查 |
| `backlink_generator.py` | 双向链接索引生成（支持跨仓库绝对 URL） |
| `review_generator.py` | 调用 LLM 生成审稿意见 |
| `pdf_generator.py` | 生成带水印和元数据的 PDF |
| `cosmos_initializer.py` | 新宇宙目录骨架生成 |
| `ai_content_filler.py` | AI 补稿（衍生论文 + 周边材料 + Wiki） |
| `grade_mapper.py` | 分级映射（内部 → 学术门户 / 档案库 / 终端） |
| `video_transcriber.py` | 民科视频转写为论文解读（v4 新增） |

### 33.2 数据文件

| 文件 | 内容 |
|------|------|
| `data/backlinks.json` | 双向链接索引 |
| `data/grade_map.json` | 分级映射表 |
| `data/cosmos_index.json` | 宇宙索引 |
| `data/achievements.json` | 成就定义 |
| `data/prompt_templates.json` | Prompt 模板 |
| `data/cross_repo_map.json` | 跨仓库 URL 映射 |

---

## 34. SEO 与反 SEO 策略

### 34.1 SEO 策略（学术门户）

- **目标关键词**：「publish paper free」「free academic journal」「论文免费发表」「国际期刊投稿」等民科搜索习惯中的词
- **个人名 SEO**：每篇民科视频转写的论文，针对该民科的网名做 SEO（title tag、meta description、heading 中包含网名）
- **白帽 SEO**：语义化 HTML、结构化数据、sitemap.xml
- 不购买广告、不做黑帽

### 34.2 反 SEO 策略（档案库 + 深渊）

- `robots.txt` 全禁
- `<meta name="robots" content="noindex, nofollow">`
- 深渊使用随机哈希路径，不生成 sitemap
- 不使用学术关键词

---

## 35. 域名策略

### 35.1 渐进式方案

| 阶段 | 方案 | 成本 |
|------|------|------|
| Phase 0 | `<org>.github.io/bait-academic` / `bait-archive` / `bait-deep` | 免费 |
| Phase 1 | 注册 `.xyz` 或 `.site` 便宜域名，配 Cloudflare CDN | 几美元/年 |
| Phase 2+ | 如有需要和预算，升级域名 | 按预算 |

### 35.2 CDN 加速

- Phase 1 起用 Cloudflare CDN，改善国内访问
- 学术门户走 CDN，档案库/深渊可不走（解谜者会翻墙）

---

## 36. SSR 订阅预留

v4 预留 SSR（Static Site Rendering）订阅的架构接口：

- 内容更新时，除构建静态页面外，可生成 RSS/Atom/JSON Feed
- 解谜者可通过 RSS 阅读器订阅特定宇宙的内容更新
- 终端会话更新也可生成 Feed
- 纯静态实现，无需后端

Phase 4 以后实现。

---

## 37. 后端预留与扩展

### 37.1 注册系统

- Phase 0–2：GitHub Issues + PR（GitHub 账号即注册）
- Phase 3+：按需接入 Supabase Auth
  - 支持邮箱注册 + GitHub OAuth
  - 为不会 GitHub 的投稿者提供表单通道
  - 免费层足够长期使用

### 37.2 后端触发条件

以下条件同时满足时考虑加后端：
1. 月均非 GitHub 投稿 > 20 篇
2. 有真实用户反馈「不会用 GitHub」
3. 法律侧对数据合规有明确结论

---

## 38. 删库跑路预案

### 38.1 设计原则

- 所有内容以 Markdown 源文件存在 bait-core → 备份就是 `git clone`
- 三个展示仓库是渲染缓存 → 删了可重建
- 站点部署在 GitHub Pages → 删仓库 = 站点消失，零残留
- 无自有服务器 → 不需要关服务器、不需要清理数据库

### 38.2 应急场景

| 场景 | 应对 |
|------|------|
| 收到投诉/律师函 | 立即删除被投诉内容，评估整体关停 |
| 需要完全关停 | 删除三个展示仓库（站点消失），保留 bait-core 备份 |
| GitHub 仓库被封 | 多镜像备份（GitLab、Codeberg、本地），README 透明声明争取解封 |
| 民科因受骗产生现实损失 | 快速响应通道，提供「真实性质证明」文档，移除相关民科内容 |
| 社区成员越界联系民科 | CODE_OF_CONDUCT 执行：警告 → 踢出 → 移除其所有内容 |

---

# 第六部分：法律与路线图

## 39. 法律与伦理框架

v3 的第 38 节（法律与伦理框架）和第 39 节（提交 GPT 的法律咨询问题清单 19 题）在 v4 中**完整保留**。以下为 v4 相比 v3 的法律相关变更要点：

### 39.1 v4 对法律风险的改善

| v3 风险点 | v4 改善 |
|----------|--------|
| 被动等鱼投稿 | 改为 SEO 钓鱼——平台从未主动联系任何人 |
| T 级转载真实论文 | 砍掉——只做解读+引用，不转载全文 |
| 「冒充机构」定性 | 对外的定位改为「论文解读平台」而非「出版机构」 |
| 证书可用于外部验证 | 验证码自证为假，二维码只跳回首页 |
| 入口隔离靠路径模糊 | 三独立仓库三独立 URL，物理隔离 |
| 数据合规（投稿表单） | Phase 0 无表单；将来用 Supabase（最小化收集+即用即删） |

### 39.2 法律前置原则

> **M0 法律绿灯必须先于任何公开发布。** 在 GPT 法律咨询完成、对 v3 第 39 节 Q1–Q4（平台定性）和 Q18（综合可行性）有明确结论前，不要公开部署可被搜索引擎索引的版本。

---

## 40. 实施路线图

### 40.1 阶段划分

**Phase 0：基础设施 + 法律定性（2–3 周）**
- [ ] 创建 bait-core / bait-academic / bait-archive / bait-deep 四个仓库
- [ ] 搭建静态站点框架（学术门户 + 档案库的基础模板）
- [ ] 配置 GitHub Actions 自动同步
- [ ] 编写 `content_validator.py` 和 `build.py`
- [ ] 编写 DISCLAIMER.md / CODE_OF_CONDUCT.md / CONTRIBUTING.md
- [ ] **完成 GPT 法律咨询（v3 第 39 节的 19 题），据结果决定是否调整范围**
- [ ] 本地内测，不做公开部署

**Phase 1：核心内容（3–4 周）**
- [ ] 创作 10–15 篇初始论文解读（含 2–3 篇真实论文解读）
- [ ] 创建 R.E.E.F. 主站宇宙设定 + Wiki
- [ ] 创建 2–3 个独立宇宙
- [ ] 建立双向链接
- [ ] 生成带水印 PDF
- [ ] 做基础 SEO

**Phase 2：互动系统（3–4 周）**
- [ ] 成就系统
- [ ] 钓客日志
- [ ] 子页面揭示机制
- [ ] 验证码与证书系统
- [ ] ISSN 七击彩蛋
- [ ] URL 参数系统
- [ ] 手机端能力分层

**Phase 3：ARG 系统（4–6 周）**
- [ ] 三层线索嵌入
- [ ] ARG 进度追踪
- [ ] 跨入口分级映射的 ARG 谜题
- [ ] 链接图谱可视化
- [ ] DIO 段-纪元对应线索铺设

**Phase 4：终端与深渊（3–4 周）**
- [ ] 终端模拟器前端（含三层权限）
- [ ] 首批终端会话内容
- [ ] H.A.D.A.L. 深渊入口
- [ ] 损坏格式内容
- [ ] SSR 订阅（JSON Feed）

**Phase 5：社区与运营（持续）**
- [ ] 投稿表单（如需要）+ Supabase Auth
- [ ] 民科视频转写工作流
- [ ] Giscus 评论
- [ ] SEO 优化（仅学术门户）
- [ ] AI 补稿工具链完善
- [ ] 社区共创引导

### 40.2 里程碑

| 里程碑 | 标志 |
|-------|------|
| M0: Legal Green Light | GPT 法律咨询完成，范围确认 |
| M1: Hello B.A.I.T. | 四个仓库就绪，构建管道跑通 |
| M2: First Catch | 初始内容库完成（≥ 15 篇解读） |
| M3: The Hook | 互动系统上线 |
| M4: Deep Waters | ARG + 终端 + 深渊完整 |
| M5: Open Waters | 社区投稿开放 |

---

## 附录：术语表

| 术语 | 含义 |
|------|------|
| B.A.I.T. | Bureau of Advanced Interdisciplinary Theories — 平台/期刊名称 |
| R.E.E.F. | Research Encyclopedia of Emerging Frontiers — 主站宇宙 |
| D.I.O. | Document Identity Ontology — 论文标识系统 |
| H.A.D.A.L. | Hidden Archive of Dimensional Anomalies & Leaks — 深渊层 |
| D.D.I. | Dimensional Deviation Index — 维度偏移指数（0–5） |
| B.I. | Bait Index / Bibliometric Index — 诱饵指数 |
| C.O.S.M.O.S. | Catalog of Systematic Models & Ontological Schemas — 宇宙编号 |
| F.I.S.H. | Formal Index of Scholarly Highlights — 论文库 |
| A.N.G.L.E.R. | Archived Network of Genuine Learning & Enlightenment Records — 钓客 |
| K.E.L.P. | Knowledge Exchange & Lexicon Platform — Wiki 系统 |
| C.O.R.A.L. | Catalog of Observed Research & Academic Lore — 宇宙索引 |
| P.E.A.R.L. | Peer Evaluation & Assessment Record Ledger — 审稿记录 |
| FG / TG / RG / LG | Fun Grade / Truth Grade / Record Grade / Log Grade |
| CAST / HOOK / CATCH / RELEASE | 抛竿 / 上钩 / 收网 / 放生 — 审稿四阶段 |
| Canon / Semi-Canon / Apocrypha / Joke | 正典 / 半正典 / 逸典 / 玩笑 |
| Fish Score | 用户洞察力评分（仅钓客可见） |
| interpretation | v4 统一内容格式：论文解读 |
| source_type | 论文解读来源类型（video_transcription / real_paper / community_fiction） |

---

## v4 相对 v3 的变更摘要

### 架构变更
- **单源维护 + 多仓库自动拉取**：bait-core（唯一维护）+ 三个展示仓库（GitHub Actions 同步）
- **URL 隔离**：三入口在不同 GitHub Pages URL 下，物理隔离

### 内容模型变更
- **统一为「论文解读」格式**：所有论文以 interpretation 格式呈现
- **砍掉 T 级完整转载**：真实论文只做解读 + 引用 + doi 链接，不转载原文
- **新增民科视频转写流程**：AI 将民科视频转写为论文解读，SEO 钓鱼

### 钓鱼模型变更
- **被动投稿 → SEO 钓鱼**：主动生成内容，等鱼通过搜索引擎自寻发现
- **不主动联系原则**：平台从不以「编辑部」名义联系任何人

### 安全与伦理变更
- **伦理框架独立章节**：对事不对人、减少伤害、不制造现实后果
- **ARG 验证码系统**：证书上的验证码自证为假
- **社区公约三件套**：DISCLAIMER.md / CODE_OF_CONDUCT.md / CONTRIBUTING.md
- **删库跑路预案**

### 新增系统
- **手机端 L0–L3 能力分层**
- **SSR 订阅预留**
- **分级标签双套**：学术门户的假分区（JCR Q1 等）+ 档案库的 Backrooms 风格大标签

### 保留的 v3 内容
- 第 38–39 节（法律框架 + 19 题 GPT 咨询清单）完整保留
- 所有脚本伪代码、Prompt 模板、成就表、Front Matter 规范保留

---

*本文档为 B.A.I.T. 平台 v4 完整技术设计方案。v4 在 v3 的多宇宙/三入口架构基础上，升级了仓库隔离方案，统一了内容模型，确立了 SEO 钓鱼模型，并大幅扩充了伦理框架与社区公约。**法律相关结论均为框架性初步判断，最终定性必须以 GPT 检索结论 + 必要时真人律师确认为准。** 世界观细节由社区共创填充。*
