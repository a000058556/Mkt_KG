---
schema_version: "1.0.0"
id: "official-news-031"
type: "source"
title: "7 月 21 日 AgileLink 升版公告（僅圖片）"
summary: "三語正文皆只有一張圖片，無可讀文字；只能作為 2025-07 AgileLink 升版公告存在的線索。"
language: "zh-TW"
status: "reference_only"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-031"]
related: ["entity-agilelink", "issue-source-gaps"]
---

# 7 月 21 日 AgileLink 升版公告（僅圖片）

## 來源與時間

[官網原頁](https://www.uguardnetworks.com/news/31)；原始記錄：[繁中 API](../../raw/official/api/news-zh-TW.json) `/data/29`，`id=31`；英日對照 [英文 API](../../raw/official/api/news-en.json) `/data/29`、[日文 API](../../raw/official/api/news-jp.json) `/data/29`。

- API `date`：2025-07-21
- `created_at`／`updated_at`：皆 2026-05-25T14:45:44Z
- 標題日期「7月21日」（無年份）

## 來源狀態

- 繁中正文只有 `[IMG /static/uploads/newslist/news-agilelink-upgrade.png]`；英文（"July 21 AgileLink Version Upgrade Announcement"）與日文（「7月21日 AgileLink バージョンアップのお知らせ」）正文同樣只有這張圖片。
- 繁中摘要欄位為「產品開發部【AgileLink 升版公告】」，可知發布單位自稱產品開發部；英日摘要只重複標題。
- 圖片未下載／OCR：不知道版本號、新增功能、修正項目或影響範圍，不得推測。

## 能使用與不能確認的內容

只能說明：官網曾於 API date 2025-07-21 發布一則 AgileLink 升版公告。不能引用任何版本、功能或相容性內容。

## 待補資料

若要使用，需下載圖片存為 `raw/assets/official-news-031/` 並檢視／OCR 後重新 Ingest，或取得產品開發部的文字版 release note。見 [來源缺口](../issues/source-gaps.md)。

## 整合去向

[AgileLink](../entities/agilelink.md)（只作版本歷史線索）、[來源缺口](../issues/source-gaps.md)。
