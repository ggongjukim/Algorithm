"""
5*5 25명
이다솜파
임도연파

이다솜파는 소문난 칠공주 결성
7명의 학생들로 구성
가로 세로 반드시 인접
이다솜파중 4명이상 이다솜파

소문난 칠공주를 결성할 수 있는 모든 경우의 수?
s 이다솜
y 임도연

완탐으로 풀려면.. 
dfs bfs 로 해야하는 거 아니감?.. 
안되는 거 있을 수 있음!

25개 갯수가 얼마 안되니까 0-24 인덱스를 가지는 배열을 만들어서 7개 조합을 해야함 => visited

완료 조건에서 
1.s >= 4 인지 확인
2.dfs bfs로 인접인지 확인
"""
from collections import deque
grid = [list(map(str,list(input()))) for _ in range(5)]
visited = [[0 for _ in range(5)] for _ in range(5)]
answer = 0

def in_range(x,y):
  return 0 <= x < 5 and 0 <= y < 5

def check_s(idx):
  x = idx // 5
  y = idx % 5
  return 1 if grid[x][y] == 'S' else 0

def can_go(x,y):
  return True if visited[x][y] else False

def check_bfs(sx,sy):
  q = deque()
  dfs_visited = [[False for _ in range(5)] for _ in range(5)]
  q.append((sx,sy))
  dfs_visited[sx][sy] = True
  cnt = 1

  while q:

    cx,cy = q.popleft()
  # 상하좌우
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    
    for dx, dy in zip(dxs,dys):
      nx, ny = cx + dx, cy + dy
      if not in_range(nx,ny):
        continue
      if not can_go(nx,ny):
        continue
      if not dfs_visited[nx][ny]:
        q.append((nx,ny))
        dfs_visited[nx][ny] = True
        cnt +=1
        
    # for i in dfs_visited:
    #   print(i)
    # print(q)
    # print("------------------")
  return cnt == 7
  
def check():
  for i in range(5):
      for j in range(5):
          if visited[i][j]:
              return check_bfs(i,j)
            
def printvisited():
  for i in visited:
    print(i)
  print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
            
def sol(cur_num,last_idx,cnt_s):
  global answer
  if cur_num == 7:
    if cnt_s >= 4: # 이다솜파 조건 S 개수
      # printvisited()
      if check():
        # printvisited()
        answer +=1
    return

  for i in range(last_idx+1, 25):
    visited[i//5][i%5] = 1
    sol(cur_num + 1,i, cnt_s + check_s(i))
    visited[i//5][i%5] = 0
    
for i in range(25):
  visited[i//5][i%5] = 1
  sol(1,i, check_s(i))
  visited[i//5][i%5] = 0

# sol(1,0, check_s(0))
print(answer)