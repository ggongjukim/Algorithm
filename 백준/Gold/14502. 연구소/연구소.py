'''
# 14502

# 연구소 벽 세우기
# N * M
# 0 빈칸
# 1 벽
# 2 바이러스

# 바이러스 => 상하좌우 전염

# 3개의 벽을 세울 수 있음
안정영역 크기의 최댓값

# 그리드 출력

# 전염 지역 찾기 => DFS BFS
# 전염 아닌 지역 
# 바이러스 퍼지는 순서 상관없나? 
'''
from collections import deque

N, M = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(N)]
copy_grid = [[-1 for _ in range(M)] for _ in range(N)]
que = deque([])
visited = [[0 for _ in range(M)] for _ in range(N)]
virus = []
zero = []
answer = 0

def printgrid():
  for i in copy_grid:
    print(i)
  print()
  for i in visited:
    print(i)


def copygrid():  # 복제하는 역할
  global visited
  for i in range(N):
    for j in range(M):
      copy_grid[i][j] = grid[i][j]
  visited = [[0 for _ in range(M)] for _ in range(N)]

def in_range(x, y):
  return 0 <= x < N and 0 <= y < M


def BFS():

  while len(que) != 0:
    x, y = que.popleft()

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
      nx, ny = x + dx, y + dy

      if in_range(nx, ny) == False:
        continue
      if copy_grid[nx][ny] != 0:  #빈칸이 아니면
        continue
      if visited[nx][ny] == 1:
        continue

      # print('통과',nx,ny)
      que.append([nx, ny])
      copy_grid[nx][ny] = 2
      visited[nx][ny] = 1


def getoriginvirus():
  for i in range(N):
    for j in range(M):
      if grid[i][j] == 2:
        virus.append([i, j])
      if grid[i][j] == 0:
        zero.append([i, j])


copygrid()
getoriginvirus()

test = []


def searchempty(test_grid): # BFS 돌려보고 마지막에 0 세기
  result = 0
  for i in range(N):
    for j in range(M):
      if test_grid[i][j] == 0:
        result += 1
  # print('result', result)
  return result


def rock(test): # 벽돌 세개 세우기 
  global answer
  copygrid()
  for i in test:  # 벽돌 쌓기
    x, y = i
    copy_grid[x][y] = 1

  for v in virus:
    x, y = v

    que.append([x, y])
    visited[x][y] = 1
    BFS()

  # printgrid()
  answer = max(answer, searchempty(copy_grid))
  # print('answer', answer)


# rock([[1,0],[0,1],[3,5]])


def back(num): # 백트래킹
  if num == 3:
    # print(test)
    # rock(test)
    temp = [zero[test[0]], zero[test[1]],zero[test[2]]]
    # print(temp)
    rock(temp)
    # if [1,0] in temp and [0,1] in temp and [3,5] in temp:
    #   print("찾음")
    return

  for i, val in enumerate(zero):

    if len(test) > 0:
      if test[-1] >= i:
        continue
    test.append(i)
    back(num + 1)
    test.pop()


back(0)
print(answer)