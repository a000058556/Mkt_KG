---
schema_version: "1.0.0"
id: "issue-source-gaps"
type: "issue"
title: "來源覆蓋與缺口"
summary: "本次僅五個來源試行；其餘等待確認後 Ingest。"
language: "zh-TW"
status: "needs_review"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-045", "official-news-056", "official-news-060", "facebook-pfbid0AMmGpcRMbRVaJt5HDHR6Ap49giTEcmR8sXYGvPregZ75e8PrgB4LLGuPNoL3Ap1Vl", "external-cio-109792"]
related: ["synthesis-pilot-findings", "event-metaage-partnership"]
---

# 來源覆蓋與缺口


## 覆蓋

目前 catalog 可盤點 60 個官網文章 ID、1 篇 FB 貼文、15 個外部來源網址，共 76 個來源單位。三語是同一官網來源的版本，不多算來源數。

pilot-001 處理 5 個單位：官網 45／56／60、FB 一篇、CIO 109792。前四個有完整文字；CIO 僅記為 reference_only。其餘 71 個未 Ingest，雖存在 reading 檔，也不代表已整合成 Wiki。

## 缺漏

- FB 歷史 feed 未收齊，單篇只有相對日期；見 [FB 來源頁](../sources/facebook-threat-intelligence-update.md)。
- 外部全文尚缺；[CIO 來源頁](../sources/external-cio-109792.md) 只保留先前摘要。
- 圖片／附件未下載及 OCR；正文不可臆測圖內數字。
- 2024 年以前與下架內容不在此次公開清單中，不能據此斷言公司沒有更早文章。

## 下一步

等待使用者確認試行成果後，依來源登錄表處理其餘資料。每批完成都更新本頁、來源狀態、索引與 log；見 [首次整合發現](../syntheses/pilot-findings.md)。
