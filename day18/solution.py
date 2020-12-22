from parse import *
import sys
from itertools import product
from collections import defaultdict

precedence = None


def precedence_1(op):
    if op == '+' or op == '*':
        return 1
    return 0


def precedence_2(op):
    if op == '+':
        return 2
    if op == "*":
        return 1
    return 0


def applyOp(a, b, op):
    if op == '+':
        return a + b
    if op == '*':
        return a * b


def evaluate(tokens):
    values = []
    ops = []
    i = 0
    while i < len(tokens):
        if tokens[i] == ' ':
            i += 1
            continue
        elif tokens[i] == '(':
            ops.append(tokens[i])
        elif tokens[i].isdigit():
            values.append(int(tokens[i]))
        elif tokens[i] == ')':
            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyOp(val1, val2, op))
            # pop opening brace.
            ops.pop()
        else:
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                values.append(applyOp(val1, val2, op))
            ops.append(tokens[i])
        i += 1
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()
        values.append(applyOp(val1, val2, op))
    return values[-1]


def get_solution_1(arr):
    return sum(list(map(lambda x: evaluate(x.replace("(", "( ").replace(")", " )").split(" ")), arr)))


def process_input(input):
    return input.split("\n")


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    precedence = precedence_1
    print(
        f"Solution 1 = {get_solution_1(input_processed)}")
    precedence = precedence_2
    print(
        f"Solution 2 = {get_solution_1(input_processed)}")
