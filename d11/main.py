from collections import deque
from functools import cache

with open("input.txt", "r") as file:
    content = file.read()

input_data: list[str] = list(filter(lambda el: len(el), content.split('\n')))

dictionary = dict()
for row in input_data:
    name, rest = row.split(':')
    list_connections = rest.strip().split(' ')
    dictionary[name.strip()] = list_connections

@cache
def solve_for(start, finish):
    q = deque()
    q.append((start, []))

    paths = []
    while len(q) > 0:
        current_name, history = q.popleft()
        if current_name == finish:
            paths.append(history + [current_name])
            continue

        if not current_name in dictionary:
            continue

        current_connections = dictionary[current_name]
        for connection in current_connections:
            if connection not in history:
                q.append((connection, history + [current_name]))

    return len(paths)


def part1():
    print("Part 1:", solve_for("you", "out"))


def part2():
    print("Part 2:",
          solve_for("svr", "dac") * solve_for("dac", "fft") * solve_for("fft", "out") +
          solve_for("svr", "fft") * solve_for("fft", "dac") * solve_for("dac", "out")
          )


part1()
part2()
