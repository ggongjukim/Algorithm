from collections import deque
N,M = map(int,input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

result = []
count = 0
# print(grid)
# print(visited)
def printall():
  for i in range(N):
    print(visited[i])
  for i in range(N):
    print(grid[i])
  print("----------------------------")

def in_range(x,y):
  return 0 <= x < N and 0 <= y < M

def bfs():
  global count

  dxs = [0,0,1,-1]
  dys = [1,-1,0,0]
  while len(que) > 0:
    x,y = que.popleft()

    for dx, dy in zip(dxs,dys):
      nx, ny = x+ dx,y+dy
    
      if not in_range(nx,ny):
        continue
      if grid[nx][ny] != 1:
        continue
      if visited[nx][ny]:
        continue
      visited[nx][ny] = True
      que.append([nx,ny])
      count += 1
      # print(count)

for i in range(N):
  for j in range(M):
    if visited[i][j]:
      continue
    if grid[i][j] != 1:
      continue
      
    visited[i][j] = True
    que = deque()
    que.append((i,j))
    count = 1
    
    bfs()
    result.append(count)
    # printall()
if len(result) == 0:
  print(0)
  print(0)
else:
  print(len(result))
  print(max(result))