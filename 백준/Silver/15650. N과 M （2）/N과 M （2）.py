"""
n 이 3이면 1 2 3 중에 고르기
visited [f f f]
중복 안되고
오름차순
m 개의 개수만 뽑아야함
조합 순서 상관없음
"""
n,m = map(int,input().split())
visited = [False] * (n)

def sol(cnt,last_idx):
  # cnt 개 수를  뽑았고, 마지막 숫자 idx는  last_idx
  if cnt == m:
    # print(visited)
    for i in range(n):
      if visited[i]:
        print(i+1,end= ' ')
    print()
    return

  for i in range(last_idx+1, n):
    visited[i] = True
    sol(cnt+1,i)
    visited[i] = False

for i in range(n):
  visited[i] = True
  sol(1, i)
  visited[i] = False