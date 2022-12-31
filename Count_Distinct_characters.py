s=input()
s=s.lower()
s1=''
for i in s:
    if i not in s1 and i!=' ':
        s1 += i
print(len(s1))