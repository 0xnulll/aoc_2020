from parse import *
import sys
import math
from collections import defaultdict
from functools import reduce


def get_solution_1(ranges, tickets, your_tickets):
    result = 0
    for row in tickets:
        for i, t in enumerate(row):
            invalid = True
            for item in ranges.values():
                for l, h in item:
                    if l <= t <= h:
                        invalid = False
                        break
            if invalid:
                result += t
                row[i] = None
    return result


def get_solution_2(ranges, tickets, your_tickets):
    result = 1
    max_len = len(ranges.keys())
    total_rows = len(tickets)
    possible_mapping = defaultdict(set)
    for i in range(max_len):
        for key, item in ranges.items():
            total = 0
            for k in range(total_rows):
                if tickets[k][i] == None:
                    total += 1  # for invalid
                elif item[0][0] <= tickets[k][i] <= item[0][1] or item[1][0] <= tickets[k][i] <= item[1][1]:
                    total += 1  # for valid
            if total == total_rows:
                # add one of possible seat type
                possible_mapping[i].add(key)

    for i in range(max_len):
        index, key = list(filter(lambda x: len(
            x[1]) == 1, possible_mapping.items()))[0]
        key = key.pop()
        for k, item in possible_mapping.items():
            if key in item:
                item.remove(key)
        if key.startswith("departure"):
            result *= your_tickets[index]
    return result


def process_input(input):
    ranges, tickets, your_tickets = defaultdict(list), [], []
    lines = input.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        if line.strip() == "":
            break
        t = list(parse("{} {:d}-{:d} or {:d}-{:d}", line))
        t[0] = t[0].strip(":")
        ranges[t[0]].append((t[1], t[2]))
        ranges[t[0]].append((t[3], t[4]))
    your_tickets += list(map(int, lines[i+2].split(",")))
    for i in range(i+5, len(lines)):
        line = lines[i]
        if line != "":
            tickets.append(list(map(int, line.split(","))))
    return ranges, tickets, your_tickets


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(*input_processed)}")
    print(f"Solution 2 = {get_solution_2(*input_processed)}")
