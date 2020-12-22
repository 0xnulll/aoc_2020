from parse import *
import sys
from collections import defaultdict, Counter


def get_solution_1(foods):
    all_allergens = {}
    all_ingrs = Counter()
    for ingrs, allergens in foods:
        for allergen in allergens:
            if allergen not in all_allergens:
                all_allergens[allergen] = set(ingrs)
            else:
                all_allergens[allergen] &= set(ingrs)
        all_ingrs.update(ingrs)

    all_allergens_set = set()
    for a in all_allergens.values():
        all_allergens_set |= all_allergens_set | a
    not_allergens = set(list(all_ingrs)) - all_allergens_set
    return sum([all_ingrs[ing] for ing in not_allergens]), all_allergens


def get_solution_2(alergens):
    matched = {}
    for i in alergens:
        key, v = [(k, list(v)[0]) for k, v in alergens.items()
                  if len(v) == 1 and k not in matched][0]
        matched[key] = v
        for key2 in alergens:
            if key2 != key:
                alergens[key2] -= set([v])
    matched = sorted(matched.items(), key=lambda x: x[0])
    matched = map(lambda x: x[1], matched)
    return ",".join(matched)


def process_input(input):
    foods = []
    for line in input.split("\n"):
        ingrs, allergens = line.strip(")").split(" (contains ")
        ingrs = ingrs.split()
        allergens = allergens.split(", ")
        foods.append((ingrs, allergens))
    return foods


if len(sys.argv) < 2:
    print("Please enter input file in argument")

with open(sys.argv[1]) as file:
    input_str = file.read()
    input_processed = process_input(input_str)
    r1, allergens = get_solution_1(input_processed)
    print(
        f"Solution 1 = {r1}")
    r2 = get_solution_2(allergens)
    print(
        f"Solution 2 = {r2}")
