'''
드래곤 커브는 세가지 속성으로 이루어짐
이차원 좌표 평면 위에서 정의
좌표 평면의 x축은 오른쪽 화살표 y축 아래쪽화살표

1. 시작점
2. 시작 방향
3. 세대

0세대 드래곤커브 길이 1인 선분 

0 0 시작 
방향 오른쪽
0세대

드래곤 커브 끝점 기준 => 끝점 : 시작점에서 선분 타고 이동시 가장 먼거리에 있는 점
방향 : 기존것 시계방향 90도 회전
1세대


0<=x<=100 0<=y<=100 만 유효한 좌표 => 마이너스는 안된다는겨?
입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다

0  1  2  3
오 위 왼 아래

입력 
첫줄 : 커브개수  N
둘줄 ~ : x y 시작점 , d 방향, g 세대

3
3 3 0 1
4 2 1 3
4 2 2 1

# K세대를 그리는 모듈 
    회전을 어뜨케하냐? 알고리즘을 어뜨케짜냐 ㅋㅋ.. . 앆!
# 네 점이 모두 드래곤 커브에 속하는 지 확인하는 모듈

시작점 -> d 방향으로 출발 // 0세대
끝점에서 통째로 90도 회전 // 0세대 
'''
N = int(input())
from collections import deque
# N = 1
onehundred = 100
grid = [[0 for _ in range(onehundred+1)] for _ in range(onehundred+1)]
def count_rec():
    ans = 0
    dxs = [0,1,1,0] 
    dys = [0,0,1,1]
    for x in range(onehundred): ## 99 99 까지만 검사하면댐
        for y in range(onehundred):
            cnt = 0 
            for dx,dy in zip(dxs,dys):
                nx , ny = x + dx, y + dy
                if grid[nx][ny] != 0:
                    cnt += 1
            if cnt == 4: # 4개가 모두 커브에 포함이 되어있으먄
                ans += 1

    return ans

def put_grid(arr):
    for i in arr:
        x,y = i
        grid[x][y] += 1

# 2 2 : 1 4 (1,-2) => 4 3(-2, -1)
# 2 2 : 2 4 (0,-2) => 4 2(-2, 0)
def make_curv(x,y,d,g):
    # 0 세대
    x,y = y,x
    grid[x][y] += 1 # 일단 시작점 += 1
    arr = []
    arr.append((x,y))
    dir = [(0,1),(-1,0),(0,-1),(1,0)] # 오 위 왼 아래
    arr.append((x + dir[d][0],y + dir[d][1]))

    for i in range(g): # 세대 만큼 반복
        mx,my = arr[-1] # 넣는 순서가 중요하다
        # arr에서 마지막 배열 빼고 90 회전해서  
        for a in range(len(arr)-2,-1,-1): # 꺼꾸로 집어넣기
            lx,ly = arr[a]
            dx, dy = mx- lx, my-ly
            dx, dy = dy,  dx*-1
            arr.append((mx- dx,my- dy))

    # print(arr)
    # grid에 숫자 채우기
    put_grid(arr)

for i in range(N):
    x,y,d,g = map(int,input().split())
    make_curv(x,y,d,g)

# for i in grid:
#     print(i)
print(count_rec())