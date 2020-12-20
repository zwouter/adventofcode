import re
file = open("data19").read().split("\n\n")
regexes = {}
rules = file[0].split("\n")
for rule in rules:
    spaced = rule.split(": ")
    regexes[spaced[0]] = spaced[1]


def get_regex(rule):
    if re.match("\".*\"", rule):
        return rule[1:-1]
    if '|' in rule:
        split = rule.split("|")
        return "({}|{})".format(get_regex(split[0]), get_regex(split[1]))
    else:
        res = ""
        for x in re.findall("\d+", rule):
            res += get_regex(regexes[x])
        return res


print(sum(bool(re.fullmatch(get_regex(regexes['0']), message)) for message in file[1].split("\n")))
