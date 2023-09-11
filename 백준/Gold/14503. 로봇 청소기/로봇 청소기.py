'''
로봇 청소기와 방의 상태가 주어졌을때 
청소하는 영역의 개수를 구하는 프로그램

벽 or 빈칸
청소기는 바라보는 방향이 있음 동서남북 중하나
처음 빈칸을 전부 청소되지 않은 상태

현재 칸 청소 안된 경우 => 현재칸 청소
현재 칸 4칸중 청소되지 않은 빈칸 없는경우 
    바라보는 방향 유지하고 한칸 후진하고 1번으로 돌아감
    벽이라 후진 불가하면 작동 멈춤
청소 되지않은 칸 있으면 
    반시계 방향 90 도 회전 (왼쪽으로)
    바라보는 방향 기준으로 앞쪽 칸이 청소되지않은 빈칸인 경우 한칸 전진

[입력]
첫줄 방크기 N M
둘줄 로봇 청소기가 있는 칸의 좌표 r, c ,d 방향 0북 1동 2남 3서
셋줄 N줄에 방 상태

[출력]
청소하는 칸의 개수
'''
from collections import deque

N,M = map(int,input().split())
s_x,s_y,d = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
que = deque([])
dirc = [(-1,0),(0,1),(1,0),(0,-1)]

# for i in grid:
    # print(i)
def in_range(x,y):
    return 0<= x < N and 0<= y < M

def can_clean(x,y):
    can = False
    for i in range(4):
        nx, ny = x + dirc[i][0], y + dirc[i][1]
        if not in_range(nx,ny):
            continue
        if grid[nx][ny] == 0: # 동서남북에 청소할 곳이 있으면
            can = True
    return can

def bfs():
    global d
    cnt = 1
    while True:
        if que:
            x,y = que.popleft()
            

        if can_clean(x,y):# 동서남북중 청소할 곳이 있는 경우
            # 반시계 90도 회전
            d -= 1
            d = 3 if d < 0 else d 
            
            nx,ny = x + dirc[d][0] , y+ dirc[d][1] # 해당 방향으로 전진
            # print("nx,ny",nx,ny)
            if grid[nx][ny] == 0: # 청소 안했으면 전진
                que.append((nx,ny))
                cnt += 1
                grid[nx][ny] = 2 # 청소했으면 2

        else: # 청소할 곳 없으면
            nx,ny = x+ dirc[d][0]*-1,y + dirc[d][1]*-1 # 뒤로 후진
            if not in_range(nx,ny): # ? 
                break
            if grid[nx][ny] == 1: # 벽이면 
                break

            que.append((nx,ny))
        # print("que",que,cnt)    
    return cnt

grid[s_x][s_y] = 2
que.append((s_x,s_y))
print(bfs())
                