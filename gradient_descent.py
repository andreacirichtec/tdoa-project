import math
from data.constellations import *
#from data.error_function import error_f

def gradient_descent_f(constellation, rec0, rec1, rec2, estimated_position, iterations = 1000, learning_rate = 0.0001, stopping_threshold = 1e-6):
    
    previous_error = 1e6

    for i in range(iterations):

        error = error_f(constellation, rec0, rec1, rec2, estimated_position)

        if (abs(previous_error) < abs(error)) or abs(previous_error-error)<=stopping_threshold:
            return estimated_position, previous_error

        previous_error = error

        de_dx = ((constellation[rec0.idB].x-estimated_position.x)/(math.sqrt((constellation[rec0.idB].x-estimated_position.x)**2+(constellation[rec0.idB].y-estimated_position.y)**2+(constellation[rec0.idB].z-estimated_position.z)**2)),
                -(constellation[rec0.idA].x-estimated_position.x)/(math.sqrt((constellation[rec0.idA].x-estimated_position.x)**2+(constellation[rec0.idA].y-estimated_position.y)**2+(constellation[rec0.idA].z-estimated_position.z)**2)), 
                (constellation[rec1.idB].x-estimated_position.x)/(math.sqrt((constellation[rec1.idB].x-estimated_position.x)**2+(constellation[rec1.idB].y-estimated_position.y)**2+(constellation[rec1.idB].z-estimated_position.z)**2)),
                -(constellation[rec1.idA].x-estimated_position.x)/(math.sqrt((constellation[rec1.idA].x-estimated_position.x)**2+(constellation[rec1.idA].y-estimated_position.y)**2+(constellation[rec1.idA].z-estimated_position.z)**2)),
                (constellation[rec2.idB].x-estimated_position.x)/(math.sqrt((constellation[rec2.idB].x-estimated_position.x)**2+(constellation[rec2.idB].y-estimated_position.y)**2+(constellation[rec2.idB].z-estimated_position.z)**2)),
                -(constellation[rec2.idA].x-estimated_position.x)/(math.sqrt((constellation[rec2.idA].x-estimated_position.x)**2+(constellation[rec2.idA].y-estimated_position.y)**2+(constellation[rec2.idA].z-estimated_position.z)**2)))

        derror_dx = sum(de_dx)        

        de_dy = ((constellation[rec0.idB].y-estimated_position.y)/(math.sqrt((constellation[rec0.idB].x-estimated_position.x)**2+(constellation[rec0.idB].y-estimated_position.y)**2+(constellation[rec0.idB].z-estimated_position.z)**2)),
                -(constellation[rec0.idA].y-estimated_position.y)/(math.sqrt((constellation[rec0.idA].x-estimated_position.x)**2+(constellation[rec0.idA].y-estimated_position.y)**2+(constellation[rec0.idA].z-estimated_position.z)**2)), 
                (constellation[rec1.idB].y-estimated_position.y)/(math.sqrt((constellation[rec1.idB].x-estimated_position.x)**2+(constellation[rec1.idB].y-estimated_position.y)**2+(constellation[rec1.idB].z-estimated_position.z)**2)),
                -(constellation[rec1.idA].y-estimated_position.y)/(math.sqrt((constellation[rec1.idA].x-estimated_position.x)**2+(constellation[rec1.idA].y-estimated_position.y)**2+(constellation[rec1.idA].z-estimated_position.z)**2)),
                (constellation[rec2.idB].y-estimated_position.y)/(math.sqrt((constellation[rec2.idB].x-estimated_position.x)**2+(constellation[rec2.idB].y-estimated_position.y)**2+(constellation[rec2.idB].z-estimated_position.z)**2)),
                -(constellation[rec2.idA].y-estimated_position.y)/(math.sqrt((constellation[rec2.idA].x-estimated_position.x)**2+(constellation[rec2.idA].y-estimated_position.y)**2+(constellation[rec2.idA].z-estimated_position.z)**2)))

        derror_dy = sum(de_dy)

        de_dz = ((constellation[rec0.idB].z-estimated_position.z)/(math.sqrt((constellation[rec0.idB].x-estimated_position.x)**2+(constellation[rec0.idB].y-estimated_position.y)**2+(constellation[rec0.idB].z-estimated_position.z)**2)),
                -(constellation[rec0.idA].z-estimated_position.z)/(math.sqrt((constellation[rec0.idA].x-estimated_position.x)**2+(constellation[rec0.idA].y-estimated_position.y)**2+(constellation[rec0.idA].z-estimated_position.z)**2)), 
                (constellation[rec1.idB].z-estimated_position.z)/(math.sqrt((constellation[rec1.idB].x-estimated_position.x)**2+(constellation[rec1.idB].y-estimated_position.y)**2+(constellation[rec1.idB].z-estimated_position.z)**2)),
                -(constellation[rec1.idA].z-estimated_position.z)/(math.sqrt((constellation[rec1.idA].x-estimated_position.x)**2+(constellation[rec1.idA].y-estimated_position.y)**2+(constellation[rec1.idA].z-estimated_position.z)**2)),
                (constellation[rec2.idB].z-estimated_position.z)/(math.sqrt((constellation[rec2.idB].x-estimated_position.x)**2+(constellation[rec2.idB].y-estimated_position.y)**2+(constellation[rec2.idB].z-estimated_position.z)**2)),
                -(constellation[rec2.idA].z-estimated_position.z)/(math.sqrt((constellation[rec2.idA].x-estimated_position.x)**2+(constellation[rec2.idA].y-estimated_position.y)**2+(constellation[rec2.idA].z-estimated_position.z)**2)))

        derror_dz = sum(de_dz)

        # print(error, estimated_position.x, estimated_position.y, estimated_position.z)

        estimated_position.x = estimated_position.x - learning_rate*derror_dx
        estimated_position.y = estimated_position.y - learning_rate*derror_dy
        estimated_position.z = estimated_position.z - learning_rate*derror_dz

    
    return estimated_position, previous_error