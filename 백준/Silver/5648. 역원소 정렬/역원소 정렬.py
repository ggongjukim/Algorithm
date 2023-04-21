from collections import deque
temp = deque(list(map(int,input().split())))
n = temp.popleft()
temp = list(temp)
arr = temp[:]
while True:
  if len(arr) >= n:
    # print(arr)
    break
  arr += list(map(int,input().split()))
  # print(arr)

def change(num):
  # print("change",num)
  temp = list(str(num))
  ans = [ temp[i] for i in range(len(temp)-1,-1,-1)]
  # print("ans",ans)
  return int(''.join(ans))
  
for i in range(n):
  arr[i] = change(arr[i])
arr = sorted(arr)
for i in arr:
  print(i)