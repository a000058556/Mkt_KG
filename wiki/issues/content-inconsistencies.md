---
schema_version: "1.0.0"
id: "issue-content-inconsistencies"
type: "issue"
title: "待確認：公司資料與內文不一致"
summary: "主管職稱、公司設立、日期欄位、未說明的技術合作與原文瑕疵彙整。"
language: "zh-TW"
status: "needs_review"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-003", "official-news-011", "official-news-024", "official-news-028", "official-news-029", "official-news-030", "official-news-032", "official-news-039", "official-news-041", "official-news-044", "official-news-046", "official-news-048", "official-news-053", "official-news-054", "official-news-055", "official-news-057"]
related: ["entity-uguard", "event-singapore-hq", "event-shuoyu-partnership"]
---

# 待確認：公司資料與內文不一致

## 公司與人員

- Jason Yen 在 [news/11](../sources/official-news-011.md)、[news/24](../sources/official-news-024.md)、[news/29](../sources/official-news-029.md)、[news/48](../sources/official-news-048.md) 為「執行長」，[news/30](../sources/official-news-030.md) 圖說寫「營運總監」；[news/29](../sources/official-news-029.md) 另記 James Chang 為總經理，[news/30](../sources/official-news-030.md) 圖說只寫「台灣區總經理」未具名。
- 新加坡設立日：[news/3](../sources/official-news-003.md)（2024-03）「成立新加坡總公司」對 [news/32](../sources/official-news-032.md)（2025-09）「成立滿一周年」；[news/41](../sources/official-news-041.md)、[news/44](../sources/official-news-044.md) 簡介寫「於2026年成立台灣分公司」。見 [新加坡總部](../events/singapore-hq.md)。

## 未說明的說法

- [news/28](../sources/official-news-028.md)「結合 OpenAI 的先進技術」只出現一次，未說明產品或合作形式；需產品／法務確認後才能使用。

## 日期欄位

API `date` 不一定是首發日：多篇 `created_at` 為 2026-05-25（批次匯入），晚於 `date`；[news/53](../sources/official-news-053.md)、[news/55](../sources/official-news-055.md) 的 `created_at` 反而早於 `date`。媒體清單的日期也早於或晚於官網 `date`。撰稿引用日期時請寫明是哪個欄位。

## 原文瑕疵（保留於 raw）

- 錯字：[news/24](../sources/official-news-024.md)「X-Veiw」「UGUAR NETWORKS」；[news/32](../sources/official-news-032.md)「改善善」；[news/39](../sources/official-news-039.md)、[news/48](../sources/official-news-048.md)「作到」；[news/41](../sources/official-news-041.md)「敢備故障」；[news/46](../sources/official-news-046.md)「UGAURDN NETWORKS」；[news/39](../sources/official-news-039.md)、[news/56](../sources/official-news-056.md)「頻寬」應指寬頻。
- 連結：[news/54](../sources/official-news-054.md) 官網連結目標為 `\`；[news/57](../sources/official-news-057.md) 連結指到 `https://uguardnetworks.com/news/56/www.uguardnetworks.com`；多篇 LinkedIn 連結是管理後台路徑 `/admin/feed/posts/`；部分英日版連結帶 fbclid。
- 產品名寫法不一：Traffic Shaper／TrafficShaper、Defense Cloud／DefenseCloud、Defense Trust／DefenseTrust。知識頁以別名表統一，引用原文保留。

各來源頁的「原文瑕疵」段有完整清單；公司資料見 [UGUARD](../entities/uguard.md)，簽約活動見 [朔宇合作](../events/shuoyu-partnership.md)。
