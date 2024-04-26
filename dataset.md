# 4/26 dataset progress record

目前我已經從 (https://www.unb.ca/cic/datasets/vpn.html) 把其中一個資料流的檔案抓下來了(VPN-PCAPs-01)。
用 Wireshark 裡面的 tshark，我可以把.pcap檔內的封包資訊抓出來，並輸出為.csv檔(好像也可以輸出json)
有觀察到不少 http 的 traffic。

![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/b6792f1d-1070-4a17-83ee-28edb7041a6e)

可以在 files 找到 vpn_hangouts_chat1a.pcap 用 wireshark 打開觀察(用來試試看而已另一個 vpn_bittorrent.pcap 更多 http traffic 但傳不上來)。
