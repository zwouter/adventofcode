fil = "data12"
f = open(fil).readlines()

# Part 1
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x = 0
y = 0
dir = 1
for i in f:
    c = i[0]
    n = int(i[1:])
    if c == "N":
        y += n
    elif c == "E":
        x += n
    elif c == "S":
        y -= n
    elif c == "W":
        x -= n
    elif c == "L":
        dir = (dir - n // 90) % 4
    elif c == "R":
        dir = (dir + n // 90) % 4
    elif c == "F":
        x += dirs[dir][0] * n
        y += dirs[dir][1] * n
print(x, "+", y, "=", abs(x) + abs(y))

# Part 2
x = 0
y = 0
way_x = 10
way_y = 1
for i in f:
    c = i[0]
    n = int(i[1:])
    if c == "N":
        way_y += n
    elif c == "E":
        way_x += n
    elif c == "S":
        way_y -= n
    elif c == "W":
        way_x -= n
    elif c == "L":
        for j in range(n // 90):
            way_x, way_y = -way_y, way_x
    elif c == "R":
        for j in range(n // 90):
            way_x, way_y = way_y, -way_x
    elif c == "F":
        x += way_x * n
        y += way_y * n
print(x, "+", y, "=", abs(x) + abs(y))


