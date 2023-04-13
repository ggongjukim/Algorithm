"""
트리를 잘라서 네트워크를 두개로 분할
두 전력망이 갖게되는 송전탑 개수 최대한 비슷하게
전선중 하나를 끊어서 가능한 비슷하도록 
백트래킹으로 할 수 있나? 

"""
from collections import deque
def bfs(start_idx,g):
    # print("g",g)
    visited = [False] * (len(g))
    visited[start_idx] = True
    q = deque([start_idx])
    while q:
        temp = q.popleft()
        for i in g[temp]:
            if visited[i]:
                continue
            q.append(i)
            visited[i] = True
    # print("visited",visited)
    return visited.count(True)
    
def sol(edge, g): # [1,3]
    g[edge[0]].remove(edge[1])
    g[edge[1]].remove(edge[0])
    
    # tmp = bfs(edge[0],g)
    tmp = abs(bfs(edge[0],g) - bfs(edge[1],g))
    # print(edge, tmp)
    g[edge[0]].append(edge[1])
    g[edge[1]].append(edge[0])
    return tmp
    
def solution(n, wires):
    answer = 101
    graph = [[] for i in range(n+1)]
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    # print(sol(wires[0],graph))
    for i in wires:
        answer = min(answer,sol(i,graph))
    
    return answer