---
schema_version: "1.0.0"
id: "external-a6b65c2e9d77"
type: "source"
title: "資安人轉載：DefenseTrust 從源頭偵測阻斷"
summary: "資安人科技網刊出官網 news/20 同稿，摘要含 Inline 部署與 100+ 萬筆比對說法。"
language: "zh-TW"
status: "reference_only"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["external-a6b65c2e9d77"]
related: ["entity-defensetrust", "concept-ngfw-complement", "concept-threat-intelligence"]
---

# 資安人轉載：DefenseTrust 從源頭偵測阻斷

## 來源與時間

[外部原頁](https://www.informationsecurity.com.tw/article/article_detail.aspx?aid=11798)，媒體：資安人科技網。[官網媒體清單](../../raw/official/api/news-links.json) `/data/11`：官網維護的標題、媒體名、`newsDate`（2025-04-09）與摘要；無媒體發布日及更新時間。`newsDate` 只是官網清單列出日期，不一定是媒體發布日。

## 內容摘要

清單摘要稱 UGUARD Defense Trust 採連網（Inline）部署，從源頭協助企業進行流量檢測，並以「全新開源資料庫架構（Non-SQL Database）」加快威脅情資查詢比對（可同時比對 100＋萬筆名單），「徹底防堵」惡意連網及頻寬浪費風險。此段與官網 [official-news-020](official-news-020.md) 內文相同；媒體標題取用 news/20 開頭副標。與 iThome 版 [external-8ba4960a7e70](external-8ba4960a7e70.md) 同稿。

## 時效與限制

- 本頁依據只有官網維護的媒體清單（標題、媒體名、`newsDate` 與截斷摘要），沒有媒體原頁全文；不能重建引言、精確條件或完整報導，也不確認媒體實際發布日。
- `newsDate` 是官網清單列出的日期，與媒體發布日、官網文章日期分開記錄。
- 清單圖片未下載、未 OCR，不推測圖內內容。
- 官網 news/20 `date` 為 2025-04-08；清單 `newsDate` 為 2025-04-09。
- 「100＋萬筆」「徹底防堵」為來源說法，沒有測試條件或版本，不可寫成保證。

## 原文瑕疵

- 「開源資料庫架構（Non-SQL Database）」用語沿用官網原文；一般稱 NoSQL，且「開源」與資料庫類型的關係未說明，撰稿前宜確認。
- 「Defense Trust」空格寫法與官網不一致。

## 整合去向

[DefenseTrust](../entities/defensetrust.md)、[補強 NGFW／EDR](../concepts/ngfw-complement.md)、[威脅情資](../concepts/threat-intelligence.md)。本頁為 reference_only，取得授權全文後應建立新 raw 快照並重新 Ingest。
