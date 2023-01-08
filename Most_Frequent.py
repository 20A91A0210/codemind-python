n=int(input())
lst=list(map(int,input().split()))
l=[]
max=0
max_count=0
for i in lst:
    if lst.count(i)>max:
        max=lst.count(i)
        max_count=i
for i in lst:
    if lst.count(i)==max:
        l.append(i)
print(min(l))