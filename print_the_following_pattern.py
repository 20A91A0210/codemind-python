n=int(input())
x=65+n-1
for row in range(n,0,-1):
    for col in range(row):
        print(chr(x),end=' ')
    x -= 1
    print()