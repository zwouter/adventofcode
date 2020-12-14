
import itertools
fil = "data14"
f = open(fil).read().replace("mem[", "").replace("]", "").split("\n")
# Part 1
mem = {}
mask = ""
for k in f:
    if k[:4] == "mask":
        mask = k[7:]
        continue
    nrs = k.split(" = ")
    n = bin(int(nrs[1]))[2:]
    n = ''.join(['0' for i in range(36-len(n))]) + n
    r = ['0' for i in range(36)]
    for i in range(36):
        if mask[i] == "X":
            r[i] = n[i]
        else:
            r[i] = mask[i]
    mem[int(nrs[0])] = int(''.join(r), 2)
print(sum(mem.values()))

# Part 2, enorm gebeund maar blijkbaar niet langzaam
mem = {}
mask = ""
for k in f:
    if k[:4] == "mask":
        mask = k[7:]
        continue
    nrs = k.split(" = ")
    n = bin(int(nrs[0]))[2:]
    n = ''.join(['0' for i in range(36-len(n))]) + n
    r = ['0' for i in range(len(n))]
    for i in range(len(n)):
        if mask[i] == "0":
            r[i] = n[i]
            continue
        if mask[i] == "1":
            r[i] = '1'
        if mask[i] == "X":
            r[i] = "X"
        else:
            r[i] = mask[i]
    a = r.count("X")
    hm = [''.join(['0' for i in range(a - len(h))]) + h for h in [bin(int(i))[2:] for i in range(2 ** a)]]
    for x in hm:
        i = 0
        q = r.copy()
        for j in range(36):
            if r[j] == "X":
                q[j] = x[i]
                i += 1
        mem[int(''.join(q), 2)] = int(nrs[1])
print(sum(mem.values()))
