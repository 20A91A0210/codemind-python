n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    if i%2==0:
        if i not in l:
            l.append(i)
print(len(l))