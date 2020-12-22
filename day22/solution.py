from parse import *
import sys
from collections import defaultdict, Counter


def get_solution_1(game):

    while True:
        p1, p2 = game[1].pop(0), game[2].pop(0)
        if p1 > p2:
            winner = 1
        else:
            winner = 2
            p1, p2 = p2, p1
        game[winner].extend([p1,p2])
        if len(game[1]) == 0 or len(game[2]) == 0:
            break
    return sum([n * (i+1) for i, n in enumerate(game[winner][::-1])])


def get_solution_2(game):

    def combat(gme):
        cache = set()
        while True:
            t1, t2 = tuple(gme[1]), tuple(gme[2])
            if t1 in cache or t2 in cache:
                return 1
            cache.add(t1)
            cache.add(t2)
            p1 = gme[1].pop(0)
            p2 = gme[2].pop(0)
            winner = 0
            if len(gme[1]) >= p1 and len(gme[2]) >= p2:
                winner = combat({1: gme[1][:p1], 2: gme[2][:p2]})
            else:
                winner = 1 if p1 > p2 else 2
            if winner == 2:
                p1, p2 = p2, p1
            gme[winner].extend([p1,p2])

            if len(gme[1]) == 0 or len(gme[2]) == 0:
                return winner
    winner = combat(game)
    return sum([n * (i+1) for i, n in enumerate(game[winner][::-1])])


def process_input(input):
    game = {}
    for line in input.split("\n\n"):
        line = line.split("\n")
        player = parse("Player {:d}:", line[0])[0]
        cards = [int(x) for x in line[1:]]
        game[player] = cards
    return game


if len(sys.argv) < 2:
    print("Please enter input file in argument")

with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    r1 = get_solution_1(input_processed)
    print(
        f"Solution 1 = {r1}")
    input_processed = process_input(input_str)
    r2 = get_solution_2(input_processed)
    print(
        f"Solution 2 = {r2}")
