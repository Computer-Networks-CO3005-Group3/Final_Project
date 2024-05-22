5/22 fingerprint3.py 程式碼完善 && random data generate
=====
1.原先將size及time之間視為獨立;現在更改為計算彼此之間的相關係數  
2.原先濾波前pdf矩陣元素總和不為1;現在將pdf矩陣進行正規化使其總和為1  
皆未更改所得值(size、time獨立，pdf總和不為1):  
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/168053836/f316db78-6bb7-4422-bb05-b589603cf625)

將size、time考慮彼此相關係數進行計算後(pdf總和不為1):
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/168053836/a82fbb61-f277-4874-9e52-a003bf90b7e1)

將size、time加入相關係數且對matrix進行正規化使pdf總和為1後:
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/168053836/8740d311-dc7c-4fd8-bffd-2a0bae777b64)
**********************************************************************************************************************************
random generator

  產生一個20,000筆regular train traffic 的packets的pdf和一個regular test traffic，檔案放在regular train fingerprint.zip和regular train fingerprint.zip那邊。

  程式碼的部分結合了承誼給的fingerprint3.py與random generate數值的function，我是在jupyter notebook寫，按一下執行就可以有結果了！

  附圖是執行結果與輸出之csv檔案示意圖

  ![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/115610077/11269b5b-21f5-443c-b4aa-5ba55abf6532)

  ![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/115610077/f4b4a8c4-42ab-4275-91c6-80d1d669c3da)



5/20 沉澱之後再出發
=====
  1. 承誼、翎喬兩邊統合了想法！目前確認使用fingerprint3.py讀程式碼沒問題，沒有bug，也有先跑了toflow.py，此次使用的dataset是除了nonvpn1、nonvpn2以外的所有資料。
  2. 與維蓉這邊也進行了串聯，與先前翎喬計算出的fingerprint正確率50%比起來，這次的正確率為57%，有些微提升。
  3. 發現有無濾波的正確率都一樣，更改濾波器的sigma值，正確率依然不變，可見我們現在的濾波器沒用。
  4. 在濾波前的pdf總和不為1，濾波後才為1，正在尋找它的bug，下圖為示意。
     ![436307417_820592286139327_7926448739171119703_n](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/115610077/9739c5c9-f64b-4b43-be27-e8e782e1db52)
  5. 本周的目標：讓PDF的總和在通過濾波器之前為1

5/18 執行須先install scipy
=====
濾波器的sigma直接設1.0
pdf的總和大約為1，所以感覺pdf計算沒有錯..吧
![image](https://github.com/Computer-Networks-CO3005-Group3/Final_Project/assets/168053836/da8973a1-b06c-467e-b863-9e679e6a18db)

5/13 需要改善的地方
=====
  1. 由小資料確認pdf計算的對錯
  2. 高斯濾波器的sigma數值給標準差
  3. 找pdf的最小值給維蓉
     
5/8 進度
=====
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
