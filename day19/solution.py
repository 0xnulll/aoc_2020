from parse import *
import sys
from itertools import product
from collections import defaultdict
from functools import wraps

def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

def get_solution_1(rules, msgs):
    @memoize
    def check(rule_id, msg, start):
        rule = rules[rule_id]
        if rule[0][0][0] == '"':
            return {start+1} if start < len(msg) and msg[start] == rule[0][0][1] else set()
        else:
            end = set()
            for subrule in rule:
                buf = {start}
                for part in subrule:
                    temp = set()
                    for loc in buf:
                        temp = temp | check(part, msg, loc)
                    buf = temp
                end = end | buf
            return end
    return sum([1 if len(msg) in check('0', msg, 0) else 0 for msg in msgs])


def process_input(input):
    input = input.split("\n\n")
    rules = {}
    msgs = input[1].split("\n")
    for line in input[0].split("\n"):
        r = line.split(":")
        rules[r[0]] = [t.strip().split(" ") for t in r[1].split("|")]
    return rules, msgs


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(
        f"Solution 1 = {get_solution_1(*input_processed)}")
    input_processed[0]['8'] = [['42'], ['42', '8']]
    input_processed[0]['11'] = [['42', '31'], ['42', '11', '31']]
    print(
        f"Solution 2 = {get_solution_1(*input_processed)}")
