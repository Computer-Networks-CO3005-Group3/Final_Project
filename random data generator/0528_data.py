import csv
import random
from IPython.display import FileLink
from IPython.display import HTML

def generate_data(num_records):
    data = []
    for _ in range(num_records):
        packet_size = random.randint(40, 12000)
        time_interval = 10**(random.uniform(-1, 4))
        data.append((packet_size, time_interval))
    return data

def save_to_csv(data, filename):
    with open(filename, mode='w') as file:
        for row in data:
            row_str = ','.join(map(str, row))
            file.write(row_str + '\n')
if __name__ == "__main__":
    num_records = 5000
    filename = '0531_data2/NONVPN_train_5000_data.csv'
    
    data = generate_data(num_records)
    save_to_csv(data, filename)

    print(f"Generated {num_records} records and saved to {filename}")

# 顯示下載鏈接
FileLink('packet_data.csv')
# 明確指定mime類型為text/csv

# 顯示下載鏈接，強制mime類型
HTML('<a download="NONVPN_train_5000_data.csv" href="0531_data2/NONVPN_train_5000_data.csv">Download CSV file</a>')
