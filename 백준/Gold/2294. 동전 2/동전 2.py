'''
n 가지 동전 
가치의 합이 k 원

동전 개수 최소
15
dp[i] = dp[i-1] + 1

4 = 2 + 2
2
15 = 12 + 1 + 1 + 1
   =  5 + 5 + 5
8 = 5 + 1 + 1 + 1

1 4
3
'''

n,k = map(int,input().split())
dp = [float("inf") for _ in range(k+1)]
check = []
for i in range(n):
    tmp = int(input())
    if tmp > k:
        continue
    check.append(tmp)
    dp[tmp] = 1
# print(dp)
check = sorted(check, reverse=True)

for i in range(1,k+1): # dp[10]
    if i in check: # 동전이면 pass 
        continue
    tmp = []
    for j in check: # 12 5 1
        # print("i-j", i-j, dp[i-j])
        if i-j < 0:
            continue
        if dp[i-j] != float("inf"): # 이전 값이 있으면
            tmp.append(dp[i-j]+1)
        # print(i, tmp)

        if len(tmp) > 0:
            dp[i] = min(dp[i], min(tmp))
            # dp[i] = min(dp[i], ans)
            
        # print(i,tmp)
    # print("--------------")
            
# print(dp)
print(dp[k] if dp[k] != float("inf") else -1)