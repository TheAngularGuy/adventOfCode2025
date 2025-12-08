from functools import cache

with open("input.txt", "r") as file:
    content = file.read()

input_data: list[str] = list(filter(lambda el: len(el), content.split('\n')))
display_grid = False

def part1():
    lines = list(map(list, input_data))

    total = 0
    for y in range(len(lines) - 1):
        for x in range(len(lines[y])):
            cell = lines[y][x]
            if cell == "S" or cell == "|":
                next_cell = lines[y + 1][x]

                if next_cell == ".":
                    lines[y + 1][x] = "|"
                elif next_cell == "^":
                    total += 1
                    # left
                    if x > 0 and lines[y + 1][x - 1] == ".":
                        lines[y + 1][x - 1] = "|"
                    # right
                    if x < len(lines[y]) - 1 and lines[y + 1][x + 1] == ".":
                        lines[y + 1][x + 1] = "|"
    if display_grid:
        for line in lines:
            print("".join(line))
    print("Part 1:", total)


@cache
def compute_from_position(y: int, x: int):
    if y == len(input_data) - 1:
        return 1

    if input_data[y][x] == "^":
        return compute_from_position(y, x + 1) + compute_from_position(y, x - 1)
    else:
        return compute_from_position(y + 1, x)


def part2():
    start_position_x = input_data[0].index("S")
    nb_paths = compute_from_position(0, start_position_x)
    print("Part 2:", nb_paths)


part1()
part2()
