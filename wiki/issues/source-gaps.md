---
schema_version: "1.0.0"
id: "issue-source-gaps"
type: "issue"
title: "來源覆蓋與缺口"
summary: "76 個來源均已處理：56 全文、20 僅線索；FB 歷史、外部全文與圖片仍缺。"
language: "zh-TW"
status: "needs_review"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-045", "official-news-056", "official-news-060", "facebook-pfbid0AMmGpcRMbRVaJt5HDHR6Ap49giTEcmR8sXYGvPregZ75e8PrgB4LLGuPNoL3Ap1Vl", "external-cio-109792", "official-news-002", "official-news-003", "official-news-016", "official-news-031", "official-news-043", "external-679fec63ebbe"]
related: ["synthesis-pilot-findings", "event-metaage-partnership", "synthesis-messaging-timeline", "issue-translation-differences"]
---

# 來源覆蓋與缺口


## 覆蓋

目前 catalog 可盤點 60 個官網文章 ID、1 篇 FB 貼文、15 個外部來源網址，共 76 個來源單位；三語是同一官網來源的版本（決策 Q8 以繁中為準）。

- pilot-001（2026-11-01）：官網 45／56／60、FB 一篇、CIO 109792；見 [首次整合發現](../syntheses/pilot-findings.md)。
- ingest-002（2026-11-01）：其餘 57 篇官網與 14 個外部來源。
- 合計 56 個全文來源已整合；20 個只記為 reference_only：14 個外部來源＋CIO（只有官網清單摘要或先前生成摘要），以及 5 篇正文只有圖片或一兩句的官網文章（[news/2](../sources/official-news-002.md)、[news/3](../sources/official-news-003.md)、[news/16](../sources/official-news-016.md)、[news/31](../sources/official-news-031.md)、[news/43](../sources/official-news-043.md)）。

## 缺漏

- FB 歷史 feed 未收齊，單篇只有相對日期；見 [FB 來源頁](../sources/facebook-threat-intelligence-update.md)。
- 外部全文尚缺；[CIO 來源頁](../sources/external-cio-109792.md) 只保留先前摘要。
- 圖片／附件未下載及 OCR；正文不可臆測圖內數字。多篇條款、版本表與活動辦法只在圖片中（例如 news/31 升版公告、news/42／43 優惠、news/59 受影響版本表）。
- 2024 年以前與下架內容不在此次公開清單中，不能據此斷言公司沒有更早文章。

## 下一步

補齊上述缺口需要使用者提供 FB 匯出、外部原稿或圖片 OCR 授權；新資料以新 raw 快照建立後重新 Ingest。各批結果見 [訊息時間軸](../syntheses/messaging-timeline.md) 與 [翻譯差異](translation-differences.md)。
