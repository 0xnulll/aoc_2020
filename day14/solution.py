from parse import *
import sys
import math
from functools import reduce


def get_solution_1(inputs):
    mask_and, mask_bit_to_change, memory_dict = None, None, {}
    for item in inputs:
        if item[0] == "mask":
            mask_and = int(
                "".join(map(lambda x: "1" if x == "X" else "0", item[1])), 2)
            mask_bit_to_change = int(
                "".join(map(lambda x: "0" if x == "X" else x, item[1])), 2)
        else:
            memory_dict[item[0]] = (item[1] & mask_and) | mask_bit_to_change
    return sum(memory_dict.values())


def modifyBit(n,  p,  b):
    mask = 1 << p
    return (n & ~mask) | ((b << p) & mask)


def get_solution_2(inputs):
    mask, x_pos, memory_dict = None, None, {}

    def recursive_modify(adr, pos, num):
        nonlocal x_pos
        if pos == len(x_pos):
            memory_dict[adr] = num
        else:
            adr1 = modifyBit(adr, x_pos[pos], 0)
            adr2 = modifyBit(adr, x_pos[pos], 1)
            recursive_modify(adr1, pos+1, num)
            recursive_modify(adr2, pos+1, num)

    for item in inputs:
        if item[0] == "mask":
            x_pos = []
            mask = int(
                "".join(map(lambda x: "1" if x == "1" else "0", item[1])), 2)
            for i, char in enumerate(item[1][::-1]):
                if char == "X":
                    x_pos.append(i)
        else:
            addr = item[0] | mask
            recursive_modify(addr, 0, item[1])

    return sum(memory_dict.values())


def process_input(input):
    input_processed = []
    for line in input.split("\n"):
        if "mask" in line:
            input_processed.append(list(parse("{} = {}", line)))
        else:
            input_processed.append(list(parse("mem[{:d}] = {:d}", line)))
    return input_processed


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(input_processed)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")
