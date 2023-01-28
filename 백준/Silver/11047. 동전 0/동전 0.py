N, K = map(int,input().split())
coin =[]
count =0
for _ in range(N):
    coin.append(int(input()))
coin = sorted(coin)
while K > 0:
    now = coin.pop()
    if now > K:
        pass
    else:
       count += (K//now)
       K = K - (K//now)*now
    # print(now, K, count)
print(count)