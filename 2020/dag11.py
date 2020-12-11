fil = "data11"
lis = list(map(lambda string:[char for char in string],open(fil).read().split("\n")))
# Part 1
f = [x.copy() for x in lis]
size_x = len(f)
size_y = len(f[0])
changed = True
while changed:
    changed = False
    cop = [x.copy() for x in f]
    for i in range(size_x):
        for j in range(size_y):
            adj = []
            for x, y in [(1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1)]:
                if 0 <= i+x < size_x and 0 <= j+y < size_y:
                    adj.append(f[i + x][j + y])
            if f[i][j] == 'L' and adj.count("#") < 1:
                changed = True
                cop[i][j] = '#'
            elif f[i][j] == '#' and adj.count("#") > 3:
                changed = True
                cop[i][j] = 'L'
    f = cop.copy()
print(sum(sum(s=='#' for s in l) for l in f))


# Part 2
f = [x.copy() for x in lis]
size_x = len(f)
size_y = len(f[0])
changed = True
while changed:
    changed = False
    cop = [x.copy() for x in f]
    for i in range(size_x):
        for j in range(size_y):
            adj = []
            for x, y in [(1, 0), (1, -1), (1, 1), (-1, 0), (-1, -1), (-1, 1), (0, 1), (0, -1)]:
                x2 = x
                y2 = y
                while 0 <= i+x < size_x and 0 <= j+y < size_y and f[i+x][j+y] == ".":
                    x += x2
                    y += y2
                if 0 <= i+x < size_x and 0 <= j+y < size_y:
                    adj.append(f[i + x][j + y])
            if f[i][j] == 'L' and adj.count("#") < 1:
                changed = True
                cop[i][j] = '#'
            elif f[i][j] == '#' and adj.count("#") > 4:
                changed = True
                cop[i][j] = 'L'
    f = cop.copy()
print(sum(sum(s=='#' for s in l) for l in f))
