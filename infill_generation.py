import numpy as np

def infill_generation(radius, extruder_radius, slice_height,infill_density):    

    range_lines =range(extruder_radius, radius*2 - extruder_radius, extruder_radius*2)

    verticales=[]
    num_lines = 0
    for x in range_lines:

        if num_lines<3:
            num_lines = num_lines+1

            #dibujo de linea
            for y in range_lines:
                verticales.append([x,y,slice_height])

        #pone a 0 el contador de lineas y salta 3 lineas
        else:
            num_lines=0
            x=x+3

    horizontales=[]
    count_v=0
    count_salir=0        
    num_lines=0
    for y in range_lines:

        if num_lines<3:
            num_lines = num_lines+1

            #dibujo de lineas
            for x in range_lines:   

                #empieza en 0 hasta 3,"lineas verticales", entonces dibuja           
                if count_v = 3:
                    horizontales.append([x,y,slice_height])
                    count_salir = count_salir+1

                    #cuenta hasta las siguientes lineas verticales y levanta el extruder
                    if count_salir = 3
                    horizontales.append([x,y,slice_height+1])
                        count_v = 0
                        count_salir = 0
                else:
                    count_v = count_v+1   

        #pone a 0 el contador de lineas y salta 3                         
        else:
            num_lines=0
            y=y+3 

    result = verticales + horizontales
    return result
