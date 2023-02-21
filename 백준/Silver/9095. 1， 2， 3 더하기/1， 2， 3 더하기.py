
N = int(input())
test = []
for _ in range(N):
    test.append(int(input()))
dp = [-1] * (max(test)+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,len(dp)):
    dp[i] = dp[i-1]+ dp[i-2] + dp[i-3]

for i in test:
    print(dp[i])