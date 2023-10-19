'''
감시

스타트링크
1번 2번 3번 4번 5번

0 빈칸
6 벽
1-5 cctv 번호

사각 지대의 최소 크기

백트래킹?
'''
from collections import deque
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
def show_grid():
    print("-------------------")
    for i in grid:
        print(i)

# show_grid()

def paint(c_x,c_y,d,B): # 1 이라 했을때
    tmp = []
    que = deque([])
    for i in d:
        que.append((c_x,c_y,i))
    # print("que",que)

    while que:
        x,y,d_ = que.popleft()
        
        for i in range(B):
            nx,ny = x+d_[0],y+d_[1]
            if not in_range(nx,ny):
                break
            if grid[nx][ny] == 6:
                break
            # print(nx,ny,grid[nx][ny])
            if grid[nx][ny] =='#':
                que.append((nx,ny,d_))
                continue
            if 1<= grid[nx][ny] <= 5 : # 건너뛰기
                que.append((nx,ny,d_))
                continue
            grid[nx][ny] = '#' # #이라고 하면 벽이랑 헷갈려서 안대
            tmp.append((nx,ny)) # 칠한 곳 찾기
            que.append((nx,ny,d_))
    return tmp


def count_zero():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                cnt += 1
    return cnt

def in_range(x,y):
    return 0<=x<N and 0<=y<M

ans = float('inf')
def back(cnt):
    global ans
    if cnt == origin_chk: # 감시 대상 범위 다 조사했다
        # show_grid()
        ans = min(ans, count_zero())
        return
    
    # 1 이라면
    # if not check:
        # return 
    c_x,c_y,dir = check[cnt]
    # for i in check:
        # c_x,c_y,dir = i
    if dir == 1:
        # 감시영역 칠하기
        d = ([(-1,0)],[(1,0)],[(0,-1)],[(0,1)])
        for j in range(4):
            tmp = paint(c_x,c_y,d[j],1)
            # show_grid()
            # 재귀
            back(cnt+1)
            # 되돌리기
            for i in range(len(tmp)):
                bx,by = tmp[i]
                grid[bx][by] = 0

    elif dir == 2:
        # 감시영역 칠하기
        d = (((-1,0),(1,0)),((0,-1),(0,1)))
        
        for j in range(2): # ((-1,0),(1,0))
            tmp = paint(c_x,c_y,d[j],2)
            # show_grid()
            # 재귀
            back(cnt+1)
            # 되돌리기
            for i in range(len(tmp)):
                bx,by = tmp[i]
                grid[bx][by] = 0

    elif dir == 3:
        # 감시영역 칠하기
        d = (((-1,0),(0,1)),((0,1),(1,0)),((1,0),(0,-1)),((0,-1),(-1,0)))
        
        for j in range(4): # ((-1,0),(1,0))
            tmp = paint(c_x,c_y,d[j],2)
            # show_grid()
            # 재귀
            back(cnt+1)
            # 되돌리기
            for i in range(len(tmp)):
                bx,by = tmp[i]
                grid[bx][by] = 0

    elif dir == 4:
        # 감시영역 칠하기
        d = (((0,-1),(-1,0),(0,1)),((-1,0),(0,1),(1,0)),((1,0),(0,-1),(0,1)),((0,-1),(-1,0),(1,0)))
        
        for j in range(4): # ((-1,0),(1,0))
            tmp = paint(c_x,c_y,d[j],3)
            # show_grid()
            # 재귀
            back(cnt+1)
            # 되돌리기
            for i in range(len(tmp)):
                bx,by = tmp[i]
                grid[bx][by] = 0
    
    elif dir == 5:
        # 감시영역 칠하기
        d = [[(0,-1),(-1,0),(0,1),(1,0)]]
        
        for j in range(1): # ((-1,0),(1,0))
            tmp = paint(c_x,c_y,d[j],4)
            # show_grid()
            # 재귀
            back(cnt+1)
            # 되돌리기
            for i in range(len(tmp)):
                bx,by = tmp[i]
                grid[bx][by] = 0

check = deque([])
origin_chk = 0
for i in range(N):
    for j in range(M):
        if 1 <= grid[i][j] <=5: # 1부터 5
            check.append((i,j,grid[i][j]))
            origin_chk += 1

# print("check",check)
back(0)
print(ans)
