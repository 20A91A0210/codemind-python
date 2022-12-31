s=input()
s=s.lower()
l=[]
s1=''
for i in s:
    if i not in l and i!=' ':
        l.append(i)
l.sort()
for j in l:
    s1 += j
print(s1)