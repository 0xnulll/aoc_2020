from parse import *
import sys
from itertools import product
from collections import defaultdict

def get_solution_1(g,with_w=False):
    active_coord = g
    if with_w :
        directions = list(product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
        directions.remove((0, 0, 0, 0))
    else:
        directions = list(product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
        directions.remove((0, 0, 0))

    for i in range(6):
        new_active_coord = []
        active_count = defaultdict(int)
        for x,y,z,w in active_coord:
            for item in directions:
                if with_w:
                    dx, dy, dz, dw = item
                else:
                   dx, dy, dz = item
                   dw = 0
                active_count[( x+dx,y+dy,z+dz,w+dw)] += 1

        for coord in active_coord:
            c = active_count.pop(coord,0)
            if c in [2,3]:
                new_active_coord.append(coord)
        for coord, c in active_count.items():
            if c == 3:
                new_active_coord.append(coord)
        active_coord = new_active_coord
    return len(active_coord)


def process_input(input):
    inputs = list(map(lambda x: list(x.strip()), input.split("\n")))
    cells = []
    max_r, max_c = len(inputs), len(inputs[0])
    for r, row in enumerate(inputs):
        for c, v in enumerate(row):
            if v == "#":
                cells.append((r, c, 0, 0))
    return cells


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(
        f"Solution 1 = {get_solution_1(input_processed,with_w=False)}")
    print(
        f"Solution 1 = {get_solution_1(input_processed,with_w=True)}")
