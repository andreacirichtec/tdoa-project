from cmath import inf
import random
import time
import pandas as pd
from random import random
from scipy.optimize import minimize
from cmath import inf

from data.constellations import *
from gradient_descent import gradient_descent_f
from nelder_mead import nelder_mead_f

# change these addresses and file names
# src_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial2-tdoa2-extracted.xlsx"
# dst_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial2-tdoa2-results-scipynm.xlsx"
# describe_dst_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial2-tdoa2-results-scipynm-describe.xlsx"

src_address = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial6-tdoa2-extracted.xlsx"
dst_address = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial6-tdoa2-results-corrected-random10.xlsx"
describe_dst_address = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial6-tdoa2-results-corrected-random10-describe.xlsx"

# read data from the csv file
read_data = pd.read_excel(src_address)

idA0_arr = []; idB0_arr = []; idA1_arr = []; idB1_arr = []; idA2_arr = []; idB2_arr = []
# idA3_arr = []; idB3_arr = []; idA4_arr = []; idB4_arr = []; idA5_arr = []; idB5_arr = []; idA6_arr = []; idB6_arr = []; idA7_arr = []; idB7_arr = []
gd_errors = []; gd_x_arr = []; gd_y_arr = []; gd_z_arr = []; gd_time_arr = []
nm_errors = []; nm_x_arr = []; nm_y_arr = []; nm_z_arr = []; nm_time_arr = []
position_x_arr = []; position_y_arr = []; position_z_arr = []; tdoa_timestamp_arr = []; pos_timestamp_arr = []

num_tdoa = len(read_data)-2
num_pos = len(read_data[read_data["t_pose"].notna()])-1

i = 0
j = 0

while (i < num_tdoa): #možda treba korak da bude 3, ali sa korakom 1 ima više len(read_data)-2
     
     print(i, "of", num_tdoa)
     get_recordings_tdoa(read_data, i)

     min_x = -5; max_x = 5
     min_y = -5; max_y = 5
     min_z = 0; max_z = 4
     randx = min_x + (random() * (max_x - min_x))
     randy = min_y + (random() * (max_y - min_y))
     randz = min_z + (random() * (max_z - min_z))

     #estimated_position = Point(rec2_pos.x, rec2_pos.y, rec2_pos.z) 
     estimated_position = Point(randx, randy, randz) #RANDOM TAČKA U PROSTORU

     time1 = time.time()
     gd_position, gd_error = gradient_descent_f(estimated_position)
     time2 = time.time()
     gd_time = time2-time1

     gd_time_arr.append(gd_time)
     gd_errors.append(gd_error)
     gd_x_arr.append(gd_position.x)
     gd_y_arr.append(gd_position.y)
     gd_z_arr.append(gd_position.z)

     # if (i==0):
     #      estimated_position_nm = [randx, randy, randz]
     nm_result_final = []
     nm_result_error = inf
     time3 = time.time()
     for j in range(10):
          randx = min_x + (random() * (max_x - min_x))
          randy = min_y + (random() * (max_y - min_y))
          randz = min_z + (random() * (max_z - min_z))
          estimated_position_nm = [randx, randy, randz]
          # print("random point = ", estimated_position_nm)

          #nm_position, nm_error = nelder_mead_f(estimated_position_nm)
          nm_result = minimize(error_f_nm, estimated_position_nm, method='Nelder-Mead', tol=1e-6)
          # print("greska = ",nm_result.fun)
          # print("estimirana tacka = (", nm_result.x[0], ",", nm_result.x[1], ",", nm_result.x[2], ")")

          if (nm_result.fun < nm_result_error):
               nm_result_final = nm_result.x
               nm_result_error = nm_result.fun
               # print("menjam tacku")
          
     time4 = time.time()
     nm_time = time4-time3


     nm_time_arr.append(nm_time)
     nm_errors.append(nm_result_error)
     nm_x_arr.append(nm_result_final[0])
     nm_y_arr.append(nm_result_final[1])
     nm_z_arr.append(nm_result_final[2])

     
     idA0_arr.append(rec0_tdoa.idA)
     idB0_arr.append(rec0_tdoa.idB)
     idA1_arr.append(rec1_tdoa.idA)
     idB1_arr.append(rec1_tdoa.idB)
     idA2_arr.append(rec2_tdoa.idA)
     idB2_arr.append(rec2_tdoa.idB)
     tdoa_timestamp_arr.append((rec0_tdoa.timestamp + rec1_tdoa.timestamp + rec2_tdoa.timestamp)/3)
     # idA3_arr.append(rec3_tdoa.idA)
     # idB3_arr.append(rec3_tdoa.idB)
     # idA4_arr.append(rec4_tdoa.idA)
     # idB4_arr.append(rec4_tdoa.idB)
     # idA5_arr.append(rec5_tdoa.idA)
     # idB5_arr.append(rec5_tdoa.idB)
     # idA6_arr.append(rec6_tdoa.idA)
     # idB6_arr.append(rec6_tdoa.idB)
     # idA7_arr.append(rec7_tdoa.idA)
     # idB7_arr.append(rec7_tdoa.idB)
     # position_x_arr.append((rec0.x + rec1.x + rec2.x + rec3.x + rec4.x + rec5.x + rec6.x + rec7.x)/8)
     # position_y_arr.append((rec0.y + rec1.y + rec2.y + rec3.y + rec4.y + rec5.y + rec6.y + rec7.y)/8)
     # position_z_arr.append((rec0.z + rec1.z + rec2.z + rec3.z + rec4.z + rec5.z + rec6.z + rec7.z)/8)
     # timestamp_arr.append((rec0_tdoa.tdoa_timestamp + rec1_tdoa.tdoa_timestamp + rec2_tdoa.tdoa_timestamp + rec3_tdoa.tdoa_timestamp + rec4_tdoa.tdoa_timestamp + rec5_tdoa.tdoa_timestamp + rec6_tdoa.tdoa_timestamp + rec7_tdoa.tdoa_timestamp)/8)
     
     # print()
     i += 1


# data = {'GD errors':gd_errors, 'GD x estimated':gd_x_arr, 'GD y estimated':gd_y_arr, 'GD z estimated':gd_z_arr, 'GD execution time':gd_time_arr, 'NM errors':nm_errors, 'NM x estimated':nm_x_arr, 'NM y estimated':nm_y_arr, 'NM z estimated':nm_z_arr, 'NM execution time':nm_time_arr, 'idA0':idA0_arr, 'idB0':idB0_arr, 'idA1':idA1_arr, 'idB1':idB1_arr, 'idA2':idA2_arr, 'idB2':idB2_arr, 'idA3':idA3_arr, 'idB3':idB3_arr, 'idA4':idA4_arr, 'idB4':idB4_arr, 'idA5':idA5_arr, 'idB5':idB5_arr, 'idA6':idA6_arr, 'idB6':idB6_arr, 'idA7':idA7_arr, 'idB7':idB7_arr, 'tdoa timestamp':tdoa_timestamp_arr, 'x position':position_x_arr, 'y position':position_y_arr, 'z position':position_z_arr, 'pos timestamp':pos_timestamp_arr}
data = {'GD errors':gd_errors, 'GD x estimated':gd_x_arr, 'GD y estimated':gd_y_arr, 'GD z estimated':gd_z_arr, 'GD execution time':gd_time_arr, 'NM errors':nm_errors, 'NM x estimated':nm_x_arr, 'NM y estimated':nm_y_arr, 'NM z estimated':nm_z_arr, 'NM execution time':nm_time_arr, 'idA0':idA0_arr, 'idB0':idB0_arr, 'idA1':idA1_arr, 'idB1':idB1_arr, 'idA2':idA2_arr, 'idB2':idB2_arr, 'tdoa timestamp':tdoa_timestamp_arr}
df = pd.DataFrame(data)

df.to_excel(dst_address, sheet_name="Data")

print(df.describe())

df2 = pd.DataFrame(df.describe())
df2.to_excel(describe_dst_address, sheet_name="Describe data")

print("DONE!")