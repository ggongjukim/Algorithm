n = int(input())
arr = []
def sol(cur_num):
  if cur_num == n:
    for i in arr:
      print(i,end=' ')
    print()
    return
  for i in range(1,n+1):
    if i in arr:
      continue
    arr.append(i)
    sol(cur_num + 1)
    arr.pop()
sol(0)