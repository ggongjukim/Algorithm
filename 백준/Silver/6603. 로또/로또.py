"""
k k개수 만큼의 후보
여기서 6개 고르기
0 이 나오면 input 끝
중복 안됨
순서 상관 없음 => 조합
"""
k = -1
arr = []
visited = []

def printlotto(v):
  for i in range(k):
    if v[i]:
      print(arr[i], end=' ')
  print()

def sol(cnt,last_idx):
  if cnt == 6:
    printlotto(visited)
    return

  for i in range(last_idx+1,k):
    visited[i] = True
    sol(cnt+1,i)
    visited[i] = False


while True:
  temp = list(map(int,input().split()))
  k, arr = temp[0], temp[1:]
  if k == 0 :
    break
  visited = [False] * k
  
  for i in range(k):
    visited[i] = True
    sol(1,i)
    visited[i] = False

  print()