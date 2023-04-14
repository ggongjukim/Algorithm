"""
네트워크
네트워크 갯수 리턴
"""
from collections import deque
def solution(n, computers): #0번 노트 부터 n-1 노드 까지
    answer = 0
    graph = [[] for _ in range(len(computers))]
    # print(graph)
    for i in range(len(computers)):
        for j in range(len(computers[0])):
            if i == j:
                continue
            # print(i,j,computers[i][j])

            if computers[i][j] == 1:
                graph[i].append(j)

    # for i in graph:
    #     print(i)
    visited = [ False for _ in range(len(computers))]
    def bfs(n):
        q = deque([n])
        visited[n] = True
        while q:
            n = q.popleft()
            
            for i in graph[n]: # 0 2
                if visited[i] == True:
                    continue
                visited[i] = True
                q.append(i)
    for i in range(len(computers)):
        if visited[i] == False:
            bfs(i)
            answer +=1
    # print(visited)
    return answer