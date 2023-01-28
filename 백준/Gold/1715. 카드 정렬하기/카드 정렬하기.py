# 정렬된 두 묶음의 숫자 A, B
# 힙?
import heapq
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
heapq.heapify(arr)

count = 0
while len(arr)>1:
    now = heapq.heappop(arr) + heapq.heappop(arr)
    heapq.heappush(arr,now)
    count += now
    # print(arr)

print(count)