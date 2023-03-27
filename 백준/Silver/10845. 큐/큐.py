import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
global que
que = deque()

def solution(order):
    # print('input', order, order == 'front')
    if order.find('push') == 0:
        x = order.split(' ')[1]
        # print("order,x",order,x)
        que.append(int(x))
        # print(que)
    elif order == 'front':
        if que:
            print(que[0])
        else:
            print(-1)

    elif order == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)

    elif order == 'size':
        print(len(que))
    elif order == 'empty':
        if que:
            print(0)
        else:
            print(1)
            
    elif order == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)



for _ in range(N):
    solution(str(sys.stdin.readline().rstrip()))
