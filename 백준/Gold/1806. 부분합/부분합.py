N,S = map(int,input().split())
arr = list(map(int,input().split()))
start, end = 0,0
tmp = arr[start]
ans = float('inf')
while True:
    # print("start,end", start,end,tmp)
    if start > len(arr)-1:
        break
    
    if tmp < S:
        if  end+1 > len(arr)-1:
            break
        end += 1 
        tmp += arr[end]
    else: # S 보다 크거나 같다 => 조건 만족
        # print("개수", end-start+1)
        ans = min(ans, end-start+1)
        tmp -= arr[start]
        start += 1
print(ans if ans != float('inf') else 0)