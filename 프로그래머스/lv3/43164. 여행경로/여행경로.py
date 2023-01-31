# 다시 방문 가능하다는 특징? 이있음
def solution(tickets):
    answer = []
    graph = {}
    tickets = sorted(tickets,reverse=True)
    # print(tickets)
    for i in tickets:
        try :graph[i[0]].append(i[1])
        except : graph[i[0]] = [i[1]] 
    # print(graph)
    stack = ["ICN"]
    path = []
    
    while len(stack)>0:
        top = stack[-1]
        if top not in graph or len(graph[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(graph[top].pop())
    return path[::-1]