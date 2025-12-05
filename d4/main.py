with open("input.txt", "r") as file:
    content = file.read()

lines: list[str] = list(filter(lambda el: len(el), content.split('\n')))


def compute(grid: list[str]):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != '@':
                continue

            sum = 0
            if i > 0 and grid[i - 1][j] != '.':
                sum += 1
            if i < len(grid[j]) - 1 and grid[i + 1][j] != '.':
                sum += 1
            if j > 0 and grid[i][j - 1] != '.':
                sum += 1
            if j < len(grid) - 1 and grid[i][j + 1] != '.':
                sum += 1
            if i > 0 and j > 0 and grid[i - 1][j - 1] != '.':
                sum += 1
            if i < len(grid[i]) - 1 and j > 0 and grid[i + 1][j - 1] != '.':
                sum += 1
            if i > 0 and j < len(grid) - 1 and grid[i - 1][j + 1] != '.':
                sum += 1
            if i < len(grid[i]) - 1 and j < len(grid) - 1 and grid[i + 1][j + 1] != '.':
                sum += 1

            if (sum < 4):
                grid[i][j] = "x"

    return grid


def part1():
    grid = list(map(list, lines))
    new_grid = compute(grid)
    sum = 0
    for i in range(len(new_grid)):
        for j in range(len(new_grid[i])):
            if new_grid[i][j] == "x":
                sum += 1
    print("Part 1:", sum)


def part2():
    grid = list(map(list, lines))
    total = 0
    while True:
        compute(grid)
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "x":
                    sum += 1
                    grid[i][j] = "."
        total += sum
        # print(sum)
        if sum == 0:
            break
    print("Part 2:", total)


part1()
part2()
