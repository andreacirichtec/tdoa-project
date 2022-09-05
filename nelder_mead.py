from distutils.log import error
from data.constellations import *
from error_function import error_f

class Simplex:
    def __init__(self, b, g1, g2, w):
        self.b = b
        self.g1 = g1
        self.g2 = g2
        self.w = w

    def sort(self, constellation, rec0, rec1, rec2):
        f0 = self.b.error(constellation, rec0, rec1, rec2)
        f1 = self.b.error(constellation, rec0, rec1, rec2)
        f2 = self.b.error(constellation, rec0, rec1, rec2)
        f3 = self.b.error(constellation, rec0, rec1, rec2)

    #     if a < b
    #     low1 = a
    #     high1 = b
    # else 
    #     low1 = b
    #     high1 = a

    # if c < d
    #     low2 = c
    #     high2 = d
    # else
    #     low2 = d
    #     high2 = c

    # if low1 < low2
    #     lowest = low1
    #     middle1 = low2
    # else
    #     lowest = low2
    #     middle1 = low1

    # if high1 > high2
    #     highest = high1
    #     middle2 = high2
    # else
    #     highest = high2
    #     middle2 = high1

    # if middle1 < middle2
    #     return (lowest,middle1,middle2,highest)
    # else
    #     return (lowest,middle2,middle1,highest)

def nelder_mead_f(constellation, rec0, rec1, rec2, points, reflection = 1, expansion = 2, contraction = 0.5, shrinkage = 0.5):

    a = Point(0,0,1)
    b = Point(0,1,0)
    c = Point(1,0,0)
    d = Point(1,1,1)

    simp = Simplex(a,b,c,d)

    print(simp.a.error(constellation, rec0, rec1, rec2))
#     # 1. ORDER
#     f0 = error_f(constellation, rec0, rec1, rec2, points[0])
#     f1 = error_f(constellation, rec0, rec1, rec2, points[1])
#     f2 = error_f(constellation, rec0, rec1, rec2, points[2])

#     if (f0>f1) and (f0>f2):
#         b = points[0]
#         if (f1>f2):
#             w = points[2]
#             g = points[1]
#         else:
#             w = points[1]
#             g = points[2]
#     elif (f0<f1) and (f0>f2):
#         b = f1
#         g = f0
#         w = f2
#     else:
#         b = f0
#         g = f2
#         w = f1

    