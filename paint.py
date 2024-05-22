import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import pandas as pd

plt.figure(figsize=(6,5))

x = np.array([2,3,4,5,6,7,8,9,10,11])
y = np.array([0.4,0.5,0.6,0.7,0.8,0.9,1.0])

xgroup_labels=['2','3','4','5','6','7','8','9','10','11']   #x軸刻度
ygroup_labels=['0.4','0.5','0.6','0.7','0.8','0.9','1.0']   #y軸刻度

plt.xticks(x,xgroup_labels,fontsize=12,fontweight='bold')
plt.yticks(y,ygroup_labels,fontsize=12,fontweight='bold')

plt.xlabel("N_sects",fontsize=14,fontweight='bold')
plt.ylabel("Hit ratio",fontsize=14,fontweight='bold')
plt.xlim(1.5,10.5)   #x軸範圍
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
    N = 2
    N_list = []
    hit_ratio_list = []
    
    # 遍歷資料夾內的檔案
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(folder_path, filename)
            a, rows = process_csv_file(csv_file_path)
            hit_ratio = a/rows
            N_list.append(N)
            hit_ratio_list.append(hit_ratio)
            N += 1
            
            print("N:", N-1)
            print("hit_ratio:", hit_ratio)

            if N == 11:
                break

    return N_list, hit_ratio_list

folder_path = 'D:/Anomaly_Score'  # 請替換為你的資料夾路徑
N_list, hit_ratio_list = process_folder(folder_path)

plt.plot(N_list, hit_ratio_list, color='blue', marker='x', linestyle='-', label='HTTP') 
plt.legend(loc='upper right')  # 添加圖例並設置位置為右上角

plt.show()
