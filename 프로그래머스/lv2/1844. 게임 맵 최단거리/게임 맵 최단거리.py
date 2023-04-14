"""
상대 진영 파괴하면 이김
상대 진영에 빨리 도착
칸의 개수의 최소값
bfs는 거리가 같으면 최소값이다

"""
from collections import deque
# visited = []
        
def solution(maps):
    # global visited
    answer = 0
    # visited = [[False] *len(maps[0]) for _ in range(len(maps))]
    
    def in_range(x,y):
        return 0 <= x < len(maps) and 0<= y < len(maps[0])

    def bfs(x,y):
        q = deque([(x,y)])
        # visited[x][y] = True
        dxs = [-1,1,0,0]
        dys = [0,0,-1,1]

        while q:
            x,y = q.popleft()
            for dx,dy in zip(dxs,dys):
                nx,ny = x + dx, y + dy
                if not in_range(nx,ny):
                    continue
                if maps[nx][ny] == 0:
                    continue
                if maps[nx][ny] == 1:            
                    q.append((nx,ny))
                    maps[nx][ny] = maps[x][y] + 1
    

    bfs(0,0)

    answer = -1 if maps[len(maps)-1][len(maps[0])-1] == 1 else maps[len(maps)-1][len(maps[0])-1]
    return answer
    