fil = "data3"
l = [list(map(int, i)) for i in list(zip(*open(fil)))[:-1]]

# Part 1
c = len(l[0])/2
low = ""
high = ""

for i in l:
    if sum(i) > c:
        low += "0"
        high += "1"
    else:
        low += "1"
        high += "0"

print(int(low, 2) * int(high, 2))

# Part 2

things = set(range(len(l[0])))

print(l)

for i in range(len(l)):
    if sum(l[i][j] for j in things) < c:
        for j in range(len(l[i])):
            if l[i][j] == 1:
                things.remove(j)
    else:
        pass
