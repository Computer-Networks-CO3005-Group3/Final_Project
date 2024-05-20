import numpy as np
import csv
import os
from tqdm import tqdm

def get_Z_sequence(F, pdf_vector):
    Z_sequence = []
    for i, packet in enumerate(F, start=1):
        s_i, t_i = packet
        # find z_i
        row = s_i - 40
        col=int((np.round((np.log10(t_i)),decimals=2)-(-8))/0.01)
        Zi = pdf_vector[row][col]
        Z_sequence.append(Zi)
        

    return Z_sequence

def calculate_anomaly_score(z_sequence, l_pdf, l_f, epsilon=1e-156):###
    # Zi to Ai
    a_sequence = [1 / (z) if z > 0 else 1 / epsilon for z in z_sequence]
    # Amin Amax N_sects
    a_min = 1
    a_max = 1 / epsilon
    n_sects = min(l_pdf, l_f)
    # Sn
    s_n_list = []
    s_n = 0
    for i in range(0, n_sects):
        s_n += (a_sequence[i] - a_min) / (a_max - a_min)
        s_n_list.append(s_n)
    return s_n_list, n_sects

def read_pdf_matrix_2(pdf_file_path):
    #npz
    data = np.load(pdf_file_path)
    pdf_vector = data['matrix']
    return pdf_vector

def read_pdf_matrix_1(pdf_file_path):
    #csv
    pdf_vector = np.loadtxt(pdf_file_path, delimiter=',')
    print("Matrix的形狀:", pdf_vector.shape)
    return pdf_vector


def classify_traffic(s_n, T=1):
    if s_n < T:
        new_class = 'regular http traffic'
    else:
        new_class = 'tunneling http traffic'
    return new_class

def process_csv_files(input_directory, pdf_file_path, output_directory):
    ###
    pdf_vector = read_pdf_matrix_1(pdf_file_path)
    #print("Matrix的形狀:", pdf_vector.shape)
    n_sects_list = []

    for filename in tqdm(os.listdir(input_directory)):
        if filename.endswith('.csv'):
            input_file_path = os.path.join(input_directory, filename)
            with open(input_file_path, 'r') as f:
                
                reader = csv.reader(f)
                next(reader)
                src_ip, dest_ip, _, _, original_class = next(reader)

                f.seek(0)
                reader = csv.reader(f)
                next(reader)
                F = [(int(pkt_size), float(time_diff)) for src_ip, dest_ip, pkt_size, time_diff, original_class in reader]

                z_sequence = get_Z_sequence(F, pdf_vector)
                l_f = len(F)
                l_pdf = len(pdf_vector)
                s_n_list, n_sects = calculate_anomaly_score(z_sequence, l_pdf, l_f)
                n_sects_list.append(n_sects)

                for i, s_n in enumerate(s_n_list, start=0):
                    new_class = classify_traffic(s_n)
                    output_csv_path = os.path.join(output_directory, f"output_{i+2}.csv")
                    with open(output_csv_path, 'a', newline='') as f:
                        fieldnames = ['src_ip', 'dest_ip', 'original_class', 'z_n', 's_n', 'new_class']
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        if os.stat(output_csv_path).st_size == 0:
                            writer.writeheader()
                        writer.writerow({'src_ip': src_ip, 'dest_ip': dest_ip, 'original_class': original_class, 'z_n': z_sequence[i], 's_n': s_n, 'new_class': new_class})
            
    min_n_sects = min(n_sects_list)
    print(n_sects_list)
    print(min_n_sects)

# TEST
#input_directory = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/Final_Project/Training_Data/'
input_directory = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/Final_Project/Testing_Data/'
output_directory = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/Anomaly_Score3/'
#pdf_file_path = 'D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/pdf_matrix.npz'
pdf_file_path = "D:/EMILY/emily/ncu/112-2/CO3005/Computer_Networks_Final_Project/matrix_3.csv"

process_csv_files(input_directory, pdf_file_path, output_directory)