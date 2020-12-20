
def mprint(t):
    for i in t:
        for j in i:
            for k in j:
                print(k)
            print("uuu")
        print("--------")
    print("Done")
    print()


def expand(lists):
    # print(lists)
    for w in range(len(lists)):
        for z in range(len(lists[w])):
            for x in range(len(lists[w][z])):
                lists[w][z][x] = ['.'] + lists[w][z][x] + ['.']
    # print(lists)
    zeroes_x = [['.' for _ in lists[0][0][0]]]
    # print(zeroes_x)
    for w in range(len(lists)):
        for z in range(len(lists[0])):
            lists[w][z] = zeroes_x + lists[w][z] + zeroes_x

    zeroes_z = [[['.' for y in lists[0][0][0]] for x in lists[0][0]]]
    for w in range(len(lists)):
        lists[w] = zeroes_z + lists[w] + zeroes_z

    zeroes_w = [[[['.' for _ in x] for x in z] for z in w] for w in lists]
    # print(zeroes_w)
    # for w in range(len(lists)):
    #     for z in range(len(lists[0])):
    #         for x in range(len(lists[0][0])):
    #             for y in range(len(lists[0][0][0])):
    #                 zeroes_w[w][z][x][y] = '.'
    # zeroes_w = [[[['.' for y in lists[0][0][0]]] for z in lists[0]]]
    lists = zeroes_w + lists + zeroes_w

    return lists


t = [[[['.', '#'], ['.', '#']]]]
mprint(t)

t = expand(t)
mprint(t)

t = expand(t)
print(len(t) * len(t[0]))
# t = expand(t)
# mprint(t)



