n=int(input())
lst=list(map(int,input().split()))
l=[]
for i in range(len(lst)-1,len(lst)//2-1,-1):
    l.append(lst[i])
for j in range(len(lst)//2):
    l.append(lst[j])
print(*l)