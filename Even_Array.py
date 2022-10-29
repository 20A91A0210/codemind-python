n=int(input())
lst=list(map(int,input().split()))
even=True
for i in lst:
    if i%2!=0:
        even=False
        break
print(even)
   