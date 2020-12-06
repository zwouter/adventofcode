fil = "data3"

# Normal method for day 3
# f = open(fil, "r").readlines()
#
# def calc(x, y):
#     return sum(1 for i, j in [(a * y, (a * x) % (len(f[0]) - 1)) for a in range(len(f))] if i < len(f) and f[i][j] == '#')

# Oneliner for day 3
import math;print([math.prod([sum(a*y<len(f)and f[a*y][(a*x)%(len(f[0])-1)]=='#'for a in range(len(f)))for x,y in[(1,1),(3,1),(5,1),(7,1),(1,2)]])for f in[open(fil).readlines()]][0])


