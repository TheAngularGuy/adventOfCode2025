with open("input.txt", "r") as file:
    content = file.read()

input_data: list[str] = list(filter(lambda el: len(el), content.split('\n')))
input_data = [list(map(int, el.split(","))) for el in input_data]
points = list(map(lambda coord: {"coord": coord, "distances": [], "index": -1, "connections": []}, input_data))


def get_cluster_from_point(index: int, visited: list[int] = []) -> list[int]:
    cluster = [index]
    point = points[index]
    if not len(point["connections"]):
        return cluster
    if index in visited:
        return []
    visited.append(index)
    for next_point in point["connections"]:
        cluster += get_cluster_from_point(next_point, visited)
    return cluster


def part2():
    # calculate distances between each node
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            if i == j:
                continue
            p1 = points[i]["coord"]
            p2 = points[j]["coord"]
            d = abs(p2[0] - p1[0]) ** 2 + abs(p2[1] - p1[1]) ** 2 + abs(p2[2] - p1[2]) ** 2
            points[i]["distances"].append({"dist": d, "index": j})

        points[i]["distances"] = sorted(points[i]["distances"], key=lambda d: d["dist"])
        points[i]["index"] = i

    # connect the X smallest distances
    i = 0
    connected_points = dict()
    while True:
        sorted_points = sorted(points, key=lambda p: p["distances"][0]["dist"] if len(p["distances"]) else float("inf"))

        point = sorted_points[0]
        point_index = point["index"]

        if not len(point["distances"]):
            i += 1
            continue

        other_point_index = point["distances"].pop(0)["index"]
        other_point = points[other_point_index]

        i_min = min(point_index, other_point_index)
        i_max = max(point_index, other_point_index)

        if (i_min, i_max) in connected_points:
            continue

        point["connections"].append(other_point_index)
        other_point["connections"].append(point_index)

        if i >= len(points):
            cluster = get_cluster_from_point(point_index, [])
            if len(cluster) == len(points):
                print(point["coord"], other_point["coord"], i)
                print("Part 2:", point["coord"][0] * other_point["coord"][0])
                break

        connected_points[(i_min, i_max)] = True
        i += 1


part2()
