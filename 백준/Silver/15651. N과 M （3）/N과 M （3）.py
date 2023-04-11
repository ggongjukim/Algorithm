"""
n 과 m
중복 가능
중복 순열
"""
n,m = map(int,input().split())
arr = []
def backtracking(cur_num):
  if cur_num == m+1:
    for i in arr:
      print(i,end=' ')
    print()
    return

  for i in range(1,n+1):
    arr.append(i)
    backtracking(cur_num+1)
    arr.pop()

backtracking(1)