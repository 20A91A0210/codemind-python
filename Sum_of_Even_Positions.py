n=int(input())
lst=list(map(int,input().split()))
s_e=0
for i in range(len(lst)):
    if i%2==0:
        s_e+=lst[i]
print(s_e)
        