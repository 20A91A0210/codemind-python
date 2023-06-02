n=int(input())
lst=list(map(int,input().split()))
l=[]
c=0
for i in lst:
    if(i!=0):
        l.append(i)
    elif (i==0):
        c +=1
for j in range(c):
    l.append(0)
print(*l)
