from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# change these addresses and file names
src_address = "C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\const1-trial1-tdoa2-results-new.xlsx"

read_data = pd.read_excel(src_address)

gd_x_arr = []; gd_y_arr = []; gd_z_arr = []; gd_error_arr = []; t_arr = []
nm_x_arr = []; nm_y_arr = []; nm_z_arr = []; nm_error_arr = []
x_arr = []; y_arr = []; z_arr = []

for i in range(0, len(read_data)-1):
    gd_error_arr.append(read_data.iloc[i,1])
    gd_x_arr.append(read_data.iloc[i,2])
    gd_y_arr.append(read_data.iloc[i,3])
    gd_z_arr.append(read_data.iloc[i,4])
    nm_error_arr.append(read_data.iloc[i,6])
    nm_x_arr.append(read_data.iloc[i,7])
    nm_y_arr.append(read_data.iloc[i,8])
    nm_z_arr.append(read_data.iloc[i,9])
    x_arr.append(read_data.iloc[i,17])
    y_arr.append(read_data.iloc[i,18])
    z_arr.append(read_data.iloc[i,19])
    t_arr.append(read_data.iloc[i,20])

gd_x_err = np.subtract(gd_x_arr, x_arr)
gd_y_err = np.subtract(gd_y_arr, y_arr)
gd_z_err = np.subtract(gd_z_arr, z_arr)

nm_x_err = np.subtract(nm_x_arr, x_arr)
nm_y_err = np.subtract(nm_y_arr, y_arr)
nm_z_err = np.subtract(nm_z_arr, z_arr)

fig = plt.figure('error function', tight_layout=True, figsize=(16,6))
plt.subplot(211)
plt.plot(t_arr, gd_error_arr)
plt.ylabel('error function[m]')
plt.title('gradient descent error')

plt.subplot(212)
plt.plot(t_arr, nm_error_arr)
plt.xlabel('timestamp')
plt.ylabel('error function[m]')
plt.title('nelder mead error')
plt.savefig('C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\slike\\const1-trial1-tdoa2-new-error-function.svg')

fig.align_labels()

figx = plt.figure('x error', tight_layout=True, figsize=(16,6))
plt.subplot(211)
plt.plot(t_arr, gd_x_arr, color = 'blue', label = 'estimated position')
plt.plot(t_arr, x_arr, color = 'red', label = 'ground truth position')
plt.ylabel('x coordinate[m]')
plt.title('gradient descent error')
plt.legend()

plt.subplot(212)
plt.plot(t_arr, nm_x_arr, color = 'blue', label = 'estimated position')
plt.plot(t_arr, x_arr, color = 'red', label = 'ground truth position')
plt.xlabel('timestamp')
plt.ylabel('x coordinate[m]')
plt.title('nelder mead error')
plt.legend()
plt.savefig('C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\slike\\const1-trial1-tdoa2-new-x-error.svg')

figx.align_labels()

figy = plt.figure('y error', tight_layout=True, figsize=(16,6))
plt.subplot(211)
plt.plot(t_arr, gd_y_arr, color = 'blue', label = 'estimated position')
plt.plot(t_arr, y_arr, color = 'red', label = 'ground truth position')
plt.ylabel('y coordinate[m]')
plt.title('gradient descent error')
plt.legend()

plt.subplot(212)
plt.plot(t_arr, nm_y_arr, color = 'blue', label = 'estimated position')
plt.plot(t_arr, y_arr, color = 'red', label = 'ground truth position')
plt.xlabel('timestamp')
plt.ylabel('y coordinate[m]')
plt.title('nelder mead error')
plt.legend()
plt.savefig('C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\slike\\const1-trial1-tdoa2-new-y-error.svg')

figy.align_labels()

figz = plt.figure('z error', tight_layout=True, figsize=(16,6))
plt.subplot(211)
plt.plot(t_arr, gd_z_arr, color = 'blue', label = 'estimated position')
plt.plot(t_arr, z_arr, color = 'red', label = 'ground truth position')
plt.ylabel('z coordinate[m]')
plt.title('gradient descent error')
plt.legend()

plt.subplot(212)
plt.plot(t_arr, nm_z_arr, color = 'blue', label = 'estimated position')
plt.plot(t_arr, z_arr, color = 'red', label = 'ground truth position')
plt.xlabel('timestamp')
plt.ylabel('z coordinate[m]')
plt.title('nelder mead error')
plt.legend()
plt.savefig('C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\slike\\const1-trial1-tdoa2-new-z-error.svg')

figz.align_labels()

fig3d_gd = plt.figure('gradient descent tracing', tight_layout=True)
plt.title('gradient descent')
ax = plt.axes(projection='3d')
ax.plot3D(gd_x_arr, gd_y_arr, gd_z_arr, 'blue', label = 'estimated position')
ax.plot3D(x_arr, y_arr, z_arr, 'red', label = 'ground truth position')
# ax.scatter3D(gd_x_arr, gd_y_arr, gd_z_arr, 'blue', label = 'estimated position')
# ax.scatter3D(x_arr, y_arr, z_arr, 'red', label = 'ground truth position')
plt.legend()
plt.savefig('C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\slike\\const1-trial1-tdoa2-new-3d-gd.svg')

fig3d_nm = plt.figure('nelder mead tracing', tight_layout=True)
plt.title('nelder mead')
bx = plt.axes(projection='3d')
bx.plot3D(nm_x_arr, nm_y_arr, nm_z_arr, 'blue', label = 'estimated position')
bx.plot3D(x_arr, y_arr, z_arr, 'red', label = 'ground truth position')
plt.legend()
plt.savefig('C:\\Users\\Andrea\\Documents\\GitHub\\tdoa-project\\data\\extracted_data\\const1\\slike\\const1-trial1-tdoa2-new-3d-nm.svg')

plt.show()
