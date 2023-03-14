#탐욕법
N,M,K = list(map(int,input().split(' ')))
count = min(N//2,M)
N -= 2 * count
M -= count

if N != 0:
    K -= N
if M != 0:
    K -= M

if K > 0:
    temp = 0
    if K%3 != 0 :
        temp = 1 
    count -= K//3 + temp
print(count)