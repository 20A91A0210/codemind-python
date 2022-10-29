n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
lst1=[]
for i in lst:
    if a>i or i>b:
        lst1.append(i)
if len(lst1)==0:
    lst1.append(-1)
print(*lst1)
        