
from collections import Counter, defaultdict
import sys


def get_solution_1(input):
    valid_pass = 0
    for item in input:
        c = Counter(item[3])
        if item[2] in c and item[0] <= c[item[2]] <= item[1]:
            valid_pass += 1

    return valid_pass


def get_solution_2(input):
    valid_pass = 0
    for item in input:
        count = 0
        str_ = item[3]
        if str_[item[0]-1] == item[2]:
            count += 1
        if str_[item[1]-1] == item[2]:
            count += 1
        if count == 1:
            valid_pass += 1
    return valid_pass


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input = file.read()
    input_processed = []
    for item in input.split("\n"):
        temp = [None]*4
        splits = item.split(":")
        temp[3] = splits[1].strip()
        splits = splits[0].split(" ")
        temp[2] = splits[1].strip()
        splits = splits[0].split("-")
        temp[0] = int(splits[0])
        temp[1] = int(splits[1])
        input_processed.append(temp)
    print(f"Solution 1 = {get_solution_1(input_processed)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")

"""
Solution 1
    Time Complexity O( length of inputs * length of each string )
    Space Complexity O( max(length of string) )

Solution 2
    Time Complexity O(length of inputs )
    Space Complexity 0
"""
