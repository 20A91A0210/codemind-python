n=int(input())
x=n
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1:
            print(x,end=' ')
        else:
            print(end=' ')
    x -= 1
    print()