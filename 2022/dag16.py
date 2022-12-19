from tqdm import tqdm
import re

file = open("data16")

split_lines = file.read().split("\n")


def split_to_valves(lines):
    res = {}
    for line in lines:
        arr = re.findall("[A-Z]{2}|\d{1,2}", line)
        res[arr[0]] = {'flow': int(arr[1]), 'valves': arr[2:]}
    return res


def reverse_valves(valves):
    res = {}
    for valve1 in valves:
        res[valve1] = []
        for valve2 in valves:
            if valve1 in valves[valve2]['valves']:
                res[valve1].append(valve2)
    return res


def find_all_paths(current, visited, valves):
    paths = []
    option = True
    for possibility in valves[current[-1]]['valves']:
        if possibility not in visited:
            option = False
            path = find_all_paths(current + [possibility], visited + [possibility], valves)
            if path:
                paths.append(path)
    if option:
        return current
    if paths:
        return paths


def flatten_paths(paths):
    print(paths, len(paths))
    if not isinstance(paths, list):
        return paths
    elif len(paths) == 1:
        return flatten_paths(paths[0])
    else:
        res = []
        for path in paths:
            res += flatten_paths(path)
        # return list(map(flatten_paths, paths))
        return res


def part1(lines):
    valves = split_to_valves(lines)
    reversed_valves = reverse_valves(valves)
    all_paths = []
    for valve in valves:
        all_paths.append(find_all_paths([valve], [valve], valves))
    print(all_paths)
    print(flatten_paths(all_paths))
    # print(valves)
    # print(reversed_valves)
    known_valves = {}


part1(split_lines.copy())
# print(flatten_paths([[[['AA', 'DD', 'CC', 'BB'], ['AA', 'DD', 'EE', 'FF', 'GG', 'HH']]]]))

def part2(lines):
    pass


part2(split_lines.copy())
