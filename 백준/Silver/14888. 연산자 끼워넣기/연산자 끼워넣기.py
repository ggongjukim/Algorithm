"""
첫줄 수 개수
둘줄 수 배열
셋줄 사칙연산 개수
사칙연산에 대해 
"""
n = int(input())
num_arr = list(map(int,input().split()))
cal = list(map(int,input().split()))
cal_arr = []
max_num = -1000000000
min_num = 1000000000
for i in range(4):
  if i == 0:
    temp = '+'
  elif i == 1:
    temp = '-'
  elif i == 2:
    temp = '*'
  elif i == 3:
    temp = '//'
  cal_arr = cal_arr + [temp] * cal[i]

# print(cal_arr)
visited = [False] * len(cal_arr)

def print_cal():
  global max_num, min_num
  temp = num_arr[0]
  for i in range(1,len(num_arr)):
    if cal_ans[i-1] == "+":
      temp = temp + num_arr[i]
    elif cal_ans[i-1] == "-":
      temp = temp - num_arr[i]
    elif cal_ans[i-1] == "*":
      temp = temp * num_arr[i]
    elif cal_ans[i-1] == "//":
      if temp < 0 :
        temp *= -1
        temp = temp // num_arr[i]
        temp *= -1
      else:
        temp = temp // num_arr[i]
  # answer.append(temp)
  if temp > max_num:
    max_num = temp
  if temp < min_num:
    min_num = temp
  return
  
cal_ans =[]
def sol(cur_num):
  if cur_num == len(cal_arr):
    print_cal()
    return
  for i in range(len(cal_arr)):
    if visited[i]:
      continue
    cal_ans.append(cal_arr[i])
    visited[i] = True
    sol(cur_num+1)
    cal_ans.pop()
    visited[i] = False
sol(0)

print(max_num)
print(min_num)