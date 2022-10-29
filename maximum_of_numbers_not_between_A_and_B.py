n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
lst1=[]
for i in lst:
    if a>i or i>b:
        lst1.append(i)
if len(lst1)==0:
    print(-1)
print(max(lst1))
        