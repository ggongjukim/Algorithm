N = int(input())
dp = [float("inf")] * (N+1)
if N >= 2:
    dp[2] = 1 
if N>= 5: 
    dp[5] = 1

# 0 1 2 3 4 5 6 7 8 9
#     1     1
for i in range(1, N+1):
    tmp, tmp1 = i,i
    if i-5 >= 0:
        tmp = i-5 
    if i-2>= 0:    
        tmp1 = i-2
    dp[i] = min(dp[tmp1]+1, dp[tmp]+1, dp[i])
print(dp[N] if dp[N] != float("inf") else -1)