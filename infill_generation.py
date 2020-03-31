import numpy as np

def infill_generation(radius, extruder_radius, slice_height):
    r = radius - extruder_radius
    lines_max = 3    
    range_lines =range(extruder_radius, radius*2 - extruder_radius, extruder_radius*2)

    num_lines = 0
    verticales=[]
    for x in range_lines:
        if num_lines<3:
            num_lines = num_lines+1
            for y in range_lines:
                verticales.append([x,y,slice_height])
        else:
            num_lines=0
            x=x+3
    
    count_v=0
    count_salir=0        
    num_lines=0
    horizontales=[]
    for y in range_lines:
        if num_lines<3:
            num_lines = num_lines+1
            for x in range_lines:              
                if count_v = 3:
                    horizontales.append([x,y,slice_height])
                    count_salir = count_salir+1
                    if count_salir = 3
                        count_v = 0
                        count_salir = 0
                else:
                    count_v = count_v+1                
        else:
            num_lines=0
            y=y+3 

    result = verticales + horizontales
    return result