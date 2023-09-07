# 아래 오 위 왼 
N = int(input())
check = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]

num = N*N

def in_range(x,y):
    return 0<= x < N and 0<= y < N

dir_num = 0
grid[0][0] = num
x,y = 0,0
while num > 1:
    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    nx, ny = x + dir[dir_num][0] , y + dir[dir_num][1]
    if not in_range(nx,ny):
        dir_num += 1
        if dir_num > 3: # 다시 0번으로 
            dir_num = 0
            
    elif grid[nx][ny] != 0:
        dir_num += 1
        if dir_num > 3: # 다시 0번으로 
            dir_num = 0
    
    x, y = x + dir[dir_num][0] , y + dir[dir_num][1]
   
    num -= 1
    grid[x][y] = num

for i in grid:
    for j in i:
        print(j,end=' ')
    print()

for i in range(N):
    for j in range(N):
        if grid[i][j] == check:
            print(i+1, j+1)