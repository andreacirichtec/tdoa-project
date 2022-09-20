from scipy.optimize import minimize
from random import random

def error_fu(x):
    error  = (x[0])**2 + (x[1])**2 + (x[2])**2
    return error

min_x = -5; max_x = 5
min_y = -5; max_y = 5
min_z = 0; max_z = 4
randx = min_x + (random() * (max_x - min_x))
randy = min_y + (random() * (max_y - min_y))
randz = min_z + (random() * (max_z - min_z))

x0 = [randx, randy, randz]
result = minimize(error_fu, x0, tol=1e-6)

print(result)