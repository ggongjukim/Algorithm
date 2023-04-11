"""
중복 가능
순열
backtracking(cur_num)
"""
n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
answer = []
def printvisited():
  for i in answer:
      print(i,end=' ')
  print()

def sol(cur_num):
  if cur_num == m+1 :
    printvisited()
    return

  for i in range(n):
    answer.append(arr[i])
    sol(cur_num+1)
    answer.pop()

sol(1)