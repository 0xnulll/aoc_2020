from parse import *
import sys
def get_solution_1(input):
    ptr, acc, visited = 0, 0, set()
    while ptr < len(input):
        op, c = input[ptr][0], int(input[ptr][1])
        if ptr in visited :
            return acc, ptr
        visited.add(ptr)
        if op == "nop":
            ptr += 1
        elif op == "acc":
            acc += c
            ptr += 1
        elif op == "jmp":
            ptr += c
    return acc, ptr

def get_solution_2(input):
    swap_dict = {
        "nop" : "jmp",
        "jmp" : "nop"
    }
    try_list = { i if item[0] in swap_dict else None for i, item in enumerate(input) }
    try_list.remove(None)
    for to_try in try_list:
        input[to_try][0] = swap_dict[input[to_try][0]]  # swap instruction
        acc, ptr = get_solution_1(input)
        if ptr == len(input):
            return acc
        input[to_try][0] = swap_dict[input[to_try][0]]  # revert instruction

def process_input(input):
    return list(map( lambda line : list(parse("{} {:d}",line)), input.split("\n") ) )

if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(input_processed)[0]}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")