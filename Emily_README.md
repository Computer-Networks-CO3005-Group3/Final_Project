
# to_flow.py  
-------------  
   
### 用法:  
#### process_traffic_data(input_file_path, output_file_path, original_class)  
#### input_file_path: 輸入csv檔所在的路徑  
#### output_file_path: 輸出csv檔所在的路徑  
#### original_class: 輸入資料的真實類別(例: regular http traffic 或 tunneling http traffic)  
   

### 功能:  
1.  #### 把相同flow的資料存成dict   
2.  #### 每個dict包含(pkt_size, time_diff, original_class)   
3.  #### 刪除只有標題的檔案，以及只有一個package的flow   
4.  #### 紀錄size跟package的最大值及最小值   
5.  #### 儲存處裡好的資料至csv檔案中，路徑為(output_file_path+原檔案名稱+pkt_size_time_diff)   
6.  #### 每個csv包含(src_ip, dest_ip, pkt_size, time_diff, original_class)   
#### 注意！在讀取 CSV 檔案後，資料將以列表（list）的形式被讀取   

![圖片](/D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/PICTURES/005710.png)   
![圖片](/D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/PICTURES/005541.png)   
![圖片](/D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/PICTURES/005630.png)   
![圖片](/D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/PICTURES/005759.png)   
   
##### 2024/05/04 更新   
   
# calculate_anomaly_score.py  
-------------  
   
### 待更新   
