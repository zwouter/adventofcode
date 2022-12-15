import ast
import itertools
from functools import cmp_to_key
file = open("data13")
lines = file.read().split("\n\n")


def eval_pairs(left1, right1):
    if isinstance(left1, int):
        left1 = [left1]
    if isinstance(right1, int):
        right1 = [right1]
    for zipped in itertools.zip_longest(left1, right1, fillvalue=-1):
        left, right = zipped
        if left == -1:
            return True
        elif right == -1:
            return False
        elif isinstance(left, list) or isinstance(right, list):
            eval = eval_pairs(left, right)
            if eval != "Sip":
                return eval
        elif left < right:
            return True
        elif right < left:
            return False
    return "Sip"


def part_1(pairs):
    correct = {}
    for i in range(len(pairs)):
        pair = lines[i].split("\n")
        correct[i + 1] = eval_pairs(ast.literal_eval(pair[0]), ast.literal_eval(pair[1]))
    return [x for x in correct if correct[x]]


print(sum(part_1(lines.copy())))


def eval_pairs2(left1, right1):
    if isinstance(left1, int):
        left1 = [left1]
    if isinstance(right1, int):
        right1 = [right1]
    for zipped in itertools.zip_longest(left1, right1, fillvalue=-1):
        left, right = zipped
        if left == -1:
            return 1
        elif right == -1:
            return -1
        elif isinstance(left, list) or isinstance(right, list):
            eval = eval_pairs2(left, right)
            if eval != "Sip":
                return eval
        elif left < right:
            return 1
        elif right < left:
            return -1
    return "Sip"


def part_2(pairs):
    flat = []
    for i in range(len(pairs)):
        pair = lines[i].split("\n")
        flat.append(ast.literal_eval(pair[0]))
        flat.append(ast.literal_eval(pair[1]))
    flat.append([[2]])
    flat.append([[6]])
    sort = sorted(flat, key=cmp_to_key(eval_pairs2), reverse=True)
    return (sort.index([[2]]) + 1) * (sort.index([[6]]) + 1)


print(part_2(lines.copy()))
