from itertools import combinations

with open("sample.txt", "r") as file:
    content = file.read()

input_data: list[str] = list(filter(lambda el: len(el), content.split('\n')))
lamps = []
buttons = []
joltages = []

for line in input_data:
    elements = line.split(" ")
    row_buttons = []
    for el in elements:
        if el[0] == "[":
            lamps.append(el[1:-1])
        elif el[0] == "(":
            row_buttons.append(el[1:-1])
        elif el[0] == "{":
            joltages.append(list(map(int, el[1:-1].split(","))))
    buttons.append(row_buttons)


def compute_presses(lamps_len, presses):
    lamp = []
    for i in range(lamps_len):
        lamp.append('.')
    for press in presses:
        indexes = list(map(int, press.split(",")))
        for i in indexes:
            if lamp[i] == '.':
                lamp[i] = '#'
            elif lamp[i] == '#':
                lamp[i] = '.'
    return "".join(lamp)


def solve_line(lamp, button_list):
    len_lamp = len(lamp)
    combination_list = []
    for i in range(len(button_list) + 1):
        combination_list += combinations(button_list, i)
    for combo in combination_list:
        presses = list(combo)
        if compute_presses(len_lamp, presses) == lamp:
            return presses
    return None


def part1():
    total = 0
    for i in range(len(input_data)):
        presses = solve_line(lamps[i], buttons[i])
        if presses is not None:
            total += len(presses)
    print("Part 2:", total)


def part2():
    # I'm still working on that equation :/
    print("Part 2:", 0)


part1()
part2()
