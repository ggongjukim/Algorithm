'''
NN 크기 땅
땅 인구수
국경선 존재

인구 이동
국경선 공유 두 나라 인구차 L 이상 R 이하 => 두 나라 공유 국경선 오늘 하루 동안 연다

인구이동 시작
인접 한 칸만 이용해 이동 가능
연합 이라고 한다

연합 인구수 = 연합 인구수 / 칸 개수

연합 해체 / 국경선 닫기

인구 이동 몇일 동안 발생?

첫줄 N L R
둘줄 N줄 각 나라 인구수
'''
import math
from collections import deque
N, L, R = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
que = deque([])

def in_range(x,y):
    return 0 <= x < N and 0<= y < N

def can_go(nx,ny,x,y):
    return  L <= abs(grid[nx][ny]-grid[x][y]) <= R

# 국경선 먼저 열기
def bfs():
    global sum_grid,cnt_grid
    temp_grid_idx = []
    
    while que:
        x,y = que.popleft()
        temp_grid_idx.append((x,y)) # 지나온 땅 인덱스
        
        dxs = [-1, 1, 0, 0] # 상하좌우 => 인구 차로 판단
        dys = [ 0, 0, -1, 1]
        for dx, dy in zip(dxs, dys):
            nx,ny = x + dx, y + dy 
            if not in_range(nx,ny):
                continue
            
            if not can_go(nx,ny,x,y):
                continue
            
            if visited[nx][ny] == 1:
                continue

            # 인구이동
            visited[nx][ny] = 1
            que.append((nx,ny))
            sum_grid += grid[nx][ny]
            cnt_grid += 1
    
    # 정산
    for i in temp_grid_idx:
        x,y = i
        grid[x][y] = sum_grid // cnt_grid

ans = 0
sum_grid = 0
cnt_grid = 0
def move():
    global sum_grid,cnt_grid,visited
    tmp = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if visited[x][y] == 1:
                continue
            visited[x][y] = 1
            que.append((x,y))
            sum_grid = grid[x][y]
            cnt_grid = 1
            bfs()
            tmp += 1
    # print('tmp',tmp)
    return tmp

while True:
    if move() == N*N:
        print(ans)
        break
    ans += 1

# for i in grid:
#     print(i)
# for i in visited:
#     print(i)