m=int(input())
n=int(input())
sum_m=0
sum_n=0
for i in range(1,m):
    if m%i==0:
        sum_m += i
for j in range(1,n):
    if n%j==0:
        sum_n += j
if sum_m==n and sum_n==m:
    print('Amicable')
else:
    print('Not Amicable')