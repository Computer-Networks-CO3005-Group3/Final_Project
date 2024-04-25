import numpy as np
import math

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


def calculate_anomaly_score(z_sequence, i, l_pdf, l_f, epsilon=1e-8):
    
    # Zi to Ai
    a_sequence = [1 / (z + epsilon) if z > 0 else 1 / epsilon for z in z_sequence]
    
    # Amin Amax N_sects
    a_min = 1
    a_max = 1 / epsilon
    n_sects = min(l_pdf, l_f)
    
    # Sn
    s_n = 0
    for i in range(i, n_sects):
        s_n += (a_sequence[i] - a_min) / (a_max - a_min)
    
    return s_n

# test
Z_sequence = [0.8, 0.2, 0.1, 0.05, 0.9, 0.7]
L_f = len(Z_sequence) # lenth of F
L_pdf = 5 # lenth of PDF
I = 2
S_n = calculate_anomaly_score(Z_sequence, I, L_pdf, L_f)

print(f"S_n = {S_n}")