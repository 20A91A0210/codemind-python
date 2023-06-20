n=int(input())
lst=list(map(int,input().split()))
k=int(input())
l=[]
for i in range(n):
    if(lst[i]+k>=max(lst)):
        l.append(True)
    else:
        l.append(False)
print(*l)