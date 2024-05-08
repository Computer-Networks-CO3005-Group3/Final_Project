import numpy as np
import os
import csv

def calculate_mean_var(filepath):
    # 初始化統計量
    total_size = 0
    total_time = 0
    total_packets = 0
    size_squares = 0
    time_squares = 0
    
    # 遍歷文件夾並計算統計量
    for filename in os.listdir(filepath):
        if filename.endswith('.csv'):
            input_file_path = os.path.join(filepath, filename)
            with open(input_file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    size = int(row[2])
                    time = float(row[3])
                    total_size += size
                    total_time += time
                    size_squares += size ** 2
                    time_squares += time ** 2
                    total_packets += 1

    # 計算平均值和方差
    mean_size = total_size / total_packets
    mean_time = total_time / total_packets
    var_size = size_squares / total_packets - mean_size ** 2
    var_time = time_squares / total_packets - mean_time ** 2

    return mean_size, mean_time, var_size, var_time

def pdf_generation(filepath, mean_size, mean_time, var_size, var_time):
    # 計算多變量機率密度函數值
    mean = np.array([mean_size, mean_time])
    covariance_matrix = np.array([[var_size, 0], [0, var_time]])
    mv_normal = multivariate_normal(mean=mean, cov=covariance_matrix)
    
    # 創建一個大小為30961x1301的矩陣
    matrix = np.zeros((30961, 1301))
    
    # 遍歷文件夾並計算機率密度函數值
    for filename in os.listdir(filepath):
        if filename.endswith('.csv'):
            input_file_path = os.path.join(filepath, filename)
            with open(input_file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    size = int(row[2])
                    time = float(row[3])
                    pdf_value = mv_normal.pdf([size, time])
                    # 將映射後的值寫入矩陣中
                    mapped_size = size - 40
                    mapped_time = int((np.round((np.log10(time)),decimals=2)-(-8))/0.01)
                    matrix[mapped_size, mapped_time] = pdf_value
    
    # 寫入CSV檔案
    output_file_path = 'C:/Users/APPLE/Desktop/Final_Project/matrix.csv'
    with open(output_file_path, 'w') as file:
        for row in matrix:
            row_str = ','.join(map(str, row))
            file.write(row_str + '\n')
    
    print("機率密度函數值矩陣已寫入CSV檔案:", output_file_path)

filepath = 'C:/Users/APPLE/Desktop/Final_Project/TEST_NonVPNcsv-03/'
mean_size, mean_time, var_size, var_time = calculate_mean_var(filepath)
pdf_generation(filepath, mean_size, mean_time, var_size, var_time)
