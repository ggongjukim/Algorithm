
from collections import deque
n = int(input())
start, end = map(int,input().split())
edge = int(input())
graph = [[] for i in range(n+1)]

for _ in range(edge):
  s,e = map(int,input().split())
  graph[s].append(e)
  graph[e].append(s)
# print(graph)
visited = [ -1 for i in range(n+1)]

def bfs(n):
  q = deque([n])
  visited[n] = 0
  
  while q:
    n = q.popleft()
    for i in graph[n]:
      if visited[i] != -1:
        continue
      visited[i] = visited[n] + 1
      q.append(i)

  return visited[end]
print(bfs(start))