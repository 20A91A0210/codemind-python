n=int(input())
lst=list(map(int,input().split()))
so=True
for i in lst:
    if i%2!=0:
        x=lst.index(i)
        if x%2==0:
            so=False
print(so)

            