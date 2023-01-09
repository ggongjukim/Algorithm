# 연결 요소의 개수
# 실버 2
# 첫줄 N M 정점 개수 간선 개수 (노드, 에지)
# 둘째줄~ M 개의 줄에 간선의 양 끝점 u v
# 출력 연결 요소의 개수
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N,M = list(map(int, input().split()))
graph = [[]for _ in range(N+1)]
visited = [False for _ in range(N+1)] 
visited[0] = True
stack =[]
result = []
count = 0
#print(graph)

for _  in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)
#print(graph)
#print(visited)

# visited 가 모두 true 일때까지
def DFS(current):
    result.append(current)
    visited[current] = True
    while len(result) != 0:
        current = result.pop()
        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                result.append(i)
    #print('result',result)

for i in range(N+1):
    if not visited[i]:
        count +=1
        DFS(i)
print(count)
