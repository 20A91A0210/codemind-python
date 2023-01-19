n=int(input())
top=0
left=0
right=2*n-2
down=2*n-2
for i in range(2*n-1):
    for j in range(2*n-1):
        min_dic=min(i-top,down-i,j-left,right-j)
        print(n-min_dic,end=' ')
    print()
    