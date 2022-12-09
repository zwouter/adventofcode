import re
file = open("data5").read()
start = file.split("\n\n")[0].split("\n")
operations = file.split("\n\n")[1].split("\n")

arrays = [[] for i in range((len(start[-1]) - 2) // 4 + 1)]
for i in range(len(start[:-1])):
    for j in range(1, len(start[i])-1)[::4]:
        letter = start[i][j]
        if letter.isupper():
            arrays[(j - 1) // 4].insert(0, letter)
for operation in operations:
    a, b, c = map(int, re.split("move|from|to", operation)[1:])
    arrays[c - 1] += reversed(arrays[b-1][-a:])
    arrays[b - 1] = arrays[b-1][:-a]

res = ""
for array in arrays:
    res += array[-1]
print(res)


arrays = [[] for i in range((len(start[-1]) - 2) // 4 + 1)]
for i in range(len(start[:-1])):
    for j in range(1, len(start[i])-1)[::4]:
        letter = start[i][j]
        if letter.isupper():
            arrays[(j - 1) // 4].insert(0, letter)
for operation in operations:
    a, b, c = map(int, re.split("move|from|to", operation)[1:])
    arrays[c - 1] += arrays[b-1][-a:]
    arrays[b - 1] = arrays[b-1][:-a]

res = ""
for array in arrays:
    res += array[-1]
print(res)

