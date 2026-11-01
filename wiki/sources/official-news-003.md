---
schema_version: "1.0.0"
id: "official-news-003"
type: "source"
title: "UGUARD NETWORKS 成立新加坡總公司（僅標題）"
summary: "三語皆無正文文字，只有標題與封面圖路徑，不能據此確認成立日期或細節。"
language: "zh-TW"
status: "reference_only"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-003"]
related: ["event-singapore-hq", "entity-uguard", "issue-source-gaps"]
---

# UGUARD NETWORKS 成立新加坡總公司（僅標題）

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/3)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/57`，`id=3`，分類「新加坡訊息」。

- API `date`：2024-03-15
- `created_at`／`updated_at`：皆為 2026-05-25T14:45:44Z
- 內文日期：無（正文為空）

## 內容狀態

繁中、英文（`news-en.json` `/data/57`）、日文（`news-jp.json` `/data/57`）正文都沒有文字，也沒有正文圖片；只有封面圖 `singapore-company.png`（未下載）。可讀資訊僅為標題「UGUARD NETWORKS 成立新加坡總公司」。

## 時效與限制

- API `date` 2024-03-15 只是文章欄位值，不能當作公司實際設立日期。
- 標題用詞不一致：繁中「新加坡總公司」，英文 "Established Singapore Company"，日文「シンガポール法人を設立」；英日未表達「總公司」。依決策 Q8 以繁中為準，但「總部」定位需人員或其他來源佐證，記為翻譯差異。
- 其他官網文章使用「新加坡商 UGUARD NETWORKS」稱呼（例如 [official-news-011](official-news-011.md)），可作旁證線索，但不等於設立細節。

## 整合去向

[新加坡總部](../events/singapore-hq.md)、[UGUARD](../entities/uguard.md)、[來源缺口](../issues/source-gaps.md)。
