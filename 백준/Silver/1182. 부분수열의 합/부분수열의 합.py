"""
F F F F F
T 

"""
n,s = map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
visited = [False] * (n)
count = 0
def sol(cnt, last_idx, m):
  global visited,count
  if cnt == m:
    temp = 0
    for i in range(n):
      if visited[i]:
        temp += arr[i]
        # print(arr[i], end=' ')
    # print()
    if temp == s:
      count += 1
    # print(visited)
    return

  for i in range(last_idx + 1, n):
    visited[i] = True
    sol(cnt+1, i, m)
    visited[i] = False
    # sol(idx + 1)
for m in range(1,n+1): # 1개 부터 n개 까지  
  for i in range(n):
    visited[i] = True
    sol(1,i,m)
    visited[i] = False
print(count)