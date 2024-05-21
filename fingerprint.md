#5/20 沉澱之後再出發
  1. 承誼、翎喬兩邊統合了想法！目前確認使用fingerprint3.py讀程式碼沒問題，沒有bug，也有先跑了toflow.py，此次使用的dataset是除了nonvpn1、nonvpn2以外的所有資料。
  2. 與維蓉這邊也進行了串聯，與先前翎喬計算出的fingerprint正確率50%比起來，這次的正確率為57%，有些微提升。
  3. 發現有無濾波的正確率都一樣，更改濾波器的sigma值，正確率依然不變，可見我們現在的濾波器沒用。
  4. 在濾波前的pdf總和不為1，濾波後才為1，正在尋找它的bug，下圖為示意。
     ![436307417_820592286139327_7926448739171119703_n](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/115610077/9739c5c9-f64b-4b43-be27-e8e782e1db52)
  5. 本周的目標：讓PDF的總和在通過濾波器之前為1

#5/18 執行須先install scipy
濾波器的sigma直接設1.0
pdf的總和大約為1，所以感覺pdf計算沒有錯..吧
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/168053836/da8973a1-b06c-467e-b863-9e679e6a18db)

#5/13 需要改善的地方
  1. 由小資料確認pdf計算的對錯
  2. 高斯濾波器的sigma數值給標準差
  3. 找pdf的最小值給維蓉
     
#5/8 進度
  1. 設計流程1：先跑Emily的to_flow.py，利用calculate_mean_var計算size、time的平均值與標準差。
  2. 設計流程2：pdf_genration，利用剛剛算出來的平均值與標準差算出pdf，並把他輸出到output.csv中。
  3. 設計流程3：把time、size做mapping，讓data可以寫進大小為30961*1301的表格中：(round(log10(time))-(-8))/0.01、size-40，並繪製出下一階段要用的matrix.csv
  4. 使用到的regular HTTP資料為：NonVPNcsv-03資料夾中的335筆flow
  5. 碰到的困難1：基本功能都有，只差沒有高斯濾波，因為我不確定高斯濾波器的sigma要設多少？應該說...多少範圍以上的要濾除？
  6. 碰到的困難2：335筆flow總共有5560筆packets的pdf要計算，矩陣大小也偏大，導致到目前寫紀錄的現在，執行1小時半都還沒輸出一個成功的output.csv，可能是我最後一段mapping的寫法的問題、或我電腦效能太差，會再修改。(一定要跑出來啊阿阿阿阿)

【5/8 17:21補充】現在的執行速度大概為12秒寫入一筆資料，如果要跑完全部5590筆可能需要18小時，該換電腦了
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/115610077/d1196a61-3784-4c5a-a3f6-4a00397c305c)
【上圖為計算出的PDF未經過mapping的結果】
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/115610077/99d7aa9f-9c06-43c8-8582-c5b6372ed9b9)
【上圖為chatgpt改良我的程式後，五秒內完成mapping的csv檔案，但是目前還沒找到與未mapping的output.csv對應到的地方，chatgpt的對應法待研究】

【5/8 18:34補充】因為我也不確定哪一個PDF算法才是對的，所以先丟了matrix.zip上來，這是由gpt幫我mapping的檔案，大家可以先試試看，如果有不合理的地方我再更正

(self reminder)：承誼的code在fingerprint，自己的code放fingerprint2，gpt的code在fingerprint3(目前fingerprint的來源)
