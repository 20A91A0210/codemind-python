n=int(input())
lst=list(map(int,input().split()))
k=int(input())
sum=0
for i in range(k):
    sum += lst[i]
print(sum)