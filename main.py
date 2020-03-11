import argparse
from perimeter_generation import *
from infill_generation import *
from gcode_emitter import *


if __name__== "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", help="cylinder radius")
    parser.add_argument("-d", help="infill density")
    parser.add_argument("-z", help="slice height")

    args = parser.parse_args()
