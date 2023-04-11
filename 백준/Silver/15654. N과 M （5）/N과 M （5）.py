"""
중복 안됨
조
visited
"""
n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
answer = []

def printanswer():
  for i in answer:
      print(i,end=' ')
  print()

def sol(cur_num):
  if cur_num == m+1 :
    printanswer()
    return

  for i in range(n):
    if arr[i] in answer:
      continue
    answer.append(arr[i])
    sol(cur_num+1)
    answer.pop()
sol(1)