n,k=map(int,input().split())
lst=list(map(int,input().split()))
count=0
for i in lst:
    if i<0:
        i=abs(i)
    i=str(i)
    if len(i)==k:
        count+=1
print(count)
