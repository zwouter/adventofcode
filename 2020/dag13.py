import math
fil = "data13"

f = open(fil).readlines()
k = f[1].split(",")
# Part 1
n = int(f[0])
d = {}
for x in k:
    if x == "x":
        continue
    p = int(x)
    d[(n//p + 1) * p - n] = p
print(min(d.keys()) * d[min(d.keys())])


# Part 2
# Bruteforce versie
# i = 0
# go = True
# q = int(k[0])
# while go:
#     i += q
#     go = False
#     for j in range(len(k)):
#         if k[j] == "x":
#             continue
#         if ((i+j) % int(k[j])) != 0:
#             go = True
#             break
# print(i)

# Slechte implementatie van chinese remainder theorem
t = [(i, int(j)) for i, j in enumerate(k) if j != "x"]
ms = [math.prod([q for p, q in t if q != j]) for i, j in t]
gg = [j for i, j in t]
assa = [-i for i, j in t]
qs = []
for m in range(len(ms)):
    res = ms[m] % gg[m]
    c = 1
    while res*c % gg[m] != 1:
        c += 1
    qs.append(c)
res = sum(assa[i] * ms[i] * qs[i] for i in range(len(qs)))
print(res % math.prod(gg))


