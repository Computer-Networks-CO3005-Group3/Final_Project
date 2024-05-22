import csv

# 設定輸入和輸出檔案名稱
input_file = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/Final_Project/regular test data.csv'
output_file_prefix = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/Final_Project/Testing_Data/'

# 開啟輸入檔案
with open(input_file, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# 確保輸入檔案有2列
if len(data) != 50000:
    print("輸入檔案不是50000行")
    exit()

# 確保每一列有2個元素
for row in data:
    if len(row) != 2:
        print("每一列不是2個元素")
        exit()

# 拆分資料並寫入輸出檔案
for i in range(5000):
    output_file = f"{output_file_prefix}{i}.csv"
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['src_ip', 'dest_ip', 'pkt_size', 'time_diff', 'original_class'])
        start = i * 10
        end = start + 10
        for row in data[start:end]:
            writer.writerow(['0', '0', row[0], row[1], 'regular http traffic'])

print("完成！")