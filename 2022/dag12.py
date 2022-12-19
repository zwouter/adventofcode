from tqdm import tqdm

file = open("data12")
lines = file.read().split("\n")
file.close()

ilen = len(lines)
jlen = len(lines[0])

# BFS
def BFS(G, root):
    Q = []
    explored = [root]
    Q.append(root)
    parents = {}
    while Q:
        v = Q.pop(0)
        cur_char = G[v[0]][v[1]]
        if cur_char == 'E':
            return v, parents
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            move_x = v[0] + x
            move_y = v[1] + y
            move = (move_x, move_y)
            if move not in explored and 0 <= move_x < ilen and 0 <= move_y < jlen:
                next_char = G[move_x][move_y]
                if cur_char == 'S':
                    cur_char = 'a'
                elif next_char == 'E':
                    next_char = 'z'
                if ord(next_char) - ord(cur_char) < 2:
                    explored.append(move)
                    Q.append(move)
                    parents[move] = v


def print_ans(answer):
    res = []
    for i in range(ilen):
        resi = []
        for j in range(jlen):
            if (i, j) in answer:
                resi.append('#')
            else:
                resi.append('.')
        res.append(resi)
    print('\n'.join(map(lambda x: ''.join(x), res)))


def get_best_path(goal, parents):
    path = []
    while True:
        goal = parents[goal]
        path.append(goal)
        if goal not in parents:
            break
    return path


def get_root(lines):
    for i in range(ilen):
        for j in range(jlen):
            if lines[i][j] == 'S':
                return i, j
    return False


# path = get_best_path(*BFS(lines.copy(), get_root(lines.copy())))
# print_ans(path)
# print(len(path))


def get_roots(lines):
    res = []
    for i in range(ilen):
        for j in range(jlen):
            if lines[i][j] == 'S' or lines[i][j] == 'a':
                res.append((i, j))
    return res


def part_2(lines):
    pairs = {}
    for root in tqdm(get_roots(lines)):
        bfs = BFS(lines, root)
        if not bfs:
            continue
        goal, parents = bfs
        pairs[root] = len(get_best_path(goal, parents))
    return min(pairs.values())
    # return min([len(get_best_path(*BFS(lines, root))) for root in get_roots(lines)])

# print(get_roots(lines.copy()))
print(part_2(lines.copy()))
