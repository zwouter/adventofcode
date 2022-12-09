file = open("data4")

lines = file.readlines()

count = 0
for line in lines:
    line0 = line.split(",")[0]
    line1 = line.split(",")[1]
    range0 = list(range(int(line0.split("-")[0]), int(line0.split("-")[1]) + 1))
    range1 = list(range(int(line1.split("-")[0]), int(line1.split("-")[1]) + 1))
    if len(set(range0 + range1)) == max(len(range0), len(range1)):
        count += 1

print(count)

count = 0
for line in lines:
    line0 = line.split(",")[0]
    line1 = line.split(",")[1]
    range0 = list(range(int(line0.split("-")[0]), int(line0.split("-")[1]) + 1))
    range1 = list(range(int(line1.split("-")[0]), int(line1.split("-")[1]) + 1))
    if len(set(range0 + range1)) < len(range0) + len(range1):
        count += 1

print(count)


import re;print(sum(max(len(e:=list(range(a,b+1))),len(f:=list(range(c,d+1))))==len(set(e+f))for[a,b,c,d]in map(lambda l:map(int,re.split(",|-",l)),open("d"))))
import re;print(sum(len(e:=list(range(a,b+1)))+len(f:=list(range(c,d+1)))>len(set(e+f))for[a,b,c,d]in map(lambda l:map(int,re.split(",|-",l)),open("d"))))


