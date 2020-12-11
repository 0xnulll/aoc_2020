from functools import reduce
from operator import mul
def get_solution_1(input,slopx,slopy):
    col, col_len = 0 , len(input[0])
    def custom_reduce(count,row):
        nonlocal col
        count = count +1 if input[row][col] == "#" else count
        col = (col+slopy)%col_len
        return count
    return reduce( custom_reduce , range(0,len(input),slopx), 0 )

def get_solution_2(input):
    return reduce(mul,map(lambda item : get_solution_1(input,item[1],item[0]), [ [1,1], [3,1], [5,1], [7,1], [1,2] ] ))

input_processed = []
with open('input.txt') as file:
    input_str = file.read()
    input_processed = [item.strip() for item in input_str.split("\n") ]
    print(f"Solution 1 = {get_solution_1(input_processed,1,3)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")
