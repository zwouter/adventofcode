import time


# Part 1
fil = list(map(int, open("data9").readlines()))
for i in range(25,len(fil)):
    s = fil[i-25:i]
    a = fil[i]
    if sum(a-x in s for x in s)==0:
        break
print(a)

# Part 2
for x in range(len(fil)):
    i = x + 2
    while sum(fil[x:i]) < a:
        i += 1
    if sum(fil[x:i]) == a:
        print(min(fil[x:i]) + max(fil[x:i]))


# Oneliners
fil = "data9"
# Oneliner 1
print([[f[i]for i in range(25,len(f))if sum(f[i]-x in f[i-25:i]for x in f[i-25:i])<1][0]for f in[list(map(int,open(fil).readlines()))]][0])

starttime = time.time()
print([sum([sum([min(f[x:i])+max(f[x:i])for i in range(x+2,len(f))if sum(f[x:i])==[f[i]for i in range(25,len(f))if sum(f[i]-x in f[i-25:i]for x in f[i-25:i])<1][0]])for x in range(len(f))])for f in [list(map(int,open(fil).readlines()))]][0])

print(time.time()-starttime)



