n=int(input())
lst=list(map(int,input().split()))
lst_1=[]
l=[]
for i in lst:
    if i not in lst_1:
        l.append(i)
        l.append(lst.count(i))
        lst_1.append(i)
print(*l)  