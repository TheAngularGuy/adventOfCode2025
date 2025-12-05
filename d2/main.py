with open("input.txt", "r") as file:
    content = file.read()

input: str = list(filter(lambda el: len(el), content.split('\n')))[0]
lines: list[str] = input.split(',')


def get_subs(input: str, divider: int) -> list[str]:
    input_len: int = len(input)
    subs: list[str] = []

    if input_len % divider != 0:
        return []

    delta = input_len // divider
    i = 0
    j = delta

    while j <= input_len:
        subs.append(input[i:j])
        i += delta
        j += delta

    return subs


def part1():
    found_ids: list[int] = []
    for id_range in lines:
        start, stop = id_range.split('-')

        for id in range(int(start), int(stop) + 1):
            id_str = str(id)
            elements = get_subs(id_str, 2)

            if len(elements) == 0:
                continue

            first = elements[0]
            all_same = True

            for element in elements:
                if element != first:
                    all_same = False

            if all_same:
                found_ids.append(id)

    print("Part1: ", sum(found_ids))


def part2():
    found_ids: list[int] = []
    for id_range in lines:
        start, stop = id_range.split('-')

        for id in range(int(start), int(stop) + 1):
            id_str = str(id)

            for divider in range(2, len(id_str) + 1):
                elements = get_subs(id_str, divider)

                if len(elements) == 0:
                    continue

                first = elements[0]
                all_same = True

                for element in elements:
                    if element != first:
                        all_same = False

                if all_same:
                    found_ids.append(id)
                    break

    print("Part2: ", sum(found_ids))


part1()
part2()
