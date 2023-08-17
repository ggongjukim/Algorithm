'''
지훈 미로 탈출
미로에서의 지훈 위치와 불이 붙은 위치 감안
지훈이가 불 타기 전에 탈출 할 수 있는지의 여부, 얼마나 빨리탈출

지훈 수평 수직 이동
불 각 지점에서 네방향으로 확산

지훈이는 미로 가장자리에 접한 공간에서 탈출 가능
벽있는 공간 통과 불가

[입력]
R C
R 행 개수
C 열 개수

탈출 불가 : IMPOSSIBLE
가장 빠른 탈출 시간

# 불 확산
# 한칸씩 이동 ..?

# j 가 지나간 길은 어떻게?
'''
from collections import deque
N,M = map(int,input().split())
grid = [list(input()) for _ in range(N)]
que = deque([])
fque = deque([])
visited  = [ [0 for _ in range(M)] for _ in range(N)]
fvisited  = [ [0 for _ in range(M)] for _ in range(N)]
dxs = [-1,1,0,0]
dys = [0,0,-1,1]

def printgrid():
    for i in range(N):
        print(grid[i])
    for i in range(N):
        print(visited[i])
    print('-----------')
    for i in range(N):
        print(fvisited[i])

# printgrid()

def fbfs():
    while fque:
        x,y, step = fque.popleft()

        for dx,dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(nx,ny):
                continue
                
            if grid[nx][ny] == '#':
                continue
            
            if fvisited[nx][ny] != 0:
                continue

            fvisited[nx][ny] = step + 1
            fque.append([nx,ny, step + 1])
            # print('fque', fque)
            # for i in range(N):
            #     print(fvisited[i])


def in_range(x,y):
    return 0 <= x < N and 0<= y < M

def bfs():
    while que:
        x,y, step = que.popleft()

        for dx,dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not in_range(nx,ny):
                continue
                
            if grid[nx][ny] == 'F' or grid[nx][ny] == '#':
                continue
            
            if visited[nx][ny] != 0:
                continue

            visited[nx][ny] = step + 1
            que.append([nx,ny, step + 1])
            # print('que', que)

# j 찾기
jx,jy = [-1,-1]
for i in range(N):
    for j in range(M):
        if grid[i][j] == 'J':
            jx,jy = [i,j]
        if grid[i][j] == 'F':
            fque.append([i,j,1])

visited[jx][jy] = 1
que.append([jx,jy,1])
bfs()

if fque:
    fx,fy,s = fque.popleft()
    fvisited[fx][fy] = 1
    fque.append([fx,fy,1])
    fbfs()
# printgrid()

answer = []
for i in range(N):
    for j in range(M):
        if i == 0 or i == N-1 or j == 0 or j == M-1:
            # print('temp', visited[i][j])
            if visited[i][j] != 0: 
                if visited[i][j] < fvisited[i][j]:
                    answer.append(visited[i][j])
                if fvisited[i][j] == 0:
                    answer.append(visited[i][j])

# print(answer)
if len(answer) > 0:
    print(min(answer))
else:
    print('IMPOSSIBLE')

'''
5 4
####
#...
#.##
#.J#
####
'''