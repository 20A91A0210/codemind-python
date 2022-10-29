n=int(input())
lst=list(map(int,input().split()))
lst1=[]
for i in lst:
    if i%2!=0:
        lst1.append(i)
for i in lst:
    if i%2==0:
        lst1.append(i)
print(*lst1)

