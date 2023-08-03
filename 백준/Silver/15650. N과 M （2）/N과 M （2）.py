N,M = list(map(int,input().split()))
arr =[]

def sol(num):
  if num == M:
    for i in arr:
      print(i,end=' ')
    print()
    return

  for i in range(1,N+1):
    if len(arr) >0:
      if arr[-1] >= i:
        continue
    arr.append(i)
    sol(num+1)
    arr.pop()

sol(0)