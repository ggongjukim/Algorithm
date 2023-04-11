"""
같은 애를 다시뽑을 수 없음 [0] [0] 안됨
큰거 뒤에 작은거 올 수 있음 1 9 is not 9 1 => 순열
backtracking
"""
n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
answer = []
allanswer = []
def printvisited():
  temp = ''
  for i in answer:
    temp += str(arr[i]) + ' '
    
  if temp in allanswer:
    return
  allanswer.append(temp)
  print(temp)
  
def sol(cur_num):
  if cur_num == m+1 :
    printvisited()
    return

  for i in range(n):
    if i in answer:
      continue
    answer.append(i)
    sol(cur_num+1)
    answer.pop()

sol(1)