## 資料說明

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


