fil = "data1"

f = open(fil, "r")
content = set([int(x) for x in f.read().split("\n")])

# Deel 1
for c in content:
    if (2020-c) in content:
        print(c * (2020-c))
        break

# Deel 2
for c in content:
    for k in content:
        for x in content:
            if c + k + x == 2020:
                print(c * k * x)
