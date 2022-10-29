n=int(input())
lst=list(map(int,input().split()))
avg=(sum(lst)//n)
bool=False
for i in lst:
    if i==avg:
        bool=True
print(bool)