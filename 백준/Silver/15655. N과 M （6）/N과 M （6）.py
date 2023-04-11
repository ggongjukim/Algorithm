"""
중복 안됨
조합
visited
"""
n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
visited = [False] * n

def printvisited(v):
  for i in range(n):
    if v[i]:
      print(arr[i],end=' ')
  print()

def sol(cnt,last_idx):
  if cnt == m:
    printvisited(visited)
    return

  for i in range(last_idx+1,n):
    visited[i] = True
    sol(cnt+1,i)
    visited[i] = False

for i in range(n):
  visited[i] = True
  sol(1,i)
  visited[i] = False