import os
import pyshark


class PcapAnalyzer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.http_packets = []

    def analyze_pcap_files(self):
        # Iterate through each file in the folder
        for filename in os.listdir(self.folder_path):
            if filename.endswith('.pcap'):
                filepath = os.path.join(self.folder_path, filename)
                self.analyze_pcap_file(filepath)
        print("analyze_pcap_files End")
    def analyze_pcap_file(self, filepath):
        # Open the pcap file
        cap = pyshark.FileCapture(filepath)
        count=0
        # Filter HTTP packets and extract relevant features
        print("processing packets...")
        for packet in cap:
            if 'http' in packet:
                print(count)
                http_packet = {
                    'timestamp': packet.sniff_time.timestamp(),
                    'packet_size': packet.length,
                    'source_ip': packet.ip.src,
                    'destination_ip': packet.ip.dst,
                    'source_port': packet.tcp.srcport,
                    'destination_port': packet.tcp.dstport,
                    'http_method': packet.http.request_method if hasattr(packet.http, 'request_method') else None,
                    'http_host': packet.http.host if hasattr(packet.http, 'host') else None,
                    'http_uri': packet.http.request_uri if hasattr(packet.http, 'request_uri') else None
                }
                self.http_packets.append(http_packet)
                count+=1
        print("analyze_pcap_file End")
        cap.close()


# Usage
folder_path = 'C:/Users/User/Desktop/Testpcap_folder'
analyzer = PcapAnalyzer(folder_path)
analyzer.analyze_pcap_files()

# Access the HTTP packets data
http_packets = analyzer.http_packets
for item in http_packets:
    print(item)
print("End")
