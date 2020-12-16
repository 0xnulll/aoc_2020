import sys


def get_solution_1(input):
    map_ = {}
    for num in input:
        if 2020 - num in map_:
            return (2020-num)*num
        else:
            map_[num] = True


def get_solution_2(input):
    for num in input:
        map_ = {}
        sum_to_match = 2020 - num

        for num2 in input:
            if sum_to_match - num2 in map_:
                return (sum_to_match-num2)*num2*num
            else:
                map_[num2] = True


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input = file.read()
    input = [int(item) for item in input.split("\n")]
    print(f"Solution 1 = {get_solution_1(input)}")

    print(f"Solution 2 = {get_solution_2(input)}")

"""
Solution 1
    Time Complexity O(n)
    Space Complexity O(n)

Solution 2
    Time Complexity O(n*n)
    Space Complexity O(n)
"""
