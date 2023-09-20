'''
1. 이 성에 있는 방의 개수
2. 가장 넓은 방의 넓이
3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방 크기

N M
M 개 줄 정수로 벽에 대한 정보

서쪽 벽 1 L
북쪽 벽 2 U
동쪽 벽 4 R
남쪽 벽 8 D
1 
2
4 
8
1 2 => 3
1 4 => 5
1 8 => 9
2 4 => 6
2 8 => 10
4 8 => 12
1 2 4 => 7
1 2 8 => 11
1 4 8 => 13
2 4 8 => 14
1 2 4 8 => 15
# 테두리에 위치한 노드는 벽이 있다
'''
from collections import deque
M,N = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
que = deque([])
dic = { # 갈 수 있는 곳 상하좌우 북2 /남8 /서1/ 동4 # 15  #1 2 4 8 서 북 동 남 / 좌 상 우 하
    '0' : [1,1,1,1],
    '1' : [0,1,1,1],
    '2' : [1,0,1,1],
    '4' : [1,1,0,1],
    '8' : [1,1,1,0],
    '3' : [0,0,1,1],
    '5' : [0,1,0,1],
    '9' : [0,1,1,0],
    '6' : [1,0,0,1],
    '10': [1,0,1,0],
    '12': [1,1,0,0],
    '7' : [0,0,0,1],
    '11' : [0,0,1,0],
    '13' : [0,1,0,0],
    '14' : [1,0,0,0],
    '15' : [0,0,0,0]
}

def in_range(x,y):
    return 0<= x < N and 0<=y <M
def bfs():
    cnt = 1
    while que:
        x,y = que.popleft()
        dir = [(0,-1),(-1,0),(0,1),(1,0)]
        for i in range(4):
            tmp = str(grid[x][y]) # '11'
            way = dic[tmp] # [0,0,1,0]
            if way[i] == 0: # 막혀있음 갈수 없음
                continue 

            dx ,dy = dir[i]
            nx,ny = x+ dx, y + dy
            if not in_range(nx,ny):
                continue
            if visited[nx][ny] != -1:
                continue

            visited[nx][ny] = idx
            que.append((nx,ny))
            cnt += 1
    return cnt
answer = []
idx = 0 # 영역의 인덱스
for i in range(N):
    for j in range(M):
        if visited[i][j] != -1:
            continue
        visited[i][j] = idx
        que = deque([(i,j)])
        tmp = bfs()
        answer.append(tmp) # 영역 개수
        idx += 1

# for i in visited:
    # print(i)

# print(answer)
print(len(answer)) # 1. 영역의 개수
print(max(answer)) # 2. 가장 넓은 방 넓이

visited2 = [[0 for _ in range(M)] for _ in range(N)]
maxcount = 0
for x in range(N):
    for y in range(M):
        if visited2[x][y] == 1:
            continue

        dxs = [-1,1,0,0]
        dys = [0,0,-1,1]
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if not in_range(nx,ny):
                continue
            if visited[x][y] == visited[nx][ny] : # 같은 영역이면
                continue
            if visited2[nx][ny] == 1:
                continue
            temp = answer[visited[x][y]] + answer[visited[nx][ny]]
            maxcount = max(maxcount,temp)
            visited2[x][y] = 1
print(maxcount)