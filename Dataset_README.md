# Dataset的成果紀錄以及進度說明(由新到舊)

## 5/1 上傳紀錄 & 相關內容說明 (Dylan)
1. NonVPNcsv_01_folder 資料夾裡面就是 NonVPNcsv_01 的所有應用網路流量，依據不同應用分開抓取裡面流量紀錄中的 HTTP traffic。目測是對的，待更進一步抽檢內容。
2. Non-VPN 資料夾裡的 HTTP 是 regular http；VPN 資料夾裡的就是 tunneled http

關於dataset的概念:
![555555](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/dc6f94af-9db7-456e-bd81-0f8b7203a0f6)
![66666](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/05a5cea3-042e-4850-b084-b47b7831adeb)

而 Testcsv_folder 和 Testpcap_folder 這兩個資料夾都是為了測試而生的小量數據，他們跟 dataset 完全沒有關係，但理論上是 regular http 且驗證過是沒問題的，你們如果有測試需求又不要跑太大量的資料，可以先用這兩個 Test 開頭裡面的東西。
**還有一個重點是，可能會發現很多CSV file打開裡面沒有數據，那就代表那個.pcap檔裡面所有流量都沒有使用到 HTTP protocal喔!**

---
## 4/30 實作紀錄 (Dylan)
修改了 test1.py，新版的是 time_diff_April30_v1.py 它可以做到:
1. 自動讀取資料夾(Testpcap_folder)中為.pcap或.pcapng的檔案(可以混雜兩種)
2. 遍歷.pcap/.pcapng檔中"所有"使用 HTTP portacal 的封包資料
3. 計算相同flow下pkt的時間差(相同flow:在相同的 source_ip & destination_ip 組合下的封包)
4. 每個獨立.pcap/.pcapng檔都獨立輸出各自的.csv檔(因為dataset是分不同應用的流量就不同一個pcap file)
5. 輸出的.csv內容是: 照順序排列的pi(有兩個column，first_col 為 pkt_size；second_col 為 time_diff) csv_folder裡面可以看。
time_diff.py和test_dataset資料夾都已經上傳到github了。大家可以試試。


驗證時差算對:
![時差完成](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/83a4b9e8-d649-493d-a495-d25fbe0ad872)
左邊是wireshark的畫面，No.2796, No.2840, No.2851都是同一個 flow (其他的pkt都是flow的唯一，time_diff都是0)用這三個pkt算彼此的時間差會跟程式跑出來的一樣。正確

---
## 4/29 Group meeting
1. 先看一下 non-VPN & VPN HTTP流量的差別 (沒看出個所以然，就當沒錯繼續做吧!)
2. 計算時間差(delta t)應該是 Source ip & Destination ip 都相同算通一個 flow(方向相同)，同個 flow 上的 packet 去算時間差 (第一個pkt沒有時間差)
3. 用 lib 儲存資料，分 flow 去存，給.csv出來 (要記錄是regular還是non-regular)

---
## 4/28 進度&方向 確認
1. 確定 Regular & Tunneled 流量來源問題(都能夠從ISCX-VPN-NonVPN-2016裡去獲取嗎?還是要自己做)
2. 要判斷 http 對話群組中，封包的時間差。怎麼判斷兩個封包是對話群組?

---
## 4/27 實作紀錄 (Dylan)
弄了一支 test1.py 可以做到:
1. 自動讀取資料夾(Testpcap_folder)中為.pcap的檔案
2. 遍歷.pcap檔中的所有使用 HTTP portacal 的封包資料
3. 存取封包資料到 http_packets 這個 dict 變數中
test1.py和資料夾都已經上傳到github了。大家可以試試

以下是結果截圖:
![111111111](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/11f551f4-ae38-4fec-a58a-72b88caf9f66)
上圖是wireshark的分析截圖；下面是python執行結果。
第二筆和最後一筆紀錄都有對應到，數量也正確。資料正確無誤地從檔案裡讀出來。

Q:
1. 紀錄的timestep其實是epchtime(一個從1970開始算的絕對時間?)，論文中的Pi要的是時間差，要做進一步處理(還是可以用其他紀錄的特徵時間做?ex: time since reference or first frame)
2. Pi中的時間差描述:"inter–time between i − th packet and the preceding one belonging to the same flow (seconds)" 代表要找出同一個流的 HTTP ? By How? 我的想法是可以去比對封包的 source ip 及 destination ip 若兩項交叉相等，則可視為同一個flow(對話) 想法而已還沒做...
3. 抽取出來的紀錄應該要用什麼樣的格式後面比較好處理? dict? array?

4/28 Ans:
1. 兩個時間(sec)都可以用來計算時間差，效果是一樣的
2. 還在研究

---
## 4/26 datateam 會議 (Dylan, Ingrid)
1. 只抓 HTTP 流量(HTTP 附近會有 TCP 的流量形成對話組，只管HTTP)
2. 用 python 寫好讀入.pcap檔->過濾處理封包->得到我們要的 HTTP traffic 的特性(time, size) 存成矩陣

Q:
1. non_vpn_資料夾裡的 HTTP 流量就是regular的流量? 而vpn_資料夾裡的 HTTP 就是有 Tunneled 的流量?
2. 我們要抓多少量?(目前抓最小的兩個 zip 就要快 7 個小時)

4/28 Ans:
1. vpn_資料夾裡的 HTTP 應該就是 Tunneled HTTP(by 老師的回信"自行生成數據的話可以用VPN")。不過我覺得可以用 Reference[2]的 tunneled traffic 製造器去自己做，然後比對看看(比對vpn的http流量和用Ref[2]製造的流量，特徵有什麼不一樣) **待確認**
2. 盡量多抓，越多越好

---
## 4/26 dataset progress record (Dylan)

目前我已經從 (https://www.unb.ca/cic/datasets/vpn.html) 把其中一個資料流的檔案抓下來了(VPN-PCAPs-01)。
用 Wireshark 裡面的 tshark，我可以把.pcap檔內的封包資訊抓出來，並輸出為.csv檔(好像也可以輸出json)
有觀察到不少 http 的 traffic。

![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/b6792f1d-1070-4a17-83ee-28edb7041a6e)

可以在 files 找到 vpn_hangouts_chat1a.pcap 用 wireshark 打開觀察(用來試試看而已另一個 vpn_bittorrent.pcap 更多 http traffic 但傳不上來)。
