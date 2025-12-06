with open("input.txt", "r") as file:
    content = file.read()

# NOTE: add a dot at the last char of the input
input: list[str] = list(filter(lambda el: len(el), content.split('\n')))


def part1():
    lines = list(map(lambda line: line.split(), input))
    operations = lines.pop(-1)

    sum = 0
    for i in range(len(lines[0])):
        result = int(lines[0][i])
        for line in lines[1:]:
            if operations[i].count('+'):
                result = result + int(line[i])
            elif operations[i].count('*'):
                result = result * int(line[i])
        sum += result
    print("Part 1: ", sum)


def compute_array_of_numbers(operation: str, numbers: list[int]) -> int:
    result = numbers[0]
    for number in numbers[1:]:
        if operation == '*':
            result = result * number
        elif operation == '+':
            result = result + number
    return result


def part2():
    lines = list(map(lambda line: line, input))

    sum = 0
    array_of_numbers = []
    for x in range(len(lines[0]) - 1, -1, -1):
        nb_str = ""
        for y in range(len(lines)):
            char = lines[y][x]
            if char.isdigit():
                nb_str += char
            else:
                if len(nb_str):
                    array_of_numbers.append(int(nb_str))
                    nb_str = ""
                if "*+".count(char):
                    sum += compute_array_of_numbers(char, array_of_numbers)
                    array_of_numbers = []
    print("Part 2: ", sum)


part1()
part2()
