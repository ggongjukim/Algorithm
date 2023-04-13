"""
n개니까 한줄에 하나식 들어가야함
아이디어가 중요함
grid 인덱스로 규칙을 찾을 수있음
"""
n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]
answer = 0
v_col = [0 for _ in range(n)] # 열 에 대한 검사
v_2 = [0]*(2*n)
v_3 = [0]*(2*n)

def sol(cur_row):
  global answer
  if cur_row == n:
    answer +=1
    return
    
  for y in range(n):
    if v_col[y] == v_2[cur_row + y] == v_3[cur_row - y] == 0:
      v_col[y] = v_2[cur_row + y] = v_3[cur_row - y] = 1
      sol(cur_row +1)
      v_col[y] = v_2[cur_row + y] = v_3[cur_row - y] = 0          


sol(0)  
print(answer)