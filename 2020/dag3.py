# import operator
# from functools import reduce
# import math
#
f = open("data3", "r").readlines()

def calc(x, y):
    return sum(1 for i, j in [(a * y, (a * x) % (len(f[0]) - 1)) for a in range(len(f))] if i < len(f) and f[i][j] == '#')


# import math;print(math.prod([sum(1for i,j in[(a*y,(a*x)%(len(open("d").readlines()[0])-1))for a in range(len(open("d").readlines()))]if i<len(open("d").readlines())and open("d").readlines()[i][j]=='#') for x,y in[(1,1),(3,1),(5,1),(7,1),(1,2)]]))
# import math;print(math.prod([sum(1for i,j in[(a*y,(a*x)%31)for a in range(323)]if i<323and open("d").readlines()[i][j]=='#') for x,y in[(1,1),(3,1),(5,1),(7,1),(1,2)]]))
# import math;print([math.prod([sum(1for i,j in[(a*y,(a*x)%(len(f[0])-1))for a in range(len(f))]if i<len(f)and f[i][j]=='#')for x,y in[(1,1),(3,1),(5,1),(7,1),(1,2)]])for f in[open("d").readlines()]][0])
import math;print([math.prod([sum(a*y<len(f)and f[a*y][(a*x)%(len(f[0])-1)]=='#'for a in range(len(f)))for x,y in[(1,1),(3,1),(5,1),(7,1),(1,2)]])for f in[open("d").readlines()]][0])


def q(r,d=1):return sum(i[l*r%(len(i)-1)]=='#'for(l,i)in enumerate(list(open("d"))[::d]));print(q(1)*q(3)*q(5)*q(7)*q(1, 2))