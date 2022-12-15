# -------------------- Part 1
file = open("data10")
lines = file.read().split("\n")
file.close()

x = 1
cyclevalues = [1]

for line in lines:
    cyclevalues.append(x)
    if line != "noop":
        x += int(line.split(" ")[1])
        cyclevalues.append(x)

# print(list(zip([(l!="noop")*[x,x:=l.split(" ")[-1]]for l in open("d").readlines()], [(l=="noop")*[x]for l in open("d").readlines()])))


print(sum(cyclevalues[i-1] * i for i in [20, 60, 100, 140, 180, 220]))


# -------------------- Part 2
file = open("data10")
lines = file.read().split("\n")
file.close()

x = 1
CRT = [['_' for _ in range(40)] for _ in range(6)]
cycle = 0

for line in lines:
    if abs((cycle % 40) - x) < 2:
        CRT[cycle // 40][cycle % 40] = '#'
    else:
        CRT[cycle // 40][cycle % 40] = '.'
    if line != "noop":
        cycle += 1
        if abs((cycle % 40) - x) < 2:
            CRT[cycle//40][cycle % 40] = '#'
        else:
            CRT[cycle//40][cycle % 40] = '.'
        x += int(line.split(" ")[1])
    cycle += 1


print('\n'.join(map(lambda x: ' '.join(x), CRT)))
