from parse import *
import sys
from itertools import product

direction = [ (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def check_rule1(arr,r,c,row,col):
    return sum([ 1 if 0<=i+r<row and 0<=j+c<col and arr[i+r][j+c] == "#" else 0 for i,j in direction ])

def check_rule2(arr,r,c,row,col):
    count = 0
    for i,j in direction :
        nr,nc = r+i, c+j
        while 0<=nr<row and 0<=nc<col:
            if arr[nr][nc] == "L":
                break
            elif arr[nr][nc] == "#":
                count += 1
                break
            nr,nc = nr+i, nc+j
    return count

def get_solution_1(input):
    row, col = len(input), len(input[0])
    to_change = [None]
    while to_change:
        count, to_change = 0, list()
        for r in range(row):
            for c in range(col):
                if input[r][c] in {"L","#"}:
                    t = check_rule1(input,r,c,row,col)
                if input[r][c] == "L" and t  == 0 :
                    to_change.append( (r,c,"#") )
                elif input[r][c] == "#" and t >= 4 :
                    to_change.append( (r,c,"L") )
                if input[r][c] == "#":
                    count += 1
        for r,c,t in to_change:
            input[r][c] = t
    return count

def get_solution_2(input):
    row, col = len(input), len(input[0])
    to_change = [None]
    while to_change:
        count, to_change = 0, list()
        for r in range(row):
            for c in range(col):
                if input[r][c] in {"L","#"}:
                    occupied = check_rule2(input,r,c,row,col)
                if input[r][c] == "L" and occupied  == 0 :
                    to_change.append( (r,c,"#") )
                elif input[r][c] == "#" and occupied >= 5 :
                    to_change.append( (r,c,"L") )
                if input[r][c] == "#":
                    count += 1
        for r,c,t in to_change:
            input[r][c] = t
    return count


def process_input(input):
    return list(map(lambda x:list(x.strip()), input.split("\n") ) )

if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1([ line.copy() for line in input_processed ])}")
    print(f"Solution 2 = {get_solution_2([ line.copy() for line in input_processed ])}")