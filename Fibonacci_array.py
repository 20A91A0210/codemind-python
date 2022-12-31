def fibonacci(l):
    fibonacci=False
    for i in range(len(l)-2):
        if l[i]+l[i+1]!=l[i+2]:
            fibonacci=False
            break
        else:
            fibonacci=True
    return fibonacci
    
n=int(input())
lst=list(map(int,input().split()))
if fibonacci(lst)==True:
    print('yes')
else:
    print('no')
            