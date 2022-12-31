s=input()
s=s.lower()
l=[]
for i in s:
    if s.count(i)==1:
        l.append(i)
l.sort()
x=''
for i in l:
    if i!=' ':
        x += i
print(x)