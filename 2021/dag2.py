
fil = "data2"


inp = [(x[0],int(x[-1]))for x in open(fil).read().splitlines()]
# inp = map(lambda x:(x[0],int(x[-1])),open(fil).read().splitlines())

h = 0
d = 0
aim = 0
for a, b in inp:
    if a == 'f':
        h+=b
        # d+=b*aim
    elif a == 'd':
        d+=b
        # aim+=b
    else:
        d-=b
        # aim-=b
print(h*d)


# print([((a=='f')*b,(a=='d')*b,(a=='u')*-b)for a,b in[(x[0],int(x[-1]))for x in open(fil).read().splitlines()]])


h=d=a=0
for b in open(fil):
 x=int(b[-2]);a+=(b[0]=="d")*x-(b[0]=="u")*x
 if"f"==b[0]:h+=x;d+=x*a
print(h*d)

# print(sum((b[0]=="d")*(x:=int(b[-2]))-x*(b[0]=="u")for b in open(fil))*sum((b[0]=="f")*int(b[-2])for b in open(fil)))

h=d=a=0
for x, y in map(lambda f:(f[0],int(f[-2])),open(fil)):a+=(x=="d")*y-y*(x=="u");h,d=[[h,d],[h+y,d+y*a]]['f'==x];print(h*d)

h=d=a=0
for b in open(fil):x,y=b[0],int(b[-2]);a+=(x=="d")*y-y*(x=="u");h,d=h+y,y*a if'f'==x else h,d;print(h*d)

# h,d=[[h,d],[h+y,d+y*a]]['f'==x]
# h,d=h+y,y*a if'f'==x else h,d
# h,d,=(u:='f'==x)*h+y,u*y*a
