from collections import deque
T = int(input())
result = 0

def show():
  for i in range(N):
    print(grid[i])
  for i in range(N):
    print(visited[i])

def grid_setting(num): # setting 하는 것
  for _ in range(num):
    y,x = map(int,input().split())
    grid[x][y] = 1
  # show()
  
def find_spot(n,m): # bfs 돌리기
  global que, result
  result = 0
  # print("result",result)
  for i in range(n):
    for j in range(m):
      if visited[i][j]:
        continue
      if grid[i][j] == 0:
        continue
      # 시작  
      visited[i][j] = True
      que = deque([(i,j)])
      result += 1
      bfs()
      
      
def in_range(x,y):
  return 0 <= x < N and 0<= y < M
  
def bfs():
  global que
  dxs = [-1, 1, 0, 0]
  dys = [0, 0, -1, 1]
  
  while que:
    x,y = que.pop()
    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy
      if not in_range(nx,ny):
        continue
      if visited[nx][ny]:
        continue
      if grid[nx][ny] == 0:
        continue
        
      visited[nx][ny] = True
      que.append((nx,ny))
      
  
for i in range(T):
  M,N,K = map(int,input().split())
  grid = [[0 for _ in range(M)] for _ in range(N)]
  visited =  [[False for _ in range(M)] for _ in range(N)]
  que = deque([])

  grid_setting(K)
  find_spot(N,M)
  print(result)
  
# show()

