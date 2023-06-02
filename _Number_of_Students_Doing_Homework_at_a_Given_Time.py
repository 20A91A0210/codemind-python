n=int(input())
starttime=list(map(int,input().split()))
m=int(input())
endtime=list(map(int,input().split()))
qt=int(input())
c=0
for i in range(n):
    if(starttime[i]<=qt<=endtime[i]):
        c+=1
print(c)
    
