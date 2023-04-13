def sol(cnt,dungeons,k):
    global answer
    answer = max(answer, cnt)

    # if cnt == len(dungeons):
    #     answer = max(answer, cnt)
    #     # return
    # if cnt > answer:
    #     answer = cnt
    #     # return
        
    for i in range(len(dungeons)):
        if k < dungeons[i][0]:
            continue
        if visited[i]:
            continue
        visited[i] = 1
        sol(cnt+1, dungeons,k - dungeons[i][1])
        visited[i] = 0
    
answer = 0
visited= []

def solution(k, dungeons):
    global visited
    visited = [False] * len(dungeons)
    sol(0,dungeons,k)
    return answer