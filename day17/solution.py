from parse import *
import sys
from itertools import product
from collections import defaultdict

directions3 = list(product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
directions3.remove((0, 0, 0))

directions4 = list(product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
directions4.remove((0, 0, 0, 0))


def check_rule3(g, r, c, z, w):
    return sum([1 if g[(i+r, j+c, k+z, 0)] == "#" else 0 for i, j, k in directions3])


def check_rule4(g, r, c, z, w):
    return sum([1 if g[(i+r, j+c, k+z, w+l)] == "#" else 0 for i, j, k, l in directions4])


def get_solution_1(g, max_r, max_c, with_w):
    max_z, max_w, min_r, min_c, min_z, min_w = 1, 1, 0, 0, 0, 0

    if with_w == False:
        check_rule = check_rule3
    else:
        check_rule = check_rule4

    def work(r, c, z, w):
        nonlocal check_rule, to_change
        t = check_rule(g, r, c, z, w)
        if g[(r, c, z, w)] == "#":
            if t not in (2, 3):
                to_change.append((r, c, z, w, "."))
        else:
            if t == 3:
                to_change.append((r, c, z, w, "#"))

    for i in range(6):
        to_change = list()
        for z in range(min_z-1, max_z+1):
            for r in range(min_r-1, max_r+1):
                for c in range(min_c-1, max_c+1):
                    if with_w:
                        for w in range(min_w-1, max_w+1):
                            work(r, c, z, w)
                    else:
                        work(r, c, z, 0)

        min_r -= 1
        min_c -= 1
        min_z -= 1
        min_w -= 1

        max_r += 1
        max_c += 1
        max_z += 1
        max_w += 1
        for r, c, z, w, v in to_change:
            g[(r, c, z, w)]=v
    return len(list(filter(lambda x: x == "#", g.values())))


def process_input(input):
    inputs = list(map(lambda x: list(x.strip()), input.split("\n")))
    cells = defaultdict(str)
    max_r, max_c = len(inputs), len(inputs[0])
    for r, row in enumerate(inputs):
        for c, v in enumerate(row):
            cells[(r, c, 0, 0)]=v
    return cells, max_r, max_c


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(
        f"Solution 1 = {get_solution_1(*input_processed,with_w=False)}")
    input_processed = process_input(input_str)
    print(
        f"Solution 1 = {get_solution_1(*input_processed,with_w=True)}")
