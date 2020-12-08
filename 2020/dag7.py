import re
fil = "data7"
f = open(fil)
dict = {x.split(" contain ")[0]:x.split(" contain ")[1].split(", ") for x in f.read().replace("bags", "bag").replace(".","").split("\n")}
s = set()
# Part 1
for k,v in dict.items():
    for x in v:
        if "shiny gold bag" in x:
            s.add(k)
changed = True
while changed:
    changed = False
    for k, v in dict.items():
        for x in v:
            x = re.split("no |\d+ ", x)[1]
            if x in s and k not in s:
                s.add(k)
                changed = True
print(len(s))

# Part 2
s.clear()
for k,v in dict.items():
    if "shiny gold bag" in k:
        for x in v:
            s.add(x)

def getsum(x):
    num = x.split(" ")[0]
    bag = re.split("no |\d+ ", x)[1]
    if num == "no":
        return 0
    else:
        res = 1
        for k, v in dict.items():
            if bag in k:
                for x in v:
                    res += getsum(x)
        return int(num) * res

print(sum(list(map(getsum, s))))

# Poging tot oneliner
# print(sum(list(map((a:=lambda x:0if(n:=x.split(" ")[0])=="no"else int(n)*sum(sum(a(x) for x in v if re.split("no |\d+ ", x)[1] in k)+1for k,v in dict.items())), s))))

