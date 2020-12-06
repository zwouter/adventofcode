# Day 4 oneliner
fil = "data4"
import re;print(sum(7==(sum(sum(q==(u:=k.split(":"))[0]and bool(re.fullmatch(g,u[1]))for k in c)for q,g in zip("byr iyr eyr hgt hcl ecl pid".split(),"(19[2-9]\d|200[0-2]) 20(1\d|20) 20(2\d|30) (1(([5-8]\d)|(9[0-3]))cm)|(59|6\d|7[0-6])in #[a-f\d]{6} amb|blu|brn|gr[yn]|hzl|oth \d{9}".split())))for c in[re.split("\n| ",c)for c in open(fil).read().split("\n\n")]))


# Normal version of day 7
# import re
# cont = [c.replace("\n"," ").split() for c in open("data4").read().split("\n\n")]
# count = 0
# require = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
# regexes = ["(19[2-9][0-9]|200[0-2])","20(1[0-9]|20)","20(2[0-9]|30)","(1(([5-8][0-9])|(9[0-3]))cm)|(59|6[0-9]|7[0-6])in","#[a-f0-9]{6}","amb|blu|brn|gry|grn|hzl|oth","[0-9]{9}"]
# for c in cont:
#     good = True
#     try:
#         for req, reg in zip(require, regexes):
#             good2 = False
#             for k in c:
#                 if req == k.split(":")[0]:
#                     good2 = re.fullmatch(reg, k.split(":")[1])
#             good = good and good2
#     except ValueError:
#         good = False
#     if good:
#         count += 1
# print(count)