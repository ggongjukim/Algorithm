"""
같은 애를 다시뽑을 수 있음 => 중복
1 9 랑 9 1 다름 => 순열
"""
n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr = list(set(arr))
arr = sorted(arr)
# print(arr)
answer = []
def printanswer():
  # print(visited)
  for i in range(len(answer)):
      print(answer[i], end=' ')
  print()
  # print(temp)
  
def sol(cnt):
  if cnt == m+1:
    printanswer()
    return

  for i in range(len(arr)):
    if cnt > 1 and answer[-1] > arr[i]:
      continue
    answer.append(arr[i])
    sol(cnt+1)
    answer.pop()
    
sol(1)