"""
같은 애를 다시뽑을 수 없음 [0] [0] 안됨
큰거 뒤에 작은거 올 수 있음 1 9 is 9 1 => 조합
visited
"""
n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
answer = []
visited = [False] * n
allanswer = []
# allanswer = []
def printvisited():
  temp = ''
  for i in range(n):
    # print(visited)
    if visited[i]:
      # print(arr[i], end=' ')
      temp += str(arr[i]) + ' '
  if temp in allanswer:
    return
  allanswer.append(temp)
  print(temp)
  
def sol(cnt, last_idx):
  if cnt == m:
    printvisited()
    return

  for i in range(last_idx+1, n):
    visited[i] = True
    sol(cnt+1,i)
    visited[i] = False
    
for i in range(n):
  visited[i] = True
  sol(1,i)
  visited[i] = False