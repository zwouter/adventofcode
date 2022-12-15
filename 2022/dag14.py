import time
file = open("data14")

start_time = time.time()

lines = file.read().split("\n")

# ----------------------------------------- Part 1
points = set()
for line in lines.copy():
    pointsets = list(map(lambda x: tuple(map(int, x.split(","))), line.split(" -> ")))
    for i in range(len(pointsets))[:-1]:
        point1 = pointsets[i]
        point2 = pointsets[i+1]
        x_point1 = point1[0]
        y_point1 = point1[1]
        for x in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
            points.add((x, y_point1))
        for y in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
            points.add((x_point1, y))

min_point = max(points, key=lambda x: x[1])[1]

sandset = points.copy()
while True:
    sand = (500, 0)
    while True:
        sand_down = (sand[0], sand[1] + 1)
        sand_left = (sand[0] - 1, sand[1] + 1)
        sand_right = (sand[0] + 1, sand[1] + 1)
        if sand_down in sandset:
            if sand_left not in sandset:
                sand = sand_left
                continue
            elif sand_right not in sandset:
                sand = sand_right
                continue
            else:
                sandset.add(sand)
            break
        sand = sand_down
        if sand[1] >= min_point:
            break
    if sand[1] >= min_point:
        break

print(len(sandset) - len(points))


# ----------------------------------------- Part 2
floor = max(points, key=lambda x: x[1])[1] + 2

for inf in range(-999999, 999999):
    points.add((inf, floor))
sandset = points.copy()

while True:
    sand = (500, 0)
    while True:
        sand_down = (sand[0], sand[1] + 1)
        sand_left = (sand[0] - 1, sand[1] + 1)
        sand_right = (sand[0] + 1, sand[1] + 1)
        if sand_down in sandset:
            if sand_left not in sandset:
                sand = sand_left
                continue
            elif sand_right not in sandset:
                sand = sand_right
                continue
            else:
                sandset.add(sand)
                break
        sand = sand_down
    if (501, 1) in sandset:
        sandset.add((500, 1))
        break

print(len(sandset) - len(points))
print(time.time() - start_time)
