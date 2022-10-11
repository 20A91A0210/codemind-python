n=int(input())
a=0
b=1
while True:
    if n<=a or n<=b:
        break
    a=a+b
    b=a+b
if n==a or n==b:
    print('True')
else:
    print('False')