import numpy as np
from collections import defaultdict
import csv
from pathlib import Path

class HTTPFingerprint:
#########################根據實際HTTP流量，構建PDF矩陣
    def __init__(self, packet_limit=40, time_delta_bins=1001, max_packet_size=1500, max_time_delta=10**3): # 只考慮40個封包, 控制fingerprint長度
        self.packet_limit = packet_limit  # 指紋長度
        self.time_delta_bins = time_delta_bins # 將時間(10^-7到10^3)量化(預設1001)
        self.max_packet_size = max_packet_size # 封包大小的上限(1500)
        self.max_time_delta = max_time_delta # 時間間隔的上限
        self.pdfs = []  # 儲存PDF矩陣

    def train(self, csv_filepath):
        # 根據 HTTP 流量 CSV 文件構建fingerprint
        traffic_traces = self.read_traffic_traces(csv_filepath) # 從CSV文件路徑中讀取HTTP數據
        packet_stats = defaultdict(lambda: defaultdict(lambda: [0, 0])) # 初始化packet_stats，為了統計每個封包大小和時間間隔
        for trace in traffic_traces:
            prev_time = 0
            for i, (size, time) in enumerate(trace):
                if i >= self.packet_limit:
                    break
                delta_t = time - prev_time # 計算時間間隔
                prev_time = time
                packet_stats[i][size][0] += 1  # 計數封包大小
                packet_stats[i][size][1] += delta_t  # 累加時間間隔

        for packet_id in range(self.packet_limit): # 構建二維pdf
            pdf = np.zeros((self.max_packet_size - 40 + 1, self.time_delta_bins)) # 初始化一個pdf矩陣，形狀為(max_..., time_...)
            for size, (count, total_delta_t) in packet_stats[packet_id].items(): # 統計每個封包大小出現的次數(count)及時間間隔總和
                avg_delta_t = total_delta_t / count if count > 0 else 0 # 特定封包大小的平均時間間隔, 當count=0表示沒有出現過
                pdf[size - 40, int(np.log10(avg_delta_t) * 100)] = count # 將count填入pdf矩陣的對應位置,因封包最小為40,因此將實際大小減40以獲得矩陣的行位置
                # np.log10...,對平均時間進行離散化(-7~3),再*100放大，且取整數,對應到pdf列
            # 標準化PDF矩陣
            pdf /= np.sum(pdf) # 使總和為1

            # 平滑PDF矩陣
            pdf = self.smooth_pdf_matrix(pdf)

            self.pdfs.append(pdf)
###########################################################################
    def read_traffic_traces(self, csv_filepath):
        #從 CSV 文件中讀取 HTTP 流量數據
        traffic_traces = []
        with open(csv_filepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile) #加地址
            for row in reader: # 每一行對應一個trace，含pkt_size、t_diff
                trace = [(int(row['packet_size']), float(row['time_diff']))] # 將每行數據轉換為pkt_size、t_diff 
                traffic_traces.append(trace) # 加到traffic_trace列表
        return traffic_traces # 返回列表

    def smooth_pdf_matrix(self, pdf_matrix, sigma=0.8):
        window = np.outer(self.gaussian(51, sigma), self.gaussian(51, sigma)) # 計算二維高斯
        return np.apply_along_axis(lambda x: np.convolve(x, window, mode='same'), axis=-1, arr=pdf_matrix) # 對PDF矩陣的每一行應用卷積 np.convolve，mode = 'same'確保卷積結果的形狀不變

    @staticmethod
    def gaussian(size, sigma):
        x = np.arange(0, size, 1, float)
        y = np.exp(-((x - size // 2) ** 2) / (2 * sigma ** 2)) # 根據給定的size和sigma，計算高斯分佈的一維向量, //是整數除法,只取整數
        return y / np.sum(y)  #將向量normalized，使總和為1

    def get_fingerprint(self):
        return np.concatenate(self.pdfs) # 將self.pdfs列表中的所有PDF矩陣連接起來，形成最終HTTP Fingerprint

# 使用示例
#desktop_path = Path.home() / "Desktop"
#csv_filepath = desktop_path / "captured_traffic.csv"  # 假設已經使用 PcapAnalyzer 程式生成了這個 CSV 文件

#fingerprint = HTTPFingerprint()
#fingerprint.train(csv_filepath)
#http_fingerprint = fingerprint.get_fingerprint()
