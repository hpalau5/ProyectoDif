import numpy as np
from math import floor,cos,sin,pi

def generate_perimeter(radius, extruder_radius, slice_height):
    r = radius - extruder_radius
    faces = 10000
    inc = 360 / faces
    result = np.zeros(faces + 1, dtype=object)

    idx = 0
    angle = 0
    while (angle < 360):
        result[idx] = (r * cos(angle * pi / 180), r * sin(angle * pi / 180), slice_height)
        idx = idx + 1
        angle = angle + inc
    
    lastx, lasty, _ = result[faces - 1]
    result[faces] = (lastx, lasty, slice_height + 1)
    return result