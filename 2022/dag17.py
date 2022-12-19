file = open("data17")

inp = file.read()

shapes = [[(0, 0), (1, 0), (2, 0), (3, 0)],                 # ----
          [(1, 0), (1, 1), (0, 1), (1, 2), (2, 1)],     # +
          [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],       # _|
          [(0, 0), (0, 1), (0, 2), (0, 3)],               # |
          [(0, 0), (1, 0), (0, 1), (1, 1)]]               # ☐


def print_blocks(fallen_blocks):
    y_start = max(fallen_blocks, key=lambda l: l[1])[1] + 4
    res = []
    for y in reversed(range(y_start)):
        cur = []
        for x in range(7):
            if (x, y) in fallen_blocks:
                cur.append('#')
            else:
                cur.append('.')
        res.append(' '.join(cur))
    res.append(' '.join(map(str, range(7))))
    print('\n'.join(res))


def process_order(order):
    res = []
    for r in order:
        if r == '>':
            res.append((1, 0))
        elif r == '<':
            res.append((-1, 0))
        res.append((0, -1))
    return res


def part1(order):
    order = process_order(order)
    block_floor = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)}
    fallen_blocks = block_floor.copy()
    shape_counter = 0
    move_counter = 0
    move_len = len(order)
    shape = None
    x_start = 2
    while shape_counter < 2022:
        if not shape:
            shape = shapes[shape_counter % 5].copy()
            shape_counter += 1
        old_shape = shape.copy()
        y_start = max(fallen_blocks, key=lambda l: l[1])[1] + 4
        for i in range(len(shape)):
            x, y = shape[i]
            x += x_start
            y += y_start
            shape[i] = (x, y)
        while not set(shape) & fallen_blocks:
            move = order[move_counter]
            move_counter = (move_counter + 1) % move_len
            old_shape = shape.copy()
            new_shape = shape.copy()
            for i in range(len(new_shape)):
                x, y = new_shape[i]
                x += move[0]
                if x < 0 or x > 6 or (x, y) in fallen_blocks:
                    break
                y += move[1]
                new_shape[i] = (x, y)
            else:
                shape = new_shape
        else:
            for stone in old_shape:
                fallen_blocks.add(stone)
            shape = None
    print(max(fallen_blocks, key=lambda l: l[1])[1])
    return fallen_blocks


print("Part 1:")
part1(inp)
# print_blocks(part1(inp))


def part2(order):
    order = process_order(order)
    block_floor = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)}
    fallen_blocks = block_floor.copy()
    shape_counter = 0
    move_counter = 0
    move_len = len(order)
    shape = None
    x_start = 2
    while shape_counter < 874:
        y_test = max(fallen_blocks, key=lambda l: l[1])[1]
        if {(0, y_test), (1, y_test), (2, y_test), (3, y_test), (4, y_test), (5, y_test), (6, y_test)}\
                .issubset(fallen_blocks):
            print("y ", y_test, "move ", move_counter, "shape ", shape_counter)
        if not shape:
            shape = shapes[shape_counter % 5].copy()
            shape_counter += 1
        old_shape = shape.copy()
        y_start = max(fallen_blocks, key=lambda l: l[1])[1] + 4
        for i in range(len(shape)):
            x, y = shape[i]
            x += x_start
            y += y_start
            shape[i] = (x, y)
        while not set(shape) & fallen_blocks:
            move = order[move_counter]
            move_counter = (move_counter + 1) % move_len
            old_shape = shape.copy()
            new_shape = shape.copy()
            for i in range(len(new_shape)):
                x, y = new_shape[i]
                x += move[0]
                if x < 0 or x > 6 or (x, y) in fallen_blocks:
                    break
                y += move[1]
                new_shape[i] = (x, y)
            else:
                shape = new_shape
        else:
            for stone in old_shape:
                fallen_blocks.add(stone)
            shape = None
    print(max(fallen_blocks, key=lambda l: l[1])[1])
    print("move ", move_counter, "shape ", shape_counter)
    return fallen_blocks


print("Part 2:")
part2(inp)
# ((((1000000000000 - 566) // 1720) * 2626) + 868) + 1326 (y after 874 = ((1000000000000 - 566) // 1720) * 1720 rounds)
