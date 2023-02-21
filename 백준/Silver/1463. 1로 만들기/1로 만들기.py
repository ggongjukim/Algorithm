N = int(input())
dp =[0,0]

for i in range(2,N+1): 
    dp.append(dp[i-1]+1) # 일단 -1 연산 한거 넣어주고
    if i%2== 0: 
        dp[i] = min([dp[i], dp[i//2]+1]) # 연산 -1 한거랑 비교 
    if i%3 == 0 : 
        dp[i] = min([dp[i],dp[i//3]+1]) # 6의 배수라도 앞에서 2로 나눈 연산값과 최소 비교를 하기 때문에 상관없다 단, elif 로 하면 안된다
print(dp[N])