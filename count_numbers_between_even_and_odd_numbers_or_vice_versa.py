n=int(input())
lst=list(map(int,input().split()))
c=0
for i in range(len(lst)):
    for j in range(i+2,len(lst)):
        if lst[i]%2==0 and lst[j]%2!=0 and j-i==2 or lst[i]%2!=0 and lst[j]%2==0 and j-i==2:
            c += 1
print(c)