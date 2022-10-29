n=int(input())
lst=list(map(int,input().split()))
t=int(input())
num=True
for i in lst:
    if t==i:
        num=True
        break
    else:
        num=False
print(num)