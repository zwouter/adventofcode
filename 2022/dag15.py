import re
import time
import tqdm

file = open("data15")
lines = file.read().split("\n")


def get_manhattan_distance(point1, point2):
    return abs(point2[0] - point1[0]) + abs(point2[1] - point1[1])


# def get_manhattan_locations(sensor, beacon):
#     distance = get_manhattan_distance(sensor, beacon)
#     reached = []
#     # for x in range(sensor[0], sensor[0] + distance):
#     for x in range(distance + 1):
#         # print("")
#         # for y in range(sensor[1], sensor[1] + distance - x):
#         for y in range(x - distance, distance - x + 1):
#             # print(sensor[0] + x, sensor[1] + y)
#             reached.append((sensor[0] + x, sensor[1] + y))
#             print((sensor[0] + x, sensor[1] + y))
#             reached.append((-(sensor[0] + x), sensor[1] + y))
#             print((-(sensor[0] + x), sensor[1] + y))
#             # reached.append()
#     return reached
#
#
# reached = get_manhattan_locations((8, 7), (2, 10))
#
# for i in range(-3, 26):
#     line = []
#     for j in range(-3, 23):
#         if (i, j) == (8, 7):
#             line.append('S')
#         elif (i, j) in reached:
#             line.append('#')
#         else:
#             line.append(".")
#     print(''.join(line))


def part1():
    sensor_distances = {}
    sensors = set()
    beacons = set()
    distances = set()
    for line in lines:
        coors = list(map(int, re.split("Sensor at x=|, y=|: closest beacon is at x=", line)[1:]))
        sensor = (coors[0], coors[1])
        beacon = (coors[2], coors[3])
        distance = get_manhattan_distance(sensor, beacon)
        sensor_distances[sensor] = distance
        distances.add(distance)
        sensors.add(sensor)
        beacons.add(beacon)
    minx = min(sensors, key=lambda a: a[0])[0] - max(distances)
    maxx = max(sensors, key=lambda a: a[0])[0] + max(distances)
    # y = 10
    y = 2000000
    count = 0
    for x in tqdm.tqdm(range(minx - 1, maxx + 1)):
        available = True
        if (x, y) in beacons or (x, y) in sensors:
            continue
        for sensor in sensors:
            if sensor_distances[sensor] >= get_manhattan_distance((x, y), sensor):
                available = False
                break
        if not available:
            count += 1
    return count


print(part1())


def get_on_dist_plus(point, distance):
    res = set()
    cur = (point[0], point[1] + distance)
    # print(cur)
    for _ in range(distance):
        res.add(cur)
        cur = (cur[0] + 1, cur[1] - 1)
    for _ in range(distance):
        res.add(cur)
        cur = (cur[0] - 1, cur[1] - 1)
    for _ in range(distance):
        res.add(cur)
        cur = (cur[0] - 1, cur[1] + 1)
    for _ in range(distance):
        res.add(cur)
        cur = (cur[0] + 1, cur[1] + 1)
    return res


def part2():
    sensor_distances = {}
    sensors = set()
    beacons = set()
    for line in lines:
        coors = list(map(int, re.split("Sensor at x=|, y=|: closest beacon is at x=", line)[1:]))
        sensor = (coors[0], coors[1])
        beacon = (coors[2], coors[3])
        distance = get_manhattan_distance(sensor, beacon)
        sensor_distances[sensor] = distance
        sensors.add(sensor)
        beacons.add(beacon)
    points_to_check = set()
    region = 4000000
    for sensor in tqdm.tqdm(sensors):
        for point in get_on_dist_plus(sensor, sensor_distances[sensor] + 1):
            if point not in beacons and point not in sensors and 0 < point[0] < region and 0 < point[1] < region:
                points_to_check.add(point)
    print("Points to check", len(points_to_check))
    for point in tqdm.tqdm(points_to_check):
        for sensor in sensors:
            if sensor_distances[sensor] >= get_manhattan_distance(point, sensor):
                break
        else:
            return point[0] * 4000000 + point[1]


# for i in range(-15, 15):
#     line = [str(i)[0]]
#     for j in range(-15, 15):
#         if (i, j) == (8, 7):
#             line.append('S')
#         elif (i, j) in get_on_dist_plus((0, 0), 9):
#             line.append('#')
#         else:
#             line.append(".")
#     print(''.join(line))
print(part2())



