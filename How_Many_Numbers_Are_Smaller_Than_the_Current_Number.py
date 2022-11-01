n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in lst:
    count =0
    for j in lst:
        if i>j:
            count += 1
    l.append(count)
print(*l)