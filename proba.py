from cmath import inf, isnan
import statistics
from random import random
from timeit import repeat
import matplotlib.pyplot as plt

import matplotlib.animation as animation

def error_fu(x, y, z):
     
    error  = x**2 + y**2 + z**2
    
    return error

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z},{self.error()})"

    def error(self):
        err = error_fu(self.x, self.y, self.z)
        return err

    def is_inside(self):
        min_x = -5; max_x = 5
        min_y = -5; max_y = 5
        min_z = 0; max_z = 4

        if(self.x > min_x) and (self.x < max_x):
            if(self.y > min_y) and (self.y < max_y):
                if(self.z > min_z) and (self.z < max_z):
                    return 1
        return 0

class Simplex:
    def __init__(self, b, gb, gw, w):
        self.b = b
        self.gb = gb
        self.gw = gw
        self.w = w

    def __str__(self):
        return f"Simplex(b(x,y,z,err),gb(x,y,z,err),gw(x,y,z,err),w(x,y,z,err)) = ({self.b},{self.gb},{self.gw},{self.w})"

    def sort(self):
        f0 = self.b.error()
        f1 = self.gb.error()
        f2 = self.gw.error()
        f3 = self.w.error()

        if (f0 < f1):
            low1 = f0
            low1_point = self.b
            high1 = f1
            high1_point = self.gb
        else: 
            low1 = f1
            low1_point = self.gb
            high1 = f0
            high1_point = self.b

        if (f2 < f3):
            low2 = f2
            low2_point = self.gw
            high2 = f3
            high2_point = self.w
        else:
            low2 = f3
            low2_point = self.w
            high2 = f2
            high2_point = self.gw

        if (low1 < low2):
            lowest_point = low1_point
            middle1 = low2
            middle1_point = low2_point
        else:
            lowest_point = low2_point
            middle1 = low1
            middle1_point = low1_point

        if (high1 > high2):
            highest_point = high1_point 
            middle2 = high2
            middle2_point = high2_point
        else:
            highest_point = high2_point
            middle2 = high1
            middle2_point = high1_point

        if (middle1 < middle2):
            return Simplex(lowest_point,middle1_point,middle2_point,highest_point)
        else:
            return Simplex(lowest_point,middle2_point,middle1_point,highest_point)


def nelder_mead_step(simp, reflection = 1, expansion = 2, contraction = 0.5, shrinkage = 0.5):

    # 1. ORDER
    print(simp)
    simp = simp.sort()
    print("sortirano ->", simp)

    # 2. CALCULATE CENTROID
    centroid = Point(0,0,0)
    centroid.x = (simp.b.x + simp.gb.x + simp.gw.x + simp.w.x)/4
    centroid.y = (simp.b.y + simp.gb.y + simp.gw.y + simp.w.y)/4
    centroid.z = (simp.b.z + simp.gb.z + simp.gw.z + simp.w.z)/4
    print("centroid = ", centroid)

    # 3. REFLECTION
    reflected = Point(0,0,0)
    reflected.x = centroid.x + reflection*(centroid.x - simp.w.x)
    reflected.y = centroid.y + reflection*(centroid.y - simp.w.y)
    reflected.z = centroid.z + reflection*(centroid.z - simp.w.z)
    print("reflected = ", reflected)

    fr = reflected.error()
    fw = simp.w.error()
    fb = simp.b.error()
    fgw = simp.gw.error()
    fgb = simp.gb.error()

    if ((fr >= fb) and (fr < fgw) and (reflected.is_inside())):
        simp = Simplex(simp.b,simp.gb,simp.gw, reflected)
        # go to step 1
        print("reflection")
        return simp
    elif ((fr < fb) and (reflected.is_inside())):
        # 4. EXPANSION
        expanded = Point(0,0,0)
        expanded.x = centroid.x + expansion*(reflected.x - centroid.x)
        expanded.y = centroid.y + expansion*(reflected.y - centroid.y)
        expanded.z = centroid.z + expansion*(reflected.z - centroid.z)
        print("expanded = ", expanded)

        fe = expanded.error()

        if ((fe < fr) and (expanded.is_inside())):
            simp = Simplex(simp.b, simp.gb, simp.gw, expanded)
            # go to step 1
            print("expansion")
            return simp
        else:
            simp = Simplex(simp.b, simp.gb, simp.gw, reflected)
            # go to step 1
            print("expansion tried -> reflection")
            return simp
    else:
        # 5. CONTRACTION
        if (fr < fw):
            contracted_out = Point(0,0,0)
            contracted_out.x = centroid.x + contraction*(reflected.x - centroid.x)
            contracted_out.y = centroid.y + contraction*(reflected.y - centroid.y)
            contracted_out.z = centroid.z + contraction*(reflected.z - centroid.z)
            print("contracted_out = ", contracted_out)

            fco = contracted_out.error()

            if ((fco < fr) and (contracted_out.is_inside())):
                simp = Simplex(simp.b, simp.gb, simp.gw, contracted_out)
                # go to step 1
                print ("contraction out")
                return simp
            else:
                # 6. SHRINKAGE
                simp.gb.x = simp.b.x + shrinkage*(simp.gb.x - simp.b.x)
                simp.gb.y = simp.b.y + shrinkage*(simp.gb.y - simp.b.y)
                simp.gb.z = simp.b.z + shrinkage*(simp.gb.z - simp.b.z)

                simp.gw.x = simp.b.x + shrinkage*(simp.gw.x - simp.b.x)
                simp.gw.y = simp.b.y + shrinkage*(simp.gw.y - simp.b.y)
                simp.gw.z = simp.b.z + shrinkage*(simp.gw.z - simp.b.z)

                simp.w.x = simp.b.x + shrinkage*(simp.w.x - simp.b.x)
                simp.w.y = simp.b.y + shrinkage*(simp.w.y - simp.b.y)
                simp.w.z = simp.b.z + shrinkage*(simp.w.z - simp.b.z)
                # go to step 1
                print("shrinkage")
                print(simp)
                return simp
        else:
            contracted_in = Point(0,0,0)
            contracted_in.x = centroid.x + contraction*(simp.w.x - centroid.x)
            contracted_in.y = centroid.y + contraction*(simp.w.y - centroid.y)
            contracted_in.z = centroid.z + contraction*(simp.w.z - centroid.z)
            print("contracted_in = ", contracted_in)

            fci = contracted_in.error()

            if (fci < fw):
                simp = Simplex(simp.b, simp.gb, simp.gw, contracted_in)
                # go to step 1
                print("contraction in")
                return simp
            else:
                # 6. SHRINKAGE
                simp.gb.x = simp.b.x + shrinkage*(simp.gb.x - simp.b.x)
                simp.gb.y = simp.b.y + shrinkage*(simp.gb.y - simp.b.y)
                simp.gb.z = simp.b.z + shrinkage*(simp.gb.z - simp.b.z)

                simp.gw.x = simp.b.x + shrinkage*(simp.gw.x - simp.b.x)
                simp.gw.y = simp.b.y + shrinkage*(simp.gw.y - simp.b.y)
                simp.gw.z = simp.b.z + shrinkage*(simp.gw.z - simp.b.z)

                simp.w.x = simp.b.x + shrinkage*(simp.w.x - simp.b.x)
                simp.w.y = simp.b.y + shrinkage*(simp.w.y - simp.b.y)
                simp.w.z = simp.b.z + shrinkage*(simp.w.z - simp.b.z)
                # go to step 1
                print("shrinkage")
                print(simp)
                return simp

def nelder_mead_f(reflection = 1, expansion = 2, contraction = 0.5, shrinkage = 0.5):
    
    min_x = -5; max_x = 5
    min_y = -5; max_y = 5
    min_z = 0; max_z = 4
    randx = min_x + (random() * (max_x - min_x))
    randy = min_y + (random() * (max_y - min_y))
    randz = min_z + (random() * (max_z - min_z))
    a = Point(randx,randy,randz)
    # print(a)
    randx = min_x + (random() * (max_x - min_x))
    randy = min_y + (random() * (max_y - min_y))
    randz = min_z + (random() * (max_z - min_z))
    b = Point(randx,randy,randz)
    # print(b)
    randx = min_x + (random() * (max_x - min_x))
    randy = min_y + (random() * (max_y - min_y))
    randz = min_z + (random() * (max_z - min_z))
    c = Point(randx,randy,randz)
    # print(c)
    randx = min_x + (random() * (max_x - min_x))
    randy = min_y + (random() * (max_y - min_y))
    randz = min_z + (random() * (max_z - min_z))
    d = Point(randx,randy,randz)
    # print(d)

    # d = estimated_position
    simp = Simplex(a,b,c,d)

    delta = 0.0000001
    std = inf
    err_arr = []

    while (std>delta):
        simp = nelder_mead_step(simp, reflection, expansion, contraction, shrinkage)

        fb = simp.b.error()
        fgb = simp.gb.error()
        fgw = simp.gw.error()
        fw = simp.w.error()

        std = statistics.stdev([fb,fgb,fgw,fw])

        print("std=",std)
        print("error=", fb)
        print()
        err_arr.append(fb)

    plt.figure()
    plt.plot(err_arr)
    plt.show()

    # print(simp.b)
    return simp.b, fb

nm_position, nm_error = nelder_mead_f()

print("Odredjena pozicija", nm_position)
print("greska =", nm_error)