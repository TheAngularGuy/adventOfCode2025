from functools import cache

with open("input.txt", "r") as file:
    content = file.read()

input_data: list[str] = list(filter(lambda el: len(el), content.split('\n')))
points: list[[int, int]] = list(map(lambda el: list(map(int, el.split(","))), input_data))


def part1():
    biggest_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ax, ay = points[i]
            bx, by = points[j]

            dx, dy = abs(ax - bx) + 1, abs(ay - by) + 1
            area = dx * dy
            biggest_area = max(biggest_area, area)

    print("Part 1:", biggest_area)


@cache
def is_point_inside(x: int, y: int) -> bool:
    inside = False

    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]

        # Check if point lies exactly on a vertical or horizontal segment
        if x1 == x2 and x == x1 and min(y1, y2) <= y <= max(y1, y2):
            return True
        if y1 == y2 and y == y1 and min(x1, x2) <= x <= max(x1, x2):
            return True

        # Ray casting alg https://youtu.be/RSXM9bgqxJM?si=rngAl96VH6sGi7G9
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside


@cache
def is_rect_inside(ax: int, ay: int, bx: int, by: int) -> bool:
    is_corners_inside = (is_point_inside(ax, ay) and
                         is_point_inside(bx, by) and
                         is_point_inside(ax, by) and
                         is_point_inside(bx, ay))
    if not is_corners_inside:
        return False

    x1, x2 = (min(ax, bx), max(ax, bx))
    y1, y2 = (min(ay, by), max(ay, by))
    for x in range(x1, x2 + 1):
        if not is_point_inside(x, y1) or not is_point_inside(x, y2):
            return False
    for y in range(y1, y2 + 1):
        if not is_point_inside(x1, y) or not is_point_inside(x2, y):
            return False
    return True


def part2():
    biggest_area = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            ax, ay = points[i]
            bx, by = points[j]

            dx, dy = abs(ax - bx) + 1, abs(ay - by) + 1
            area = dx * dy

            if area > biggest_area:
                is_valid = is_rect_inside(ax, ay, bx, by)
                if is_valid:
                    biggest_area = area
    print("Part 2:", biggest_area)


part1()
part2()  # very slow, takes 3 or 5 min on my mac
