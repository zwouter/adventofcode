import math

lines = open("data8").read().split("\n")
lines = [list(map(int, l)) for l in lines]

length = len(lines)
lenrange = range(length)

def checkrow(row):
    res = []
    max = -1
    for r in row:
        if int(r) > max:
            res.append(True)
            max = int(r)
        else:
            res.append(False)
    return res


def checkmatrix(matrix):
    res = []
    for row in matrix:
        resrow = []
        check1 = checkrow(row)
        check2 = list(reversed(checkrow(reversed(row))))
        for i in lenrange:
            resrow.append(check1[i] or check2[i])
        res.append(resrow)
    return res


def checkall(matrix):
    res = 0
    check1 = checkmatrix(matrix)
    check2 = checkmatrix([[row[i] for row in matrix] for i in lenrange])
    for i in lenrange:
        for j in lenrange:
            res += check1[i][j] or check2[j][i]
    return res


print(checkall(lines))

# ----------------------------------------------------   Part 2
lines = [list(map(int, l)) for l in lines]
transpose = [list(map(int, [row[i] for row in lines])) for i in lenrange]


def checkunit(i, j):
    height = lines[i][j]
    res = [0, 0, 0, 0]
    x = j + 1
    while 0 <= x < length:
        if lines[i][x] >= height:
            res[0] += 1
            break
        x += 1
        res[0] += 1
    x = j - 1
    while 0 <= x < length:
        if lines[i][x] >= height:
            res[1] += 1
            break
        x -= 1
        res[1] += 1
    y = i + 1
    while 0 <= y < length:
        if lines[y][j] >= height:
            res[2] += 1
            break
        y += 1
        res[2] += 1
    y = i - 1
    while 0 <= y < length:
        if lines[y][j] >= height:
            res[3] += 1
            break
        y -= 1
        res[3] += 1
    return res


def getmaxprod():
    res = 0
    for i in lenrange:
        for j in lenrange:
            res = max(res, math.prod(checkunit(i, j)))
    return res


print(getmaxprod())
