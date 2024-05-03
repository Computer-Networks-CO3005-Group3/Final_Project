
# to_flow.py  
-------------  
   
### 用法：  
#### process_traffic_data(input_file_path, output_file_path, original_class)  
#### input_file_path: 輸入csv檔所在的路徑  
#### output_file_path: 輸出csv檔所在的路徑  
#### original_class: 輸入資料的真實類別(例: regular http traffic 或 tunneling http traffic)  
   

### 功能  
1.  #### 把相同flow的資料存成dict   
2.  #### 每個dict包含(pkt_size, time_diff, original_class)   
3.  #### 刪除只有標題的檔案   
4.  #### 紀錄size跟package的最大值及最小值   
5.  #### 儲存處裡好的資料至csv檔案中，檔名與原輸入檔案相同   
6.  #### 每個csv包含(src_ip, dest_ip, pkt_size, time_diff, original_class)   
   
##### 2024/05/03 更新   
   
# calculate_anomaly_score.py  
-------------  
   
### 待更新   
