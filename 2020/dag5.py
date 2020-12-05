# Original way

#import re
# f = open("data5")
# ids = []
# for x in f:
#     x = re.sub("F|L","0",re.sub("B|R","1",x))
#     row = int(x[:7], 2)
#     col = int(x[7:], 2)
#     ids.append(row * 8 + col)
# print(max(ids))
# print([i for i in range(min(ids), max(ids)) if i not in ids][0])

# print([[i for i in range(min((k)), max(k)) if i not in (k)][0] for k in [[int((z:=re.sub("F|L","0",re.sub("B|R","1",x)))[:7],2)*8+int(z[7:],2)for x in open("data5")]]][0])


# ids = [int(re.sub("F|L","0",re.sub("B|R","1",x)), 2)for x in open("data5")]
# Oneliner
import re;print([[i for i in range(min(d),max(d))if i not in d][0]for d in[[int(re.sub("F|L","0",re.sub("B|R","1",x)),2)for x in open("d")]]][0])

