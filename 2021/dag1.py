fil = "data1"

# Part 1
som = 0
lines = [int(a) for a in open(fil).readlines()]
for i in range(len(lines))[:-1]:
    if lines[i] < lines[i + 1]:
        som += 1
print(som)

# Part 2
som = 0
lines = [int(a) for a in open(fil).readlines()]
for i in range(len(lines))[:-3]:
    if lines[i] < lines[i+3]:
        som += 1
print(som)

# Oneliner
print((lambda f:sum(int(f[i])<int(f[i+3])for i in range(len(f)-3)))(open(fil).readlines()))