def vowels(s):
    nv=0
    for i in s:
        if i in 'aeiouAEIOU':
            nv+= 1
    return nv
s=list(map(str,input().split()))
l=[]
for i in s:
    l.append(vowels(i))
print(l.count(max(l)))