
f = [1, 0, 18, 10, 19, 6]
d = {}
last = 0
l = []
for i in range(30000000):
    if i < len(f):
        last = f[i]
    else:
        if len(d[last]) < 2:
            last = 0
        else:
            last = d[last][-1] - d[last][-2]
    if last in d:
        d[last].append(i)
    else:
        d[last] = [i]
print(last)

