# Open data
f = open("data17").read().split("\n")

# -------------------------Part 1
# Make 3D list out of input
lists = [[[x for x in y] for y in f]]
# List to help find all neighbours
neighs = [-1, 0, 1]
neighs = [(z1, x1, y1) for z1 in neighs for x1 in neighs for y1 in neighs]
for i in range(6):
    # Add all extra items in the lists, initiate them to inactive
    # Add extra items in z
    zeroes_z = [[['.' for y in lists[0][0]] for x in lists[0]]]
    lists = zeroes_z + lists + zeroes_z
    # Add extra items in x
    zeroes_x = [['.' for x in range(len(lists[0]))]]
    for z in range(len(lists)):
        lists[z] = zeroes_x + lists[z] + zeroes_x
    # Add extra items in y
    for z in range(len(lists)):
        for x in range(len(lists[z])):
            lists[z][x] = ['.'] + lists[z][x] + ['.']
    # Update all values to their new values
    copy = [[l.copy() for l in lis] for lis in lists]
    for z in range(len(copy)):
        for x in range(len(copy[z])):
            for y in range(len(copy[z][x])):
                neighbours = []
                for z1, x1, y1 in neighs:
                    if not z1 == x1 == y1 == 0 and z + z1 in range(len(copy)) and x + x1 in range(len(copy[0])) and y + y1 in range(len(copy[0][0])):
                        neighbours.append(copy[z + z1][x + x1][y + y1])
                if copy[z][x][y] == '#' and not 1 < neighbours.count('#') < 4:
                    lists[z][x][y] = '.'
                elif copy[z][x][y] == '.' and neighbours.count('#') == 3:
                    lists[z][x][y] = '#'
print(sum(sum(x.count('#') for x in z) for z in lists))


# -------------------------Part 2
# Make 3D list out of input
lists = [[[[x for x in y] for y in f]]]
# List to help find all neighbours
neighs = [-1, 0, 1]
neighs = [(w1, z1, x1, y1) for w1 in neighs for z1 in neighs for x1 in neighs for y1 in neighs]
for i in range(6):
    # Add all extra items in the lists, initiate them to inactive
    # Add extra items in w
    zeroes_w = [[[['.' for y in lists[0][0][0]]] for z in lists[0]]]
    lists = zeroes_w + lists + zeroes_w
    # Add extra items for z
    for w in range(len(lists)):
        zeroes_z = [[['.' for y in lists[w][0][0]] for x in lists[w][0]]]
        lists[w] = zeroes_z + lists[w] + zeroes_z
    # Add extra items in x
    for w in range(len(lists)):
        for z in range(len(lists[0])):
            zeroes_x = [['.' for x in range(len(lists[w][z]))]]
            lists[w][z] = zeroes_x + lists[w][z] + zeroes_x
    # Add extra items in y
    for w in range(len(lists)):
        for z in range(len(lists[0])):
            for x in range(len(lists[0][0])):
                lists[w][z][x] = ['.'] + lists[w][z][x] + ['.']
    # Update all values to their new values
    # copy = [[l.copy() for l in lis] for lis in lists]
    copy = [[[x.copy() for x in z] for z in w] for w in lists]
    for w in range(len(copy)):
        for z in range(len(copy[0])):
            for x in range(len(copy[0][0])):
                for y in range(len(copy[0][0][0])):
                    neighbours = []
                    for w1, z1, x1, y1 in neighs:
                        if not w1 == z1 == x1 == y1 == 0 and w + w1 in range(len(copy)) and z + z1 in range(len(copy[0])) \
                                and x + x1 in range(len(copy[0][0])) and y + y1 in range(len(copy[0][0][0])):
                            neighbours.append(copy[w + w1][z + z1][x + x1][y + y1])
                    if copy[w][z][x][y] == '#' and not 1 < neighbours.count('#') < 4:
                        lists[w][z][x][y] = '.'
                    elif copy[w][z][x][y] == '.' and neighbours.count('#') == 3:
                        lists[w][z][x][y] = '#'
print(sum(sum(sum(x.count('#') for x in z) for z in w) for w in lists))

print(len(lists) * len(lists[0]))

# for w in range(len(lists)):
#     print(w, len(lists[0]))

# for w in lists:
#     for z in w:
#         for x in z:
#             print(x)
#         print("------")
