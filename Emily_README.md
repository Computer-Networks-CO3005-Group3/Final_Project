
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

![圖片](https://github.com/emilytsao168/Computer_Networks_Final_Project/blob/main/005710.png)   
![圖片](https://github.com/emilytsao168/Computer_Networks_Final_Project/blob/main/005541.png)   
![圖片](https://github.com/emilytsao168/Computer_Networks_Final_Project/blob/main/005630.png)   
![圖片](https://github.com/emilytsao168/Computer_Networks_Final_Project/blob/main/005759.png)   
   
##### 2024/05/04 更新   
   
# calculate_anomaly_score_V2.py  
-------------  
   
-   ### get_Z_sequence(F, pdf_vector)   
    #### 把單一個F(flow)中的值(每個package的Pi)和pdf矩陣餵入，並計算出每個Pi的Zi，存成list回傳。   

-   ### calculate_anomaly_score(z_sequence, l_pdf, l_f, epsilon=1e-8)   
    #### 根據求出的Zi、pdf矩陣長度(regular http traffic package 數量)、待測flow長度(package 數量)、自訂epsilon=1e-8，計算出Sn(anomaly_score)，並且回傳從i=1到i=Nsects的所有Sn值。   

-   ### read_pdf_matrix   
    #### 從csv讀入pdf矩陣存成list後回傳。
    #### read_pdf_matrix_1和read_pdf_matrix_2的區別是讀入檔案的副檔名為.csv或是.npz   

-   ### classify_traffic   
    #### 透過判斷Sn是否大於閾值(T=1)，回傳該待測F(flow)為regular http traffic或tunneling http traffic。   

-   ### process_csv_files   
1.  #### 讀入指定路徑下的所有待測F(flow)。
2.  #### 計算待測F的Zi
3.  #### 計算待測F的Sn
4.  #### 判斷待測F為regular http traffic或tunneling http traffic，將(src_ip, dest_ip,  original_class, z_n, s_n,  new_class)依次存入csv檔中，並且每個檔案中為i相同的多個flow。

    
##### 2024/05/08 更新   
