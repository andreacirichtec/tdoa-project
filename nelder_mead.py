from distutils.log import error
from data.constellations import *

class Simplex:
    def __init__(self, b, gb, gw, w):
        self.b = b
        self.gb = gb
        self.gw = gw
        self.w = w

    def __str__(self):
        return f"Simplex(b(x,y,z),gb(x,y,z),gw(x,y,z),w(x,y,z)) = ({self.b},{self.gb},{self.gw},{self.w})"

    def sort(self, constellation, rec0, rec1, rec2):
        f0 = self.b.error(constellation, rec0, rec1, rec2)
        f1 = self.gb.error(constellation, rec0, rec1, rec2)
        f2 = self.gw.error(constellation, rec0, rec1, rec2)
        f3 = self.w.error(constellation, rec0, rec1, rec2)

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

def nelder_mead_step(simp, constellation, rec0, rec1, rec2, points, reflection = 1, expansion = 2, contraction = 0.5, shrinkage = 0.5):

    # 1. ORDER
    simp = simp.sort(constellation, rec0, rec1, rec2)
    print(simp)

    # 2. CALCULATE CENTROID
    centroid = Point(0,0,0)
    centroid.x = (simp.b.x + simp.gb.x + simp.gw.x + simp.w.x)/4
    centroid.y = (simp.b.y + simp.gb.y + simp.gw.y + simp.w.y)/4
    centroid.z = (simp.b.z + simp.gb.z + simp.gw.z + simp.w.z)/4
    #centroid = Point(x,y,z)
    print("centroid = ", centroid)

    # 3. REFLECTION
    reflected = Point(0,0,0)
    reflected.x = centroid.x + reflection*(centroid.x - simp.w.x)
    reflected.y = centroid.y + reflection*(centroid.y - simp.w.y)
    reflected.z = centroid.z + reflection*(centroid.z - simp.w.z)

    fr = reflected.error(constellation, rec0, rec1, rec2)
    fw = simp.w.error(constellation, rec0, rec1, rec2)
    fb = simp.b.error(constellation, rec0, rec1, rec2)
    fgw = simp.gw.error(constellation, rec0, rec1, rec2)

    if (fr >= fb) and (fr < fgw):
        simp = Simplex(simp.b,simp.gb,simp.gw, reflected)
        # go to step 1
        print("reflection")
        return simp
    elif (fr < fb):
        # 4. EXPANSION
        expanded = Point(0,0,0)
        expanded.x = centroid.x + expansion*(reflected.x - centroid.x)
        expanded.y = centroid.y + expansion*(reflected.y - centroid.y)
        expanded.z = centroid.z + expansion*(reflected.z - centroid.z)

        fe = expanded.error(constellation, rec0, rec1, rec2)

        if (fe < fr):
            simp = Simplex(simp.b, simp.gb, simp.gw, expanded)
            # go to step 1
            print("expansion")
            return simp
        else:
            simp = Simplex(simp.b, simp.gb, simp.gw, reflected)
            # go to step 1
            print("expansion - reflection")
            return simp
    else:
        # 5. CONTRACTION
        if (fr < fw):
            contracted_out = Point(0,0,0)
            contracted_out.x = centroid.x + contraction*(reflected.x - centroid.x)
            contracted_out.y = centroid.y + contraction*(reflected.y - centroid.y)
            contracted_out.z = centroid.z + contraction*(reflected.z - centroid.z)

            fco = contracted_out.error(constellation, rec0, rec1, rec2)

            if (fco < fr):
                simp = Simplex(simp.b, simp.gb, simp.gw, contracted_out)
                # go to step 1
                print ("contraction")
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
                return simp
        else:
            contracted_in = Point(0,0,0)
            contracted_in.x = centroid.x + contraction*(simp.w.x - centroid.x)
            contracted_in.y = centroid.y + contraction*(simp.w.y - centroid.y)
            contracted_in.z = centroid.z + contraction*(simp.w.z - centroid.z)

            fci = contracted_in.error(constellation, rec0, rec1, rec2)

            if (fci < fw):
                simp = Simplex(simp.b, simp.gb, simp.gw, contracted_in)
                # go to step 1
                print("contraction")
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
                return simp

    # print("none of the above")
    # print()
    # return simp

def nelder_mead_f(constellation, rec0, rec1, rec2, points, reflection = 1, expansion = 2, contraction = 0.5, shrinkage = 0.5):
    
    a = Point(0,0,1)
    b = Point(0,1,0)
    c = Point(1,0,0)
    d = Point(1,1,1)
    simp = Simplex(a,b,c,d)

    print(simp)
    print(simp.b.error(constellation, rec0, rec1, rec2))

    simp = nelder_mead_step(simp, constellation, rec0, rec1, rec2, points, reflection, expansion, contraction, shrinkage)

    return