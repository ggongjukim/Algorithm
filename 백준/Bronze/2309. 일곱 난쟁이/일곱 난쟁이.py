"""
합이 100 이 되게 하려면
visited 를 만들어서 넣었다 뺐다 하던지 
아니면 7개 넣는 재귀를 만들어서 하던
"""
arr = [ int(input()) for _ in range(9)]
# print(arr)
arr = sorted(arr, reverse = True)
# print(arr)
answer = []
isSolved = False
def real(array):
  return sum(array) == 100

def backtracking(cur_num):
  global isSolved
  if cur_num == 8:
    if real(answer) and not isSolved:
      temp = sorted(answer)
      isSolved = True
      for i in temp:
        print(i)
    return
  for i in range(len(arr)):
    if sum(answer) > 100:
      continue
    if len(answer) >= 1 and answer[-1] <= arr[i]:
      continue
    answer.append(arr[i])
    backtracking(cur_num + 1)
    answer.pop()

backtracking(1)