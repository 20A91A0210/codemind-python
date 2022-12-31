s=list(map(str,input().split()))
count=0
v='aeiouAEIOU'
for i in s:
    for j in range(len(i)):
        if (i[j] not in v and i[-(j+1)] in v) or (i[j] in v and i[-(j+1)]  not in v) :
            count += 1
print(count//2)