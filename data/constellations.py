import math
from pickle import FALSE, TRUE

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def error(self):
        err = error_f_nm(self)
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

class Recording:
    def __init__(self, idA, idB, dt, x, y, z, timestamp):
        self.idA = idA
        self.idB = idB
        self.dt = dt
        self.x = x
        self.y = y
        self.z = z
        self.timestamp = timestamp

    def change(self, idA, idB, dt, x, y, z, timestamp):
        self.idA = idA
        self.idB = idB
        self.dt = dt
        self.x = x
        self.y = y
        self.z = z
        self.timestamp = timestamp

    def __str__(self):
        return f"Recording: \nidA={self.idA}\nidB={self.idB}\ndt={self.dt}\n(x,y,z)=({self.x},{self.y},{self.y}\ntimestamp={self.timestamp})"

constellation1 = [Point(-2.4174718660841163,-4.020796001114614,0.18179046793237785),
                    Point(-2.820490062889947,3.5250373345173456,2.5874240006860396),
                    Point(3.4819322476730066,3.3050399505325867,0.15447010668018804),
                    Point(3.4507246660737074,-3.7181145718099624,2.6693201245043428),
                    Point(-3.2776160385636026,-3.8689686503275325,2.67389716671206),
                    Point(3.2654739320660124,-3.6510796042048415,0.1752474453973762),
                    Point(3.8321293068358147,3.652084854209938,2.624927324400282),
                    Point(-2.7227724068629255,3.21907986264268,0.15829414514009574)]
constellation2 = [Point(-3.033898891277714,-4.035088834097403,0.20945086446420988),
                    Point(-0.36968246264075166,3.825877804038863,2.592643048382574),
                    Point(3.6836125407405986,3.7136093268388684,0.17473470963376952),
                    Point(4.064736049875435,-0.8343536171418291,2.614688385620916),
                    Point(-3.514975262704036,-1.0010534450401993,2.611899957120244),
                    Point(3.926566529739807,-3.785779375648486,0.19692182829390426),
                    Point(1.1500737583151717,-4.232385847576266,2.6060676498370903),
                    Point(-3.1622190943963324,3.348676021506,0.1797870375417553)]
constellation3 = [Point(-3.0400739913644617,-4.029878605797746,0.2086374396157397),
                    Point(-3.2322604228535727,3.7560564637264355,2.946689630262403),
                    Point(3.676682796054712,3.715609004632582,0.17403476155729386),
                    Point(4.104077249319202,-4.274469287062838,3.2020642683316893),
                    Point(-3.041510989575704,-4.410450309911892,3.0430580370331044),
                    Point(3.917772330969977,-3.786201138515536,0.19753353417151204),
                    Point(4.061509380447565,3.8548627765644454,3.1409729774538255),
                    Point(-3.168670058421678,3.3521825925451214,0.17908062216020118)]
constellation4 = [Point(-3.0101983925222484,-4.058910586060332,0.19628971181502824),
                    Point(-3.2586741011048006,3.6966310342207858,2.9101573298708),
                    Point(3.650786659616108,3.732984329061774,0.18955347520686663),
                    Point(3.5038524799758757,-3.955396056926031,3.0376408838394457),
                    Point(-2.7909463463466433,-4.13542201753855,2.847636358540227),
                    Point(3.953882519480277,-3.7624630950139464,0.20347693202729109),
                    Point(3.4654089074024688,3.55896956542648,2.9710608167433157),
                    Point(-3.2112336178645373,3.304121110232922,0.17617659290117677)]

constellation = constellation1

def error_f_gd(estimated_position):

    global constellation
    
    e1 = (math.sqrt((constellation[rec0.idA].x-estimated_position.x)**2+(constellation[rec0.idA].y-estimated_position.y)**2+(constellation[rec0.idA].z-estimated_position.z)**2), 
        -math.sqrt((constellation[rec0.idB].x-estimated_position.x)**2+(constellation[rec0.idB].y-estimated_position.y)**2+(constellation[rec0.idB].z-estimated_position.z)**2),
        rec0.dt)

    e2 = (math.sqrt((constellation[rec1.idA].x-estimated_position.x)**2+(constellation[rec1.idA].y-estimated_position.y)**2+(constellation[rec1.idA].z-estimated_position.z)**2),
        -math.sqrt((constellation[rec1.idB].x-estimated_position.x)**2+(constellation[rec1.idB].y-estimated_position.y)**2+(constellation[rec1.idB].z-estimated_position.z)**2), 
        rec1.dt)

    e3 = (math.sqrt((constellation[rec2.idA].x-estimated_position.x)**2+(constellation[rec2.idA].y-estimated_position.y)**2+(constellation[rec2.idA].z-estimated_position.z)**2),   
        -math.sqrt((constellation[rec2.idB].x-estimated_position.x)**2+(constellation[rec2.idB].y-estimated_position.y)**2+(constellation[rec2.idB].z-estimated_position.z)**2),
        rec2.dt)

    # error = (sum(e1))**2 + (sum(e2))**2 + (sum(e3))**2
    error = (sum(e1)) + (sum(e2)) + (sum(e3))
    
    return error

rec0 = Recording(0,0,0,0,0,0,0)
rec1 = Recording(0,0,0,0,0,0,0)
rec2 = Recording(0,0,0,0,0,0,0)

def get_recordings(read_data, i):

    global rec0
    global rec1
    global rec2

    num = len(read_data)-2

    k = 1
    rec0.change(read_data.iloc[i,0], read_data.iloc[i,1], read_data.iloc[i,2], read_data.iloc[i,3], read_data.iloc[i,4], read_data.iloc[i,5], read_data.iloc[i,6])
    rec1.change(read_data.iloc[i+k,0], read_data.iloc[i+k,1], read_data.iloc[i+k,2], read_data.iloc[i+k,3], read_data.iloc[i+k,4], read_data.iloc[i+k,5], read_data.iloc[i+k,6])
    while ((rec0.idA == rec1.idA) and (rec0.idB == rec1.idB)) or ((rec0.idA == rec1.idB) and (rec0.idB == rec1.idA)):
        k += 1
        rec1.change(read_data.iloc[i+k,0], read_data.iloc[i+k,1], read_data.iloc[i+k,2], read_data.iloc[i+k,3], read_data.iloc[i+k,4], read_data.iloc[i+k,5], read_data.iloc[i+k,6])
        num -= 1
    k += 1
    rec2.change(read_data.iloc[i+k,0], read_data.iloc[i+k,1], read_data.iloc[i+k,2], read_data.iloc[i+k,3], read_data.iloc[i+k,4], read_data.iloc[i+k,5], read_data.iloc[i+k,6])
    while ((rec0.idA == rec2.idA) and (rec0.idB == rec2.idB)) or ((rec0.idA == rec2.idB) and (rec0.idB == rec2.idA)) or ((rec1.idA == rec2.idA) and (rec1.idB == rec2.idB)) or ((rec1.idA == rec2.idB) and (rec1.idB == rec2.idA)):
        k += 1
        rec2.change(read_data.iloc[i+k,0], read_data.iloc[i+k,1], read_data.iloc[i+k,2], read_data.iloc[i+k,3], read_data.iloc[i+k,4], read_data.iloc[i+k,5], read_data.iloc[i+k,6])
        num -= 1

def error_f_nm(a):

    global constellation
    global rec0
    global rec1
    global rec2


    min_x = -5; max_x = 5
    min_y = -5; max_y = 5
    min_z = 0; max_z = 4

    if (a[0]>max_x) or (a[0]<min_x) or (a[1]>max_y) or (a[1]<min_y) or (a[2]>max_z) or (a[2]<min_z):
        return 1000000000000
    
    e1 = (math.sqrt((constellation[rec0.idA].x-a[0])**2+(constellation[rec0.idA].y-a[1])**2+(constellation[rec0.idA].z-a[2])**2), 
        -math.sqrt((constellation[rec0.idB].x-a[0])**2+(constellation[rec0.idB].y-a[1])**2+(constellation[rec0.idB].z-a[2])**2),
        rec0.dt) 

    e2 = (math.sqrt((constellation[rec1.idA].x-a[0])**2+(constellation[rec1.idA].y-a[1])**2+(constellation[rec1.idA].z-a[2])**2),
        -math.sqrt((constellation[rec1.idB].x-a[0])**2+(constellation[rec1.idB].y-a[1])**2+(constellation[rec1.idB].z-a[2])**2), 
        rec1.dt)

    e3 = (math.sqrt((constellation[rec2.idA].x-a[0])**2+(constellation[rec2.idA].y-a[1])**2+(constellation[rec2.idA].z-a[2])**2),   
        -math.sqrt((constellation[rec2.idB].x-a[0])**2+(constellation[rec2.idB].y-a[1])**2+(constellation[rec2.idB].z-a[2])**2),
        rec2.dt)

    error = (sum(e1))**2 + (sum(e2))**2 + (sum(e3))**2
    
    return error