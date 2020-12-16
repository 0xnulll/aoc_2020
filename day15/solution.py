from parse import *
import sys
import math
from collections import defaultdict
from functools import reduce


def get_solution_1(inputs, n):
    spoken_dict, spoken_number, l = defaultdict(list), None, len(inputs)
    for i in range(l):
        spoken_number = inputs[i]
        spoken_dict[spoken_number].append(i)
    for i in range(l, n):
        if len(spoken_dict[spoken_number]) <= 1:
            spoken_number = 0
        else:
            t = spoken_dict[spoken_number]
            spoken_number = t[0] - t[1]
        spoken_dict[spoken_number].insert(0, i)
        if len(spoken_dict[spoken_number]) > 2:
            spoken_dict[spoken_number].pop()
    return spoken_number


def process_input(input):
    return list(map(int, input.split(",")))


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(input_processed,2020)}")
    print(f"Solution 2 = {get_solution_1(input_processed,30000000)}")
