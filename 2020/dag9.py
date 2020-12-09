fil = list(map(int, open("data9").readlines()))

i_start = 0
i_end = pream = 25
b = 0

while True:
    s = fil[i_start:i_end]
    a = fil[i_end]
    good = False
    for x in s:
        if a - x in s:
            good = True
    if not good:
        b = a
        break
    i_end += 1
    i_start += 1

print(a)
for x in range(len(fil)):
    i = x + 2
    while (sum(fil[x:i]) < a):
        i += 1
    if sum(fil[x:i]) == a:
        print(min(fil[x:i]) + max(fil[x:i]))

