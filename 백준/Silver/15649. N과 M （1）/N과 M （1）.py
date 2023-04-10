n,m = map(int,input().split())
answer = []
def backtracking(cur_num):
  if cur_num == m+1:
    for i in answer:
      print(i,end=' ')
    print()
    return

  for i in range(1,n+1):
    if cur_num > 1 and i in answer:
      continue
    answer.append(i)
    backtracking(cur_num+1)
    answer.pop()

backtracking(1)