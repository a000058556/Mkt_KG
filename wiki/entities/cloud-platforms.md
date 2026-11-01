---
schema_version: "1.0.0"
id: "entity-cloud-platforms"
type: "entity"
title: "DefenseCloud 與 AgileCloud"
summary: "DefenseCloud 情資雲與訂閱方案、AgileCloud 雲端監控的來源說法；數字口徑待確認。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-045", "official-news-017", "official-news-018", "official-news-020", "official-news-041", "official-news-046", "official-news-048", "official-news-054", "official-news-055", "external-37c35327340f", "external-b7bcc1e07edf"]
related: ["entity-uguard", "concept-threat-intelligence", "entity-defensetrust", "issue-threat-intel-figures", "event-computex-2026"]
---

# DefenseCloud 與 AgileCloud


## DefenseCloud

- 角色：UGUARD 自建情資雲與獵捕系統，以蜜罐與欺敵技術誘導攻擊者、蒐集情資，整合開源與第三方情資後匯入 [DefenseTrust](defensetrust.md)（[news/17](../sources/official-news-017.md)、[news/18](../sources/official-news-018.md)、[news/20](../sources/official-news-020.md)）。[news/41](../sources/official-news-041.md)、[news/46](../sources/official-news-046.md) 稱其為 SaaS 威脅情資服務平台。
- 訂閱方案（[news/46](../sources/official-news-046.md)，2026-04）：個人／小型企業「查詢月訂閱制」Pro 套餐（稱每小時更新）；企業版 Enterprise_Custom 完全客製化 TI 雲端服務、「依需求提供無限制資料量」，洽業務。媒體同稿見 [iThome PR](../sources/external-37c35327340f.md)。
- 服務形式（[news/54](../sources/official-news-054.md)，2026-06）：全球情資即時查詢、結合 DefenseTrust、訂閱制情資服務、情資買斷／年度服務；媒體以「發表 DefenseCloud 與 Defense Trust 整合方案」報導，見 [資安人](../sources/external-b7bcc1e07edf.md)。
- 覆蓋：「224 個國家（與地區）」（[news/46](../sources/official-news-046.md)、[news/54](../sources/official-news-054.md)、[news/55](../sources/official-news-055.md)）。經使用者確認，情資最晚每小時更新，DefenseTrust 每 3 分鐘請求一次（[澄清](../sources/human-2026-11-01-002.md)）；最新情資保持在百萬筆等級（[確認](../sources/human-2026-11-01-003.md)）。224 國覆蓋已確認（[確認](../sources/human-2026-11-01-005.md)），見 [情資數字](../issues/threat-intel-figures.md)。

## AgileCloud

[合作公告](../sources/official-news-045.md) 的 Jason Yen 引言把 AgileCloud 描述為雲端管理平台；[news/48](../sources/official-news-048.md)（COMPUTEX 2026）稱其為 AI 驅動的雲端監控平台，提供跨據點雲端報表與硬體異常智慧告警。見 [COMPUTEX 2026](../events/computex-2026.md)。

## 證據邊界

方案價格、現行套餐內容、資料量口徑與設備相容性未在來源中說明；這些是時間點的來源說法，撰稿前需產品確認。目前兩個平台仍共用本頁，資料增加後可拆頁並保留別名導向。關聯：[UGUARD](uguard.md)、[威脅情資](../concepts/threat-intelligence.md)。
