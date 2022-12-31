s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
l=[]
s=''
for i in s1:
    if i in s2 and i!=' ' and i not in l:
        l.append(i)
l.sort()
for i in l:
    s += i
if len(l)==0:
    print(-1)
else:
    print(s)