---
schema_version: "1.0.0"
id: "entity-trafficshaper"
type: "entity"
title: "TrafficShaper"
summary: "Layer 7 應用辨識、頻寬政策與 In-line／SPAN 部署的來源說法；與 AgileShaper 關係待確認。"
language: "zh-TW"
status: "source_reported"
created: "2026-11-01"
updated: "2026-11-01"
sources: ["official-news-045", "official-news-060", "facebook-pfbid0AMmGpcRMbRVaJt5HDHR6Ap49giTEcmR8sXYGvPregZ75e8PrgB4LLGuPNoL3Ap1Vl", "official-news-008", "official-news-017", "official-news-024", "official-news-035", "official-news-044", "official-news-057"]
related: ["issue-facebook-cta", "issue-time-sensitive-claims", "concept-traffic-management", "entity-agileshaper", "entity-x-view"]
---

# TrafficShaper


## 來源支持的產品說法

- [news/35](../sources/official-news-035.md)（2025-12）：以 Layer 7 應用辨識與流量管理，掌握誰在何時使用哪些應用，並依使用者、群組、應用、網站類型分配與控管頻寬；儀表板呈現 L7 QoS 應用流量、上傳／下載趨勢、熱門服務、設備 CPU／記憶體／連線數、Top 10 Domain；可搭配使用者身分辨識與認證；支援硬體式與軟體式 Bypass。
- [news/57](../sources/official-news-057.md)（2026-09）：Layer 7 Application Identification 辨識應用、使用者／設備、Domain／Service 與上下行趨勢；Top Applications／Top Domains 視覺化、頻寬管理與關鍵服務優先。
- 部署模式：In-line 可做頻寬、QoS 與流量政策；SPAN 只複製流量做連線紀錄與報表，不改架構（[news/8](../sources/official-news-008.md)、[news/35](../sources/official-news-035.md)、[news/57](../sources/official-news-057.md)）。[news/8](../sources/official-news-008.md)（2024-08）以 tOS 稱呼系統，功能列 B/W-M、QoS、AAA、Behavior Mgt、Security、Reporting。
- 2025 年的產品線列有 Traffic Shaper（[news/17](../sources/official-news-017.md)、[news/24](../sources/official-news-024.md)）；[news/44](../sources/official-news-044.md) 把它與 AgileLink 一起列為 AI／SaaS 流量的解法，報表由 [X-View](x-view.md) 呈現。

受眾問題與寫法見 [頻寬與流量管理](../concepts/traffic-management.md)。

## 其他來源關聯

- [合作公告](../sources/official-news-045.md) 的汰舊換新段列有 Traffic Shaper E／F 系列舊機。
- [修補快照](../sources/official-news-060.md) 記錄 2026-10-30 時 TrafficShaper 修復中；這不構成現行狀態。
- [Facebook 貼文](../sources/facebook-threat-intelligence-update.md) 的 DefenseTrust CTA 指向 TrafficShaper，不代表兩者功能相同，見 [CTA 待確認](../issues/facebook-cta.md)。

## 待確認

2026 COMPUTEX 預告的 [AgileShaper](agileshaper.md) 經確認仍在開發中、預計 2027 年下半年發布，但與 TrafficShaper 的關係未說明。「確保營運不中斷」等旁路說法沒有測試條件；產品名在原文有 Traffic Shaper／TrafficShaper 兩種寫法。
