import heapq
N, K = map(int,input().split())
jws = [list(map(int,input().split())) for _ in range(N)]
bags = [ int(input()) for _ in range(K)]
jws = sorted(jws)
bags = sorted(bags)
# print(jws, bags)

s = 0
ans = 0
tmp = []
for bag in bags:
    # print("bag",bag)
    if s == N:
        ans += heapq.heappop(tmp) * -1 if tmp else 0
        continue
    for i in range(s,N):
        
        # print("i",i,jws[i])
        weight, cost = jws[i]
        if weight > bag:
            s = i
            # print("tmp",tmp)
            ans += heapq.heappop(tmp) * -1 if tmp else 0
            break # 다음가방

        heapq.heappush(tmp,cost*-1) # 가능한 애들 계속 추가
        if i == N-1:
            ans += heapq.heappop(tmp) * -1 if tmp else 0
            s = i + 1
print(ans)