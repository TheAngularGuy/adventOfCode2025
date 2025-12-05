with open("input.txt", "r") as file:
    content = file.read()

ranges, ids = content.split("\n\n")
ranges = list(map(lambda range: range.split("-"), ranges.split("\n")))
ranges = sorted(ranges, key=lambda range: int(range[0]))


def merge_ranges():
    list_ranges: list[list[int]] = []
    i = 0
    for range in ranges:
        is_last = i == len(ranges) - 1
        if is_last:
            list_ranges.append(range)
            break

        current_min, current_max = range
        next_min, next_max = ranges[i + 1]

        if int(current_max) >= int(next_min):
            ranges[i + 1][0] = current_min
            ranges[i + 1][1] = max(current_max, next_max)
        else:
            list_ranges.append(range)

        i += 1

    return list_ranges


list_merged_ranges = merge_ranges()

sum = 0
for id in ids.split("\n"):
    for range in list_merged_ranges:
        current_min, current_max = range
        if int(current_min) <= int(id) <= int(current_max):
            sum += 1
            break
print("Part 1:", sum)

sum = 0
for range in list_merged_ranges:
    current_min, current_max = range
    sum += (int(current_max) - (int(current_min) - 1))
print("Part 2:", sum)
