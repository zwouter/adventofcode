monkeys_test = {0: {'items': [79, 98], 'op': lambda x: x * 19, 'test': 23, 'true': 2, 'false': 3, 'count': 0},
                1: {'items': [54, 65, 75, 74], 'op': lambda x: x + 6, 'test': 19, 'true': 2, 'false': 0, 'count': 0},
                2: {'items': [79, 60, 97], 'op': lambda x: x * x, 'test': 13, 'true': 1, 'false': 3, 'count': 0},
                3: {'items': [74], 'op': lambda x: x + 3, 'test': 17, 'true': 0, 'false': 1, 'count': 0}}

monkeys_real = {0: {'items': [93, 98], 'op': lambda x: x * 17, 'test': 19, 'true': 5, 'false': 3, 'count': 0},
                1: {'items': [95, 72, 98, 82, 86], 'op': lambda x: x + 5, 'test': 13, 'true': 7, 'false': 6, 'count': 0},
                2: {'items': [85, 62, 82, 86, 70, 65, 83, 76], 'op': lambda x: x + 8, 'test': 5, 'true': 3, 'false': 0, 'count': 0},
                3: {'items': [86, 70, 71, 56], 'op': lambda x: x + 1, 'test': 7, 'true': 4, 'false': 5, 'count': 0},
                4: {'items': [77, 71, 86, 52, 81, 67], 'op': lambda x: x + 4, 'test': 17, 'true': 1, 'false': 6, 'count': 0},
                5: {'items': [89, 87, 60, 78, 54, 77, 98], 'op': lambda x: x * 7, 'test': 2, 'true': 1, 'false': 4, 'count': 0},
                6: {'items': [69, 65, 63], 'op': lambda x: x + 6, 'test': 3, 'true': 7, 'false': 2, 'count': 0},
                7: {'items': [89], 'op': lambda x: x * x, 'test': 11, 'true': 0, 'false': 2, 'count': 0}}

# -------------------------------------------------- Part 1
monkeys = monkeys_real.copy()

for _ in range(20):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        for j in range(len(monkey['items'])):
            item = monkey['items'][0]
            monkey['items'] = monkey['items'][1:]
            new = monkey['op'](item) // 3
            if new % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(new)
            else:
                monkeys[monkey['false']]['items'].append(new)
            monkey['count'] += 1
    # for monkey in monkeys:
    #     print(monkey, ": ", monkeys[monkey]['items'])

counts = []
for monkey in monkeys.values():
    counts.append(monkey['count'])
counts = list(sorted(counts))
print(counts[-1] * counts[-2])

# --------------------------------------------------
monkeys_test = {0: {'items': [79, 98], 'op': lambda x: x * 19, 'test': 23, 'true': 2, 'false': 3, 'count': 0},
                1: {'items': [54, 65, 75, 74], 'op': lambda x: x + 6, 'test': 19, 'true': 2, 'false': 0, 'count': 0},
                2: {'items': [79, 60, 97], 'op': lambda x: x * x, 'test': 13, 'true': 1, 'false': 3, 'count': 0},
                3: {'items': [74], 'op': lambda x: x + 3, 'test': 17, 'true': 0, 'false': 1, 'count': 0}}

monkeys_real = {0: {'items': [93, 98], 'op': lambda x: x * 17, 'test': 19, 'true': 5, 'false': 3, 'count': 0},
                1: {'items': [95, 72, 98, 82, 86], 'op': lambda x: x + 5, 'test': 13, 'true': 7, 'false': 6, 'count': 0},
                2: {'items': [85, 62, 82, 86, 70, 65, 83, 76], 'op': lambda x: x + 8, 'test': 5, 'true': 3, 'false': 0, 'count': 0},
                3: {'items': [86, 70, 71, 56], 'op': lambda x: x + 1, 'test': 7, 'true': 4, 'false': 5, 'count': 0},
                4: {'items': [77, 71, 86, 52, 81, 67], 'op': lambda x: x + 4, 'test': 17, 'true': 1, 'false': 6, 'count': 0},
                5: {'items': [89, 87, 60, 78, 54, 77, 98], 'op': lambda x: x * 7, 'test': 2, 'true': 1, 'false': 4, 'count': 0},
                6: {'items': [69, 65, 63], 'op': lambda x: x + 6, 'test': 3, 'true': 7, 'false': 2, 'count': 0},
                7: {'items': [89], 'op': lambda x: x * x, 'test': 11, 'true': 0, 'false': 2, 'count': 0}}


# -------------------------------------------------- Part 2

import math

monkeys = monkeys_real.copy()

lcm = math.prod([monkey['test'] for monkey in monkeys.values()])

round = 0
for _ in range(10000):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        for j in range(len(monkey['items'])):
            item = monkey['items'][0]
            monkey['items'] = monkey['items'][1:]
            new = monkey['op'](item) % lcm
            if new % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(new)
            else:
                monkeys[monkey['false']]['items'].append(new)
            monkey['count'] += 1
    round += 1
    # print(round)

counts = []
for monkey in monkeys.values():
    counts.append(monkey['count'])
counts = list(sorted(counts))
print(counts[-1] * counts[-2])
