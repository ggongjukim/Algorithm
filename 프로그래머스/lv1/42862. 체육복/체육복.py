def solution(n, lost, reserve):
    answer = 0
    arr = [1 for i in range(0,n+2)]
    arr[0] = 0
    arr[n+1] = 0
    # print(arr)
    for i in reserve:
        arr[i] +=1
    # print(arr)
    for i in lost:
        arr[i] -=1
    # print(arr)

    for i in range(1,n+1):
        if arr[i] == 2 and arr[i+1]==0 :
            arr[i] -=1
            arr[i+1] +=1
        if arr[i]== 0 and arr[i+1]==2:
            arr[i] +=1
            arr[i+1] -=1
    arr[n+1] = 0
    # print(arr)
    for i in arr:
        if i >= 1:
            answer +=1
    return answer