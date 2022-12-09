file = open("data3")

lines = file.readlines()

overlaps=[]
for line in lines:
    first = line[:len(line)//2]
    second = line[len(line)//2:]
    overlap = [ord(x)-96 for x in first if x in second][0]
    if overlap < 0:
        overlap = overlap + 58
    overlaps.append(overlap)


print(sum(overlaps))


overlaps=[]
for i in range(len(lines)-2):
    if i % 3 != 0:
        continue
    overlap = [ord(x)-96 for x in lines[i] if x in lines[i+1] and x in lines[i+2]][0]
    if overlap < 0:
        overlap = overlap + 58
    overlaps.append(overlap)
print(sum(overlaps))

