with open("input.txt", "r") as file:
    content = file.read()

lines = list(filter(lambda el: len(el), content.split('\n')))

cursor = 50
nb_zero_part1 = 0
nb_zero_part2 = 0

for instruction in lines:
    direction = instruction[0]
    amount = int(instruction[1:])
    delta = 1 if direction == 'R' else -1

    nb_zero_part2 += amount // 100
    left_amount = amount % 100
    new_cursor = cursor + left_amount * delta

    if ((cursor > 0 and new_cursor <= 0) or (cursor < 100 and new_cursor >= 100)):
        nb_zero_part2 += 1

    cursor = new_cursor % 100

    if cursor == 0:
        nb_zero_part1 += 1

print("Part 1: ", nb_zero_part1)
print("Part 2: ", nb_zero_part2)
