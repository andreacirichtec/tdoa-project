from distutils.log import error
from data.constellations import *

class Simplex:
    def __init__(self, b, g1, g2, w):
        self.b = b
        self.g1 = g1
        self.g2 = g2
        self.w = w

    def __str__(self):
        return f"Simplex(b(x,y,z),g1(x,y,z),g2(x,y,z),w(x,y,z)) = ({self.b},{self.g1},{self.g2},{self.w})"

    def sort(self, constellation, rec0, rec1, rec2):
        f0 = self.b.error(constellation, rec0, rec1, rec2)
        f1 = self.g1.error(constellation, rec0, rec1, rec2)
        f2 = self.g2.error(constellation, rec0, rec1, rec2)
        f3 = self.w.error(constellation, rec0, rec1, rec2)

        if (f0 < f1):
            low1 = f0
            low1_point = self.b
            high1 = f1
            high1_point = self.g1
        else: 
            low1 = f1
            low1_point = self.g1
            high1 = f0
            high1_point = self.b

        if (f2 < f3):
            low2 = f2
            low2_point = self.g2
            high2 = f3
            high2_point = self.w
        else:
            low2 = f3
            low2_point = self.w
            high2 = f2
            high2_point = self.g2

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

def nelder_mead_f(constellation, rec0, rec1, rec2, points, reflection = 1, expansion = 2, contraction = 0.5, shrinkage = 0.5):

    a = Point(0,0,1)
    b = Point(0,1,0)
    c = Point(1,0,0)
    d = Point(1,1,1)
    simp = Simplex(a,b,c,d)

    print(simp)
    print(simp.b.error(constellation, rec0, rec1, rec2))
    # 1. ORDER
    simp = simp.sort(constellation, rec0, rec1, rec2)
    print(simp)

    # 2. CALCULATE CENTROID
    centroid = Point(0,0,0)
    centroid.x = (simp.b.x + simp.g1.x + simp.g2.x + simp.w.x)/4
    centroid.y = (simp.b.y + simp.g1.y + simp.g2.y + simp.w.y)/4
    centroid.z = (simp.b.z + simp.g1.z + simp.g2.z + simp.w.z)/4
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

    if (fr >= fb) and (fr < fw):
        simp = Simplex(simp.b,simp.g1,simp.g2, reflected)
        # go to step 1
    
    # 4. EXPANSION
    expanded = Point(0,0,0)
    expanded.x = centroid.x + expansion*(reflected.x - centroid.x)
    expanded.y = centroid.y + expansion*(reflected.y - centroid.y)
    expanded.z = centroid.z + expansion*(reflected.z - centroid.z)

    fe = expanded.error(constellation, rec0, rec1, rec2)

    if (fe < fr):
        simp = Simplex(simp.b, simp.g1, simp.g2, expanded)
        # go to step 1
    else:
        simp = Simplex(simp.b, simp.g1, simp.g2, reflected)
        # go to step 1

    # 5. CONTRACTION

    print(simp)
    print()
    return