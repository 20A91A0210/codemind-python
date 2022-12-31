n=int(input())
x=65
for row in range(n):
    for col in range(n):
        print(chr(x),end=' ')
    x+= 1
    print()