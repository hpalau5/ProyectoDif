import numpy as np
from math import floor,cos,sin,pi

def generate_perimeter(radius, extruder_radius, slice_height):
    r = radius - extruder_radius
    faces = 100
    angle = 360 / faces

    rango = range(0, 360, floor(angle))
    result = np.zeros(len(rango) + 1, dtype=object)

    for idx, angle in enumerate(rango):
        result[idx] = (r * cos(angle * pi / 180), r * sin(angle * pi / 180), slice_height)

    lastx, lasty, _ = result[len(rango) - 1]
    result[len(rango)] = (lastx, lasty, slice_height + 1)
    return result