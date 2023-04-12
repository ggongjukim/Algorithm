"""
K 중에 하나 뽑는 행위를 N 번하기
N 개중에 M개 뽑기
"""
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
answer = 0

def sol(cur_num, cnt_broken):
  global answer
  if cur_num == n:
    answer = max(answer, cnt_broken)
    return
    
  if arr[cur_num][0] <= 0: # 현재 계란이 깨져있다면 => 다음계란
    sol(cur_num + 1, cnt_broken)
    return

  flag = False
  for i in range(n):
    if arr[i][0] <= 0: # 계란이 깨져있다면 => 다음계란으
      continue
    if i == cur_num:
      continue
    flag = True
    arr[cur_num][0] -= arr[i][1]
    arr[i][0] -= arr[cur_num][1]
    sol(cur_num + 1 , cnt_broken + int(arr[cur_num][0] <= 0) + int(arr[i][0] <= 0))
    arr[cur_num][0] += arr[i][1]
    arr[i][0] += arr[cur_num][1]
  if flag == False:
    sol(cur_num+1, cnt_broken)

sol(0,0)
print(answer)
      