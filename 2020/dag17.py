# Open data
f = open("data17").read().split("\n")
# Make 3D list out of input
lists = [[[x for x in y] for y in f]]
# List to help find all neighbours
neighs = [-1, 0, 1]
neighs = [(z1, x1, y1) for z1 in neighs for x1 in neighs for y1 in neighs]

for i in range(6):
    # Add all extra items in the lists, initiate them to inactive
    # Add extra items in z
    zeroes_z = [[['.' for x in y] for y in z] for z in lists]
    lists = zeroes_z + lists + zeroes_z
    # Add extra items in x
    for z in range(len(lists)):
        zeroes_x = [['.' for x in range(len(lists[z]))]]
        lists[z] = zeroes_x + lists[z] + zeroes_x
    # Add extra items in y
    for z in range(len(lists)):
        for x in range(len(lists[0])):
            lists[z][x] = ['.'] + lists[z][x] + ['.']
    # Update all values to their new values
    copy = [[l.copy() for l in lis] for lis in lists]
    for z in range(len(copy)):
        for x in range(len(copy[0])):
            for y in range(len(copy[0][0])):
                neighbours = []
                for z1, x1, y1 in neighs:
                    if not z1 == x1 == y1 == 0 and z + z1 in range(len(copy)) and x + x1 in range(len(copy[0])) and y + y1 in range(len(copy[0][0])):
                        neighbours.append(copy[z + z1][x + x1][y + y1])
                if copy[z][x][y] == '#' and not 1 < neighbours.count('#') < 4:
                    lists[z][x][y] = '.'
                elif copy[z][x][y] == '.' and neighbours.count('#') == 3:
                    lists[z][x][y] = '#'
# for z in lists:
#     for x in z:
#         print(x)
#     print("---------")

print(sum(sum(x.count('#') for x in z) for z in lists))

