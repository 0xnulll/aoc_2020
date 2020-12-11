from parse import *
import sys
def get_solution_1(input):
    diff = { 1: 1, 3: 1 }
    for i in range(1,len(input)):
        dif = input[i] - input[i-1]
        diff[dif] += 1
    return diff[1] * diff[3]


def get_solution_2(input):
    input = [input[0]] + input + [input[-1]+3]
    n = len(input)
    cache = [0] * n
    cache[0] = 1
    for i in range(1,n):
        if i-1 >= 0 and input[i] - input[i-1] <= 3:
            cache[i] += cache[i-1]
        if i-2 >= 0 and input[i] - input[i-2] <= 3:
            cache[i] += cache[i-2]
        if i-3 >= 0 and input[i] - input[i-3] <= 3:
            cache[i] += cache[i-3]
    return cache[n-1]


def process_input(input):
    return list(map(int, input.split("\n") ) )

if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    input_processed = sorted(input_processed)
    print(f"Solution 1 = {get_solution_1(input_processed)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")