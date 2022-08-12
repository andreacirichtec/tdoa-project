import math
from data.constellations import *

def gradient_descent_f(constellation, rec0, rec1, rec2, estimated_position, iterations = 1000, learning_rate = 0.0001, stopping_threshold = 1e-6):
    
    previous_error = 1e6

    for i in range(iterations):

        e = (math.sqrt((constellation3[rec0.idA].x-estimated_position.x)**2+(constellation3[rec0.idA].y-estimated_position.y)**2+(constellation3[rec0.idA].z-estimated_position.z)**2), 
        -math.sqrt((constellation3[rec0.idB].x-estimated_position.x)**2+(constellation3[rec0.idB].y-estimated_position.y)**2+(constellation3[rec0.idB].z-estimated_position.z)**2),
        -rec0.dt,
        math.sqrt((constellation3[rec1.idA].x-estimated_position.x)**2+(constellation3[rec1.idA].y-estimated_position.y)**2+(constellation3[rec0.idA].z-estimated_position.z)**2),
        -math.sqrt((constellation3[rec1.idB].x-estimated_position.x)**2+(constellation3[rec1.idB].y-estimated_position.y)**2+(constellation3[rec0.idB].z-estimated_position.z)**2), 
        -rec1.dt,
        math.sqrt((constellation3[rec2.idA].x-estimated_position.x)**2+(constellation3[rec2.idA].y-estimated_position.y)**2+(constellation3[rec0.idA].z-estimated_position.z)**2),   
        -math.sqrt((constellation3[rec2.idB].x-estimated_position.x)**2+(constellation3[rec2.idB].y-estimated_position.y)**2+(constellation3[rec0.idB].z-estimated_position.z)**2),
        -rec2.dt)

        error = sum(e) 

        if (abs(previous_error) < abs(error)) or abs(previous_error-error)<=stopping_threshold:
            return estimated_position, previous_error

        previous_error = error

        de_dx = ((constellation3[rec0.idB].x-estimated_position.x)/(math.sqrt((constellation3[rec0.idB].x-estimated_position.x)**2+(constellation3[rec0.idB].y-estimated_position.y)**2+(constellation3[rec0.idB].z-estimated_position.z)**2)),
                -(constellation3[rec0.idA].x-estimated_position.x)/(math.sqrt((constellation3[rec0.idA].x-estimated_position.x)**2+(constellation3[rec0.idA].y-estimated_position.y)**2+(constellation3[rec0.idA].z-estimated_position.z)**2)), 
                (constellation3[rec1.idB].x-estimated_position.x)/(math.sqrt((constellation3[rec1.idB].x-estimated_position.x)**2+(constellation3[rec1.idB].y-estimated_position.y)**2+(constellation3[rec1.idB].z-estimated_position.z)**2)),
                -(constellation3[rec1.idA].x-estimated_position.x)/(math.sqrt((constellation3[rec1.idA].x-estimated_position.x)**2+(constellation3[rec1.idA].y-estimated_position.y)**2+(constellation3[rec1.idA].z-estimated_position.z)**2)),
                (constellation3[rec2.idB].x-estimated_position.x)/(math.sqrt((constellation3[rec2.idB].x-estimated_position.x)**2+(constellation3[rec2.idB].y-estimated_position.y)**2+(constellation3[rec2.idB].z-estimated_position.z)**2)),
                -(constellation3[rec2.idA].x-estimated_position.x)/(math.sqrt((constellation3[rec2.idA].x-estimated_position.x)**2+(constellation3[rec2.idA].y-estimated_position.y)**2+(constellation3[rec2.idA].z-estimated_position.z)**2)))

        derror_dx = sum(de_dx)        

        de_dy = ((constellation3[rec0.idB].y-estimated_position.y)/(math.sqrt((constellation3[rec0.idB].x-estimated_position.x)**2+(constellation3[rec0.idB].y-estimated_position.y)**2+(constellation3[rec0.idB].z-estimated_position.z)**2)),
                -(constellation3[rec0.idA].y-estimated_position.y)/(math.sqrt((constellation3[rec0.idA].x-estimated_position.x)**2+(constellation3[rec0.idA].y-estimated_position.y)**2+(constellation3[rec0.idA].z-estimated_position.z)**2)), 
                (constellation3[rec1.idB].y-estimated_position.y)/(math.sqrt((constellation3[rec1.idB].x-estimated_position.x)**2+(constellation3[rec1.idB].y-estimated_position.y)**2+(constellation3[rec1.idB].z-estimated_position.z)**2)),
                -(constellation3[rec1.idA].y-estimated_position.y)/(math.sqrt((constellation3[rec1.idA].x-estimated_position.x)**2+(constellation3[rec1.idA].y-estimated_position.y)**2+(constellation3[rec1.idA].z-estimated_position.z)**2)),
                (constellation3[rec2.idB].y-estimated_position.y)/(math.sqrt((constellation3[rec2.idB].x-estimated_position.x)**2+(constellation3[rec2.idB].y-estimated_position.y)**2+(constellation3[rec2.idB].z-estimated_position.z)**2)),
                -(constellation3[rec2.idA].y-estimated_position.y)/(math.sqrt((constellation3[rec2.idA].x-estimated_position.x)**2+(constellation3[rec2.idA].y-estimated_position.y)**2+(constellation3[rec2.idA].z-estimated_position.z)**2)))

        derror_dy = sum(de_dy)

        de_dz = ((constellation3[rec0.idB].z-estimated_position.z)/(math.sqrt((constellation3[rec0.idB].x-estimated_position.x)**2+(constellation3[rec0.idB].y-estimated_position.y)**2+(constellation3[rec0.idB].z-estimated_position.z)**2)),
                -(constellation3[rec0.idA].z-estimated_position.z)/(math.sqrt((constellation3[rec0.idA].x-estimated_position.x)**2+(constellation3[rec0.idA].y-estimated_position.y)**2+(constellation3[rec0.idA].z-estimated_position.z)**2)), 
                (constellation3[rec1.idB].z-estimated_position.z)/(math.sqrt((constellation3[rec1.idB].x-estimated_position.x)**2+(constellation3[rec1.idB].y-estimated_position.y)**2+(constellation3[rec1.idB].z-estimated_position.z)**2)),
                -(constellation3[rec1.idA].z-estimated_position.z)/(math.sqrt((constellation3[rec1.idA].x-estimated_position.x)**2+(constellation3[rec1.idA].y-estimated_position.y)**2+(constellation3[rec1.idA].z-estimated_position.z)**2)),
                (constellation3[rec2.idB].z-estimated_position.z)/(math.sqrt((constellation3[rec2.idB].x-estimated_position.x)**2+(constellation3[rec2.idB].y-estimated_position.y)**2+(constellation3[rec2.idB].z-estimated_position.z)**2)),
                -(constellation3[rec2.idA].z-estimated_position.z)/(math.sqrt((constellation3[rec2.idA].x-estimated_position.x)**2+(constellation3[rec2.idA].y-estimated_position.y)**2+(constellation3[rec2.idA].z-estimated_position.z)**2)))

        derror_dz = sum(de_dz)

        #print(error, estimated_position.x, estimated_position.y, estimated_position.z)

        estimated_position.x = estimated_position.x - learning_rate*derror_dx
        estimated_position.y = estimated_position.y - learning_rate*derror_dy
        estimated_position.z = estimated_position.z - learning_rate*derror_dz
    
    return estimated_position, previous_error