def prime(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count += 1
    return count
x=int(input())
if prime(x)==2:
    lst=[]
    while x!=0:
        r=x%10
        lst.append(r)
        x //=10
    lstp=[]
    for j in lst:
        if prime(j)==2:
            lstp.append(j)
        else:
            break
    if len(lst)==len(lstp):
        print('Mega Prime')
    else:
        print('Not Mega Prime')
else:
    print('Not Mega Prime')