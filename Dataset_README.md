# Dataset的成果紀錄以及進度說明(由新到舊)

## 4/29 Group meeting
1. 先看一下 non-VPN & VPN HTTP流量的差別 (沒看出個所以然)
2. 計算時間差(delta t)應該是 Source ip & Destination ip 都相同算通一個 flow(方向相同)，同個 flow 上的 packet 去算時間差 (第一個pkt沒有時間差)
3. 用 lib 儲存資料，分 flow 去存，給.csv出來 (要記錄是regular還是non-regular)

## 4/28 進度&方向 確認
1. 確定 Regular & Tunneled 流量來源問題(都能夠從ISCX-VPN-NonVPN-2016裡去獲取嗎?還是要自己做)
2. 要判斷 http 對話群組中，封包的時間差。怎麼判斷兩個封包是對話群組?

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

## 4/26 datateam 會議 (Dylan, Ingrid)
1. 只抓 HTTP 流量(HTTP 附近會有 TCP 的流量形成對話組，只管HTTP)
2. 用 python 寫好讀入.pcap檔->過濾處理封包->得到我們要的 HTTP traffic 的特性(time, size) 存成矩陣

Q:
1. non_vpn_資料夾裡的 HTTP 流量就是regular的流量? 而vpn_資料夾裡的 HTTP 就是有 Tunneled 的流量?
2. 我們要抓多少量?(目前抓最小的兩個 zip 就要快 7 個小時)

4/28 Ans:
1. vpn_資料夾裡的 HTTP 應該就是 Tunneled HTTP(by 老師的回信"自行生成數據的話可以用VPN")。不過我覺得可以用 Reference[2]的 tunneled traffic 製造器去自己做，然後比對看看(比對vpn的http流量和用Ref[2]製造的流量，特徵有什麼不一樣) **待確認**
2. 盡量多抓，越多越好

## 4/26 dataset progress record (Dylan)

目前我已經從 (https://www.unb.ca/cic/datasets/vpn.html) 把其中一個資料流的檔案抓下來了(VPN-PCAPs-01)。
用 Wireshark 裡面的 tshark，我可以把.pcap檔內的封包資訊抓出來，並輸出為.csv檔(好像也可以輸出json)
有觀察到不少 http 的 traffic。

![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/b6792f1d-1070-4a17-83ee-28edb7041a6e)

可以在 files 找到 vpn_hangouts_chat1a.pcap 用 wireshark 打開觀察(用來試試看而已另一個 vpn_bittorrent.pcap 更多 http traffic 但傳不上來)。
