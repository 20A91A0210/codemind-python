s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
l=[]
for i in s1:
    if i not in s2 and i not in l and i!=' ':
        l.append(i)
for i in s2:
    if i not in s1 and i not in l and i!=' ':
        l.append(i)
l.sort()
s=''
for j in l:
    s += j
print(s)
    