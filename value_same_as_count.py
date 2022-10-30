n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    x=l.count(i)
    if x==i:
        l1.append(i)
l1=list(set(l1))
print(len(l1))