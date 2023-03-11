N = int(input())
arr = []

for _ in range(N):
    arr.append(int(input()))
dp = [-1] * (max(arr)+1)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(6,max(arr)+1):
    dp[i] = dp[i-1] +dp[i-5]

for i in arr:
    print(dp[i])