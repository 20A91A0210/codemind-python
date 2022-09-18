m,n=map(int,input().split())
i=1
while 1:
    if i%m==0 and i%n==0:
        print(i)
        break
    i += 1