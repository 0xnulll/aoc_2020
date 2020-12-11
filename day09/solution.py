from parse import *
import sys
def get_solution_1(input):
    pr_len, num_set = 5 if len(input) < 25 else 25, set()
    num_set = num_set.union(set(input[0:pr_len]))
    for i in range(pr_len,len(input)):
        flag = False
        for num in num_set:
            if num in num_set and input[i] - num in num_set:
                flag = True
                break
        if flag == False:
            return input[i]
        num_set.remove(input[i-pr_len])
        num_set.add(input[i])

def get_solution_2(input):
    invalid_num = get_solution_1(input)
    left, right = 0, 1
    total_sum = sum(input[left:right+1])
    while right <= len(input) and left < right:
        if total_sum == invalid_num:
            break
        if total_sum < invalid_num:
            right += 1
            total_sum += input[right]
        elif total_sum > invalid_num:
            total_sum -= input[left]
            left += 1
    return min( input[left:right+1]) + max( input[left:right+1])

def process_input(input):
    return list(map(int, input.split("\n") ) )

if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(input_processed)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")