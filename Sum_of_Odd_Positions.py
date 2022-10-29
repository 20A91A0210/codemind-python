n=int(input())
lst=list(map(int,input().split()))
s_o=0
for i in range(len(lst)):
    if i%2!=0:
        s_o += lst[i]
print(s_o)
    