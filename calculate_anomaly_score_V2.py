import numpy as np
import math
import csv
import os

def get_Z_sequence(F, pdf_vector):
    Z_sequence = []
    for i, packet in enumerate(F, start=1):
        s_i, t_i = packet
        # quantification
        log_t_i = math.log10(t_i)
        quant_t_i = round(log_t_i, -2)
        # find z_i
        pdf_matrix = pdf_vector[i-1]
        row = s_i - 40  # packet size ranges from 40 to 1500
        col = int((quant_t_i - (-7)) / 0.01)
        Zi = pdf_matrix[row][col]
        Z_sequence.append(Zi)
    return Z_sequence

def calculate_anomaly_score(z_sequence, l_pdf, l_f, epsilon=1e-8):
    # Zi to Ai
    a_sequence = [1 / (z + epsilon) if z > 0 else 1 / epsilon for z in z_sequence]
    # Amin Amax N_sects
    a_min = 1
    a_max = 1 / epsilon
    n_sects = min(l_pdf, l_f)
    # Sn
    s_n_list = []
    for i in range(1, n_sects + 1):
        s_n = 0
        for j in range(i, n_sects):
            s_n += (a_sequence[j] - a_min) / (a_max - a_min)
        s_n_list.append(s_n)
    return s_n_list

def read_pdf_matrix(pdf_file_path):
    pdf_vector = []
    with open(pdf_file_path, 'r') as f:
        reader = csv.reader(f)
        pdf_matrix = []
        for row in reader:
            pdf_matrix.append([float(value) for value in row])
        if len(pdf_matrix) == 1461 and len(pdf_matrix[0]) == 1001:
            pdf_vector.append(pdf_matrix)
        else:
            print(f"Warning: File {pdf_file_path} does not contain a 1461x1001 matrix.")
    return pdf_vector

def classify_traffic(s_n, T=1):
    if s_n < T:
        new_class = 'regular http traffic'
    else:
        new_class = 'tunneling http traffic'
    return new_class

def process_csv_files(input_directory, pdf_file_path, output_directory):
    pdf_vector = read_pdf_matrix(pdf_file_path)

    for filename in os.listdir(input_directory):
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
                s_n_list = calculate_anomaly_score(z_sequence, l_pdf, l_f)

                for i, s_n in enumerate(s_n_list, start=1):
                    new_class = classify_traffic(s_n)
                    output_csv_path = os.path.join(output_directory, f"output_{i}.csv")
                    with open(output_csv_path, 'a', newline='') as f:
                        fieldnames = ['src_ip', 'dest_ip', 'original_class', 's_n', 'new_class']
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        if os.stat(output_csv_path).st_size == 0:
                            writer.writeheader()
                        writer.writerow({'src_ip': src_ip, 'dest_ip': dest_ip, 'original_class': original_class, 's_n': s_n, 'new_class': new_class})

# TEST
input_directory = '/path/to/input/csv/files'
output_directory = '/path/to/output/directory'
pdf_file_path = '/path/to/pdf/matrix.csv'

process_csv_files(input_directory, pdf_file_path, output_directory)