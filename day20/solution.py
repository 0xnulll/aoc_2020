from parse import *
import sys
from functools import wraps
import math
import re

tile_len = 9
board = None
board_len = None


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


def flip_tile(tile):
    return [row[::-1] for row in tile]


def rotations(tile):
    o = {tuple(tile)}
    tile_len = len(tile)-1
    for n in range(4):
        tile = ["".join([tile[i][k] for i in range(tile_len, -1, -1)])
                for k in range(tile_len+1)]
        o.add(tuple(tile))
    return o


def get_groups(tile):
    return rotations(tile) | rotations(flip_tile(tile))


def get_solution_1(tiles):
    global board, board_len
    board_len = int(math.sqrt(len(tiles.keys())))
    stack = list(reversed([(r, c) for c in range(board_len)
                           for r in range(board_len)]))
    board = [[0] * board_len for _ in range(board_len)]

    def solve():
        if not stack:
            return board[0][0][0] * board[-1][0][0] * board[0][-1][0] * board[-1][-1][0]
        r, c = stack.pop()
        for tile_id in list(tiles):
            tile_grps = tiles[tile_id]
            del tiles[tile_id]
            for tile in tile_grps:
                if r > 0:
                    if board[r-1][c][1][-1] != tile[0]:
                        continue
                if c > 0:
                    if [row[-1] for row in board[r][c-1][1]] != [row[0] for row in tile]:
                        continue
                board[r][c] = (tile_id, tile)
                res = solve()
                if res:
                    return res
            tiles[tile_id] = tile_grps
        stack.append((r, c))
        return None
    return solve()


def get_solution_2(board):
    global board_len
    board_stiched = []
    pattern = [r"..................#.",
               r"#....##....##....###", r".#..#..#..#..#..#..."]

    for r in range(board_len):
        for k in range(1, tile_len):
            t = "".join([board[r][c][1][k][1:tile_len]
                         for c in range(board_len)])
            board_stiched.append(t)

    p_len = len(pattern[0])
    board_len = len(board_stiched)
    roughness = sum([row.count("#") for row in board_stiched])
    for tile in get_groups(board_stiched):
        count = 0
        for r in range(0, board_len-3):
            for c in range(board_len - p_len):
                if re.match(pattern[0], tile[r][c:p_len+c]) \
                        and re.match(pattern[1], tile[r+1][c:p_len+c]) \
                        and re.match(pattern[2], tile[r+2][c:p_len+c]):
                    count += 1
        if count:
            return roughness - count*15


def process_input(input):
    squares = input.split("\n\n")
    o = {}
    for s in squares:
        s = s.split("\n")
        id = parse("Tile {:d}:", s[0])[0]
        o[id] = get_groups(s[1:])
    return o


if len(sys.argv) < 2:
    print("Please enter input file in argument")

with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(
        f"Solution 1 = {get_solution_1(input_processed)}")
    print(
        f"Solution 2 = {get_solution_2(board)}")
