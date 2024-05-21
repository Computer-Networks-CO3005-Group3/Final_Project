import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import pandas as pd

#regular http traffic
#tunneling http traffic

plt.figure(figsize=(6,5))

x = np.array([0,1,2,3,4,5,6,7,8,9,10,11])
y = np.array([0.4,0.5,0.6,0.7,0.8,0.9,1.0])

xgroup_labels=['0','1','2','3','4','5','6','7','8','9','10','11']   #x軸刻度
ygroup_labels=['0.4','0.5','0.6','0.7','0.8','0.9','1.0']   #y軸刻度

plt.xticks(x,xgroup_labels,fontsize=18,fontweight='bold')
plt.yticks(y,ygroup_labels,fontsize=18,fontweight='bold')

plt.xlabel("N_sects",fontsize=20,fontweight='bold')
plt.ylabel("Hit ratio",fontsize=20,fontweight='bold')
plt.xlim(0,11)   #x軸範圍
plt.ylim(0.4,1.0)   #y軸範圍

def compare_classes(original_class, new_class):
    if original_class == new_class:
        return 1
    else:
        return 0

def process_csv_file(csv_file):
    a = 0  # 變數a
    total_rows = 0  # 總行數

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # 跳過標題行
        for row in reader:
            original_class = row[2]  # 第三列是original_class
            new_class = row[5]  # 第六列是new_class
            
            a += compare_classes(original_class, new_class)
            total_rows += 1

    return a, total_rows

def process_folder(folder_path):
    
    total_rows = 0
    N = 1
    # 遍歷資料夾內的檔案
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(folder_path, filename)
            a, rows = process_csv_file(csv_file_path)
            hit_ratio = a/rows
            N += 1
            print("N:", N)
            print("hit_ratio:", hit_ratio)
            
            plt.plot(N, hit_ratio, color = 'blue', marker = 'x', label='HTTP') 

            if N ==10:
                break

    return total_rows, N, hit_ratio

folder_path = 'D:/Anomaly_Score'  
N, total_rows, hit_ratio = process_folder(folder_path)
print("Total rows processed across all CSV files:", total_rows)
plt.legend(loc='upper right')  #添加圖例並設定位置在右上角

plt.show()
