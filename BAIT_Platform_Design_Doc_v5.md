# B.A.I.T. 平台完整设计文档 v5

> **Bureau of Advanced Interdisciplinary Theories**  
> 一个安全优先的虚构学术文稿工坊、社区小说档案库与 ARG 世界观共创平台。  
> v5 的核心目标是：保留 paper 写作体验、多入口世界观、社区共创与解谜乐趣，同时避免真实人物误认、主动骚扰、现实学术背书误用、截图传播误导与跨法域法律风险。

---

## v5 总原则

v5 不再把“让现实人物相信自己被真实期刊收录”作为产品目标。平台可以提供强烈的学术排版、审阅流程、虚构机构世界观和社区共创沉浸感，但这些沉浸感必须建立在可见、持续、可截图、可 OCR、可翻译的披露基础上。

核心判断如下：

1. **B.A.I.T. 不是现实学术期刊、预印本服务器、收录机构或认证机构。**
2. **平台内容只能经过社区编辑审核、内容边界审核、风格审核和世界观一致性审核，不构成现实学术同行评审。**
3. **真实人物不能作为站内论文作者、投稿者、被收录者或认证对象。**
4. **真实人物只能作为公开材料背景对象（Source Subject / Public Context）出现，并且必须明确未参与、未授权、未背书。**
5. **所有入口都必须能让正常用户主动发现平台性质；入口差异只体现在信息量、叙事深度和交互复杂度，不体现在真假披露的有无。**
6. **用户协议、冷门页面、源码注释、PDF 元数据和 ARG 谜题只能作为补充披露，不能承担主要告知责任。**
7. **禁止任何社区成员主动联系、挑衅、诱导、嘲讽、围攻现实人物。**
8. **截图、PDF、分享卡片必须自带上下文水印，避免脱离原页面后被误用。**

---

## 目录

### 第一部分：定位与风险重构

1. [v5 项目定位](#1-v5-项目定位)
2. [从 v1-v4 到 v5 的关键调整](#2-从-v1-v4-到-v5-的关键调整)
3. [用户群体重新定义](#3-用户群体重新定义)
4. [不可突破的安全边界](#4-不可突破的安全边界)

### 第二部分：信息架构与多入口

5. [多入口安全信息架构](#5-多入口安全信息架构)
6. [公开入口：Fictional Academic Workshop](#6-公开入口fictional-academic-workshop)
7. [社区入口：Source Context & Collaboration](#7-社区入口source-context--collaboration)
8. [档案入口：R.E.E.F. / H.A.D.A.L. 世界观](#8-档案入口reef--hadal-世界观)
9. [管理入口：审核、下架与风控](#9-管理入口审核下架与风控)

### 第三部分：内容模型与真实人物处理

10. [统一内容模型](#10-统一内容模型)
11. [真实人物 Source Subject 规则](#11-真实人物-source-subject-规则)
12. [虚构作者与社区编辑身份](#12-虚构作者与社区编辑身份)
13. [真实论文评论与引用策略](#13-真实论文评论与引用策略)
14. [Front Matter v5 规范](#14-front-matter-v5-规范)

### 第四部分：披露、截图水印与导出物

15. [三层披露体系](#15-三层披露体系)
16. [截图水印与分享防误用](#16-截图水印与分享防误用)
17. [PDF 与打印页规则](#17-pdf-与打印页规则)
18. [Release Card：替代证书/奖状](#18-release-card替代证书奖状)
19. [移动端与电脑端一致性原则](#19-移动端与电脑端一致性原则)

### 第五部分：审核流程与社区治理

20. [CAST / HOOK / CATCH / RELEASE v5 解释](#20-cast--hook--catch--release-v5-解释)
21. [社区编辑审核标准](#21-社区编辑审核标准)
22. [社区公约硬规则](#22-社区公约硬规则)
23. [违规处理与 Abuse Response](#23-违规处理与-abuse-response)
24. [投诉、下架与更正机制](#24-投诉下架与更正机制)

### 第六部分：世界观、ARG 与沉浸体验

25. [R.E.E.F. 多宇宙架构保留方案](#25-reef-多宇宙架构保留方案)
26. [SCP / Backrooms 风格档案层](#26-scp--backrooms-风格档案层)
27. [ARG 线索边界](#27-arg-线索边界)
28. [Paper 写作体验与沉浸式流程](#28-paper-写作体验与沉浸式流程)

### 第七部分：法律、运营与路线图

29. [跨法域风险框架](#29-跨法域风险框架)
30. [必须新增的政策文件](#30-必须新增的政策文件)
31. [技术实现建议](#31-技术实现建议)
32. [实施路线图 v5](#32-实施路线图-v5)
33. [附录：推荐固定文案](#附录推荐固定文案)
34. [附录：术语表](#附录术语表)

---

# 第一部分：定位与风险重构

## 1. v5 项目定位

B.A.I.T. v5 是一个由三类内容共同组成的虚构学术创作系统：

1. **虚构学术文稿工坊**：为用户提供 paper 风格写作、社区编辑反馈、修订流程、PDF 导出和文稿展示体验。
2. **社区小说档案库**：像 SCP、Backrooms 一样，将荒诞理论、虚构研究、异常档案、人物设定和多宇宙叙事组织成一个可共创的小说集合。
3. **ARG 解谜平台**：通过多入口、编号映射、隐藏链接、终端模拟和档案分级提供探索体验。

v5 的核心叙事仍可保留“学术机构表皮”和“跨维度档案”的世界观，但平台不能向任何现实用户暗示：其内容已经获得真实期刊发表、学术收录、权威认证、现实同行评审或机构背书。

### 1.1 v5 对外一句话定位

中文：

> B.A.I.T. 是一个社区虚构文稿与推想型学术写作工坊，不是真实学术期刊、预印本服务器、收录机构或认证机构。

英文：

> B.A.I.T. is a fictional community manuscript workshop and speculative academic archive, not a real journal, preprint server, indexing service, or certification body.

### 1.2 v5 保留的乐趣

v5 并不取消沉浸式体验，而是改变沉浸来源：

| 沉浸来源 | 保留 | 调整 |
|---|---|---|
| 学术排版 | 保留 | 页面标签必须标明虚构文稿 |
| 审核流程 | 保留 | 改为社区编辑审核，不称现实同行评审 |
| 虚构作者 | 保留 | 不映射真实人物 |
| 真实人物背景 | 有条件保留 | 只能作为 Source Subject / Public Context |
| PDF 导出 | 保留 | 每页带上下文水印 |
| 证书/奖状 | 改造后保留 | 改为 Release Card / Archive Card |
| 多入口 | 保留 | 披露强度不因入口而消失 |
| ARG | 保留 | 不用于隐藏平台真实性质 |

---

## 2. 从 v1-v4 到 v5 的关键调整

### 2.1 保留内容

v1-v4 中以下内容仍然适合保留：

- B.A.I.T. / R.E.E.F. / H.A.D.A.L. / D.I.O. / B.I. 等命名体系。
- 多宇宙架构、宇宙合并、Wiki、终端会话、异常档案。
- CAST / HOOK / CATCH / RELEASE 四阶段流程。
- 双向链接、链接图谱、DIO 编号规律、ARG 成就系统。
- PDF 水印、截图水印、分享卡片上下文标识。
- 内容安全审查、社区治理、删库跑路预案。
- 真实论文只做评论、引用、解读，不转载全文。

### 2.2 必须删除或重写的内容

以下内容在 v5 中删除或重写：

| v1-v4 设计 | v5 处理 |
|---|---|
| 真实人物定向 SEO 钓鱼 | 删除。不得针对真实人名/网名做“发现自己被收录”的链路。 |
| 把真实人物作为论文作者 | 删除。真实人物只能作为 Source Subject。 |
| 假 JCR / CAS 分区 | 删除或仅在档案入口作为明确虚构标签，不在公开入口使用。 |
| 真实收录证书 / 录用证明 | 删除。改为 Fictional Release Card。 |
| 验证码输入后才揭示为假 | 改为二维码直接跳转说明页，验证码仅作档案索引。 |
| 反翻译隐藏披露 | 删除。披露必须可翻译、可 OCR。 |
| 手机端比电脑端更难发现真相 | 删除。两端披露一致。 |
| peer review / accepted / indexed | 改为 community review / screened / archived。 |

### 2.3 设计方向变化

v4 的核心张力是“真实感 vs 可发现真相”。v5 的核心原则改为：

> 真实感来自流程、排版、术语和世界观；安全性来自显性标签、来源分离、社区公约和导出物水印。不得通过隐藏事实制造真实感。

---

## 3. 用户群体重新定义

### 3.1 A 组：社区参与者 / 解谜者 / 维护者

A 组包括：

- ARG 玩家
- GitHub 贡献者
- 文稿创作者
- 社区编辑
- 世界观维护者
- 站点开发者
- 对学术戏仿文化有辨识能力的普通用户

A 组可以看到更完整的来源上下文、真实人物背景、映射关系、社区审核记录、世界观设定和 ARG 深层内容。

### 3.2 B 组：普通访客 / 文稿体验者 / 低辨识用户

B 组包括：

- 非社区用户
- 通过搜索或分享进入的人
- 只看公开页面的人
- 对 paper 流程感兴趣的人
- 可能误读学术格式的人

v5 不把 B 组定义为“被钓对象”，而定义为“需要被保护的普通访客”。他们可以获得完整的 paper 写作和阅读体验，但不能被诱导相信平台提供现实学术背书。

### 3.3 C 组：真实人物 / Source Subject

C 组是站内内容可能提及的现实人物、公开材料发布者、视频作者或民科辞海等外部页面中的人物。

C 组不是平台用户时，必须满足以下原则：

1. 不得作为站内作者。
2. 不得被写成投稿者。
3. 不得被写成被收录、被认证、被授权对象。
4. 不得被主动联系、私信、评论区喊话、围观或挑衅。
5. 如果相关内容造成实际伤害或本人提出异议，应快速下架或改写。

---

## 4. 不可突破的安全边界

### 4.1 内容禁区

以下内容禁止发布：

1. 政治敏感内容。
2. 邪教、极端主义、煽动性群体动员。
3. 医疗、健康、药物、治疗建议。
4. 金融、投资、赌博建议。
5. 种族、性别、地域、残障、年龄歧视。
6. 针对真实个人的人身攻击、侮辱、隐私挖掘。
7. 对现实人物的虚假指控、伪造获奖、伪造窃取成果叙事。
8. 可能引导危险实验、化学混合、物理冒险或自伤他伤的内容。
9. 未成年人相关不当内容。
10. 任何暗示平台提供现实学术认证或职业资质证明的内容。

### 4.2 交互禁区

以下行为禁止：

- 主动联系真实人物本人或亲友。
- 去抖音、快手、B站、知乎、贴吧等评论区留言“你被发表了”。
- 私信告知“我们帮你整理成论文了”。
- 伪造“某人窃取你的成果拿奖/发表”的话术。
- 组织网友围观、嘲讽、举报、钓鱼、截图传播。
- 使用 B.A.I.T. 名义对外沟通。

### 4.3 披露禁区

以下做法不得作为主要披露方式：

- 只在用户协议中写明。
- 只在页脚极小文字中写明。
- 只在源码注释中写明。
- 只在 PDF 元数据中写明。
- 只在 ARG 隐藏页中写明。
- 只用英文写明且刻意阻止翻译。
- 用 SVG、Unicode 变体、零宽字符或图片文字隐藏关键披露。

---

# 第二部分：信息架构与多入口

## 5. 多入口安全信息架构

v5 保留多入口，但入口差异必须被重新定义。

### 5.1 三个公开入口 + 一个管理入口

| 入口 | 面向对象 | 内容重点 | 披露要求 |
|---|---|---|---|
| 公开入口 | 普通访客、B 组 | paper 风格阅读、文稿工坊、虚构作者 | 短标签常显，完整说明页脚可见 |
| 社区入口 | A 组协作者 | 来源上下文、社区规则、讨论、审核记录 | 可显示真实人物背景，但必须带未授权未背书说明 |
| 档案入口 | ARG / 世界观玩家 | R.E.E.F. / H.A.D.A.L. / 异常档案 | 明确“虚构档案/小说集合” |
| 管理入口 | 维护者 | 审核、风控、下架、投诉处理 | 内部日志完整记录 |

### 5.2 入口之间的核心差异

入口可以在以下方面不同：

- 视觉风格。
- 信息量。
- 是否显示真实人物 Source Subject 卡片。
- 是否显示世界观分级。
- 是否显示 ARG 线索。
- 是否显示审核记录。
- 是否允许评论和协作。

入口不能在以下方面不同：

- 是否披露“不是现实期刊”。
- 是否披露“真实人物不是作者”。
- 是否披露“社区审核不等于现实同行评审”。
- 是否披露“导出物不是证书”。

---

## 6. 公开入口：Fictional Academic Workshop

公开入口是最像 paper 的入口，但必须有短披露。

### 6.1 首页模块

首页建议结构：

1. 顶部导航：B.A.I.T. / Manuscripts / Workshop / Archive / About。
2. 顶部细横幅：`社区虚构文稿工坊 / Fictional Academic Workshop`。
3. Hero 区：介绍平台为推想型学术写作、社区编辑和虚构档案项目。
4. 最新文稿列表：展示虚构作者、标题、主题标签、内容类型。
5. Workshop 入口：引导用户体验 paper 写作流程。
6. About / Policy 入口：显眼但不打断沉浸。

### 6.2 文章页模块

文章页建议结构：

1. 顶部细横幅。
2. 标题。
3. 标题下徽章：`Community Manuscript`、`Fictional`、`Not Journal Publication`。
4. 虚构作者信息。
5. 摘要、关键词、正文、参考文献。
6. 社区编辑审核摘要。
7. 页脚完整说明。

公开入口默认不显示真实人物外链。如果需要显示，应仅显示简化的 Source Context 摘要，不显示引战性、嘲讽性或人身信息。

### 6.3 公开入口禁用词

公开入口不得使用以下词作为真实功能描述：

- accepted
- certified
- indexed
- peer-reviewed
- official publication
- journal acceptance
- JCR Q1 / CAS 一区
- certificate of acceptance
- DOI registration

可替代为：

- archived
- community-edited
- workshop feedback
- fictional release
- release card
- community manuscript
- speculative commentary

---

## 7. 社区入口：Source Context & Collaboration

社区入口用于 A 组协作者理解来源、审核、世界观映射和社区规则。

### 7.1 社区入口可显示内容

社区入口可以显示：

- Source Subject 卡片。
- External Context 链接。
- 公开材料来源说明。
- 社区编辑记录。
- 审核风险等级。
- 争议处理状态。
- 下架/更正记录。
- 宇宙映射关系。

### 7.2 Source Subject 卡片

Source Subject 卡片必须独立于作者信息，推荐结构：

```text
Source Context / 公开材料背景

Source Subject: 李某某
External Context: 民科辞海存档 / 公开视频 / 公开帖子
Relationship: Background subject only

Notice:
该人物不是本文作者，未参与投稿，未授权，未背书。
本文为基于公开材料的社区虚构评论/整理。
```

### 7.3 社区入口警示

社区入口顶部应固定显示：

> 社区协作不得转化为现实骚扰。禁止联系、私信、评论区喊话、围观、挑衅、伪造获奖或伪造学术承认。

---

## 8. 档案入口：R.E.E.F. / H.A.D.A.L. 世界观

档案入口是 SCP / Backrooms 风格的叙事层。

### 8.1 内容形式

档案入口包括：

- R.E.E.F. 宇宙索引。
- H.A.D.A.L. 深渊内容。
- 异常档案。
- 终端会话。
- Wiki 条目。
- 编年史。
- 宇宙合并记录。

### 8.2 分级标签

档案入口可使用 Backrooms 风格标签，例如：

- Δ-0 BASELINE ANOMALY
- Δ-1 MINOR DEVIATION
- Δ-2 SIGNIFICANT DEVIATION
- Δ-3 CRITICAL DEVIATION
- R-1 CONTAINED
- L-3 QUARANTINED

但这些标签只能评估**文本/宇宙偏移**，不能评估现实人物价值、智力、人格或社会危险性。

### 8.3 档案入口披露

档案入口应显示：

> R.E.E.F. / H.A.D.A.L. 是 B.A.I.T. 的虚构世界观档案层。其分级用于小说和 ARG 结构，不用于评价现实人物。

---

## 9. 管理入口：审核、下架与风控

管理入口是维护者处理风险的内部系统。

### 9.1 管理功能

管理入口应支持：

- 内容提交队列。
- Front Matter 完整性检查。
- 敏感内容扫描。
- 真实人物命中检查。
- 来源材料记录。
- Source Subject 风险评级。
- 社区审核意见。
- 投诉处理记录。
- 下架和更正按钮。
- 发布前截图预览。
- PDF 水印预览。

### 9.2 风险等级

建议使用以下内部风险等级：

| 等级 | 含义 | 处置 |
|---|---|---|
| Green | 纯虚构，无真实人物，无危险内容 | 可发布 |
| Yellow | 有真实公开材料，但无个人攻击 | 二人审核 |
| Orange | 涉及真实人物、争议内容或误认风险 | 维护者会审，默认不公开入口展示 |
| Red | 可能导致骚扰、诽谤、危险行为或现实损害 | 拒绝或下架 |

---

# 第三部分：内容模型与真实人物处理

## 10. 统一内容模型

v5 内容分为七类。

| content_mode | 名称 | 是否可公开入口展示 | 是否可含真实人物 |
|---|---|---|---|
| fictional_manuscript | 虚构文稿 | 是 | 默认否 |
| speculative_commentary | 推想型评论 | 是 | 有条件 |
| real_paper_commentary | 真实论文评论 | 是 | 仅真实论文作者，须准确引用 |
| community_lore | 社区世界观 | 社区/档案入口 | 默认否 |
| source_context | 来源背景卡 | 社区入口 | 是 |
| terminal_record | 终端记录 | 档案入口 | 否 |
| release_card | 虚构发布卡 | 是 | 不得作为认证 |

### 10.1 虚构文稿

虚构文稿是平台主体，具有 paper 格式，但内容属于社区创作或推想型虚构。

### 10.2 推想型评论

推想型评论可以基于公开材料，但必须明确为评论、整理或虚构化改写，不可冒充原作者投稿。

### 10.3 真实论文评论

真实论文评论仅允许评论真实存在的论文、预印本或开放获取材料。必须保留真实标题、作者、DOI/URL 和许可证信息，不得将真实作者写成 B.A.I.T. 成员。

---

## 11. 真实人物 Source Subject 规则

### 11.1 基本规则

真实人物只能作为 Source Subject 出现，不能作为：

- Article Author
- Corresponding Author
- Submitted By
- Accepted Author
- Certified Researcher
- B.A.I.T. Fellow
- Editorial Board Member

### 11.2 Source Subject 展示规则

| 项目 | 规则 |
|---|---|
| 姓名 | 可用公开页面已有姓名；若有争议，使用化名或 initials |
| 外链 | 仅放在 Source Context 区 |
| 生平 | 不事无巨细描写，避免隐私化、人肉化 |
| 评价 | 只评价公开理论文本，不评价人格、智力、家庭、职业 |
| 争议 | 用中性语言，不写煽动性嘲讽 |
| 纠错 | 提供更正/下架入口 |

### 11.3 推荐 Source Context 文案

> 外部链接仅用于公开材料背景说明。该人物不是本文作者，未参与投稿、未授权、未背书。本文为社区虚构评论/整理，不构成现实学术发表或认证。

英文：

> External links are provided only as public context. The person referenced here is not the author of this manuscript and has not submitted, authorized, endorsed, or participated in this page.

### 11.4 不推荐写法

以下写法禁止：

- “我们为某某发表了论文”。
- “某某已被 B.A.I.T. 收录”。
- “某某的成果通过审核”。
- “某某获得 B.A.I.T. 认证”。
- “某某被国际期刊注意到”。
- “某某论文正式发布”。

---

## 12. 虚构作者与社区编辑身份

### 12.1 虚构作者原则

虚构作者可用于增强世界观，但必须满足：

- 不映射真实人物。
- 不使用真实人物肖像。
- 不使用真实机构的真实部门名。
- 不暗示真实学术任职。
- 站内作者页标明 fictional profile。

### 12.2 社区编辑署名

社区编辑可以使用笔名，例如：

- Editor A.
- Dr. Null Current
- R.E.E.F. Editorial Unit
- B.A.I.T. Community Desk

社区编辑署名不代表现实学术资质。

### 12.3 作者页结构

作者页应显示：

- Fictional Profile 标签。
- 所属虚构部门。
- 参与文稿列表。
- 世界观角色说明。
- 不对应现实人物的说明。

---

## 13. 真实论文评论与引用策略

### 13.1 合法引用原则

真实论文只能以以下形式使用：

- 参考文献引用。
- DOI / arXiv / publisher URL 链接。
- 摘要性评论。
- 合理短引文。
- 许可证允许的内容引用。

不得：

- 全文转载付费论文。
- 修改真实论文后再发布。
- 将真实作者改写为 B.A.I.T. 作者。
- 声称 B.A.I.T. 收录或认证真实论文。

### 13.2 真实论文评论页标签

真实论文评论页必须标明：

- `Commentary on real work`
- `Not the original paper`
- `No affiliation with original authors unless stated`

### 13.3 参考文献混编

虚构文稿中可以引用真实文献作为背景，但必须避免让引用构成虚假背书。虚构引用和真实引用应在维护者视图中可区分；公开页可使用统一格式，但不得伪造 DOI。

---

## 14. Front Matter v5 规范

每篇文稿必须包含以下 Front Matter：

```yaml
---
title: "A Speculative Interpretation of Dimensional Heat Transfer"
content_mode: fictional_manuscript
visibility: public
language: en

fictional_disclosure: true
not_real_journal: true
not_peer_reviewed: true
not_certification: true

article_authors:
  - name: "Dr. A. Mercer"
    type: fictional_profile
    profile_id: "DIO:B.A.I.T.AUTH.2026.0001"

community_editors:
  - name: "B.A.I.T. Community Desk"
    type: pseudonym

source_subjects:
  - name: null
    type: none
    external_context_url: null
    affiliation_notice: "No real person is the author or submitter of this manuscript."

source_basis:
  type: community_original
  description: "Original fictional manuscript created for B.A.I.T."
  rights_status: CC-BY-SA-4.0

review_type: community_editorial_review
review_scope:
  - style
  - safety
  - consistency
  - readability
  - source_context

review_status: release
review_terms:
  cast: "Submission Intake"
  hook: "Community Editorial Screening"
  catch: "Style & Safety Review"
  release: "Archive Publication"

dio: "DIO:B.A.I.T.2026.0001"
cosmos: "COSMOS-CNS-001"
grade: FG-2
ddi: 2
bi_score: 61.5

screenshot_watermark: true
pdf_watermark: true
release_card_allowed: true
release_card_type: fictional_manuscript_card

risk_level: green
takedown_contact: "abuse@placeholder.example"
---
```

### 14.1 涉及真实人物时的 Front Matter

```yaml
source_subjects:
  - name: "李某某"
    type: public_context_subject
    external_context_url: "https://example.org/public-context"
    affiliation_notice: "This person is not the author, submitter, endorser, or participant of this manuscript."
    display_in_public_entry: false
    display_in_community_entry: true
    harassment_risk: orange
```

涉及真实人物时，`display_in_public_entry` 默认必须为 `false`。若要公开入口显示，必须经过维护者会审并使用最短上下文说明。

---

# 第四部分：披露、截图水印与导出物

## 15. 三层披露体系

v5 使用三层披露：短披露、上下文披露、完整披露。

### 15.1 第一层：短披露

短披露不破坏沉浸感，但必须常显。

位置：

- 标题旁徽章。
- 页面顶部细横幅。
- 文稿信息卡。
- PDF 页脚。
- 分享图角标。

推荐短文案：

> 社区虚构文稿，非现实期刊发表。  
> Fictional community manuscript, not a journal publication.

### 15.2 第二层：上下文披露

涉及真实人物或外部材料时显示。

位置：

- Source Context 卡片。
- 文章正文前。
- 社区入口详情页。

推荐文案：

> 若本文涉及公开人物或公开材料，仅用于背景说明或社区评论；该人物不是本文作者，未参与投稿、未授权、未背书。

### 15.3 第三层：完整披露

位置：

- About。
- DISCLAIMER.md。
- EDITORIAL_POLICY.md。
- TERMS.md。
- 页脚链接。
- PDF 最后一页。

完整披露说明平台性质、审核范围、真实人物规则、投诉渠道、版权、许可和社区行为边界。

---

## 16. 截图水印与分享防误用

截图传播是 v5 的核心风险之一。用户可能只看到截图，不看到页脚、用户协议或完整说明。因此页面必须提供截图上下文水印。

### 16.1 页面截图水印

所有文稿页叠加浅色斜向水印：

```text
社区虚构文稿 / Community Fictional Manuscript
```

水印要求：

- 不影响阅读。
- 截图时可见。
- 深浅主题均可见。
- 移动端和桌面端都显示。
- 不能通过普通 UI 设置关闭。

### 16.2 截图角标

页面右下角固定角标：

```text
非正式学术凭证 / Not an academic certificate
```

或者：

```text
截图可能缺失上下文，请以原页面说明为准
```

第二种适合社区入口；第一种适合公开文稿页和 Release Card。

### 16.3 分享卡片

Open Graph / Twitter Card / 小红书式分享图必须显示：

- B.A.I.T. logo。
- 文稿标题。
- `Fictional community manuscript` 标签。
- `Not journal publication` 角标。

### 16.4 禁止误导性分享标题

分享标题不得生成：

- “某某论文发表”。
- “某某理论被收录”。
- “B.A.I.T. 接受某某研究”。
- “国际期刊确认某某理论”。

---

## 17. PDF 与打印页规则

### 17.1 PDF 首页

PDF 首页必须显示：

```text
B.A.I.T. Community Manuscript
Fictional / Speculative / Community-edited
Not a real journal publication, certificate, or academic endorsement.
```

中文：

```text
B.A.I.T. 社区虚构文稿
非现实期刊发表，非学术认证，非机构背书。
```

### 17.2 PDF 页脚

每页页脚：

```text
B.A.I.T. fictional community manuscript · Not a journal publication · DIO:B.A.I.T.2026.0001
```

### 17.3 PDF 元数据

PDF 元数据：

```text
Subject: FICTIONAL COMMUNITY MANUSCRIPT - NOT REAL JOURNAL PUBLICATION
Keywords: fictional, parody, community manuscript, not peer-reviewed, not certificate
```

### 17.4 打印样式

打印页必须保留：

- 页眉短披露。
- 页脚短披露。
- 斜向浅水印。
- Source Subject 未授权未背书说明。

---

## 18. Release Card：替代证书/奖状

v1-v4 中的证书和奖状需要彻底改造。

### 18.1 禁止名称

不得使用：

- Certificate
- Acceptance Letter
- Publication Certificate
- Indexing Certificate
- Certification ID
- Acceptance ID
- 录用证明
- 收录证明
- 认证编号

### 18.2 推荐名称

可使用：

- Fictional Manuscript Card
- Community Release Card
- Archive Display Sheet
- R.E.E.F. Release Sheet
- B.A.I.T. Display Card
- 社区展示卡
- 虚构文稿发布卡

### 18.3 Release Card 固定文案

英文：

> This card is a fictional community display item. It is not proof of academic publication, peer review, indexing, certification, employment qualification, or institutional endorsement.

中文：

> 本卡片为社区虚构文稿展示物，不是学术发表、同行评审、收录、认证、任职资格或机构背书的证明。

### 18.4 QR 码规则

QR 码直接跳转到说明页，说明页第一屏显示：

> B.A.I.T. 是社区虚构文稿工坊，不是真实期刊或认证机构。

不得要求输入验证码后才显示真相。

### 18.5 Release Card 编号

可以有 DIO 编号，但必须解释为站内虚构档案编号：

> DIO is an internal fictional archive identifier, not a DOI and not an academic registration number.

---

## 19. 移动端与电脑端一致性原则

### 19.1 保留差异

手机端和电脑端可以在功能上不同：

| 功能 | 手机端 | 电脑端 |
|---|---|---|
| 写作 | 分步向导 | 全文编辑器 |
| 引用 | 简化输入 | 引用管理器 |
| 图谱 | 简化 | 完整交互 |
| 终端 | 只读或触摸优化 | 完整键盘交互 |
| 审核记录 | 摘要 | 完整详情 |

### 19.2 不得差异

手机端和电脑端不能在以下方面不同：

- 是否显示虚构标签。
- 是否显示非期刊说明。
- 是否显示截图水印。
- 是否显示 Source Subject 未授权未背书说明。
- 是否保留 PDF 水印。

### 19.3 移动端截图优化

移动端容易被截图传播，因此移动端标题区必须包含短标签：

```text
Community Manuscript · Fictional · Not Journal Publication
```

中文可简写为：

```text
社区虚构文稿 · 非现实期刊发表
```

---

# 第五部分：审核流程与社区治理

## 20. CAST / HOOK / CATCH / RELEASE v5 解释

v5 保留世界观术语，但每个术语旁边必须有现实解释。

| 术语 | v5 现实解释 | 不得解释为 |
|---|---|---|
| CAST | Submission Intake / 投稿接收 | 正式投稿到真实期刊 |
| HOOK | Community Editorial Screening / 社区编辑初筛 | 真实同行评审中 |
| CATCH | Style & Safety Review / 风格与安全审核 | 学术有效性确认 |
| RELEASE | Archive Publication / 档案展示发布 | 真实期刊发表或收录 |

### 20.1 状态显示示例

推荐：

```text
HOOK — Community Editorial Screening
The manuscript is being reviewed for style, safety, source context, and fictional-world consistency.
```

不推荐：

```text
Under peer review by expert panel.
```

---

## 21. 社区编辑审核标准

社区审核内容包括：

1. **格式完整性**：标题、摘要、关键词、正文、参考文献是否完整。
2. **可读性**：文本是否通顺、结构是否清晰。
3. **安全边界**：是否涉及禁区内容。
4. **真实人物风险**：是否可能造成人身攻击、骚扰或误认。
5. **来源清晰度**：公开材料来源是否记录，是否符合许可。
6. **世界观一致性**：是否符合 R.E.E.F. / C.O.S.M.O.S. 设定。
7. **ARG 适配性**：线索是否有趣且不承担披露义务。
8. **导出安全性**：截图、PDF、分享卡片是否有水印和上下文。

### 21.1 审核结论

审核结论使用：

- Ready for Archive
- Needs Revision
- Safety Hold
- Source Clarification Required
- Rejected for Risk

不得使用：

- Accepted for publication
- Peer-reviewed accepted
- Indexed
- Certified

---

## 22. 社区公约硬规则

### 22.1 反骚扰规则

社区成员不得：

1. 主动联系真实人物本人、家属、同事或社交账号。
2. 在其评论区、私信、直播间、贴吧、知乎、B站、抖音、快手等平台提及 B.A.I.T. 内容。
3. 声称“你的研究被我们发表/整理/收录/认证”。
4. 伪造“某某窃取你成果获奖/发表/拿诺奖”。
5. 引导真实人物点击站内页面以制造反应。
6. 组织围观、嘲笑、二创羞辱或转发攻击。
7. 人肉搜索、补充隐私、挖掘家庭和职业细节。

### 22.2 创作规则

社区创作必须：

- 对事不对人。
- 只评论公开理论文本和公开言论。
- 避免生平细节化。
- 避免侮辱性标签。
- 避免激化现实冲突。
- 保留更正和下架通道。

### 22.3 署名规则

- 站内作者必须是虚构作者、社区笔名或自愿投稿者。
- 真实人物不得作为作者署名。
- Source Subject 不得出现在作者栏。

---

## 23. 违规处理与 Abuse Response

### 23.1 违规等级

| 等级 | 行为 | 处理 |
|---|---|---|
| Minor | 轻微用词不当、格式错误 | 要求修改 |
| Moderate | 暗示真实人物参与或背书 | 退回、记录警告 |
| Major | 主动联系真实人物或评论区挑衅 | 删除内容、封禁账号 |
| Critical | 造成现实骚扰、诽谤、危险行为 | 下架相关内容、公开澄清、必要时保留证据 |

### 23.2 Abuse Response 文件

仓库必须有 `ABUSE_RESPONSE.md`，包括：

- 如何举报。
- 维护者响应时限。
- 如何临时下架。
- 如何判断骚扰。
- 如何处理站外冒充者。
- 如何发布澄清。

### 23.3 站外冒充者声明

固定声明：

> 任何在站外声称代表 B.A.I.T. 联系现实人物、索要费用、要求互动、制造挑衅或引导围观的行为，均不代表 B.A.I.T. 社区。请截图并提交 Abuse Report。

---

## 24. 投诉、下架与更正机制

### 24.1 快速下架原则

以下情况应先下架再讨论：

- 真实人物本人或代理人提出异议。
- 内容被用于站外骚扰。
- 页面被截图误用为真实发表证明。
- 社区成员违反外部联系禁令。
- 内容涉及危险实验或违法风险。

### 24.2 更正流程

1. 收到投诉。
2. 24-72 小时内临时处理。
3. 维护者会审。
4. 决定删除、改写、保留或加注。
5. 记录到 takedown log。

### 24.3 Takedown 页面

`TAKEDOWN.md` 应包含：

- 联系方式。
- 需要提供的信息。
- 处理时限。
- 内容删除标准。
- 误用截图处理建议。

---

# 第六部分：世界观、ARG 与沉浸体验

## 25. R.E.E.F. 多宇宙架构保留方案

R.E.E.F. 仍是主站宇宙，用于容纳不同虚构理论、文稿和异常档案。

### 25.1 宇宙结构

每个宇宙包含：

- 基础公理。
- 衍生理论。
- 虚构人物。
- 术语词典。
- 文稿列表。
- 异常档案。
- 终端会话。
- 与其他宇宙的关系。

### 25.2 与真实人物的关系

真实人物不能成为宇宙角色本身。可以存在“公开材料启发的虚构宇宙”，但必须：

- 更换人物姓名。
- 去除隐私细节。
- 保留 Source Context 分离。
- 在社区入口说明灵感来自公开材料，不表示本人参与。

---

## 26. SCP / Backrooms 风格档案层

档案层使用异常分类、分级标签和终端记录增强叙事。

### 26.1 分级对象

分级只能作用于：

- 文稿荒诞程度。
- 世界观偏移程度。
- ARG 深度。
- 文本风险。
- 档案损坏程度。

分级不能作用于：

- 真实人物智力。
- 真实人物价值。
- 真实人物危害性。
- 真实人物人格。

### 26.2 档案标签示例

```text
ANOMALY CLASSIFICATION
Δ-2 SIGNIFICANT DEVIATION
Object of classification: manuscript logic and fictional-world deviation.
This classification does not evaluate any real person.
```

---

## 27. ARG 线索边界

ARG 可以隐藏：

- 世界观秘密。
- DIO 编号规律。
- 终端密码。
- 宇宙合并线索。
- 虚构人物关系。
- 深渊入口。

ARG 不得隐藏：

- 平台是虚构项目。
- 内容不是现实期刊发表。
- 真实人物不是作者。
- 社区审核不是同行评审。
- Release Card 不是证书。

### 27.1 反翻译策略调整

v5 不使用反翻译技术隐藏披露。可以使用 SVG、Unicode、零宽字符作为 ARG 谜题，但不能用于免责声明、来源说明、未授权未背书说明。

---

## 28. Paper 写作体验与沉浸式流程

### 28.1 写作向导

提供完整 paper 写作体验：

1. 选择文稿类型。
2. 填写题目。
3. 生成摘要结构。
4. 填写关键词。
5. 写引言。
6. 写方法或理论框架。
7. 写结果或核心论证。
8. 写讨论。
9. 添加参考文献。
10. 生成社区编辑反馈。
11. 修订。
12. 导出 PDF / Release Card。

### 28.2 社区反馈

反馈使用以下类型：

- Style Feedback
- Structure Feedback
- Source Clarity Feedback
- Safety Feedback
- Fictional Consistency Feedback
- ARG Integration Feedback

### 28.3 沉浸语气

允许使用正式学术语气，但需避免现实背书。例如：

推荐：

> The manuscript has passed community style and safety screening for archive display.

不推荐：

> The manuscript has been accepted after peer review.

---

# 第七部分：法律、运营与路线图

## 29. 跨法域风险框架

> 本节为产品风险框架，不构成法律意见。公开上线前应咨询熟悉中国互联网合规、美国平台托管规则、版权和名誉权问题的专业人士。

### 29.1 中国大陆相关风险

重点风险：

- 名誉权、肖像权、隐私权。
- 网络暴力、引战、骚扰。
- 伪科学内容被误信。
- 危险实验传播。
- 用户生成内容责任。
- 平台被误认为组织性欺骗。

缓解：

- 不主动联系真实人物。
- 不把真实人物作为作者。
- 明确反网暴公约。
- 快速下架机制。
- 不发布危险实验指导。
- 不收费、不广告、不捐赠。

### 29.2 美国 / GitHub Pages 相关风险

重点风险：

- DMCA / 版权投诉。
- 平台 ToS 违规。
- 诽谤和骚扰。
- 冒充机构。

缓解：

- 只引用公开材料。
- 遵守许可证。
- 保留 Source Context。
- 不使用真实机构背书。
- 保留 takedown 流程。

### 29.3 欧盟相关风险

重点风险：

- GDPR 个人数据。
- 人格权。
- 被遗忘权请求。

缓解：

- 最小化真实人物数据。
- 不收集非必要个人信息。
- 提供删除请求通道。

---

## 30. 必须新增的政策文件

v5 仓库根目录必须包含：

| 文件 | 功能 |
|---|---|
| `README.md` | 项目性质总说明 |
| `DISCLAIMER.md` | 免责声明 |
| `EDITORIAL_POLICY.md` | 社区编辑审核原则 |
| `CODE_OF_CONDUCT.md` | 社区行为准则 |
| `ABUSE_RESPONSE.md` | 反骚扰与违规响应 |
| `TAKEDOWN.md` | 下架和更正机制 |
| `CONTENT_PROVENANCE.md` | 来源、许可与真实人物规则 |
| `PRIVACY.md` | 隐私与数据最小化 |
| `TERMS.md` | 使用条款 |
| `CONTRIBUTING.md` | 投稿和 PR 规则 |

### 30.1 README 顶部固定声明

```markdown
> B.A.I.T. is a fictional community manuscript workshop and speculative archive.
> It is not a real academic journal, preprint server, indexing service, certification body, or institutional publisher.
```

中文：

```markdown
> B.A.I.T. 是社区虚构文稿工坊与推想型档案项目，
> 不是真实学术期刊、预印本服务器、收录机构、认证机构或现实出版机构。
```

---

## 31. 技术实现建议

### 31.1 仓库结构

```text
bait-core/
  content/
    manuscripts/
    source-context/
    cosmos/
    archive-records/
    terminal/
    release-cards/
  data/
    content_index.json
    source_subjects.json
    risk_register.json
    takedown_log.json
    grade_map.json
  scripts/
    build.py
    content_validator.py
    source_subject_checker.py
    disclosure_checker.py
    screenshot_watermark_checker.py
    pdf_generator.py
    release_card_generator.py
    backlink_generator.py
  policies/
    DISCLAIMER.md
    EDITORIAL_POLICY.md
    CODE_OF_CONDUCT.md
    ABUSE_RESPONSE.md
    TAKEDOWN.md
    CONTENT_PROVENANCE.md
    PRIVACY.md
```

### 31.2 构建检查

发布前自动检查：

- 是否有 `fictional_disclosure: true`。
- 是否有禁用词。
- 是否涉及真实人物。
- Source Subject 是否错误显示为作者。
- 是否存在截图水印。
- PDF 是否带每页水印。
- Release Card 是否无证书措辞。
- 是否有 takedown 联系方式。

### 31.3 禁用词检查

`content_validator.py` 应检查：

- accepted for publication
- peer-reviewed journal
- certificate
- indexed by
- official recognition
- JCR
- CAS 一区
- SCI 收录
- DOI registered

允许这些词出现在政策文档的“禁用词说明”里，但不得出现在公开文稿作为功能描述。

### 31.4 截图水印实现

CSS 示例：

```css
.manuscript-page::before {
  content: "社区虚构文稿 / Community Fictional Manuscript";
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 10;
  opacity: 0.055;
  font-size: clamp(24px, 5vw, 72px);
  transform: rotate(-24deg);
  display: grid;
  place-items: center;
  white-space: nowrap;
}

.screenshot-corner-mark {
  position: fixed;
  right: 12px;
  bottom: 12px;
  z-index: 11;
  opacity: 0.78;
  font-size: 12px;
}
```

此样式仅为说明，实际实现需兼顾移动端、深色模式、打印样式和 PDF 渲染。

---

## 32. 实施路线图 v5

### Phase 0：安全文档与架构定版

- [ ] 完成 v5 设计文档审查。
- [ ] 明确不可突破边界。
- [ ] 编写政策文件。
- [ ] 编写固定文案表。
- [ ] 完成法律咨询问题清单。

### Phase 1：静态站点骨架

- [ ] 建立公开入口。
- [ ] 建立社区入口。
- [ ] 建立档案入口。
- [ ] 建立管理入口原型。
- [ ] 实现短披露组件。
- [ ] 实现页脚完整披露。

### Phase 2：内容模型与审核工具

- [ ] 实现 Front Matter v5。
- [ ] 实现 Source Subject 检查。
- [ ] 实现禁用词检查。
- [ ] 实现截图水印检查。
- [ ] 实现 PDF 水印生成。
- [ ] 实现 Release Card 生成。

### Phase 3：社区治理上线

- [ ] 发布 CODE_OF_CONDUCT。
- [ ] 发布 ABUSE_RESPONSE。
- [ ] 发布 TAKEDOWN。
- [ ] 建立举报入口。
- [ ] 建立违规处理日志。

### Phase 4：世界观与写作体验

- [ ] 写作向导。
- [ ] 社区编辑反馈。
- [ ] R.E.E.F. 宇宙索引。
- [ ] 档案分级。
- [ ] 终端模拟。
- [ ] ARG 成就系统。

### Phase 5：受控公开测试

- [ ] 只用纯虚构内容测试。
- [ ] 不涉及真实人物。
- [ ] 检查截图传播效果。
- [ ] 检查手机端披露。
- [ ] 检查 PDF 和分享卡片。
- [ ] 收集外部反馈后再考虑 Source Subject 功能。

---

# 附录：推荐固定文案

## A. 首页短文案

```text
B.A.I.T. 是社区虚构文稿工坊与推想型学术档案项目。
它不是真实学术期刊、预印本服务器、收录机构或认证机构。
```

## B. 文章页短标签

```text
社区虚构文稿 · 非现实期刊发表
Fictional community manuscript · Not a journal publication
```

## C. Source Subject 卡片

```text
公开材料背景 / Public Context

本栏所列外部人物或材料仅用于背景说明。
该人物不是本文作者，未参与投稿，未授权，未背书。
本文为社区虚构评论/整理，不构成现实学术发表或认证。
```

## D. 审核说明

```text
本文仅经过社区编辑审核。审核范围包括格式、可读性、内容边界、来源说明、世界观一致性与导出安全性；不构成现实学术同行评审。
```

## E. Release Card 说明

```text
本卡片为社区虚构文稿展示物，不是学术发表、同行评审、收录、认证、任职资格或机构背书的证明。
```

## F. 站外冒充声明

```text
任何在站外声称代表 B.A.I.T. 联系现实人物、索要费用、要求互动、制造挑衅或引导围观的行为，均不代表 B.A.I.T. 社区。
```

## G. 社区禁令短版

```text
禁止联系真实人物本人或其社媒账号。
禁止声称其研究被发表、收录、认证或获奖。
禁止伪造挑衅性消息、组织围观或制造网络暴力。
```

---

# 附录：术语表

| 术语 | v5 含义 |
|---|---|
| B.A.I.T. | Bureau of Advanced Interdisciplinary Theories，虚构学术文稿工坊 |
| R.E.E.F. | Research Encyclopedia of Emerging Frontiers，主站虚构宇宙 |
| H.A.D.A.L. | Hidden Archive of Dimensional Anomalies & Leaks，深层档案入口 |
| D.I.O. | Document Identity Ontology，站内虚构档案编号，不是 DOI |
| B.I. | Bait Index / Bibliometric-style Index，站内文本风格评分，不是学术指标 |
| CAST | Submission Intake，投稿接收阶段 |
| HOOK | Community Editorial Screening，社区编辑初筛 |
| CATCH | Style & Safety Review，风格与安全审核 |
| RELEASE | Archive Publication，档案展示发布 |
| Source Subject | 公开材料背景对象，不是作者 |
| Article Author | 站内虚构作者、社区笔名或自愿投稿者 |
| Release Card | 虚构文稿展示卡，不是证书 |
| Community Editorial Review | 社区编辑审核，不是现实同行评审 |
| Fictional Manuscript | 社区虚构文稿 |
| Speculative Commentary | 推想型评论 |
| Public Context | 外部公开背景资料 |

---

## v5 结语

v5 的核心不是削弱 B.A.I.T. 的世界观，而是让世界观从“可能误导现实人物的伪装系统”转向“安全可持续的虚构学术创作系统”。

平台仍然可以像 paper，仍然可以有审阅流程，仍然可以有虚构机构、宇宙、档案、终端、深渊、成就和 ARG；但它不能让真实人物被包装成作者，不能让社区成员借站点名义去挑衅，不能让截图或 PDF 被当成现实学术凭证。

最终目标是：

> 让正常用户能发现这是一个 fake paper / fictional manuscript 项目；让社区用户能共创一个复杂、好玩的多宇宙档案；让被提及的现实人物不被进一步骚扰；让平台在国内外法律和伦理风险下尽可能稳妥地运行。

*本文档为 B.A.I.T. v5 安全优先总设计文档。法律相关内容仅为风险框架，不构成法律意见。公开上线前应进行专业法律咨询和小范围受控测试。*
