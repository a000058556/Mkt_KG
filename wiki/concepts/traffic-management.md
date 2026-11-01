---
schema_version: "1.0.0"
id: "concept-traffic-management"
type: "concept"
title: "頻寬與應用流量管理"
summary: "把「網路變慢」從加頻寬轉為應用可視化與政策分級，連到 TrafficShaper。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-008", "official-news-035", "official-news-044", "official-news-057"]
related: ["entity-trafficshaper", "entity-agilelink", "writing-product-article"]
---

# 頻寬與應用流量管理

## 來源論點

- [news/44](../sources/official-news-044.md)（2026-03）：AI、SaaS（ChatGPT、M365、Zoom、Google Workspace、ERP）與遠距工作讓流量變複雜，症狀是視訊卡頓、ERP 變慢；增加頻寬未必能解決，需要流量可視化與管理。
- [news/35](../sources/official-news-035.md)（2025-12）：SaaS、雲端、視訊與 AI 讓流量問題變成關鍵服務保障、可視性與異常追蹤，只靠防火牆或升級頻寬難以因應。
- [news/57](../sources/official-news-057.md)（2026-09）提出政策分級範例：關鍵服務（ERP、VPN、CRM、視訊）優先；一般辦公（Web、Email、Office 365、Google Workspace）合理配置；非關鍵（YouTube、大檔下載、影音）限制或降低優先。
- 部署上，[news/8](../sources/official-news-008.md)、[news/35](../sources/official-news-035.md)、[news/57](../sources/official-news-057.md) 都區分 In-line（可做頻寬、QoS、政策）與 SPAN（不改架構、只做紀錄與報表）兩種模式。

## 撰稿用途

可用「網路變慢，真的只是頻寬不夠嗎？」的反問開場，接「先看懂流量」，再談政策分級與部署模式；產品關聯為 [TrafficShaper](../entities/trafficshaper.md)，[news/44](../sources/official-news-044.md) 也把 [AgileLink](../entities/agilelink.md) 一起列入。範例結構見 [產品文章](../writing/product-article.md)。來源未提供改善幅度數據，不要自行補數字。
