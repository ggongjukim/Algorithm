N = int(input())
count =0
N = 1000-N
arr = [500,100,50,10,5,1]
for i in arr:
    count += N//i
    N = N%i
print(count)