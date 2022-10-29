n=int(input())
lst=list(map(int,input().split()))
so=se=0
for i in range(len(lst)):
    if i%2==0:
        se+=lst[i]
    else:
        i%2!=0
        so+=lst[i]
if abs(se-so)==0:
    print('YES')
else:
    print('NO')
    