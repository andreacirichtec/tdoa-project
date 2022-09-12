import math
from sqlite3 import Timestamp
import time
import pandas as pd
from data.constellations import *
from gradient_descent import gradient_descent_f
from statistics import mean

from nelder_mead import nelder_mead_f

# change these addresses and file names
src_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial6-tdoa3-extracted.xlsx"
dst_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial6-tdoa3-results-updated.xlsx"
describe_dst_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial6-tdoa3-results-updated-describe.xlsx"

# read data from the csv file
read_data = pd.read_excel(src_address)

idA0_arr = []; idB0_arr = []; idA1_arr = []; idB1_arr = []; idA2_arr = []; idB2_arr = []
gd_errors = []; gd_x_arr = []; gd_y_arr = []; gd_z_arr = []; gd_time_arr = []
nm_errors = []; nm_x_arr = []; nm_y_arr = []; nm_z_arr = []; nm_time_arr = []
position_x_arr = []; position_y_arr = []; position_z_arr = []; timestamp_arr = []
num = len(read_data)-2
i = 0

while (i < num): #možda treba korak da bude 3, ali sa korakom 1 ima više len(read_data)-2
     k = 1
     rec0 = Recording(read_data.iloc[i,0], read_data.iloc[i,1], read_data.iloc[i,2], read_data.iloc[i,3], read_data.iloc[i,4], read_data.iloc[i,5], read_data.iloc[i,6])
     rec1 = Recording(read_data.iloc[i+k,0], read_data.iloc[i+k,1], read_data.iloc[i+k,2], read_data.iloc[i+k,3], read_data.iloc[i+k,4], read_data.iloc[i+k,5], read_data.iloc[i,6])
     while ((rec0.idA == rec1.idA) and (rec0.idB == rec1.idB)) or ((rec0.idA == rec1.idB) and (rec0.idB == rec1.idA)):
          k += 1
          rec1 = Recording(read_data.iloc[i+k,0], read_data.iloc[i+k,1], read_data.iloc[i+k,2], read_data.iloc[i+k,3], read_data.iloc[i+k,4], read_data.iloc[i+k,5], read_data.iloc[i,6])
          num -= 1
     k += 1
     rec2 = Recording(read_data.iloc[i+k,0], read_data.iloc[i+k,1], read_data.iloc[i+k,2], read_data.iloc[i+k,3], read_data.iloc[i+k,4], read_data.iloc[i+k,5], read_data.iloc[i,6])
     while ((rec0.idA == rec2.idA) and (rec0.idB == rec2.idB)) or ((rec0.idA == rec2.idB) and (rec0.idB == rec2.idA)) or ((rec1.idA == rec2.idA) and (rec1.idB == rec2.idB)) or ((rec1.idA == rec2.idB) and (rec1.idB == rec2.idA)):
          k += 1
          rec2 = Recording(read_data.iloc[i+k,0], read_data.iloc[i+k,1], read_data.iloc[i+k,2], read_data.iloc[i+k,3], read_data.iloc[i+k,4], read_data.iloc[i+k,5], read_data.iloc[i,6])
          num -= 1
     i += 1

     idA0_arr.append(rec0.idA)
     idB0_arr.append(rec0.idB)
     idA1_arr.append(rec1.idA)
     idB1_arr.append(rec1.idB)
     idA2_arr.append(rec2.idA)
     idB2_arr.append(rec2.idB)
     position_x_arr.append((rec0.x + rec1.x + rec2.x)/3)
     position_y_arr.append((rec0.y + rec1.y + rec2.y)/3)
     position_z_arr.append((rec0.z + rec1.z + rec2.z)/3)
     timestamp_arr.append((rec0.timestamp + rec1.timestamp + rec2.timestamp)/3)

     estimated_position = Point(rec2.x, rec2.y, rec2.z) #RANDOM TAČKA U PROSTORU
     
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

data = {'GD errors':gd_errors, 'GD x estimated':gd_x_arr, 'GD y estimated':gd_y_arr, 'GD z estimated':gd_z_arr, 'GD execution time':gd_time_arr, 'NM errors':nm_errors, 'NM x estimated':nm_x_arr, 'NM y estimated':nm_y_arr, 'NM z estimated':nm_z_arr, 'NM execution time':nm_time_arr, 'idA0':idA0_arr, 'idB0':idB0_arr, 'idA1':idA1_arr, 'idB1':idB1_arr, 'idA2':idA2_arr, 'idB2':idB2_arr, 'x position':position_x_arr, 'y position':position_y_arr, 'z position':position_z_arr, 'timestamp':timestamp_arr}
df = pd.DataFrame(data)

df.to_excel(dst_address, sheet_name="Data")

print(df.describe())

df2 = pd.DataFrame(df.describe())
df2.to_excel(describe_dst_address, sheet_name="Describe data")

print("DONE!")