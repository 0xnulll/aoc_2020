from functools import reduce

def get_solution_1(input):
    return sum([ len(reduce( lambda old,x: old.union(set(list(x))),item, set())) for item in input])

def get_solution_2(input):
    return sum([ len(reduce( lambda old,x: old.intersection(set(list(x))),item, set(list(item[0])))) for item in input])

def process_input(input):
    return list(map(lambda x: x.split("\n"), input.split("\n\n")))

with open('input.txt') as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(input_processed)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")
