import re


def calc_1(eq):
    while re.findall("\(.*?\)", eq):
        pattern = min(re.findall("(?=(\(.*?\)))", eq), key=len)
        eq = eq.replace(pattern, str(calc_1(pattern[1:-1])))
    while len(re.findall("\d+", eq)) > 1:
        nrs = re.findall("\d+", eq)
        ops = re.findall("\+|\*", eq)
        rest = re.sub("\d+ (\+|\*) \d+", "",  eq, 1)
        if ops[0] == '+':
            eq = str(int(nrs[0]) + int(nrs[1])) + rest
        else:
            eq = str(int(nrs[0]) * int(nrs[1])) + rest
    return int(re.findall("\d+", eq)[0])


def calc_2(eq):
    while re.findall("\(.*?\)", eq):
        pattern = min(re.findall("(?=(\(.*?\)))", eq), key=len)
        eq = eq.replace(pattern, str(calc_2(pattern[1:-1])))
    while re.findall("\d+ \+ \d+", eq):
        pattern = re.findall("\d+ \+ \d+", eq)[0]
        nrs = re.findall("\d+", pattern)
        eq = eq.replace(pattern, str(int(nrs[0]) + int(nrs[1])), 1)
    while re.findall("\d+ \* \d+", eq):
        nrs = re.findall("\d+", eq)
        rest = re.sub("\d+ \* \d+", "",  eq, 1)
        eq = str(int(nrs[0]) * int(nrs[1])) + rest
    return int(re.findall("\d+", eq)[0])


file = open("data18").read().split("\n")

# Solve part 1
res = 0
for f in file:
    res += calc_1(f)
print(res)

# Solve part 2
res = 0
for f in file:
    res += calc_2(f)
print(res)

