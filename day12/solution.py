from parse import *
import sys
import math


class DirectedVector:
    def __init__(self, x, y, dir=0):
        self.x = x
        self.y = y
        self.dir = dir

    def getManhattanDistance(self):
        return round(abs(self.y) + abs(self.x))


def get_solution_1(input):
    ship_pos = DirectedVector(x=0, y=0, dir=0)
    for move, move_val in input:
        if move == "N":
            ship_pos.x += move_val
        if move == "S":
            ship_pos.x -= move_val
        if move == "E":
            ship_pos.y += move_val
        if move == "W":
            ship_pos.y -= move_val
        if move == "L":
            ship_pos.dir += move_val
        if move == "R":
            ship_pos.dir -= move_val
        if move == "F":
            rad = math.radians(ship_pos.dir)
            ship_pos.x, ship_pos.y = ship_pos.x + move_val * \
                math.sin(rad), ship_pos.y + move_val * math.cos(rad)
    return ship_pos.getManhattanDistance()


def get_solution_2(input):
    ship_pos = DirectedVector(x=0, y=0)
    waypoint_pos = DirectedVector(x=10, y=1)
    for move, move_val in input:
        if move == "N":
            waypoint_pos.y += move_val
        if move == "S":
            waypoint_pos.y -= move_val
        if move == "E":
            waypoint_pos.x += move_val
        if move == "W":
            waypoint_pos.x -= move_val
        if move == "L":
            rad = math.atan2(waypoint_pos.y, waypoint_pos.x) + \
                math.radians(move_val)
            dist = math.sqrt(waypoint_pos.y**2 + waypoint_pos.x**2)
            waypoint_pos.x,  waypoint_pos.y = dist * \
                math.cos(rad),  dist * math.sin(rad)
        if move == "R":
            rad = math.atan2(waypoint_pos.y, waypoint_pos.x) - \
                math.radians(move_val)
            dist = math.sqrt(waypoint_pos.y**2 + waypoint_pos.x ** 2)
            waypoint_pos.x,  waypoint_pos.y = dist * \
                math.cos(rad),  dist * math.sin(rad)
        if move == "F":
            ship_pos.x, ship_pos.y = ship_pos.x + move_val * \
                waypoint_pos.x,  ship_pos.y + move_val * waypoint_pos.y
    return ship_pos.getManhattanDistance()


def process_input(input):
    return list(map(lambda x: tuple(parse("{}{:d}", x)), input.split("\n")))


if len(sys.argv) < 2:
    print("Please enter input file in argument")
    exit(1)
with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    print(f"Solution 1 = {get_solution_1(input_processed)}")
    print(f"Solution 2 = {get_solution_2(input_processed)}")
