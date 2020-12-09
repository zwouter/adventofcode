fil = "data8"
f = open(fil).readlines()

def terminates(x):
    acc = 0
    i = 0
    s = set()
    while i < len(x):
        if i in s:
            return False, acc
        s.add(i)
        ins = x[i].split(" ")[0]
        num = x[i].split(" ")[1]
        num = int(num[1:]) if num[0] == "+" else -int(num[1:])
        if ins == "nop":
            i += 1
        elif ins == "jmp":
            i += num
        elif ins == "acc":
            acc += num
            i += 1
    return True, acc


print(terminates(f)[1])

for i in range(len(f)):
    x = f.copy()
    ins = x[i].split(" ")[0]
    num = x[i].split(" ")[1]
    if ins == "nop":
        x[i] = "jmp " + num
    elif ins == "jmp":
        x[i] = "nop " + num
    else:
        continue
    if terminates(x)[0]:
        print(terminates(x)[1])
        break
