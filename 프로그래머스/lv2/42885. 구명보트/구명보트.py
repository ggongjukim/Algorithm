from collections import deque
def solution(people, limit):
    answer = 0
    people = sorted(people)
    que = deque(people)
    while len(que)>1:
        if que[0] + que[-1] <= limit:
            que.pop()
            que.popleft()
            answer +=1
        else:
            que.pop()
            answer +=1
        # print(people)
    if len(que) >0:
        answer+=1
    return answer