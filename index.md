# UGUARD 行銷知識庫

先從產品、議題或寫作頁閱讀；需要查證時沿來源頁追溯 raw。頁面是來源化知識，不代表現行宣稱已核准。

來源登錄 85 筆：全文已 Ingest 65、線索已登記 20、待處理 0。

目前進度：[pilot 執行紀錄](schema/ingest-runs.json)；[首次整合發現](wiki/syntheses/pilot-findings.md)。

[Agent 規範](AGENTS.md) · [Schema](schema/SCHEMA.md) · [流程](docs/WORKFLOWS.md) · [操作日誌](log.md) · [首次報告](reports/2026-11-01-ingest-pilot-001.md)

## 公司、夥伴與產品

- [AAEON 研揚科技](wiki/entities/aaeon.md) — UGUARD 的硬體策略夥伴；記錄 2024 合作與 COMPUTEX 2025 共同展出的來源說法。（historical_only）
- [AgileLink](wiki/entities/agilelink.md) — 整合多 WAN、策略路由與 DNS 安全定位的歷史產品敘述，與修補狀態分層保存。（source_reported）
- [AgileShaper](wiki/entities/agileshaper.md) — TrafficShaper 的上位版，開發中，預計 2027 年下半年發布（使用者確認）。（needs_review）
- [Axiomtek 艾訊](wiki/entities/axiomtek.md) — 工業電腦硬體夥伴；記錄 2025 合作公告、COMPUTEX 2026 共同展出與相容性說法。（source_reported）
- [通路與代理夥伴](wiki/entities/channel-partners.md) — 官網 2026-11-01 精選夥伴清單與歷年代理公告的對照；以官網快照為現況依據。（source_reported）
- [DefenseCloud 與 AgileCloud](wiki/entities/cloud-platforms.md) — DefenseCloud 情資雲與訂閱方案、AgileCloud 雲端監控的來源說法；數字口徑待確認。（source_reported）
- [DefenseTrust](wiki/entities/defensetrust.md) — 整合情資比對、策略阻擋、部署與報表的來源說法，數字與絕對化用語另列待確認。（source_reported）
- [Innotel](wiki/entities/innotel.md) — 2024 年宣布的越南品牌代理商；目前只有一篇官網短公告。（historical_only）
- [MetaAge 邁達特](wiki/entities/metaage.md) — 保留 2026 合作公告中的代理與在地服務角色。（source_reported）
- [朔宇科技 PETACOM](wiki/entities/shuoyu.md) — 2025 年簽約的台灣資安代理商；記錄簽約活動與聯絡窗口的來源說法。（historical_only）
- [TrafficShaper](wiki/entities/trafficshaper.md) — Layer 7 應用辨識、頻寬政策與 In-line／SPAN 部署的來源說法；上位版 AgileShaper 開發中。（source_reported）
- [UGUARD NETWORKS](wiki/entities/uguard.md) — 依試行來源整理公司定位與產品關聯，保留時間限制。（source_reported）
- [WarpTunnel™](wiki/entities/warptunnel.md) — AgileLink 的多路徑 VPN／雲端隧道功能，記錄來源說法與「零時差」用語風險。（source_reported）
- [X-View 集中報表](wiki/entities/x-view.md) — 跨 AgileLink、DefenseTrust、Traffic Shaper 的集中管理報表與 AI 情資報告說法。（source_reported）

## 概念與受眾問題

- [GTC：全球流量協作與 DNS 保護](wiki/concepts/global-traffic-collaboration.md) — AgileLink 的 GTC DNS 以入站流量分流與 DNSSEC 敘述 DNS 層面的可用性與安全。（source_reported）
- [ISO/IEC 27001:2022 與威脅情資](wiki/concepts/iso-27001.md) — 以 2022 版新增控制作為導入背景；來源只支持「協助」，不能寫成「符合」。（needs_review）
- [舊設備替代與汰舊換新](wiki/concepts/legacy-replacement.md) — 從 2024 年 FortiWAN 替代到 2026 汰舊換新方案的訴求；方案經確認仍在辦理。（historical_only）
- [補強 NGFW／EDR 的情資防禦](wiki/concepts/ngfw-complement.md) — DefenseTrust 以「防火牆好幫手」定位補強 NGFW／EDR；標題「超越」用語需審慎。（source_reported）
- [威脅情資在行銷文章中的表達](wiki/concepts/threat-intelligence.md) — 以更新、比對、策略與日誌說明情資如何支援防護。（inferred）
- [頻寬與應用流量管理](wiki/concepts/traffic-management.md) — 把「網路變慢」從加頻寬轉為應用可視化與政策分級，連到 TrafficShaper。（source_reported）
- [WAN 韌性與多線路備援](wiki/concepts/wan-resilience.md) — 把線路多樣性、替代路徑與流量政策連到營運需求。（inferred）

## 合作與活動

- [UGUARD × AAEON 研揚合作](wiki/events/aaeon-partnership.md) — 2024-10 宣布全球策略夥伴並測試 FWS 設備，2025 COMPUTEX 再次共同展出。（historical_only）
- [UGUARD × 艾訊硬體合作](wiki/events/axiomtek-partnership.md) — 2025-12 宣布硬體合作，2026-05 新聞稿與 COMPUTEX 2026 共同展出。（historical_only）
- [COMPUTEX 2025 參展](wiki/events/computex-2025.md) — 2025-05-20～23 南港 L0329 參展，與 AAEON 合辦講座與闖關活動；贈品活動已結束。（historical_only）
- [COMPUTEX 2026 與艾訊共同展出](wiki/events/computex-2026.md) — 2026-06-02～05 南港 M0427a，主軸「從連線、流量到威脅情資」；展會已結束。（historical_only）
- [CVE-2026-109618／109619 PHP 漏洞事件](wiki/events/cve-2026-php.md) — 2026-10 PHP 漏洞的說明公告與修補進度；僅為截至 2026-10-30 的歷史資料。（historical_only）
- [2024 資安大會參展](wiki/events/cybersec-expo-2024.md) — 2024 資安大會南港二館 C119 攤位與拉霸闖關活動；只保留歷史紀錄。（historical_only）
- [台灣區老客戶免費企業健檢](wiki/events/health-check-campaign.md) — 2025-09 起的健檢活動，使用者確認仍在辦理，原訂至 2026-12-31。（approved_current）
- [UGUARD × 邁達特合作與相關活動](wiki/events/metaage-partnership.md) — 分離新聞稿日期、網站發布日期及優惠有效期限。（historical_only）
- [UGUARD × 朔宇科技代理簽約](wiki/events/shuoyu-partnership.md) — 2025-07-03 於台北 JR 東日本飯店簽約暨產品更新發表；預告稿與花絮分開保存。（historical_only）
- [新加坡總部與公司里程碑](wiki/events/singapore-hq.md) — 2024-03 新加坡公司、2025-09 週年與 STARLINK 整合宣告；設立日與總部定位待確認。（needs_review）

## 寫作知識

- [品牌語氣與用語觀察](wiki/writing/brand-observations.md) — 基於約 60 篇官網與社群全文的暫定寫作觀察，並非品牌正式手冊。（inferred）
- [展會與講座邀請寫法](wiki/writing/event-invitation.md) — 從資安大會與兩屆 COMPUTEX 的預告、議程、活動與花絮文歸納寫法。（inferred）
- [合作新聞稿：角色、價值與引言](wiki/writing/partnership-announcement.md) — 區分合作事實、活動條款與主管引言的來源要求。（inferred）
- [產品文章：從痛點到機制與行動](wiki/writing/product-article.md) — 把受眾、痛點、證據與 CTA 分開填寫，保留發布前核對。（inferred）
- [社群與節慶短文寫法](wiki/writing/social-posts.md) — 從 10 餘篇節慶／社群貼文歸納結構與語氣；觀察而非正式規範。（inferred）

## 綜合分析

- [產品訊息演進：2024–2026](wiki/syntheses/messaging-timeline.md) — 依官網 API 日期整理產品組合、主打訊息與合作夥伴的變化，供選題與避免引用過時說法。（inferred）
- [首次 Ingest：可累積的行銷知識](wiki/syntheses/pilot-findings.md) — 以跨來源整合示範產品、合作、時效及文案觀察。（inferred）

## 來源摘要

- [艾訊新聞：COMPUTEX 2026 攜手 UGUARD 展出](wiki/sources/external-285134be29ce.md) — 艾訊官網新聞的清單摘要，描述 COMPUTEX 2026 與 UGUARD 共同展出；屬已過期展會資訊。（reference_only）
- [資安人轉載：UGUARD 攜手邁達特](wiki/sources/external-339127206f46.md) — 資安人科技網刊出的 UGUARD／邁達特合作新聞稿，與 iThome PR 版同題同稿。（reference_only）
- [iThome 轉載：DefenseCloud 訂閱查詢全球黑名單](wiki/sources/external-37c35327340f.md) — iThome PR 頻道轉載官網 news/46，清單只有截斷摘要。（reference_only）
- [iThome 轉載：UGUARD 攜手邁達特（PR 頻道）](wiki/sources/external-52cb8621fccb.md) — iThome PR 頻道刊出的 UGUARD／邁達特合作新聞稿，與官網 news/45 及資安人版同稿。（reference_only）
- [資安人：DefenseTrust 與 ISO/IEC 27001:2022](wiki/sources/external-5a6da7c9528e.md) — 資安人科技網刊出官網 news/17 同稿；媒體標題把「符合…之期待」改為「符合…新標準」。（reference_only）
- [iThome：艾訊攜手 UGUARD 企業網路管理方案](wiki/sources/external-679fec63ebbe.md) — 只有 metadata 與先前 Agent 生成摘要的艾訊／UGUARD 案例報導線索，待補全文。（reference_only）
- [iThome 轉載：超越 NGFW 與 EDR 的解決方案](wiki/sources/external-8ba4960a7e70.md) — iThome PR 頻道轉載官網 news/20，清單摘要只有一行副標。（reference_only）
- [CTIMES 轉載：網路備援不能只是有第二條線](wiki/sources/external-93018eaab6d5.md) — 官網媒體清單中的 CTIMES 轉載，對應官網 news/56 的 AgileLink 備援文章。（reference_only）
- [iThome 轉載：AgileLink 掌控 WAN 端主控力](wiki/sources/external-a101bb7881fe.md) — iThome PR 頻道轉載官網 news/39 的 AgileLink 文章。（reference_only）
- [資安人轉載：DefenseTrust 從源頭偵測阻斷](wiki/sources/external-a6b65c2e9d77.md) — 資安人科技網刊出官網 news/20 同稿，摘要含 Inline 部署與 100+ 萬筆比對說法。（reference_only）
- [資安人：DefenseCloud 與 Defense Trust 整合方案](wiki/sources/external-b7bcc1e07edf.md) — 資安人科技網報導的清單紀錄，摘要只有一行副標，對應官網 news/54。（reference_only）
- [CIO Taiwan：朔宇科技與 UGUARD 簽署代理](wiki/sources/external-b8eefd2576c2.md) — CIO Taiwan 對朔宇簽約儀式的報導，清單只有截斷摘要；官網有活動預告與花絮。（reference_only）
- [iThome 轉載：DefenseTrust 新世代威脅情資解決方案](wiki/sources/external-c8131160ce99.md) — iThome PR 頻道轉載官網 news/18，摘要以國內勒索事件開頭。（reference_only）
- [CIO 109792：邁達特合作報導參考](wiki/sources/external-cio-109792.md) — 僅有先前生成摘要與 metadata，作為待補全文的媒體線索。（reference_only）
- [iThome：邁達特代理 UGUARD（邁達特端新聞稿）](wiki/sources/external-fb73abcbfef6.md) — iThome PR 頻道的邁達特端合作新聞稿，與 CIO 109792 同稿；官網 news 未見同文。（reference_only）
- [Facebook：威脅情資持續更新](wiki/sources/facebook-threat-intelligence-update.md) — 以痛點、機制、條列及 CTA 說明 DefenseTrust；發現 CTA 目的地不符。（source_reported）
- [使用者確認：情資更新頻率與健檢活動](wiki/sources/human-2026-11-01-001.md) — 2026-11-01 使用者確認情資每小時更新、老客戶健檢仍在辦理；為核准紀錄的證據。（source_reported）
- [使用者澄清：情資請求與更新頻率](wiki/sources/human-2026-11-01-002.md) — 每 3 分鐘是 DefenseTrust 的情資請求頻率，情資最晚每小時更新；取代前一筆每小時的寫法。（source_reported）
- [使用者確認：最新情資保持在百萬筆等級](wiki/sources/human-2026-11-01-003.md) — 2026-11-01 使用者確認最新情資數量保持在百萬筆等級；千萬、億級說法不作現行依據。（source_reported）
- [使用者確認：攔截超過 80% 為正確描述](wiki/sources/human-2026-11-01-004.md) — 2026-11-01 使用者確認 DefenseTrust「攔截超過 80%」是正確描述；誤報率未確認。（source_reported）
- [使用者確認：224 國正確、零誤判不可用](wiki/sources/human-2026-11-01-005.md) — 2026-11-01 使用者確認情資涵蓋 224 個國家，並判定「零誤判／誤報率近乎零」不可用。（source_reported）
- [使用者確認：AgileShaper 開發狀態](wiki/sources/human-2026-11-01-006.md) — 2026-11-01 使用者確認 AgileShaper 仍在開發中，預計 2027 年下半年發布。（source_reported）
- [使用者確認：汰舊換新方案仍在辦理](wiki/sources/human-2026-11-01-007.md) — 2026-11-01 使用者確認汰舊換新方案仍在辦理，並指示代理商現況以官網為準。（source_reported）
- [使用者確認：AgileShaper 是 TrafficShaper 的上位版](wiki/sources/human-2026-11-01-008.md) — 2026-11-01 使用者確認 AgileShaper 定位為 TrafficShaper 的上位版。（source_reported）
- [官網精選合作夥伴（2026-11-01 快照）](wiki/sources/official-featured-partners.md) — 官網 /partners/featured 在 2026-11-01 列出的 6 家通路夥伴與地區。（source_reported）
- [AgileLink 作為 FortiWAN 替代方案的短文](wiki/sources/official-news-001.md) — 以 FortiWAN 為標題切入，介紹 AgileLink NGWM 的多線路整合與故障移轉說法；無規格或測試條件。（source_reported）
- [2024 資安大會 C119 攤位公告（僅圖片）](wiki/sources/official-news-002.md) — 三語正文皆只有一張圖片，只能從標題得知參展與攤位號碼。（reference_only）
- [UGUARD NETWORKS 成立新加坡總公司（僅標題）](wiki/sources/official-news-003.md) — 三語皆無正文文字，只有標題與封面圖路徑，不能據此確認成立日期或細節。（reference_only）
- [資安展攤位「闖關任務玩拉霸」活動](wiki/sources/official-news-004.md) — 2024 資安大會 C119 攤位遊戲與贈品說明，屬已結束的展會活動。（historical_only）
- [2024 端午節祝賀貼文](wiki/sources/official-news-005.md) — 端午節社群短文，以 DefenseTrust「不受零時差攻擊」作節慶標語；英文譯文意思相反。（historical_only）
- [DefenseTrust 新世代威脅管理短文](wiki/sources/official-news-006.md) — DefenseTrust 早期社群介紹：情資每小時更新、上千萬筆情資與分析報告的來源說法。（source_reported）
- [全球流量協作（GTC）短文](wiki/sources/official-news-007.md) — GTC 將外部連入內部服務的流量分散到不同線路，並列出支援的 DNS 記錄類型。（source_reported）
- [Traffic Shaper 部署模式：In-line 與 SPAN](wiki/sources/official-news-008.md) — 以文字說明 tOS 的 In-line 與 SPAN 兩種部署模式及各自功能。（source_reported）
- [與越南 Innotel 簽署品牌代理](wiki/sources/official-news-009.md) — 2024 年公告 Innotel 成為越南品牌代理，負責推廣與銷售全產品。（historical_only）
- [2024 中秋節祝賀貼文](wiki/sources/official-news-010.md) — 中秋節社群短文，以「中秋月圓，防禦不缺」結合節慶與網路防禦。（historical_only）
- [UGUARD 與研揚 AAEON 成為全球策略夥伴](wiki/sources/official-news-011.md) — 2024 年合作新聞稿：共同測試 AAEON FWS-7541／FWS-7840，含雙方執行長引言與公司簡介。（historical_only）
- [DefenseTrust 全球 IP 分析與大規模阻擋](wiki/sources/official-news-012.md) — DefenseTrust 可辨識破億 IP、阻擋多類已知惡意連線及 SSL 連線的來源說法；英日數量譯為十億。（source_reported）
- [DefenseTrust 精準阻擋與情資每日更新](wiki/sources/official-news-013.md) — DefenseTrust 定位為企業威脅情資中心，含「每日更新」「零誤判」等需審慎處理的來源說法。（source_reported）
- [2024 耶誕節祝賀貼文](wiki/sources/official-news-014.md) — 耶誕節社群短文，感謝支持並重申提供全球企業網路安全解決方案的願景。（historical_only）
- [2025 新年祝賀貼文](wiki/sources/official-news-015.md) — 跨年社群短文，以「網路不中斷」作節慶標語。（historical_only）
- [DefenseTrust 與 ISO 27001:2022 條款提醒（僅圖片）](wiki/sources/official-news-016.md) — 三語正文只有一句標語與圖片；ISO 條款內容在未讀圖片中，需以 news/17 為文字依據。（reference_only）
- [DefenseTrust 對應 ISO/IEC 27001:2022 新增 11 項控制](wiki/sources/official-news-017.md) — 2025 年新聞稿把 DefenseTrust 功能對應到 ISO 27001:2022 新增控制；屬合規類來源說法，未經驗證。（source_reported）
- [DefenseTrust 情資雲與 Inline 部署新聞稿](wiki/sources/official-news-018.md) — 介紹 Defense Cloud 蜜罐／欺敵、OSINT 與第三方情資整合、DPDK 與旁路機制；含 >80% 與零誤判說法。（source_reported）
- [2025 COMPUTEX 參展預告](wiki/sources/official-news-019.md) — 2025 COMPUTEX 南港一館 4F L0329 參展預告，列出六大展出解決方案。（historical_only）
- [DefenseTrust：補強 NGFW 與 EDR 的情資方案](wiki/sources/official-news-020.md) — 以 Akira 攻擊無 EDR 攝影機為例，說明 DefenseTrust Inline 情資阻斷、情資規模與 X-View 報表。（source_reported）
- [2025 COMPUTEX 即將登場（展前預告）](wiki/sources/official-news-021.md) — COMPUTEX 2025 攤位 L0329 展前預告，列出 DefenseTrust、AI 小助手、X-View 三項展示重點。（historical_only）
- [COMPUTEX 2025 威脅情資防護分享講座預告](wiki/sources/official-news-022.md) — COMPUTEX 2025 攤位講座議程（AgileLink GTC DNS、DefenseTrust 零日防護、X-View），每日第二場由 AAEON 主講。（historical_only）
- [COMPUTEX 2025 UGUARD 強勢登場（攤位活動預告）](wiki/sources/official-news-023.md) — COMPUTEX 2025 攤位亮點與前 10 名送 7-11 禮券的現場活動預告。（historical_only）
- [UGUARD 與研揚聯手亮相 COMPUTEX 2025（DefenseTrust × FWS-7541）](wiki/sources/official-news-024.md) — COMPUTEX 2025 主新聞稿：DefenseTrust 搭載 AAEON FWS-7541、六大解決方案、產品特色、主管引言與攤位活動。（historical_only）
- [COMPUTEX 2025「威脅情資 x AI邊緣運算」講座（UGUARD 議程）](wiki/sources/official-news-025.md) — UGUARD 與 AAEON 合辦講座的 UGUARD 三天議程與禮券活動預告。（historical_only）
- [COMPUTEX 2025「威脅情資 x AI邊緣運算」講座（AAEON 議程）](wiki/sources/official-news-026.md) — 同講座系列的 AAEON 15:30 場次預告，列出三天講題。（historical_only）
- [COMPUTEX 2025 問卷闖關 ✕ 轉轉樂抽獎](wiki/sources/official-news-027.md) — UGUARD 與 AAEON 兩攤問卷闖關後至 UGUARD 攤位轉盤抽獎的展場活動辦法。（historical_only）
- [2025 COMPUTEX 邀請探索資安科技（展前最後邀請）](wiki/sources/official-news-028.md) — COMPUTEX 2025 展前邀請：地點、日期、時段與三項攤位亮點；提及結合 OpenAI 技術。（historical_only）
- [UGUARD 攜手朔宇科技：7 月 3 日聯合簽約暨產品更新發表會預告](wiki/sources/official-news-029.md) — 2025-06 預告與台灣代理商朔宇科技（PETACOM）簽約及產品發表會，含三方主管引言與展示產品。（historical_only）
- [UGUARD × 朔宇科技簽約儀式暨產品發表會花絮](wiki/sources/official-news-030.md) — 2025-07 朔宇簽約與發表會的活動花絮，主要是圖說；標題沿用 029 預告文。（historical_only）
- [7 月 21 日 AgileLink 升版公告（僅圖片）](wiki/sources/official-news-031.md) — 三語正文皆只有一張圖片，無可讀文字；只能作為 2025-07 AgileLink 升版公告存在的線索。（reference_only）
- [新加坡總部成立 1 周年、STARLINK 整合與台灣老客戶免費健檢](wiki/sources/official-news-032.md) — 2025-09 新聞稿：新加坡總部週年、宣稱完成 STARLINK 低軌衛星整合至 AgileLink，並啟動至 2026-12-31 的老客戶免費健檢。（historical_only）
- [WarpTunnel™：安全遠端連線](wiki/sources/official-news-033.md) — 由海纜中斷、AI 攻擊、APT 與混合辦公痛點介紹 AgileLink WarpTunnel 加密隧道、多路徑備援與適用產業。（source_reported）
- [DefenseTrust：次世代防火牆的好幫手](wiki/sources/official-news-034.md) — 以減輕 NGFW 負載為角度介紹 DefenseTrust 與 Defense Cloud，含每 3 分鐘更新 120 萬筆情資的來源說法。（source_reported）
- [Traffic Shaper：雲端與 AI 時代的網路管理](wiki/sources/official-news-035.md) — 介紹 Traffic Shaper 的 L7 應用辨識、頻寬分配、儀表板與 Inline／SPAN 部署及 Bypass 設計。（source_reported）
- [2025 聖誕祝福](wiki/sources/official-news-036.md) — 向 IT 人員致謝的聖誕節社群短文，含標語 Secure Every Connection & Protect Every Moment。（historical_only）
- [UGUARD 與艾訊（Axiomtek）展開硬體合作夥伴關係](wiki/sources/official-news-037.md) — 2025-12 短公告：與艾訊硬體合作，宣稱已在多款艾訊網通平台完成相容性驗證。（historical_only）
- [2026 新年祝福](wiki/sources/official-news-038.md) — 迎接 2026 的新年社群短文，標語 Securing the Digital Future, Together。（historical_only）
- [AgileLink：掌控 WAN 端的主控力](wiki/sources/official-news-039.md) — 從 ISP／線路中斷風險介紹 AgileLink 多線路整合、PBR 與頻寬管理、GTC DNS、WarpTunnel 聚合、STARLINK 與 CEF/Syslog。（source_reported）
- [2026 馬年新春祝福](wiki/sources/official-news-040.md) — 2026 農曆新年社群短文，以守護網路防線與連線品質為祝福主題。（historical_only）
- [DefenseTrust 威脅資料庫介紹與老客戶健檢活動](wiki/sources/official-news-041.md) — DefenseTrust 產品說法（80%、業界最快、每天更新等）及至 2026-12-31 的健檢活動，均屬來源說法。（source_reported）
- [2026 企業網路強化方案（短篇公告）](wiki/sources/official-news-042.md) — 僅一段產品說明與「銷售活動」字樣，方案條款在圖片中；條款文字見 news/45，已於 2026-10-31 截止。（historical_only）
- [汰舊換新升級方案（短篇公告）](wiki/sources/official-news-043.md) — 僅兩句說明，禮遇內容在圖片；期限 2027-12-25 見 news/45，本篇文字未載。（reference_only）
- [AI 與 SaaS 流量暴增下的流量管理](wiki/sources/official-news-044.md) — 以 AI／SaaS 流量壅塞痛點介紹 AgileLink 與 Traffic Shaper，文末附無期限的優惠摘要。（source_reported）
- [UGUARD 與邁達特合作公告](wiki/sources/official-news-045.md) — 合作訊息、企業定位及促銷條款並存，須分離事件時間與有效期間。（source_reported）
- [DefenseCloud 訂閱查詢上線與方案](wiki/sources/official-news-046.md) — 介紹 DefenseCloud 月訂閱 Pro 與 Enterprise_Custom 方案，並附 COMPUTEX 2026 展出內容。（source_reported）
- [COMPUTEX 2026 與艾訊聯展社群預告](wiki/sources/official-news-047.md) — 社群貼文格式的展會預告：四項展出主題、展期 2026-06-02～06-05、展位 M0427a。（historical_only）
- [COMPUTEX 2026 與艾訊聯展新聞稿（完整版）](wiki/sources/official-news-048.md) — COMPUTEX 2026 系列中內容最完整的新聞稿：展品、艾訊硬體機型、雙方主管引言。（historical_only）
- [COMPUTEX 2026 與艾訊聯展新聞稿（刪節版）](wiki/sources/official-news-049.md) — news/48 的刪節重貼版本，缺艾訊機型與引言，標題截斷。（historical_only）
- [COMPUTEX 2026 社群預告（第一版）](wiki/sources/official-news-050.md) — 四點亮點＋展期展位的社群短文，未點名艾訊；與 news/51 幾乎相同。（historical_only）
- [COMPUTEX 2026 社群預告（第二版）](wiki/sources/official-news-051.md) — news/50 的修訂重貼，加入聯絡資訊與 #Axiomtek。（historical_only）
- [COMPUTEX 2026 展出邀請（EDM 版）](wiki/sources/official-news-052.md) — news/48 去除艾訊段落後的展出邀請版本。（historical_only）
- [2026 端午節祝賀](wiki/sources/official-news-053.md) — 端午節社群祝賀短文，結合「層層防護」比喻；無產品細節。（historical_only）
- [DefenseCloud 雲端情報與 DefenseTrust 地端防禦](wiki/sources/official-news-054.md) — 雲地整合敘事：DefenseCloud 情資來源、DefenseTrust 地端阻擋、應用情境與企業版方案。（source_reported）
- [AI 時代駭客行為改變與 DefenseTrust 主動防禦](wiki/sources/official-news-055.md) — 以 AI 驅動攻擊變化切入，介紹 DefenseTrust 整合 DefenseCloud、最快每 3 分鐘同步等說法。（source_reported）
- [AgileLink：多線路備援與策略路由](wiki/sources/official-news-056.md) — 由營運中斷痛點介紹多 WAN 整合及 PBR，未提供切換 SLA。（source_reported）
- [網路變慢不只是頻寬：TrafficShaper 流量可視化](wiki/sources/official-news-057.md) — 以「網路變慢」痛點介紹 TrafficShaper 的 Layer 7 辨識、可視化、頻寬政策及 In-line／SPAN 模式。（source_reported）
- [可疑 IP／Domain 的即時阻擋：DefenseTrust 情資比對](wiki/sources/official-news-058.md) — 說明 DefenseTrust 情資更新、分類比對、策略阻擋與日誌；即既有 FB 貼文所連結的官網全文。（source_reported）
- [PHP 重大漏洞公告（CVE-2026-109618／109619）](wiki/sources/official-news-059.md) — 2026-10-27 的漏洞說明公告：風險、兩漏洞差異、建議行動；受影響產品表僅在圖片，修補進度另見 news/60。（historical_only）
- [2026-10-30 修補進度快照](wiki/sources/official-news-060.md) — 保留公告當時三項產品的不同處理狀態，不作目前修補建議。（historical_only）

## 待確認與缺口

- [待確認：公司資料與內文不一致](wiki/issues/content-inconsistencies.md) — 主管職稱、公司設立、日期欄位、未說明的技術合作與原文瑕疵彙整。（needs_review）
- [待確認：DefenseTrust CTA 指向 TrafficShaper](wiki/issues/facebook-cta.md) — 保留來源錯配，撰稿前確認應使用的產品連結。（needs_review）
- [紀錄：news/45 中英日內容差異](wiki/issues/promotion-language.md) — 中文版多出產品說明段及主動防禦段 AgileLink 條件；依決策 Q8 以繁中為準。（historical_only）
- [來源覆蓋與缺口](wiki/issues/source-gaps.md) — 76 個來源均已處理：56 全文、20 僅線索；FB 歷史、外部全文與圖片仍缺。（needs_review）
- [威脅情資數字：已核准口徑與禁用說法](wiki/issues/threat-intel-figures.md) — 情資頻率、量級、224 國與攔截超過 80% 已核准；零誤判不可使用。（source_reported）
- [待確認：活動、修補進度與絕對化宣稱](wiki/issues/time-sensitive-claims.md) — 區分過期、歷史狀態及缺乏測試條件的宣傳措辭。（needs_review）
- [待修正：英日版翻譯差異](wiki/issues/translation-differences.md) — 英日版的反義、數量級、數字歸屬與增刪段落；依決策 Q8 以繁中為準，但英日網頁需修正。（needs_review）
