from itertools import combinations
# from sympy import Symbol, nsolve

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
    print("Part 1:", total)


def part2():
    # I'm still working on that equation :/
    # b4 + b5 = 3
    # b1 + b5 = 5
    # b2 + b3 + b4 = 4
    # b0 + b1 + b3 = 7
    for joltage_list, btn_list in zip(joltages, buttons):
        for i, joltage in enumerate(joltage_list):
            sums = []
            for j, button in enumerate(btn_list):
                if button.count(str(i)):
                    sums.append(f"b{j}")

            print("equation:", "+".join(sums), "=", joltage)
        print('--')
    print("Part 2:", 0)


part1()
part2()
