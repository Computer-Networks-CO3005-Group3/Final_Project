import numpy as np
from collections import defaultdict
import csv
import os
from pathlib import Path
import numpy as np
from scipy.stats import multivariate_normal

def calculate_mean_var(filepath):
    size = 0
    time = 0
    n=0
    size_square=0
    time_square=0
    
    for filename in os.listdir(filepath):
            if filename.endswith('.csv'):
                input_file_path = os.path.join(filepath, filename)
                with open(input_file_path, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in list(reader):
                        value1 = int(row[2])
                        value2 = float(row[3])
                        size+=value1
                        time+=value2
                        n+=1
    size/=n
    time/=n
    print(size) #size average
    print(time) #time average
    print(n) #total packets number
    

    for filename in os.listdir(filepath):
            if filename.endswith('.csv'):
                input_file_path = os.path.join(filepath, filename)
                with open(input_file_path, 'r') as file:
                    reader = csv.reader(file)
                    next(reader)
                    for row in list(reader):
                        value1 = int(row[2])
                        value2 = float(row[3])
                        size_square+=(value1-size)**2
                        time_square+=(value2-time)**2
    size_square/=n
    time_square/=n
    print(size_square) #size variance
    print(time_square) #time variance
    pdf_generation(size,time,size_square,time_square)
    
def pdf_generation(size,time,size_square,time_square):
    # 假設size和time為兩個獨立變數
    mean = np.array([size, time])  # 平均值向量
    variances = np.array([size_square, time_square])  # 變數的方差 
    covariance_matrix = np.diag(variances)  # 對角矩陣
    # 建立多變量機率密度函數對象
    mv_normal = multivariate_normal(mean=mean, cov=covariance_matrix)
    #寫成輸出檔案
    with open('C:/Users/APPLE/Desktop/Final_Project/output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
    # 設定一組要計算機率密度函數值的點
        for filename in os.listdir(filepath):
                if filename.endswith('.csv'):
                    input_file_path = os.path.join(filepath, filename)
                    with open(input_file_path, 'r') as file:
                        reader = csv.reader(file)
                        next(reader)
                        for row in list(reader):
                            value1 = int(row[2])
                            value2 = float(row[3])
                            pos = np.dstack((value1, value2))
                            # 計算機率密度函數值
                            pdf_values = mv_normal.pdf(pos)
                            mapping(value1, value2, pdf_values)
                            #print("機率密度函數值:", value1, value2, pdf_values)
                            writer.writerow([value1, value2, pdf_values])
    '''PDF總和為1
    pdf_integral, _ = np.linalg.eig(covariance_matrix)
    pdf_integral = np.prod(np.sqrt(2 * np.pi * pdf_integral))
    pdf_integral *= mv_normal.pdf(mean)
    print("機率密度函數值積分:", pdf_integral)'''
      
def mapping(value1, value2, pdf_values):
    row=value1-40
    column=int((np.round((np.log10(value2)),decimals=2)-(-8))/0.01)
    print(row,column)
    # 創建一個大小為30961x1301的隨機矩陣
    matrix = np.zeros((30961, 1301))
    matrix[row-1, column-1] = pdf_values
    with open('C:/Users/APPLE/Desktop/Final_Project/matrix.csv', 'w') as file:
        for row in matrix:
            row_str = ','.join(map(str, row))  # 將一行轉換為字串，元素用逗號分隔
            file.write(row_str + '\n')  # 將該行寫入檔案，並換行

filepath = 'C:/Users/APPLE/Desktop/Final_Project/TEST_NonVPNcsv-03/'
calculate_mean_var(filepath)
