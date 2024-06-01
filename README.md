# Final_Project

>## 6/1 會議記錄
>### 論文在 Nsects 比較高時，準確率下降的原因:
>- 推測是因為在看 regular 的 Anomaly score 在 flow 中看越多封包後，異常分數會累積並超過閾值，導致被判定為 tunneled，準確率下降。
>- 新版範圍的結果剛好倒過來，無法解釋，最後看一下畫圖出來的東西，真的不行就用舊版的(至少還能說明只有 Nsects=3 高起來的原因)
>


>## 5/30 會議記錄
>大家都辛苦了~終於有能打的結果了 不過還是要加緊腳步喔 撐到下禮拜就結束了! 加油 >_<
>
>持續修正簡報，可以的話練習講講看
>
>想一下我們的 "未來展望" 或 "在這一次的實作中有什麼可以做得更好"
>
>需要幫忙就趕快提出來!!!
>#### 筱婷:
>- 把生成資料的部分(相關的數據特徵)確認清楚製作簡報
>
>#### 詮恩:
>- 將生成的資料拿去畫圖給筱婷放報告
>
>#### 翎喬:
>- 做手動調整 N=2、N=3 的數據
>
>#### 維蓉:
>- 找出並分析 準確率在 N=3 時大於 N=2 的原因
>
>#### 俊穎:
>- 把hitratio的圖搞定 並確認是對的結果(想一下如何驗證)
>
>#### 承誼&俊穎:
>- 結果的分析，畫圖及製作簡報(應該要有train regular vs tunnel、手動調整 Nsects 的比較、與原論文的結果比較，共三項)
>

>## 5/20 會議記錄
>
>#### 共編簡報:
>
>https://docs.google.com/presentation/d/1xW0g74baKMOSCpuagSwAkiRFRNa6VYQz/edit?usp=sharing&ouid=110904508139372047303&rtpof=true&sd=true
>
>### 工作進度計畫:
>
>#### data 組:
>- 確認承誼找到的 MACCDC dataset 可以用
>  
>  5/21,00:12a.m. PS.我剛剛看了一下，我們好像沒有辦法確定這個 trace 裡到底哪些是 regular http；哪些不是。不過也還好 我會先抓一些，如果真的要用 就手動把一些我們覺得很像 tunneled 特徵的 pkt 拿掉(maybe like size 偏大的 pkt)，剩下的 pkt 我們就當 regular 去用。
>- 把他抓下來 (deadline: 禮拜五5/24晚上)
>- 初版簡報生出來 (deadline: 禮拜五5/24晚上)
>
>#### figerprint 組:
>- 將 NonVPNcsv-01、NonVPNcsv-02 以外的 dataset 用新的濾波器版本去建立 fingerprint (deadline: 禮拜二5/21晚上)
>- 初版簡報生出來 (deadline: 禮拜五5/24晚上)
>
>#### A_score 組:
>- 把濾波器版本的 fingerprint 算 anomaly score (deadline: 禮拜五5/24晚上)
>- 定一下 Nsects 要多少 加 畫圖 (deadline: 禮拜五5/24晚上)
>- 初版簡報生出來 (deadline: 禮拜五5/24晚上)

