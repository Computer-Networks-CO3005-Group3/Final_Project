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

##### regular http traffic 訓練
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/0156dfa0-c9c6-46e0-a064-a69a72ebcef2)
![Figure_0528r](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/2aee2bb2-2352-4590-8464-5cfda3be95d4)

##### tunneling http traffic 訓練
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/cc644803-d4f2-4c21-8de4-05185b70b936)
![Figure_0528t](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/184f25c9-28c0-44a7-af7f-fe310c996be2)

##### 2024/5/28 22:10

### Anomaly_Score_0528_r_3
##### regular http traffic 訓練
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/db74051c-0a34-408b-85f7-4578bdf340f9)
![Figure_0528r3](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/d79eef19-cec5-4144-8d80-a13ea51c7555)

##### tunneling http traffic 訓練
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/e8cd16f1-6e10-4bfa-ab51-d4318608ad56)
![Figure_0528t3](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/b64f5903-31c4-4082-b444-1d20557e6081)

### Anomaly_Score_0528_r_3_N2
##### regular http traffic 訓練
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/ca977a8e-84a6-455c-b2f7-24bdddf722b1)
![Figure_0528r3_N2](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/66262ab7-9210-4c16-b610-1aa7372dec65)

##### tunneling http traffic 訓練
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/564827a0-aa88-4ab7-8a3c-e736f5048fb2)
![Figure_0528t3_N2](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/cc10fcef-7c1c-41ce-896b-6d6d5bf519e1)


### Anomaly_Score_0528_r_3_N3
##### regular http traffic 訓練
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/cd9df6ca-608d-4c87-9b70-27444d704875)
![Figure_0528r3_N3](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/d2a2b877-44c7-4742-b7a6-ae280a8e7c31)

##### tunneling http traffic 訓練
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/b483d10d-c296-4a50-9fc2-a796deece016)
![Figure_0528t3_N3](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/8c8675dc-417b-4e01-980f-b637bc199500)

### Anomaly_Score_0601_r_N4
##### regular http traffic 訓練
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/97155c83-1796-45c4-94c2-ad2ace66d369)
![Figure_0601r_N4](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/127335630/f1992df7-fd4e-43fc-aed5-704bc390e3a1)

##### 2024/6/1 19:10
