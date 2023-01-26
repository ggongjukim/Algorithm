import heapq
def solution(scoville, K):
    # scoville = [1,1]
    # K = 3
    answer = 0
    heapq.heapify(scoville)
    # m = heapq.heappop(scoville)
    # print("start",scoville)

    while scoville[0] < K:
        if len(scoville) == 1 :
            answer = -1
            break
        new = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        heapq.heappush(scoville, new)
        # print("heap",scoville)
        answer += 1
        # m = heapq.heappop(scoville)
        
        
    return answer