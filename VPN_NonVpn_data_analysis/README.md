## 資料說明

### 5/24
今天針對資料夾中，以"使用相同應用"(也就是相同名稱的csv檔)的紀錄做了一下更深入的對比和分析，發現 netflix 和 spotify 以這兩個為名稱的csv檔都同時有在 vpn 及 nonvpn 的資料夾中，因此先對兩者做了分析。

### Netflix
![1](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/c1cfd15c-c7a4-4997-b883-ac23944c1ebd)

分別為 VPN(左) 及 NonVPN(右) 的資料夾中得到的所有有關 netflix 的流量紀錄，下面一張把兩者疊起來。
![vpn_nonvpn_result](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/d20de73f-1ffa-4e8f-88e3-6f38c5b12c8d)

可以發現 NonVPN 因為尺寸變化很大，這樣疊上 VPN 看不出分布的比較，因此將pkt_size範圍設定在0~2000
![2](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/0b3e9d00-9357-4710-b0ed-2e6c4e0defe9)

下面一張把兩者疊起來。
![limited_vpn_nonvpn_result](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/d1865355-617d-4334-a891-205ae9ca56eb)

### Netflix (pkt_size = 0-2000)結論:
- time_diff 的分布大多在取對數的-2~2；接近2的區域有更多
- pkt_size 的分布在 vpn 和 nonvpn 有很大的區別，就是 vpn 存在明顯的上界 MAX:1359
- 大部分的封包特性都重疊，分不太開，不是很理想的狀況


### Spotify
![3](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/bc8b2e1c-a2fb-428d-9fd2-797a2d1edf90)

分別為 VPN(左) 及 NonVPN(右) 的資料夾中得到的所有有關 spotify 的流量紀錄，下面一張把兩者疊起來。
![vpn_nonvpn_result](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/c78bb1bf-781b-42db-8607-6e376d1fbe0a)

同樣的問題，NonVPN 因為尺寸變化很大，這樣疊上 VPN 看不出分布的比較，因此將pkt_size範圍設定在0~2000
![4](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/79a4ce19-9904-4a93-a444-fc10fa352d13)

下面一張把兩者疊起來。
![limited_vpn_nonvpn_result](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/a94e7df4-52b0-4370-a444-7c0b22e99316)

### Spotify (pkt_size = 0-2000)結論:
- time_diff 在兩者的分布有區別；特別是VPN的部分在-2.5~0之間有多
- pkt_size 在兩者的分布也有區別；就是 vpn 存在明顯的上界(MAX: 1360)，並且size在自身範圍內分布均勻
- 缺點是 data 不太多，但確實有機會分辨兩個族群，也許可以用生成相似資料去增加 data 量

### 5/23
這個資料夾分析了 VPN-NonVPN 五個 data folder 中的 http traffic。
經過 emily 的 to_flow.py 把 flow 都分開之後，將圖統計並繪製，
每個資料夾中提供:
- 每個 flow 的 pkt 分布圖(圖表中的變異量和標準差是採用python中.var()及.std()直接計算而得)
- 個別資料夾(vpn01、vpn02、nonvpn01、nonvpn02、nonvpn03) 內中所有 pkt 分布

### 結果速看:
>### vpn01
>![combined_scatter_plot](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/09b0d7b5-cd07-4a42-950f-eea4afd30035)

>### vpn02
>![combined_scatter_plot](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/ecb6e998-7428-4845-b2d6-e22b66ddd580)

>### nonvpn01
>![combined_scatter_plot](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/4c0a70be-76ea-40a4-adb6-ce049d7e32bb)

>### nonvpn02
>![combined_scatter_plot](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/a71a856c-8eaf-447a-9e83-03bd6bdf9c91)

>### nonvpn03
>![combined_scatter_plot](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/73822955/3c0319eb-63ed-4381-a517-388f20174559)


