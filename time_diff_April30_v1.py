import os
import pyshark
import csv
from collections import defaultdict
from pathlib import Path

class PcapAnalyzer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.http_packets = []

    def analyze_pcap_files(self):
        # Iterate through each file in the folder
        for filename in os.listdir(self.folder_path):
            print("****************************************************\n")
            if filename.endswith(('.pcap', '.pcapng')):
                filepath = os.path.join(self.folder_path, filename)
                self.analyze_pcap_file(filepath, filename)
        print("[folder  end]")

    def analyze_pcap_file(self, filepath, filename):
        # Open the pcap file
        cap = pyshark.FileCapture(filepath)
        count = 1
        # Initialize the query table
        query_table = defaultdict(list)
        print("[analyzing]", filename)
        # Filter HTTP packets and extract relevant features
        print("pkt", end=" ")
        for packet in cap:
            if 'http' in packet:
                print(count, end=" ")
                source_ip = packet.ip.src
                destination_ip = packet.ip.dst
                timestamp = packet.sniff_time.timestamp()

                # Check if the source_ip and destination_ip exist in the query table
                if (source_ip, destination_ip) in query_table:
                    # Calculate the time difference between the current packet and the last entry
                    time_diff = timestamp - query_table[(source_ip, destination_ip)][-1]
                    query_table[(source_ip, destination_ip)][-1] = timestamp

                else:
                    # No entry found, add a new entry with time_diff as 0
                    time_diff = 0.0
                    query_table[(source_ip, destination_ip)].append(timestamp)

                http_packet = {
                    # 'source_ip': source_ip,
                    # 'destination_ip': destination_ip,
                    'packet_size': packet.length,
                    'time_diff': time_diff
                }

                self.http_packets.append(http_packet)
                count += 1
        print("\n")
        print("[analyze end]", filename)
        self.save_to_csv(self.http_packets, filename)
        cap.close()

    def save_to_csv(self, http_packets, filename):
        print("[writing csv]", filename)
        # fieldnames = ['source_ip', 'destination_ip', 'packet_size', 'time_diff']
        fieldnames = ['packet_size', 'time_diff']
        # 構建CSV文件的完整路徑
        desktop_path = Path.home() / "C:/Users/User/Desktop"
        csv_filepath = desktop_path / f"{filename.replace('.pcap', '').replace('.pcapng', '')}.csv"

        with open(csv_filepath, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # 寫入欄位名稱
            writer.writeheader()

            # 逐個dict寫入CSV文件
            for packet in http_packets:
                writer.writerow(packet)
        print("[writing end]")

# Usage
folder_path = 'C:/Users/User/Desktop/Testpcap_folder'
analyzer = PcapAnalyzer(folder_path)
analyzer.analyze_pcap_files()

# Access the HTTP packets data
http_packets = analyzer.http_packets
print("END")
