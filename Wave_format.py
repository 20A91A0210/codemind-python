n=int(input())
l=list(map(int,input().split()))
l.sort()
l.reverse()
i=1
while(i<len(l)):
    temp=l[i]
    l[i]=l[i-1]
    l[i-1]=temp
    i += 2
print(*l)