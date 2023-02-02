import sys

T = int(sys.stdin.readline())
  
def sol():
  answer =0
  N = int(sys.stdin.readline())
  arr = []
  for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))
  arr = sorted(arr)
  dic = {arr[0][0]:arr[0][1]}
  min = arr[0][1]
  for i in range(1,N):
    if min > arr[i][1]:#dic에 넣기
      dic[arr[i][0]] = arr[i][1]
      min = arr[i][1]
      
  return len(dic)


for _ in range(T):
  print(sol())