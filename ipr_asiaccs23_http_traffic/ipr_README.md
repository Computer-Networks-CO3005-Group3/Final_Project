### ipr_asiaccs23 資料說明

這個dataset是從這邊找到的: https://traces.cs.umass.edu/index.php/Network/Network

裡面有篇paper "Investigating Traffic Analysis Attacks on Apple iCloud Private Relay" 裡面提到他們蒐集的data有包含safari的網頁瀏覽。

這邊是paper(連結: https://dl.acm.org/doi/10.1145/3579856.3595793 )內原文的截圖:

![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/cdd67274-52b8-4b56-a7c1-cc8943e44df6)

克勞迪翻譯:

*"我們設計了一個實驗環境,根據第4.2節和第4.1節所述的威脅模型執行網站指紋識別和流量關聯攻擊。對於這兩種實驗,我們使用了兩臺運行 macOS Monterey (12.2版)、8 Gb RAM 的 Macbook M1 機器。我們使用 Apple 的開放式腳本架構 (osascript) 通過 bash 腳本模擬瀏覽事件(如全頁滾動)。在每個實驗中,我們使用 Safari 15.3版本,並啟用了瀏覽器內置的私密瀏覽(PR)和跨站點追蹤防護選項。我們使用了單個 iCloud+ 帳戶和訂閱來在我們的 Mac 上啟用 PR。我們使用 tcpdump 收集流量跡象,並根據進程 ID 隔離 Safari 流量。所有跡象都是在單個瀏覽器實例和單個標籤會話中收集的。對於我們的流量關聯實驗,我們在 Digital Ocean 平台上設置了作為 VPS 實例部署的 Ubuntu 虛擬機(VM)。這些 VM 設置在不同的區域,並配置了 Apache Web 服務器通過 HTTP 提供 Web 流量。我們從兩個方面收集了該實驗的流量:一是在我們的本地機器上,另一是在服務器上。關於數據收集的更多細節將在後面的第6.2節和第6.3節中說明。考慮到道德因素,我們只使用我們自己產生的流量執行了這些攻擊,在我們的實驗中沒有收集或使用其他PR用戶的任何私人數據。"*
