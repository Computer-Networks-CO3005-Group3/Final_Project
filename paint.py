import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import pandas as pd

#folder_path = 'D:\Anomaly_Score'  # 請替換為你的資料夾路徑

def compare_classes(original_class, new_class):
    if original_class == new_class:
        return 1
    else:
        return 0

def process_csv_file(csv_file):
    a = 0  # 變數x
    rows = 0  # 總行數

    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # 跳過標題行
        for row in reader:
            original_class = row[2]  # 第三列是original_class
            new_class = row[5]  # 第六列是new_class
            
            a += compare_classes(original_class, new_class)
            rows += 1

    return a, rows

def process_folder(folder_path):
    total_a = 0
    total_rows = 0
    hit_ratio = 0
    N = 2
    
    # 遍歷資料夾內的檔案
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(folder_path, filename)
            a, rows = process_csv_file(csv_file_path)
            hit_ratio = a/rows
            N += 1

            print(" a across N.CSV files:", a,N)
            print(" rows across N.CSV files:", rows,N) 
            print(" hit_ratio:", hit_ratio)

            plt.scatter(hit_ratio,c = 'blue',s=150,marker = 'd') 
            plt.show()
    return a, rows, hit_ratio, N


folder_path = 'D:\Anomaly_Score'  #請替換資料夾路徑

plt.figure(figsize=(6,5))

x = np.array([100,200,300,400,500,600,700])
y = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

xgroup_labels=['100','200','300','400','500','600','700']   #x軸刻度
ygroup_labels=['0.0','0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1.0']   #y軸刻度

plt.xticks(x,xgroup_labels,fontsize=18,fontweight='bold')
plt.yticks(y,ygroup_labels,fontsize=18,fontweight='bold')

plt.xlabel("N_sects",fontsize=20,fontweight='bold')
plt.ylabel("Hit ratio",fontsize=20,fontweight='bold')
plt.xlim(0,700)   #x軸範圍
plt.ylim(0.0,1.0)   #y軸範圍
plt.show()
