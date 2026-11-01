---
schema_version: "1.0.0"
id: "issue-threat-intel-figures"
type: "issue"
title: "待確認：威脅情資更新頻率與數量"
summary: "各篇更新頻率（每小時／每日／每 3 分鐘）、情資筆數與攔截率說法不一致。"
language: "zh-TW"
status: "needs_review"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-006", "official-news-012", "official-news-013", "official-news-018", "official-news-020", "official-news-024", "official-news-034", "official-news-041", "official-news-046", "official-news-047", "official-news-048", "official-news-054", "official-news-055", "official-news-058", "external-a6b65c2e9d77"]
related: ["entity-defensetrust", "entity-cloud-platforms", "concept-threat-intelligence"]
---

# 待確認：威脅情資更新頻率與數量

## 更新頻率

| 說法 | 來源（API 日期） |
|---|---|
| 每小時更新 | [news/6](../sources/official-news-006.md)（2024-07）；DefenseCloud Pro 套餐 [news/46](../sources/official-news-046.md)（2026-04） |
| 每日更新 | [news/13](../sources/official-news-013.md)（2024-11）；[news/41](../sources/official-news-041.md)（2026-02）、[news/54](../sources/official-news-054.md)（2026-06）「每天更新、業界最快」 |
| 每分／日 | [news/24](../sources/official-news-024.md)（2025-05） |
| 每 3 分鐘 | [news/34](../sources/official-news-034.md)（2025-11）；[news/47](../sources/official-news-047.md)、[news/48](../sources/official-news-048.md)（2026-05）「即時 3 分鐘」；[news/55](../sources/official-news-055.md)（2026-07）「最快每 3 分鐘」 |

## 數量與成效

| 說法 | 來源 |
|---|---|
| 全球情資上千萬筆 | [news/6](../sources/official-news-006.md) |
| 可辨識破億個 IP（英文 over a billion、日文 10 億件以上） | [news/12](../sources/official-news-012.md) |
| 比對約 600 萬筆 OSINT 與第三方情資，提供 13 類約 100 萬筆；可同時比對 100＋萬筆 | [news/20](../sources/official-news-020.md)、[媒體同稿](../sources/external-a6b65c2e9d77.md) |
| 約百萬筆 | [news/24](../sources/official-news-024.md) |
| 每 3 分鐘更新超過 120 萬筆 | [news/34](../sources/official-news-034.md) |
| 涵蓋 224 個國家（與地區） | [news/46](../sources/official-news-046.md)、[news/54](../sources/official-news-054.md)、[news/55](../sources/official-news-055.md) |
| 攔截超過 80% 已知惡意網站 | [news/18](../sources/official-news-018.md)、[news/20](../sources/official-news-020.md)、[news/41](../sources/official-news-041.md)、[news/54](../sources/official-news-054.md) |
| 零誤判／誤報率近乎零 | [news/13](../sources/official-news-013.md)、[news/18](../sources/official-news-018.md)、[news/41](../sources/official-news-041.md)、[news/54](../sources/official-news-054.md) |

## 判斷與處置

這些數字可能對應不同產品、方案、資料層（全量情資、分類名單、比對容量）或不同年份，也可能只是文案差異；來源沒有說明。撰稿不得任選一個當現況，須由產品確認現行數字、口徑與適用方案，並標明時間。[news/58](../sources/official-news-058.md) 完全不用數字、只講流程與日誌，是較安全的寫法。相關頁：[DefenseTrust](../entities/defensetrust.md)、[DefenseCloud](../entities/cloud-platforms.md)。
