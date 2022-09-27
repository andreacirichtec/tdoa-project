from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from constellations import *

# change these addresses and file names
# src_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial2-tdoa2-results-scipynm.xlsx"
tdoa_src_address = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial6-tdoa2-results-corrected-random10.xlsx"
pos_src_address  = "/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial6-tdoa2-extracted.xlsx"

read_data = pd.read_excel(tdoa_src_address)
read_pos = pd.read_excel(pos_src_address)

gd_x_arr = []; gd_y_arr = []; gd_z_arr = []; gd_error_arr = []; t_tdoa_arr = []
nm_x_arr = []; nm_y_arr = []; nm_z_arr = []; nm_error_arr = []
x_arr = []; y_arr = []; z_arr = []; t_pos_arr = []

num_tdoa = len(read_data)-1
num_pos = len(read_pos[read_pos["t_pose"].notna()])-1

j = 0

for i in range(0, num_tdoa):
    gd_error_arr.append(read_data.iloc[i,1])
    gd_x_arr.append(read_data.iloc[i,2])
    gd_y_arr.append(read_data.iloc[i,3])
    gd_z_arr.append(read_data.iloc[i,4])
    nm_error_arr.append(read_data.iloc[i,6])
    nm_x_arr.append(read_data.iloc[i,7])
    nm_y_arr.append(read_data.iloc[i,8])
    nm_z_arr.append(read_data.iloc[i,9])
    t_tdoa_arr.append(read_data.iloc[i,17])

for j in range(0,num_pos):

    #  get_recordings_pos(read_pos, j)

     x_arr.append(read_pos.iloc[j,4])
     y_arr.append(read_pos.iloc[j,5])
     z_arr.append(read_pos.iloc[j,6])
     t_pos_arr.append(read_pos.iloc[j,7])

# gd_x_err = np.subtract(gd_x_arr, x_arr)
# gd_y_err = np.subtract(gd_y_arr, y_arr)
# gd_z_err = np.subtract(gd_z_arr, z_arr)

# nm_x_err = np.subtract(nm_x_arr, x_arr)
# nm_y_err = np.subtract(nm_y_arr, y_arr)
# nm_z_err = np.subtract(nm_z_arr, z_arr)

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

fig = plt.figure('Gradient Descent', tight_layout=True, figsize=(14,14))
plt.subplot(411)
plt.plot(t_tdoa_arr, gd_error_arr)
plt.xlabel('timestamp[s]')
plt.ylabel('error function[m]')
plt.title('Gradient Descent optimization error')

plt.subplot(412)
plt.plot(t_tdoa_arr, gd_x_arr, color = 'blue', label = 'estimated position')
plt.plot(t_pos_arr, x_arr, color = 'red', label = 'ground truth position')
plt.xlabel('timestamp[s]')
plt.ylabel('x coordinate[m]')
plt.title('x coordinate error')
plt.legend()

plt.subplot(413)
plt.plot(t_tdoa_arr, gd_y_arr, color = 'blue', label = 'estimated position')
plt.plot(t_pos_arr, y_arr, color = 'red', label = 'ground truth position')
plt.xlabel('timestamp[s]')
plt.ylabel('y coordinate[m]')
plt.title('y coordinate error')
plt.legend()

plt.subplot(414)
plt.plot(t_tdoa_arr, gd_z_arr, color = 'blue', label = 'estimated position')
plt.plot(t_pos_arr, z_arr, color = 'red', label = 'ground truth position')
plt.xlabel('timestamp[s]')
plt.ylabel('z coordinate[m]')
plt.title('z coordinate error')
plt.legend()
plt.savefig('/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial6-tdoa2-gd.png')

fig.align_labels()

fig = plt.figure('Nelder-Mead', tight_layout=True, figsize=(14,14))
plt.subplot(411)
plt.plot(t_tdoa_arr, nm_error_arr)
plt.xlabel('timestamp[s]')
plt.ylabel('error function[m]')
plt.title('Nelder-Mead optimization error')

plt.subplot(412)
plt.plot(t_tdoa_arr, nm_x_arr, color = 'blue', label = 'estimated position')
plt.plot(t_pos_arr, x_arr, color = 'red', label = 'ground truth position')
plt.xlabel('timestamp[s]')
plt.ylabel('x coordinate[m]')
plt.title('x coordinate error')
plt.legend()

plt.subplot(413)
plt.plot(t_tdoa_arr, nm_y_arr, color = 'blue', label = 'estimated position')
plt.plot(t_pos_arr, y_arr, color = 'red', label = 'ground truth position')
plt.xlabel('timestamp[s]')
plt.ylabel('y coordinate[m]')
plt.title('y coordinate error')
plt.legend()

plt.subplot(414)
plt.plot(t_tdoa_arr, nm_z_arr, color = 'blue', label = 'estimated position')
plt.plot(t_pos_arr, z_arr, color = 'red', label = 'ground truth position')
plt.xlabel('timestamp[s]')
plt.ylabel('z coordinate[m]')
plt.title('z coordinate error')
plt.legend()
plt.savefig('/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial6-tdoa2-nm-10.png')

fig.align_labels()

# fig3d_gd = plt.figure('gradient descent tracing', tight_layout=True)
# plt.title('gradient descent')
# plt.box(False)
# plt.xticks([])
# plt.yticks([])
# ax = plt.axes(projection='3d')
# ax.plot3D(gd_x_arr, gd_y_arr, gd_z_arr, 'blue', label = 'estimated position')
# ax.plot3D(x_arr, y_arr, z_arr, 'red', label = 'ground truth position')
# # ax.scatter3D(gd_x_arr, gd_y_arr, gd_z_arr, 'blue', label = 'estimated position')
# # ax.scatter3D(x_arr, y_arr, z_arr, 'red', label = 'ground truth position')
# plt.legend()
# # plt.savefig('C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\slike\\const1-trial2-tdoa2-scipynm3-3d-gd.png')
# plt.savefig('/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial4-tdoa2-ajmo-random10-3d-gd.png')

# fig3d_nm = plt.figure('nelder mead tracing', tight_layout=True)
# plt.title('nelder mead')
# plt.box(False)
# plt.xticks([])
# plt.yticks([])
# bx = plt.axes(projection='3d')
# bx.plot3D(nm_x_arr, nm_y_arr, nm_z_arr, 'blue', label = 'estimated position')
# bx.plot3D(x_arr, y_arr, z_arr, 'red', label = 'ground truth position')
# # bx.scatter3D(nm_x_arr, nm_y_arr, nm_z_arr, 'blue', label = 'estimated position')
# # bx.scatter3D(x_arr, y_arr, z_arr, 'red', label = 'ground truth position')
# plt.legend()
# # plt.savefig('C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\slike\\const1-trial2-tdoa2-scipynm3-3d-nm.png')
# plt.savefig('/Users/andreaciric/Documents/GitHub/tdoa-project/data/extracted_data/const1/const1-trial4-tdoa2-ajmo-random10-3d-nm.png')


plt.show()
