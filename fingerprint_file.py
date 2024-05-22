import numpy as np
import csv
from scipy.stats import multivariate_normal
from scipy.ndimage import gaussian_filter

def calculate_mean_var(file_path):
    # 初始化統計量
    total_size = 0
    total_time = 0
    total_packets = 0
    size_squares = 0
    time_squares = 0
    size_time_product = 0

    # 讀取CSV文件並計算統計量
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            size = int(row[0])
            time = float(row[1])
            total_size += size
            total_time += time
            size_squares += size ** 2
            time_squares += time ** 2
            size_time_product += size * time
            total_packets += 1

    # 計算平均值和方差
    mean_size = total_size / total_packets
    mean_time = total_time / total_packets
    var_size = size_squares / total_packets - mean_size ** 2
    var_time = time_squares / total_packets - mean_time ** 2
    cov_size_time = size_time_product / total_packets - mean_size * mean_time

    return mean_size, mean_time, var_size, var_time, cov_size_time

def pdf_generation(file_path, mean_size, mean_time, var_size, var_time, cov_size_time):
    # 計算多變量機率密度函數值
    mean = np.array([mean_size, mean_time])
    covariance_matrix = np.array([[var_size, cov_size_time], [cov_size_time, var_time]])
    mv_normal = multivariate_normal(mean=mean, cov=covariance_matrix)

    # 創建一個大小為30961x1301的矩陣
    matrix = np.zeros((501, 501))

    # 讀取CSV文件並計算機率密度函數值
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            size = int(row[0])
            time = float(row[1])
            if time <= 0:
                continue
            pdf_value = mv_normal.pdf([size, time])
            # 將映射後的值寫入矩陣中
            mapped_size = round((size-40)*500/30960)
            mapped_time = int((np.round((np.log10(time)),decimals=2)-(-8))/0.01*500/1300)
            matrix[mapped_size, mapped_time] = pdf_value

    # 對PDF矩陣進行歸一化
    matrix /= matrix.sum()

    # 對PDF矩陣應用二維高斯濾波器
    # sigma = 0.2 # 高斯核的標準差,可根據需要調整
    # filtered_matrix = gaussian_filter(matrix, sigma, mode='constant')
    # 確保濾波後的矩陣依然符合PDF性質(所有元素和為1)
    # filtered_matrix /= filtered_matrix.sum()

    min_nonzero_value = np.min(matrix[np.nonzero(matrix)])
    print(f"PDF矩陣中非零的最小值為: {min_nonzero_value}")

    # 寫入CSV檔案
    output_file_path = 'C:/Users/張/Desktop/Final_Project-main/matrix.csv'
    with open(output_file_path, 'w') as file:
        for row in matrix:
            row_str = ','.join(map(str, row))
            file.write(row_str + '\n')

    print(f"濾波前PDF矩陣元素範圍: {matrix.min()} - {matrix.max()}")
    print(f"濾波前PDF矩陣元素總和: {matrix.sum()}")

    # 繪製濾波前PDF矩陣
    # plt.figure()
    # plt.imshow(matrix, cmap='hot')
    # plt.colorbar()
    # plt.title('Unfiltered PDF Matrix')
    # plt.show()

    print("機率密度函數值矩陣已寫入CSV檔案:", output_file_path)

# 設置要讀取的單一CSV文件路徑
file_path = 'C:/Users/張/Desktop/final_project/packet_data.csv'
mean_size, mean_time, var_size, var_time, cov_size_time = calculate_mean_var(file_path)
pdf_generation(file_path, mean_size, mean_time, var_size, var_time, cov_size_time)
