from math import sqrt, ceil

def infill_generation(radius, extruder_radius, slice_height, infill_density):    
    offset_radius = radius - extruder_radius
    spacing =  offset_radius / (offset_radius - (2 * extruder_radius - offset_radius) * infill_density / 100)

    if infill_density != 0:
        verticales=[]
        x = 0
        while (x < offset_radius - extruder_radius):
            sin = sqrt(1 - (x / offset_radius) ** 2)
            y = offset_radius * sin
            verticales.append((x, y, slice_height))
            verticales.append((x, -y, slice_height))
            verticales.append((x, -y, slice_height + 1))
            x = x + spacing
        
        for point in verticales[3:len(verticales)]:
            x, y, z =  point
            verticales.append((-x, y, z))

        horizontales=[]
        y = 0
        while (y < offset_radius - extruder_radius):
            cos = sqrt(1 - (y / offset_radius) ** 2)
            x = offset_radius * cos
            horizontales.append((x, y, slice_height))
            horizontales.append((-x, y, slice_height))
            horizontales.append((-x, y, slice_height + 1))
            y = y + spacing
        
        for point in horizontales[3:len(horizontales)]:
            x, y, z =  point
            horizontales.append((x, -y, z))

        result = verticales + horizontales
        return result
    else:
        return []
