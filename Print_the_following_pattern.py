n=int(input())
i=1
for row in range(n,0,-1): #5,4,3,2,1  #4,3,2,1
    for col in range(i,n+1):  #1,2,3,4,5     # 2,3,4,5  
        print(col,end=' ')
    i +=1
    print()