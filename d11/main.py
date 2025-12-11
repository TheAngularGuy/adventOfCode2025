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
def solve_from_to(curent, finish):
    if curent == finish:
        return 1

    result = 0
    if curent in dictionary:
        for connection in dictionary[curent]:
            result += solve_from_to(connection, finish)
    return result


def part1():
    print("Part 1:", solve_from_to("you", "out"))


def part2():
    print("Part 2:",
          solve_from_to("svr", "dac") * solve_from_to("dac", "fft") * solve_from_to("fft", "out") +
          solve_from_to("svr", "fft") * solve_from_to("fft", "dac") * solve_from_to("dac", "out")
          )


part1()
part2()
