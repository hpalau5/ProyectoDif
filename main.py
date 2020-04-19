import argparse
from perimeter_generation import *
from infill_generation import *
from gcode_emitter import *


if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", help="extruder radius", default=0.2)
    parser.add_argument("-d", help="infill density (0-100)", default=20)
    parser.add_argument("-z", help="slice height", default=0)

    args = parser.parse_args()
    
    emit_header()
    perimeter_list = generate_perimeter(5, int(args.r), int(args.z))
    infill_list = infill_generation(5, int(args.r), int(args.z), int(args.d))
    emit_gcode(perimeter_list)
    emit_gcode(infill_list)