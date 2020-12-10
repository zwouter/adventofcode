fil = "data10"

f = set(map(int, open(fil).readlines()))

# Part 1
i = 0
diff = {1: 0, 2: 0, 3: 1}
while i < max(f):
    for x in range(1, 4):
        if i + x in f:
            diff[x] += 1
            i += x
            break
# print(diff[1] * diff[3])


# Part 2
# Compleet vergeten hoe dynamic programming werkt dus maar een super inefficiente oplossing.
# Gestart op 12:57
# def countit(start, s):
#     res = 1
#     for i in range(start, len(s)):
#         one = False
#         for x in range(1, 4):
#             if s[i] + x in s:
#                 if one:
#                     res += countit(i + x, s)
#                 else:
#                     one = True
#     return res
#
# print(countit(0, [0]+list(f)))


# Dynamic programming way
f = [0] + list(f)
m = [1 for i in range(len(f))]
for i in range(len(f)-2, -1, -1):
    l = f[i:i+4]
    s = [j for j in l if f[i] < j < f[i]+4]
    t = [m[f.index(j)] for j in s]
    m[i] = sum(t)
# print(m[0])


# Oneliner
print([[sum(m[f.index(j)]for j in[j for j in f[i:i+4]if f[i]<j<f[i]+4])for i in range(len(f)-2,-1,-1)][-1]for f in[sorted(map(int,open(fil)))]][0])

