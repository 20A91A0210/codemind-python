n=int(input())
l=list(map(int,input().split()))
lst=[]
p=1
for i in l:
    p *= i
for j in l:
    lst.append(p//j)
print(*lst)