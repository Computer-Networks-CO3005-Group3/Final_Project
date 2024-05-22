import csv
import os

def count_output_files(output_dir):
    file_count = 0
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            if file.endswith(".csv"):
                file_count += 1
    return file_count

def process_traffic_data(input_file, output_file, original_class):

    file_list = os.listdir(input_file)
    max_time_diff = float('-inf')
    min_time_diff = float('inf')
    max_pkt_size = float('-inf')
    min_pkt_size = float('inf')

    for filename in file_list:
        if filename.endswith('.csv'):
            input_file_path = os.path.join(input_file, filename)
            flows = {}
            

            # read_csv
            with open(input_file_path, 'r') as f:
                reader = csv.reader(f)
                next(reader)

                for src_ip, dest_ip, pkt_size, time_diff in reader:

                    if float(time_diff) > 0:
                        pkt_size = int(pkt_size)
                        time_diff = float(time_diff)
                        max_pkt_size = max(max_pkt_size, pkt_size)
                        min_pkt_size = min(min_pkt_size, pkt_size)
                        max_time_diff = max(max_time_diff, time_diff)
                        min_time_diff = min(min_time_diff, time_diff)

                        flow_key = (src_ip, dest_ip)
                        if flow_key not in flows:
                            flows[flow_key] = []
                        flows[flow_key].append({'pkt_size': int(pkt_size), 'time_diff': float(time_diff), 'original_class': original_class})
                    
                for flow_key, flow_data in flows.items():
                        
                    #flow_dir = os.path.join(output_file, filename)
                    #os.makedirs(flow_dir, exist_ok=True)
                    #output_file_path = os.path.join(flow_dir, f"{flow_key[0]}_{flow_key[1]}.csv")
                    output_file_path = os.path.join(output_file, f"{flow_key[0]}_{flow_key[1]}.csv")

                    # write_csv
                    with open(output_file_path, 'w', newline='') as f:
                        fieldnames = ['src_ip', 'dest_ip', 'pkt_size', 'time_diff', 'original_class']
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()

                        for packet in flow_data:
                            writer.writerow({'src_ip': flow_key[0], 'dest_ip': flow_key[1], 'pkt_size': packet['pkt_size'], 'time_diff': packet['time_diff'], 'original_class': packet['original_class']})

    print("\nFile output completed!!!\n")
    print(f"Max pkt_size: {max_pkt_size}")
    print(f"Min pkt_size: {min_pkt_size}")
    print(f"Max time_diff: {max_time_diff}")
    print(f"Min time_diff: {min_time_diff}")

# TEST
input_filepath = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/Final_Project/VPNcsv-01/'
output_filepath = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/Final_Project/Testing_Data/'

process_traffic_data(input_filepath, output_filepath, 'tunneling http trafficc')
#(例: regular http traffic 或 tunneling http traffic)

output_file_count = count_output_files(output_filepath)
print(f"Total output CSV files: {output_file_count}")