from collections import deque
n,m = map(int,input().split())
grid = [list(map(int,list(input()))) for _ in range(n)]
# print(grid)
def in_range(x,y):
  return 0 <= x < n and 0 <= y < m

def bfs(x,y):
  q = deque([(x,y)])
  grid[x][y] = 1
  dxs = [-1, 1, 0, 0]
  dys = [0, 0, -1, 1]
  while q:
    x,y = q.popleft()
    for dx, dy in zip(dxs,dys):
      nx, ny = x + dx, y + dy
      if not in_range(nx,ny):
        continue
      if grid[nx][ny] == 0:
        continue
      if grid[nx][ny] != 1: # 왔던곳이면
        continue
      grid[nx][ny] = grid[x][y] + 1
      q.append((nx,ny))
bfs(0,0)
print(grid[n-1][m-1])