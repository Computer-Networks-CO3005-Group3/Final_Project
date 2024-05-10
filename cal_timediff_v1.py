import csv
import os

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            source_ip, dest_ip, packet_size, arrival_time = row
            data.append((source_ip, dest_ip, int(packet_size), float(arrival_time)))
    return data

def process_data(data):
    query_table = {}
    result = []
    for source_ip, dest_ip, packet_size, arrival_time in data:
        key = (source_ip, dest_ip)
        if key in query_table:
            previous_time = query_table[key]
            time_diff = arrival_time - previous_time
            result.append({'source_ip': source_ip, 'dest_ip': dest_ip, 'packet_size': packet_size, 'time_diff': time_diff})
            query_table[key] = arrival_time
        else:
            query_table[key] = arrival_time
            result.append({'source_ip': source_ip, 'dest_ip': dest_ip, 'packet_size': packet_size, 'time_diff': 0})
    return result

def write_csv(input_file, data):
    output_file = os.path.join('C:/Users/User/Desktop/Pytsharkocsv_folder', os.path.basename(input_file).split('.')[0] + '_o.csv')
    fields = ['source_ip', 'dest_ip', 'packet_size', 'time_diff']
    with open(output_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(data)

def main():
    input_folder = 'C:\\Users\\User\\Desktop\\tsharkcsv_folder'
    for filename in os.listdir(input_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(input_folder, filename)
            data = read_csv(file_path)
            result = process_data(data)
            write_csv(file_path, result)

if __name__ == '__main__':
    main()
