# Hit Ratio

### Anomaly_Score成果
##### 附圖為目前根據不同N_sects所算出來的hit_ratio，感覺N_sects值太大會不太準?(因為N_sects在大於100後，hit_ratio大致都在0.6幾左右，故放以下這幾張示意圖)
![螢幕擷取畫面 2024-05-20 225807](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/d9b879fc-98d2-468a-9b66-12902beeacd0)
![螢幕擷取畫面 2024-05-20 225831](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/b71074a7-750c-4abb-b435-6ba426478f24)
![螢幕擷取畫面 2024-05-20 225857](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/d337e74f-714f-4678-9b77-9fa89fbe0c0e)
![螢幕擷取畫面 2024-05-20 225919](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/f80c39c7-afcb-4fbc-bf54-7fab4151ad51)

##### 2024/5/20 23:30


### 折線圖
![螢幕擷取畫面 2024-05-21 210028](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/32fed4fa-a718-4e2f-8dd7-cbdb34c55024)
##### 目前先畫出各個點的圖，取N_sects在2~10之間。
##### 目前想到後續還有一些可以修改的地方:
##### 1.把點連起來
##### 2.讓右上角的圖例不要重複出現

##### 2024/5/21 21:05


### 修改後的折線圖
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/151cc263-7f18-43b0-9e2c-76031cb0733b)
##### 已經把點連起來且讓右上角的圖例不要重複出現了。
##### 至於N_sects上升，Hit ratio上升的原因，推測可能是因為package有足夠多的flow很少，導致Hit ratio會產生上升的假象。

##### 2024/5/22 21:20

### Anomaly_Score5成果
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/aa34c12f-562c-42b2-9a73-ee3dd35ef9e5)
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/1469732c-1f76-4be3-b031-daca1a9ff241)
##### 目前N=2時的Hit ratio已經上升到0.978

##### 2024/5/24 21:30
