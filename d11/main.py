from itertools import combinations
from z3 import *

with open("input.txt", "r") as file:
    content = file.read()

input_data: list[str] = list(filter(lambda el: len(el), content.split('\n')))


def part1():
    total = 0
    print("Part 1:", total)


part1()
