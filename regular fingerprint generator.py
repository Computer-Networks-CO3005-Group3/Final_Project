import csv
import random
import numpy as np
from scipy.stats import multivariate_normal
from IPython.display import FileLink
from IPython.display import HTML

def generate_data(num_records):
    data = []
    for _ in range(num_records):
        packet_size = random.randint(40, 1500)
        time_interval = 10**(random.uniform(-7, 3))
        data.append((packet_size, time_interval))
    return data

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Packet Size', 'Time Interval'])  # 包含標頭
        writer.writerows(data)

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
        next(reader)  # 跳過標頭
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
        next(reader)  # 跳過標頭
        for row in reader:
            size = int(row[0])
            time = float(row[1])
            if time <= 0:
                continue
            pdf_value = mv_normal.pdf([size, time])
            # 將映射後的值寫入矩陣中
            mapped_size = round((size-40)*500/30960)
            mapped_time = int((np.round((np.log10(time)),decimals=2)-(-8))/0.01*500/1300)
            '''
            mapped_size = size - 40
            mapped_time = int(np.log10(time) * 100 + 700)
            '''
            if 0 <= mapped_size < matrix.shape[0] and 0 <= mapped_time < matrix.shape[1]:
                matrix[mapped_size, mapped_time] = pdf_value

    # 對PDF矩陣進行歸一化
    matrix /= matrix.sum()

    min_nonzero_value = np.min(matrix[np.nonzero(matrix)])
    print(f"PDF矩陣中非零的最小值為: {min_nonzero_value}")

    # 寫入CSV檔案
    #output_file_path = 'matrix.csv'
    #with open(output_file_path, 'w', newline='') as file:
        #writer = csv.writer(file)
        #for row in matrix:
           # writer.writerow(row)
        # 寫入CSV檔案
    output_file_path = 'matrix.csv'
    with open(output_file_path, 'w') as file:
        for row in matrix:
            row_str = ','.join(map(str, row))
            file.write(row_str + '\n')

    print(f"PDF矩陣元素範圍: {matrix.min()} - {matrix.max()}")
    print(f"PDF矩陣元素總和: {matrix.sum()}")

    print("機率密度函數值矩陣已寫入CSV檔案:", output_file_path)

if __name__ == "__main__":
    num_records = 200000  # 修改這裡以生成 5000 筆資料
    input_filename = 'packet_data.csv'

    # 生成數據並保存到CSV文件
    data = generate_data(num_records)
    save_to_csv(data, input_filename)
    print(f"Generated {num_records} records and saved to {input_filename}")

    # 計算平均值和方差
    mean_size, mean_time, var_size, var_time, cov_size_time = calculate_mean_var(input_filename)

    # 生成PDF矩陣並保存到CSV文件
    pdf_generation(input_filename, mean_size, mean_time, var_size, var_time, cov_size_time)
    
# 顯示下載鏈接
FileLink('matrix.csv')
# 明確指定mime類型為text/csv

# 顯示下載鏈接，強制mime類型
HTML('<a download="matrix.csv" href="matrix.csv">Download CSV file</a>')
