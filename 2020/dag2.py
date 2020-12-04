# import re
# f = open("data2", "r").readlines()
#
# # Preprocessing
# c = [re.split("\W+", x) for x in f]
# print(c)


# Part1
# print(len([1 for v in c if int(v[0]) <= len(re.findall(v[2], v[3])) <= int(v[1])]))

# import re;print(sum(1for a,b,c,d,_ in[re.split('\W+',x)for x in open('d').readlines()]if int(a)<=len(re.findall(c,d))<=int(b)))

# Part2
# print(len([1 for v in c if (v[3][int(v[0]) - 1] == v[2]) != (v[3][int(v[1]) - 1] == v[2])]))

# import re;print(sum(1for a,b,c,d,_ in[re.split('\W+',x)for x in open('d').readlines()]if(d[int(a)-1]==c)^(d[int(b)-1]==c)))
# import re;print(sum((d[int(a)-1]==c)^(d[int(b)-1]==c)for a,b,c,d,_ in[re.split('\W+',x)for x in open('d')]))

print(sum(sum(d[int(a)-1]==c[0]for a in b.split("-"))==1for b,c,d in map(str.split,open("d"))))


# print([re.  open('d').readlines()])
# print(list(map(lambda s:re.split('\W+',s),open('d').readlines())))
# print([re.split('\W+',x)for x in open('d').readlines()])
