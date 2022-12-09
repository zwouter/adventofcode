#12:17
file = open("data7").read().split("\n")

structure = {"/": {"dir_size": 0}}
cur = "/"

dirs = [cur]
curStruct = structure[cur]

for line in file[1:]:
    if line[:4] == "$ cd":
        cd = line.split("cd ")[1]
        if cd == "..":
            cur = dirs[-2]
            dirs = dirs[:-1]
            curStruct = structure
            for dir in dirs:
                curStruct = curStruct[dir]
            continue
        if cd not in curStruct:
            curStruct[cd] = {"dir_size": 0}
        cur = cd
        dirs.append(cd)
        curStruct = curStruct[cd]
    elif line[:4] == "$ ls" or line[:3] == "dir":
        continue
    else:
        curStruct["dir_size"] += int(line.split(" ")[0])

sizes = {}


def get_size(x, curStruct, dirs):
    dirs.append(x)
    size = curStruct["dir_size"] + sum(get_size(x, curStruct[x], dirs.copy()) for x in curStruct.keys() if x != "dir_size")
    sizes['/'.join(dirs)] = size
    return size


def calculate_all_sizes():
    root = "/"
    get_size(root, structure[root], [])


calculate_all_sizes()

print(sum(size for size in sizes.values() if size <= 100000))
print(min(size for size in sizes.values() if size > sizes["/"] - 40000000))
