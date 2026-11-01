# UGUARD 行銷知識庫

先從產品、議題或寫作頁閱讀；需要查證時沿來源頁追溯 raw。頁面是來源化知識，不代表現行宣稱已核准。

來源登錄 76 筆：全文已 Ingest 4、線索已登記 1、待處理 71。

目前進度：[pilot 執行紀錄](schema/ingest-runs.json)；[首次整合發現](wiki/syntheses/pilot-findings.md)。

[Agent 規範](AGENTS.md) · [Schema](schema/SCHEMA.md) · [流程](docs/WORKFLOWS.md) · [操作日誌](log.md) · [首次報告](reports/2026-11-01-ingest-pilot-001.md)

## 公司、夥伴與產品

- [AgileLink](wiki/entities/agilelink.md) — 整合多 WAN 與策略路由的歷史產品敘述，與修補狀態分層保存。（source_reported）
- [DefenseCloud 與 AgileCloud](wiki/entities/cloud-platforms.md) — 先保存合作公告中的兩項雲端平台定位，等待更多產品來源。（source_reported）
- [DefenseTrust](wiki/entities/defensetrust.md) — 區分情資比對、策略阻擋與觀察紀錄，避免擴大為全威脅保證。（source_reported）
- [MetaAge 邁達特](wiki/entities/metaage.md) — 保留 2026 合作公告中的代理與在地服務角色。（source_reported）
- [TrafficShaper](wiki/entities/trafficshaper.md) — 此試行只支持產品出現在公告與舊機方案中，尚未整理功能全文。（source_reported）
- [UGUARD NETWORKS](wiki/entities/uguard.md) — 依試行來源整理公司定位與產品關聯，保留時間限制。（source_reported）

## 概念與受眾問題

- [威脅情資在行銷文章中的表達](wiki/concepts/threat-intelligence.md) — 以更新、比對、策略與日誌說明情資如何支援防護。（inferred）
- [WAN 韌性與多線路備援](wiki/concepts/wan-resilience.md) — 把線路多樣性、替代路徑與流量政策連到營運需求。（inferred）

## 合作與活動

- [UGUARD × 邁達特合作與相關活動](wiki/events/metaage-partnership.md) — 分離新聞稿日期、網站發布日期及優惠有效期限。（historical_only）

## 寫作知識

- [品牌語氣與用語觀察](wiki/writing/brand-observations.md) — 基於四篇完整文字來源的暫定寫作觀察，並非品牌正式手冊。（inferred）
- [合作新聞稿：角色、價值與引言](wiki/writing/partnership-announcement.md) — 區分合作事實、活動條款與主管引言的來源要求。（inferred）
- [產品文章：從痛點到機制與行動](wiki/writing/product-article.md) — 把受眾、痛點、證據與 CTA 分開填寫，保留發布前核對。（inferred）

## 綜合分析

- [首次 Ingest：可累積的行銷知識](wiki/syntheses/pilot-findings.md) — 以跨來源整合示範產品、合作、時效及文案觀察。（inferred）

## 來源摘要

- [CIO 109792：邁達特合作報導參考](wiki/sources/external-cio-109792.md) — 僅有先前生成摘要與 metadata，作為待補全文的媒體線索。（reference_only）
- [Facebook：威脅情資持續更新](wiki/sources/facebook-threat-intelligence-update.md) — 以痛點、機制、條列及 CTA 說明 DefenseTrust；發現 CTA 目的地不符。（source_reported）
- [UGUARD 與邁達特合作公告](wiki/sources/official-news-045.md) — 合作訊息、企業定位及促銷條款並存，須分離事件時間與有效期間。（source_reported）
- [AgileLink：多線路備援與策略路由](wiki/sources/official-news-056.md) — 由營運中斷痛點介紹多 WAN 整合及 PBR，未提供切換 SLA。（source_reported）
- [2026-10-30 修補進度快照](wiki/sources/official-news-060.md) — 保留公告當時三項產品的不同處理狀態，不作目前修補建議。（historical_only）

## 待確認與缺口

- [待確認：DefenseTrust CTA 指向 TrafficShaper](wiki/issues/facebook-cta.md) — 保留來源錯配，撰稿前確認應使用的產品連結。（needs_review）
- [待確認：主動防禦優惠的語言差異](wiki/issues/promotion-language.md) — 中文段落含 AgileLink 條件，英日對應段落只述 DefenseTrust。（needs_review）
- [來源覆蓋與缺口](wiki/issues/source-gaps.md) — 本次僅五個來源試行；其餘等待確認後 Ingest。（needs_review）
- [待確認：活動、修補進度與絕對化宣稱](wiki/issues/time-sensitive-claims.md) — 區分過期、歷史狀態及缺乏測試條件的宣傳措辭。（needs_review）
