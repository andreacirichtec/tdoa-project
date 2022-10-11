import pandas as pd
import numpy as np
from constellations import *

# change these addresses and file names
# src_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial2-tdoa2-results-scipynm.xlsx"
tdoa_src_address1 = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial1-tdoa2-results-corrected-random.xlsx"
tdoa_src_address2 = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial2-tdoa2-results-corrected-random.xlsx"
tdoa_src_address3 = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial3-tdoa2-results-corrected-random.xlsx"
tdoa_src_address4 = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial4-tdoa2-results-corrected-random.xlsx"
tdoa_src_address5 = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial5-tdoa2-results-corrected-random.xlsx"
tdoa_src_address6 = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial6-tdoa2-results-corrected-random.xlsx"

read_data1 = pd.read_excel(tdoa_src_address1)
read_data2 = pd.read_excel(tdoa_src_address2)
read_data3 = pd.read_excel(tdoa_src_address3)
read_data4 = pd.read_excel(tdoa_src_address4)
read_data5 = pd.read_excel(tdoa_src_address5)
read_data6 = pd.read_excel(tdoa_src_address6)

gd_x_arr = []; gd_y_arr = []; gd_z_arr = []; gd_error_arr = []; t_tdoa_arr = []
nm_x_arr = []; nm_y_arr = []; nm_z_arr = []; nm_error_arr = []

num_tdoa1 = len(read_data1)-1
num_tdoa2 = len(read_data2)-1
num_tdoa3 = len(read_data3)-1
num_tdoa4 = len(read_data4)-1
num_tdoa5 = len(read_data5)-1
num_tdoa6 = len(read_data6)-1

j = 0

for i in range(0, num_tdoa1):
    gd_error_arr.append(read_data1.iloc[i,1])
    nm_error_arr.append(read_data1.iloc[i,6])

for i in range(0, num_tdoa2):
    gd_error_arr.append(read_data2.iloc[i,1])
    nm_error_arr.append(read_data2.iloc[i,6])

for i in range(0, num_tdoa3):
    gd_error_arr.append(read_data3.iloc[i,1])
    nm_error_arr.append(read_data3.iloc[i,6])

for i in range(0, num_tdoa4):
    gd_error_arr.append(read_data4.iloc[i,1])
    nm_error_arr.append(read_data4.iloc[i,6])

for i in range(0, num_tdoa5):
    gd_error_arr.append(read_data5.iloc[i,1])
    nm_error_arr.append(read_data5.iloc[i,6])

for i in range(0, num_tdoa6):
    gd_error_arr.append(read_data6.iloc[i,1])
    nm_error_arr.append(read_data6.iloc[i,6])

print("Srednja vrednost greške gd = ", np.mean(gd_error_arr))
print("Standardna devijacija greške gd = ", np.std(gd_error_arr))
print("Srednja vrednost greške nm = ", np.mean(nm_error_arr))
print("Standardna devijacija greške nm = ", np.std(nm_error_arr))