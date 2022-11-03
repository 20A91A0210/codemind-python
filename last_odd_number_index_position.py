n=int(input())
lst=list(map(int,input().split()))
l=0
for i in range(len(lst)):
    if lst[i]%2!=0 :
        l=i
print(l)