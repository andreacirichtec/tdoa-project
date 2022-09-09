import math
import time
import pandas as pd
from data.constellations import *
from gradient_descent import gradient_descent_f
from statistics import mean

from nelder_mead import nelder_mead_f

# change these addresses and file names
src_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial1-tdoa2-extracted.xlsx"
dst_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial1-tdoa2-results.xlsx"

# read data from the csv file
read_data = pd.read_excel(src_address)
gd_errors = []; gd_x_arr = []; gd_y_arr = []; gd_z_arr = []; gd_time_arr = []
nm_errors = []; nm_x_arr = []; nm_y_arr = []; nm_z_arr = []; nm_time_arr = []

for i in range(0, len(read_data)-2, 1): #možda treba korak da bude 3, ali sa korakom 1 ima više len(read_data)-2
     rec0 = Recording(read_data.iloc[i,0], read_data.iloc[i,1], read_data.iloc[i,2], read_data.iloc[i,3], read_data.iloc[i,4],read_data.iloc[i,5])
     rec1 = Recording(read_data.iloc[i+1,0], read_data.iloc[i+1,1], read_data.iloc[i+1,2], read_data.iloc[i+1,3], read_data.iloc[i+1,4],read_data.iloc[i+1,5])
     rec2 = Recording(read_data.iloc[i+2,0], read_data.iloc[i+2,1], read_data.iloc[i+2,2], read_data.iloc[i+2,3], read_data.iloc[i+2,4],read_data.iloc[i+2,5])

     estimated_position = Point(rec2.x, rec2.y, rec2.z)
     
     time1 = time.time()
     gd_position, gd_error = gradient_descent_f(constellation1, rec0, rec1, rec2, estimated_position)
     time2 = time.time()
     gd_time = time2-time1

     gd_time_arr.append(gd_time)
     gd_errors.append(gd_error)
     gd_x_arr.append(gd_position.x)
     gd_y_arr.append(gd_position.y)
     gd_z_arr.append(gd_position.z)

     time3 = time.time()
     nm_position, nm_error = nelder_mead_f(constellation1, rec0, rec1, rec2, estimated_position)
     time4 = time.time()
     nm_time = time4-time3

     nm_time_arr.append(nm_time)
     nm_errors.append(nm_error)
     nm_x_arr.append(nm_position.x)
     nm_y_arr.append(nm_position.y)
     nm_z_arr.append(nm_position.z)
     
     print(i)
     # print("gradient descent error =", gd_error)
     # print("nelder mead error =", nm_error)
     # print("timegd =", gd_time)
     # print("timenm =", nm_time)

data = {'GD errors':gd_errors, 'GD x estimated':gd_x_arr, 'GD y estimated':gd_y_arr, 'GD z estimated':gd_z_arr, 'GD execution time':gd_time_arr, 'NM errors':nm_errors, 'NM x estimated':nm_x_arr, 'NM y estimated':nm_y_arr, 'NM z estimated':nm_z_arr, 'NM execution time':nm_time_arr}
df = pd.DataFrame(data)

df.to_excel(dst_address, index=False)

print(df.describe())

print("DONE!")