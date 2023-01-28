N = int(input())
arr = []
for _ in range(N):
    now = int(input())
    if now ==0:
        if len(arr) == 0:            
            arr.append(now)
        else:
            arr.pop() 
    else:
        arr.append(now)

print(sum(arr))
