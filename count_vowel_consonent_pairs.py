i=input()
count=0
v='aeiouAEIOU'
for j in range(len(i)):
    if (i[j] not in v and i[-(j+1)] in v and i[j]!=' ') or (i[j] in v and i[-(j+1)]  not in v and i[-(j+1)]!=' ') :
        count += 1
print(count//2)