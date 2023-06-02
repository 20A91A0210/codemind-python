n=int(input())
lst=list(map(int,input().split()))
l=[]
c=0
for i in range(0,n):
    c=0
    for j in range(i+1,n):
        c += 1
        flag=0
        if(lst[i]<lst[j]):
            flag=1
            break
    if(flag==0):
        c=0
    l.append(c)
print(*l)
            