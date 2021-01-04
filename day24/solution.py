from parse import *
import sys
from collections import defaultdict, Counter


directions = {
    "e": (1, 0),
    "se": (.5, -.5),
    "sw": (-.5, -.5),
    "w": (-1, 0),
    "nw": (-.5, .5),
    "ne": (.5, .5)
}


def get_solution_1(instructions):
    tiles = set()
    for ins in instructions:
        x, y, token = 0, 0, ""
        for c in ins:
            if token not in directions:
                token += c
            else:
                x += directions[token][0]
                y += directions[token][1]
                token = c
        x += directions[token][0]
        y += directions[token][1]
        if (x, y) in tiles:
            tiles.remove((x, y))
        else:
            tiles.add((x, y))

    return len(tiles), tiles


def get_solution_2(tiles):
    for i in range(100):
        count_dic = defaultdict(int)
        # Populating adjacent tiles
        new = set()
        for x, y in tiles:
            for dx, dy in directions.values():
                count_dic[(x+dx), (y+dy)] += 1
        for (x, y), c in count_dic.items():
            if (x, y) in tiles:
                if c == 0 or c > 2:
                    pass
                else:
                    new.add((x, y))
            else:
                if c == 2:
                    new.add((x, y))
        tiles = new
    return len(tiles)


def process_input(input):
    return input.split("\n")


if len(sys.argv) < 2:
    print("Please enter input file in argument")

with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    r1, tiles = get_solution_1(input_processed)
    print(
        f"Solution 1 = {r1}")
    r2 = get_solution_2(tiles)
    print(
        f"Solution 2 = {r2}")
