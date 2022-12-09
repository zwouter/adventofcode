# 11:18
input = open("data6").read()

chars = []
for i in range(len(input)):
    char = input[i]
    chars.append(char)
    if len(chars) > 4:
        chars.remove(chars[0])
    if len(set(chars)) == 4:
        # print(i+1)
        break

chars = []
for i in range(len(input)):
    char = input[i]
    chars.append(char)
    if len(chars) > 14:
        chars.remove(chars[0])
    if len(set(chars)) == 14:
        # print(i+1)
        break

print(min(i+4for i,_ in list(enumerate(open("d").read()))if len(set(open("d").read()[i:i+4]))==4))
print(min(i+14for i,_ in list(enumerate(open("d").read()))if len(set(open("d").read()[i:i+14]))==14))
d=open("d").read();print(min(i+14for i,_ in list(enumerate(d))if len(set(d[i:i+14]))==14))

