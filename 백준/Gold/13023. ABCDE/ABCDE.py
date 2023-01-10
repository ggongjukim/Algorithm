# A-B-C-D-E 관계 있는지 찾기
# 첫줄 N M 노드, 에지
# 둘째줄~ M 정수 a,b 에지
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N,M = list(map(int,input().split()))
graph = [[]for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a,b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
# print('graph',graph)

result =[False]
def DFS(num, depth):
    # print('num', num, graph[num])
    visited[num] = True
    if depth == 5 :
        result[0] = True
        return
    for i in graph[num]:
        if not visited[i]:
            DFS(i,depth+1)
    visited[num] = False

answer = 0
for i in range(N):
    # visited 초기화
    # visited = [False] * N
    DFS(i,1)
    if result[0] :
        answer =1 
        break
    # print(i, visited)

print(answer)