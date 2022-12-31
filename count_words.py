s=list(map(str,input().split()))
count=0
v='aeiouAEIOU'
for i in s:
    if (i[0] in v and i[-1] not in v):
        count += 1
print(count)