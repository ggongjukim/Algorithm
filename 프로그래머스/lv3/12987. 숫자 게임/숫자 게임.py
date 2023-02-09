import heapq
def solution(A, B):
    answer = 0
    A = [-1*i for i in A]
    B = [-1*i for i in B]
    heapq.heapify(A)
    heapq.heapify(B)
    while A and B:
        bigA = heapq.heappop(A)
        bigB = heapq.heappop(B)
        if -1*bigA < -1*bigB:
            answer +=1
        else:
            heapq.heappush(B,bigB)
    return answer