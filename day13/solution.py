from parse import *
import sys
import math
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_solution_1(start, bus_ids):
    low_time, ans = 0, 0
    for bus_id in bus_ids:
        if bus_id != "x":
            t = start / int(bus_id)
            if round(t) != math.floor(t):
                if low_time < math.floor(t) * int(bus_id):
                    low_time = round(t) * int(bus_id) - start
                    ans = low_time * int(bus_id)
    return ans


def get_solution_2(start, bus_ids):
    ans = 1
    n_arr = []
    a_arr = []
    for i, bus_id in enumerate(bus_ids):
        if bus_id != "x":
            n_arr.append(int(bus_id))
            a_arr.append(int(bus_id)-i)
    return chinese_remainder(n_arr, a_arr)


def process_input(input):
    input = input.split("\n")
    start = int(input[0])
    bus_ids = input[1].split(",")
    return start, bus_ids


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(*input_processed)}")
    print(f"Solution 2 = {get_solution_2(*input_processed)}")
