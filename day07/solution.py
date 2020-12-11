from parse import *
import sys
def get_solution_1(input):
    bag_set = set()
    visited = {}
    def dfs_helper(bag_to_check):
        nonlocal bag_set,visited
        if bag_to_check in visited:
            return visited[bag_to_check]
        for count, bag in input[bag_to_check]:
            if bag == "shiny gold":
                visited[bag_to_check] = True
                return True
            elif dfs_helper(bag):   # if any of the child node contains route to "shiny gold"
                    visited[bag_to_check] = True
                    return True
        visited[bag_to_check] = False
        return visited[bag_to_check]

    for bag in input:
        if bag not in bag_set:
            if dfs_helper(bag) :
                bag_set.add(bag)
    return len(bag_set)

def get_solution_2(input):
    cache={}
    def dfs_helper(bag_to_check):
        nonlocal cache
        total_bag = 1
        for count, bag in input[bag_to_check]:
            cache_count = cache[bag] if bag in cache else dfs_helper(bag)
            total_bag += count *  cache_count
        cache[bag_to_check] = total_bag
        return total_bag
    return dfs_helper("shiny gold") - 1

def process_input(input):
    input_processed = {}
    for line in input.split("\n"):
        token = line.split("bags contain")
        root = token[0].strip()
        if root not in input_processed:
            input_processed[root]=set()
        for bag_str in token[1].split(","):
            temp =  parse("{:d} {} bag",bag_str.strip("s."))
            if temp:
                input_processed[root].add((temp[0], temp[1].strip()))
    return input_processed
if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(input_processed)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")