# 贡献指南 / Contributing

## 欢迎

B.A.I.T. 是一个社区虚构学术文稿工坊。欢迎你参与虚构世界的共创。

## 重要：先读这个

在贡献之前，请确认你已阅读并理解：

- [DISCLAIMER.md](./DISCLAIMER.md) — 平台性质说明
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) — 社区行为准则

**B.A.I.T. 不是真实学术期刊。你提交的文稿不会被真实学术发表、收录、认证。**

## 投稿方式

### 方式一：GitHub PR（推荐）

1. Fork [bait-core](https://github.com/bohuyeshan/bait-core) 仓库
2. 在 `content/manuscripts/<年份>/<序号>/` 下创建 `index.md`
3. 按 Front Matter 规范填写元数据
4. 提交 PR，选择 `submission` 模板

### 方式二：GitHub Issue

如果你不熟悉 PR 流程，可以提交 Issue（选择 `submission` 模板），
社区编辑将帮你整理文稿。

## Front Matter 规范

```yaml
---
title: "你的文稿标题"
dio: "DIO:B.A.I.T.<YYYY>.<SEQ>"       # 站内虚构档案编号，非真实DOI
authors:
  - name: "笔名"                        # 虚构作者名，不映射真实人物
    affiliation: "虚构机构"
    fictional: true
format: interpretation                  # interpretation / document / terminal / wiki
source_type: community_fiction          # community_fiction / real_paper / voluntary_submission
grade: FG-2                             # FG-0~3 / TG-1~3
ddi: 3                                  # 维度偏移指数 0-5
cosmos: "COSMOS-MIX-001"               # 所属宇宙编号
date: 2025-06-16
review_status: CAST                     # CAST / HOOK / CATCH / RELEASE
canon_level: Semi-Canon                 # Canon / Semi-Canon / Apocrypha / Joke
keywords: ["关键词1", "关键词2"]
fictional_disclosure: true              # 必须为 true
---
```

## 内容要求

- 所有作者必须是虚构身份或自愿投稿笔名，不得映射真实人物
- 参考文献中混编真实论文引用（带 doi.org 链接），混编比例视分级而定
- 文稿必须包含虚构披露声明
- 不得涉及禁区内容（政治/医疗/金融/歧视/人身攻击）

## 自愿投稿者（真实人物主动参与）

如果你是真实人物，主动提交自己的内容，必须：
- 使用笔名作为作者
- 在 PR 或 Issue 中勾选提交声明
- 理解 B.A.I.T. 是虚构项目，不提供现实学术发表

## 许可

提交到 B.A.I.T. 的文稿内容默认以 [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可发布。
