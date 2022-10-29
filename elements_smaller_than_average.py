n=int(input())
lst=list(map(int,input().split()))
c=0
for i in lst:
    if i<=(sum(lst)//n):
        c += 1
print(c)
       
        