from collections import deque
m,n,h = map(int,input().split())
grid = []
for i in range(h):
  grid.append([list(map(int,input().split())) for _ in range(n)])

def in_range(z,x,y):
  return 0 <= x < n and 0 <= y < m and 0 <= z < h

  
def bfs():
  q = deque(tmt)
  # grid[z][x][y] = 1
  
  dzs = [-1, 1, 0, 0, 0, 0]
  dxs = [ 0, 0,-1, 1, 0, 0]
  dys = [ 0, 0, 0, 0,-1, 1]
  while q:
    z,x,y = q.popleft()
    for dz,dx,dy in zip(dzs,dxs,dys):
      nz, nx,ny = z+dz, x+dx ,y+dy
      # print(z,x,y,"=>",nz,nx,ny)
      if not in_range(nz,nx,ny):
        continue
      if grid[nz][nx][ny] == 0:
        grid[nz][nx][ny] = grid[z][x][y] + 1
        q.append((nz,nx,ny))
        # print(q)
         
tmt = []
for z in range(h):
  for x in range(n):
    for y in range(m):
      if grid[z][x][y] == 1:
        tmt.append((z,x,y))
bfs()

# for z in range(h):
#   for x in range(n):
#     print(grid[z][x])
## 확인하기
max_day = 0        
is_zero = False
for z in range(h):
  for x in range(n):
    for y in range(m):
      if grid[z][x][y] == 0:
        print(-1)
        exit(0)
    max_day = max(max_day,max(grid[z][x]))
print(max_day-1)
