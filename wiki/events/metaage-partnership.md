---
schema_version: "1.0.0"
id: "event-metaage-partnership"
type: "event"
title: "UGUARD × 邁達特合作與相關活動"
summary: "分離新聞稿日期、網站發布日期及優惠有效期限。"
language: "zh-TW"
status: "historical_only"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-045", "external-cio-109792", "official-news-042", "official-news-043", "official-news-044", "external-52cb8621fccb", "external-339127206f46", "external-fb73abcbfef6", "human-2026-11-01-007", "official-featured-partners"]
related: ["entity-metaage", "entity-uguard", "issue-promotion-language", "issue-time-sensitive-claims", "concept-legacy-replacement", "entity-channel-partners"]
---

# UGUARD × 邁達特合作與相關活動


## 時間軸

| 日期 | 來源中的意義 |
|---|---|
| 2026-03-26 | 官網 news/45 內文新聞稿標示日期；不是已驗證的實際簽約日 |
| 2026-03-31 | CIO 摘要記錄中的媒體發布日期；未取得全文 |
| 2026-04-21 | 官網 news/45 API 的 `date` 欄位；不保證是網頁實際上線日 |
| 2026-05-25 | 官網 news/45 API 的 `created_at`，晚於 `date` 欄位 |
| 2026-09-15 | 官網 news/45 API 的更新日期 |
| 2026-10-31 | WAN 與主動防禦優惠的原訂截止日 |
| 2027-12-25 | 汰舊換新方案的原訂截止日 |

依據：[官網來源](../sources/official-news-045.md) 的 metadata、開頭及活動條款；[CIO 來源](../sources/external-cio-109792.md) 的 metadata。

## 相關公告與媒體

- [news/42](../sources/official-news-042.md)（2026-03-19）是「2026企業網路強化方案」獨立公告，文字與 news/45「企業資安升級專案啟動」段逐字相同，條款在圖片中；期限依 news/45 為 2026-10-31，已過期。
- [news/43](../sources/official-news-043.md)（2026-03-19）是「汰舊換新．升級方案」公告，條款在圖片中；見 [舊設備替代](../concepts/legacy-replacement.md)。
- [news/44](../sources/official-news-044.md)（2026-03-24）文末重述兩種優惠但沒寫期限，「主動防禦強化專案」只列 DefenseTrust，與 news/45 繁中版不同。
- 媒體：[iThome PR](../sources/external-52cb8621fccb.md)、[資安人](../sources/external-339127206f46.md) 為 UGUARD 版同稿；[iThome PR 邁達特版](../sources/external-fb73abcbfef6.md) 與 CIO 同為邁達特端稿件。媒體清單日期（03-27、03-31）早於官網 news/45 的 API `date`（04-21）。

## 可作歷史敘述的重點

公告將 UGUARD 的網路安全技術與邁達特在地通路／服務串聯為代理合作。可用於回顧合作里程碑，不能由歷史公告自行確定當前代理狀態。

## 活動使用限制

以 2026-11-01 為評估日，前兩項優惠已過原訂截止日；未取得延長證據。汰舊換新方案經 [使用者確認](../sources/human-2026-11-01-007.md)仍在辦理（原訂至 2027-12-25），條件依 news/45 描述。邁達特在 2026-11-01 仍列於 [官網夥伴清單](../entities/channel-partners.md)。中文促銷段落及產品說明段與英日版存在差異，見 [語言差異](../issues/promotion-language.md)。本頁未建立任何已核准的現行優惠。
