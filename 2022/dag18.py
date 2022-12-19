file = open("data18")

inp = list(map(lambda x: list(map(int, x.split(","))), file.read().split("\n")))


def get_touch_count(shape, prev_shapes):
    touches = 0
    x, y, z = shape
    for a, b, c in prev_shapes:
        ax = abs(a - x)
        by = abs(b - y)
        cz = abs(c - z)
        if ax + by + cz == 1:
            touches += 1
    return touches


def part1(shapes):
    count = 0
    prev_shapes = set()
    for shape in shapes:
        count += 6 - 2 * get_touch_count(shape, prev_shapes)
        prev_shapes.add(tuple(shape))
    return count


print(part1(inp.copy()))


def part2(shapes):
    # Part 1
    count = 0
    prev_shapes = set()
    for shape in shapes:
        count += 6 - 2 * get_touch_count(shape, prev_shapes)
        prev_shapes.add(tuple(shape))

    # Get lava range
    min_x = min(prev_shapes, key=lambda l: l[0])[0]
    max_x = max(prev_shapes, key=lambda l: l[0])[0]
    min_y = min(prev_shapes, key=lambda l: l[1])[1]
    max_y = max(prev_shapes, key=lambda l: l[1])[1]
    min_z = min(prev_shapes, key=lambda l: l[2])[2]
    max_z = max(prev_shapes, key=lambda l: l[2])[2]

    # Start counting bubbles. Only works for 1x1x1 bubbles
    bubbles = set()
    old_bubbles = {0}
    while old_bubbles != bubbles:
        old_bubbles = bubbles.copy()
        used_space = prev_shapes | bubbles
        for x in range(min_x, max_x):
            for y in range(min_y, max_y):
                for z in range(min_z, max_z):
                    xyz = (x, y, z)
                    if xyz not in used_space and get_touch_count(xyz, used_space) == 6:
                        bubbles.add(xyz)
    print(count - part1(bubbles))


part2(inp.copy())
# 4338 too high
