from parse import *
import sys
from collections import defaultdict, Counter


def get_loop_size(v):
    s, val, i = 7, 1, 0
    while val != v:
        val *= s
        val = val % 20201227
        i += 1
    return i


def get_public_key(s, loop_size):
    val = 1
    for i in range(loop_size):
        val *= s
        val %= 20201227
    return val


def get_solution_1(nums):
    l1 = get_loop_size(nums[0])
    l2 = get_loop_size(nums[1])
    return get_public_key(nums[0], l2)


def process_input(input):
    return list(map(int, input.split()))


if len(sys.argv) < 2:
    print("Please enter input file in argument")

with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    r1 = get_solution_1(input_processed)
    print(
        f"Solution 1 = {r1}")
