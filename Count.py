n=int(input())
lst=map(int,input().split())
so=se=0
for i in lst:
    if i%2==0:
        se += 1
    else:
        so += 1
print(se,so)