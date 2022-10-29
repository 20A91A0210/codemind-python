n=int(input())
lst=list(map(int,input().split()))
binary=True
for i in lst:
    if i!=0 and i!=1:
        binary=False
    else:
        binary=True
print(binary)