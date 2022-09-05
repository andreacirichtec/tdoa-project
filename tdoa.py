import math
import time
import pandas as pd
from data.constellations import *
from gradient_descent import gradient_descent_f
from statistics import mean

# change these addresses and file names
src_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial6-tdoa2-extracted.xlsx"
dst_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial6-tdoa2-results.xlsx"

# read data from the csv file
read_data = pd.read_excel(src_address)
errors = []; x_arr = []; y_arr = []; z_arr = []; time_arr = []

for i in range(0, len(read_data)-2, 1): #možda treba korak da bude 3, ali sa korakom 1 ima više len(read_data)-2
     rec0 = Recording(read_data.iloc[i,0], read_data.iloc[i,1], read_data.iloc[i,2], read_data.iloc[i,3], read_data.iloc[i,4],read_data.iloc[i,5])
     rec1 = Recording(read_data.iloc[i+1,0], read_data.iloc[i+1,1], read_data.iloc[i+1,2], read_data.iloc[i+1,3], read_data.iloc[i+1,4],read_data.iloc[i+1,5])
     rec2 = Recording(read_data.iloc[i+2,0], read_data.iloc[i+2,1], read_data.iloc[i+2,2], read_data.iloc[i+2,3], read_data.iloc[i+2,4],read_data.iloc[i+2,5])

     estimated_position = Point(rec2.x, rec2.y, rec2.z)
     
     time1 = time.time()
     position, final_error = gradient_descent_f(constellation1, rec0, rec1, rec2, estimated_position)
     time2 = time.time()

     time_arr.append(time2-time1)
     errors.append(final_error)
     x_arr.append(position.x)
     y_arr.append(position.y)
     z_arr.append(position.z)
     
     print(i)
     #print(position.x, position.y, position.z, final_error)
     #print("error for x, y and z axis:", abs(rec2.x - position.x)*1000, "cm", abs(rec2.y - position.y)*1000, "cm", abs(rec2.z - position.z)*1000, "cm")

#data = {'errors':errors, 'x estimated':x_arr, 'y estimated':y_arr, 'z estimated':z_arr, 'execution time':time_arr}
#df = pd.DataFrame(data)

#df.to_excel(dst_address, index=False)

#print(df.describe())
#print("error mean = ", mean(errors))

print("DONE!")