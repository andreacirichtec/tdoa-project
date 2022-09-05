import math
from constellations import *

def error_f(constellation, rec0, rec1, rec2, estimated_position):
    
    e = (math.sqrt((constellation[rec0.idA].x-estimated_position.x)**2+(constellation[rec0.idA].y-estimated_position.y)**2+(constellation[rec0.idA].z-estimated_position.z)**2), 
        -math.sqrt((constellation[rec0.idB].x-estimated_position.x)**2+(constellation[rec0.idB].y-estimated_position.y)**2+(constellation[rec0.idB].z-estimated_position.z)**2),
        -rec0.dt,
        math.sqrt((constellation[rec1.idA].x-estimated_position.x)**2+(constellation[rec1.idA].y-estimated_position.y)**2+(constellation[rec0.idA].z-estimated_position.z)**2),
        -math.sqrt((constellation[rec1.idB].x-estimated_position.x)**2+(constellation[rec1.idB].y-estimated_position.y)**2+(constellation[rec0.idB].z-estimated_position.z)**2), 
        -rec1.dt,
        math.sqrt((constellation[rec2.idA].x-estimated_position.x)**2+(constellation[rec2.idA].y-estimated_position.y)**2+(constellation[rec0.idA].z-estimated_position.z)**2),   
        -math.sqrt((constellation[rec2.idB].x-estimated_position.x)**2+(constellation[rec2.idB].y-estimated_position.y)**2+(constellation[rec0.idB].z-estimated_position.z)**2),
        -rec2.dt)

    error = sum(e) 
    
    return error