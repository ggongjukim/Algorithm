'''
N N 인 도시
빈칸 0
치킨집 2
집 1

도시 칸 (r,c)
r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서 부터 c번째 칸

r과 c 는 1부터 시작

치킨 매우 조아한다
치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
집을 기준으로 정해지며
각 집은 치킨 거리를 가지고 있다
도시의 치킨 거리 : 모든 집의 치킨 거리의 합

거리 r1r2 + c1c2

가장 수익을 많이 낼 수 있는 치킨집의 개수
최대 M

어떻게 고르면 도시의 치킨 거리가 가장 작게 될지

폐업시키지 않을 치킨집을 최대 M개 골랐을 때
도시 치킨 거리의 최솟값 출력


'''
import math
N,M = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(N)]
chick_arr = {}
home_arr = []
count = -1
## 치킨집 고르기
for i in range(N):
  for j in range(N):
    
    if grid[i][j] == 2:
      count += 1
      chick_arr[count] = [i,j]
    
    if grid[i][j] == 1:
      home_arr.append([i,j])
# print(chick_arr)
answer = []

def decode(arr):
  global answer
  tmp = []
  for i in arr:
    tmp.append(chick_arr[i])
#   print(tmp)

  tmp_answer = 0
  ## 치킨 거리 세기
  for i in home_arr: # 0 3
    x1,y1 = i
    dir = N + N
    for j in tmp: # 4 4
      x2,y2 = j
      dir = min(abs(x1-x2) + abs(y1-y2), dir)
    tmp_answer += dir
#   print('tmp_answer', tmp_answer)
  answer.append(tmp_answer)


arr = []
def back(cur_num):
  if cur_num == M:
    decode(arr)
    return

  for i in range(len(chick_arr)):
    if len(arr) > 0 and arr[-1] >= i:
      continue 
    arr.append(i)
    back(cur_num+1)
    arr.pop()
    
back(0)
print(min(answer))