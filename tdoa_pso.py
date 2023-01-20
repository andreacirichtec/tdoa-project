from cmath import inf
import random
import time
import pandas as pd
import random
from scipy.optimize import minimize
from cmath import inf

from pso import *
from data.constellations import *
from gradient_descent import gradient_descent_f


# change these addresses and file names
# windows
# src_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial2-tdoa2-extracted.xlsx"
# dst_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial2-tdoa2-results-pso20200.xlsx"
# describe_dst_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial2-tdoa2-results-pso20200-describe.xlsx"

# macOS
src_address = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial1-tdoa2-extracted.xlsx"
dst_address = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial1-tdoa2-results-pso20200.xlsx"
describe_dst_address = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial1-tdoa2-results-pso20200-describe.xlsx"

# read data from the csv file
read_data = pd.read_excel(src_address)

idA0_arr = []; idB0_arr = []; idA1_arr = []; idB1_arr = []; idA2_arr = []; idB2_arr = []
gd_errors = []; gd_x_arr = []; gd_y_arr = []; gd_z_arr = []; gd_time_arr = []
pso_errors = []; pso_x_arr = []; pso_y_arr = []; pso_z_arr = []; pso_time_arr = []
position_x_arr = []; position_y_arr = []; position_z_arr = []; tdoa_timestamp_arr = []; pos_timestamp_arr = []
num_iterations_arr = []

num_tdoa = len(read_data)-2
bounds = [(-5,5),(-5,5),(0,4)]

i = 0
j = 0

timestamp1 = 0
timestamp2 = 0
speed_limit = 98 #The Batmobile speed

pso_result_final = []
pso_result_temp = []
last_five_x = []; last_five_y = []; last_five_z = []

while (i < 1000): #možda treba korak da bude 3, ali sa korakom 1 ima više len(read_data)-2
     
     print(i, "of", num_tdoa)
     get_recordings_tdoa(read_data, i)

     timestamp2 = rec2_tdoa.timestamp
     distance_limit = (timestamp2 - timestamp1)*speed_limit
     timestamp1 = rec0_tdoa.timestamp

     min_x = -5; max_x = 5
     min_y = -5; max_y = 5
     min_z = 0; max_z = 4
     randx = min_x + (random.random() * (max_x - min_x))
     randy = min_y + (random.random() * (max_y - min_y))
     randz = min_z + (random.random() * (max_z - min_z))

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

     pso_result_error = inf
     time3 = time.time()
     num_iterations = 0

     while True:
          randx = min_x + (random.random() * (max_x - min_x))
          randy = min_y + (random.random() * (max_y - min_y))
          randz = min_z + (random.random() * (max_z - min_z))
          estimated_position_pso = [randx, randy, randz]

          pso_result, pso_result_error = PSO(error_f_pso,estimated_position_pso,bounds,num_particles=20,maxiter=200)
          num_iterations+=1

          if (i < 5) and (pso_result_error < distance_limit):
               pso_result_final = pso_result
               break

          if (pso_result_error < distance_limit) and (abs(pso_result[0]-last_five_x_avg) < distance_limit) and (abs(pso_result[1]-last_five_y_avg) < distance_limit) and (abs(pso_result[2]-last_five_z_avg) < distance_limit):
               pso_result_final = pso_result
               break
          
          # random granica, izmeniti
          if (num_iterations > 500):
               break

     if (i < 4):
          last_five_x.append(pso_result_final[0])
          last_five_y.append(pso_result_final[1])
          last_five_z.append(pso_result_final[2])
     else:
          last_five_x.append(pso_result_final[0])
          last_five_y.append(pso_result_final[1])
          last_five_z.append(pso_result_final[2])
          last_five_x_avg = sum(last_five_x)/len(last_five_x)
          last_five_y_avg = sum(last_five_y)/len(last_five_y)
          last_five_z_avg = sum(last_five_z)/len(last_five_z)
          last_five_x.pop(0)
          last_five_y.pop(0)
          last_five_z.pop(0)
          
     time4 = time.time()
     pso_time = time4-time3

     num_iterations_arr.append(num_iterations)
     pso_time_arr.append(pso_time)
     pso_errors.append(pso_result_error)
     pso_x_arr.append(pso_result_final[0])
     pso_y_arr.append(pso_result_final[1])
     pso_z_arr.append(pso_result_final[2])

     idA0_arr.append(rec0_tdoa.idA)
     idB0_arr.append(rec0_tdoa.idB)
     idA1_arr.append(rec1_tdoa.idA)
     idB1_arr.append(rec1_tdoa.idB)
     idA2_arr.append(rec2_tdoa.idA)
     idB2_arr.append(rec2_tdoa.idB)
     tdoa_timestamp_arr.append((rec0_tdoa.timestamp + rec1_tdoa.timestamp + rec2_tdoa.timestamp)/3)

     i += 1

data = {'GD errors':gd_errors, 'GD x estimated':gd_x_arr, 'GD y estimated':gd_y_arr, 'GD z estimated':gd_z_arr, 'GD execution time':gd_time_arr, 'PSO errors':pso_errors, 'PSO x estimated':pso_x_arr, 'PSO y estimated':pso_y_arr, 'PSO z estimated':pso_z_arr, 'PSO execution time':pso_time_arr, 'idA0':idA0_arr, 'idB0':idB0_arr, 'idA1':idA1_arr, 'idB1':idB1_arr, 'idA2':idA2_arr, 'idB2':idB2_arr, 'tdoa timestamp':tdoa_timestamp_arr, 'iterations number':num_iterations}
df = pd.DataFrame(data)

df.to_excel(dst_address, sheet_name="Data")

print(df.describe())

df2 = pd.DataFrame(df.describe())
df2.to_excel(describe_dst_address, sheet_name="Describe data")

print("DONE!")