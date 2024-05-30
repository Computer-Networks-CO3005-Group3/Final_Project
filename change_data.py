import os
import csv
import numpy as np
import random
import shutil
from tqdm import tqdm

# 指定包含 CSV 文件的目录
input_directory = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/Final_Project/ME/Testing_Data_0528/'
output_directory = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/Final_Project/ME/'

# 新建一个文件夹
new_folder_name = 'Testing_Data_0528_N2/'
new_folder_path = os.path.join(output_directory, new_folder_name)
os.makedirs(new_folder_path, exist_ok=True)

# 遍历目录中的所有 CSV 文件，并显示进度条
for filename in tqdm(os.listdir(input_directory), desc="Processing files"):
    if filename.endswith('.csv'):
        input_file_path = os.path.join(input_directory, filename)
        output_file_path = os.path.join(new_folder_path, filename)
        
        # 检查文件名中是否包含判别码 't'
        if '_t' in filename:
            # 读取 CSV 文件
            with open(input_file_path, 'r') as csv_file:
                reader = csv.reader(csv_file)
                data = list(reader)
                
                # 随机生成新的值
                packet_size = random.randint(40, 12000)
                time_interval = 10**(random.uniform(-8, -2))
                
                
                # 修改第二行的第三列和第四列
                data[1][2] = packet_size
                data[1][3] = time_interval
                
                # 保存修改后的 CSV 文件
                with open(output_file_path, 'w', newline='') as new_csv_file:
                    writer = csv.writer(new_csv_file)
                    writer.writerows(data)
                    
                # tqdm.write(f"修改并保存了文件: {filename} 到 {output_file_path}")
        else:
            # 直接复制文件到新的路径
            shutil.copy(input_file_path, output_file_path)
            # tqdm.write(f"复制了文件: {filename} 到 {output_file_path}")

# tqdm.write("所有文件修改并保存完成。")

