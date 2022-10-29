n=int(input())
lst=list(map(int,input().split()))
even_count=0
for i in lst:
    count=0
    while i!=0:
        i //= 10
        count +=1
    if count%2==0:
        even_count+=1
print(even_count)
        