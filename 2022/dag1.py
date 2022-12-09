# file = open("data1")
#
# lists = []
# cur = []
# for line in file.readlines():
#     if line != "\n":
#         cur.append(int(line))
#     else:
#         lists.append(sum(cur))
#         cur = []
# # Exc 1
# print(max(lists))
# # Exc 2
# print(sum(list(reversed(sorted(lists)))[:3]))


print(max([sum(y)for y in[map(int,x.split("\n"))for x in open("d").read().split("\n\n")]]))
# Met spieken
# print(max(sum(map(int,x.split()))for x in open("d").read().split("\n\n")))

print(sum(sorted([sum(y)for y in[map(int,x.split("\n"))for x in open("d").read().split("\n\n")]])[-3:]))
# Met spieken
# print(sum(sorted(sum(map(int,x.split()))for x in open("d").read().split("\n\n"))[-3:]))

