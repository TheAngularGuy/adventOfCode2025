import re

with open("input.txt", "r") as file:
    content = file.read()

input_data: list[str] = list(filter(lambda el: len(el), content.split('\n')))

total = 0
for line in input_data:
    if 'x' not in line:
        continue
    numbers = list(map(int, re.findall(r'\d+', line)))
    w, h = numbers[:2]
    count = sum(numbers[2:])
    total += count * 9 <= w * h
print(total)