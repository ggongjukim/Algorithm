from collections import deque
def solution(number, k):
    # number= "4321"
    # k = 1
    answer = ''
    que = deque(number)
    arr = []
    while len(que)> 0: # 4 1 7 7 2 5 2 8 4 1
        current = int(que.popleft())
        # 검사
        while len(arr) > 0 and current > arr[-1]:
            if k == 0 :
                break
            arr.pop()
            k -=1

        arr.append(current)
    while k != 0 :
        arr.pop()
        k -=1
    
    arr = list(map(str,arr))
    answer = ''.join(arr)
    return answer