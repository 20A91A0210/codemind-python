s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
s1=s1.split(' ')
s2=s2.split(' ')
l=[]
for i in s2:
    i=i.lower()
    if i in s1:
        l.append(i)
print(*l)