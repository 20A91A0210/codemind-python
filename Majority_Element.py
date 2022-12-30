n=int(input())
lst=list(map(int,input().split()))
num=0
for i in lst:
    if lst.count(i)>n/2:
        num=i
print(num)