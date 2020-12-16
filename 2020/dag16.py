import re
f = re.split("\w+ tickets?", open("data16").read())

# Part 1
ranges = []
for x in f[0].split("\n"):
    a = re.findall("\d+-\d+", x)
    if len(a) > 0:
        for i in a:
            x = i.split("-")
            ranges.append(range(int(x[0]), int(x[1])+1))
w = set()
c = 0
l = f[2].split("\n")[1:]
for x in range(len(l)):
    for a in l[x].split(","):
        a = int(a)
        good = False
        for b in ranges:
            if a in b:
                good = True
                break
        if not good:
            w.add(x)
            c += a
# print(c)


# Part 2
ranges = {}
for x in f[0].split("\n"):
    a = re.findall("\d+-\d+", x)
    if len(a) > 0:
        b = []
        for i in a:
            q = i.split("-")
            b += range(int(q[0]), int(q[1])+1)
        ranges[x.split(":")[0]] = b

s = {}
l = f[2].split("\n")[1:]
for i in range(len(ranges)):
    for k, v in ranges.items():
        good = True
        for j in range(len(l)):
            if j not in w and int(l[j].split(",")[i]) not in v:
                good = False
        if good:
            if k in s:
                s[k].append(i)
            else:
                s[k] = [i]

# Part 2
result = {}
h = 1
while h:
    h = None
    for k in s.keys():
        v = s[k]
        if len(v) == 1:
            h = v[0]
            result[k] = v[0]
            break
    if h is not None:
        for k in s.keys():
            v = s[k]
            if h in v:
                v.remove(h)

print(result)

l = f[1].split(",")
res = 1
for k, v in result.items():
    if "departure" in k:
        res *= int(l[v])
print(res)

