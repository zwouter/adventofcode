# import regex
import re
file = open("data19").read().split("\n\n")
regexes = {}
rules = file[0].split("\n")
for rule in rules:
    spaced = rule.split(": ")
    key = spaced[0]
    if key == '8':
        value = '(42)+'
    elif key == '11':
        value = ''
    regexes[spaced[0]] = spaced[1]

counts = {'8': 0, '11': 0}


def get_regex(rule):
    if re.match("\".*\"", rule):
        return rule[1:-1]
    if rule == '42 | 42 8':
        return "("+get_regex('42')+")+"
    elif rule == "42 31 | 42 11 31":
        res = ""
        # return "("+get_regex('42')+get_regex('31')+")"
        for i in range(15):
            res += "((" + get_regex('42') + "){"+str(i)+"}(" + get_regex('31') + "){"+str(i)+"}" + ")|"
        return res[:-1]
    if '|' in rule:
        split = rule.split("|")
        return "({}|{})".format(get_regex(split[0]), get_regex(split[1]))
    else:
        res = ""
        nrs = re.findall("\d+", rule)
        for x in nrs:
            res += get_regex(regexes[x])
        return res


print(sum(bool(re.fullmatch(get_regex(regexes['0']), message)) for message in file[1].split("\n")))


# print(re.findall("a{n}b{n}", "aaabbb"))

# print(re.findall("(?P<name>a(?P=name))|a", "a"))
# print(regex.findall("(a(?:a(?R)?)?)", "aaaaaaakk"))
