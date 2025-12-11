from collections import deque

with open("input.txt", "r") as file:
    content = file.read()

input_data: list[str] = list(filter(lambda el: len(el), content.split('\n')))


def part1():
    dictionary = dict()

    for row in input_data:
        name, rest = row.split(':')
        list_connections = rest.strip().split(' ')
        dictionary[name.strip()] = list_connections

    q = deque()
    q.append(('you', []))

    paths = []
    while len(q) > 0:
        current_name, history = q.popleft()
        if current_name == 'out':
            paths.append(history + [current_name])
            continue

        current_connections = dictionary[current_name]
        for connection in current_connections:
            if connection not in history:
                q.append((connection, history + [current_name]))

    print("Part 1:", len(paths))
part1()
