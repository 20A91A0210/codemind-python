n=int(input())
for row in range(n):
    for col in range(n):
        if row==col or row+col==n-1 :
            print('x',end='')
        else:
            print('0',end='')
    print()