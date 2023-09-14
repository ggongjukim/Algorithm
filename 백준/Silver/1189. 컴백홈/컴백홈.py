'''
한수 왼쪽 아래 
집   오른쪽 위
집에 돌아가는 방법 다양하다
한수가 집에 돌아갈 수 있는 모든 경우
T 는 못가는 부분
거리가 K인 가짓수
'''
from collections import deque
R,C,K = map(int,input().split())
grid = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
# que= deque([])
dxs =[-1,1,0,0]
dys =[0,0,1,-1]

def in_range(x,y):
    return 0<=x < R and 0<=y <C
ans = 0
def back(x,y,cnt):
    global ans
    if [x,y]==[0,C-1]:# 오른쪽 위면 return
        if cnt == K:
            ans += 1
        return
    
    for dx,dy in zip(dxs,dys):
        nx,ny = x+dx, y + dy
        if not in_range(nx,ny):
            continue
        if grid[nx][ny] == 'T':
            continue
        grid[nx][ny] = 'T'
        back(nx,ny,cnt+1)
        grid[nx][ny] = '.'

grid[R-1][0] = 'T'
back(R-1,0,1)
print(ans)