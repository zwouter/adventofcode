file = open("data2")

lines = file.readlines()

wins = {1:3, 2:1, 3:2}

a_score = 0
b_score = 0
for line in lines:
    a = (ord(line.split()[0]) - 64) % 23
    b = (ord(line.split()[1]) - 64) % 23
    b_score += b + (3 if a==b else 0) + (6 if wins[b]==a else 0)
print(b_score)


print(sum({'AX':3,'AY':4,'AZ':8,'BX':1,'BY':5,'BZ':9,'CX':2,'CY':6,'CZ':7}[l[::2]]for l in open("d")))
print(sum('  BXCXAXAYBYCYCZAZBZ'.index(l[::2])for l in open("d"))//2)

# b = (ord(line.split()[1]) - 64) % 23
