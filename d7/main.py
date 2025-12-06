with open("input.txt", "r") as file:
    content = file.read()

input_data: list[str] = list(filter(lambda el: len(el), content.split('\n')))


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
    for line in lines:
        print("".join(line))
    print("Part 1:", total)


compute_next_line_cache = dict()
def compute_next_line(y: int, x: int):
    if (x, y) in compute_next_line_cache:
        return compute_next_line_cache[(x, y)]

    if y == len(input_data) - 1:
        compute_next_line_cache[(x, y)] = 1
        return 1

    cell = input_data[y][x]
    if cell == "^":
        total = compute_next_line(y, x - 1) + compute_next_line(y, x + 1)
        compute_next_line_cache[(x, y)] = total
        return total
    else:
        total = compute_next_line(y + 1, x)
        compute_next_line_cache[(x, y)] = total
        return total


def part2():
    start_position_x = input_data[0].index("S")
    nb_paths = compute_next_line(0, start_position_x)
    print("Part 2:", nb_paths)


part1()
part2()
