'''
N개의 아파트, 일부 아파트 옥상 기지국 설치
4g -> 5g
5g 전달범위 4g 보다 좁음 => 전달 안되는 아파트 존재

N 아파트 배열
stations 기지국 위치
W 전달 범위

겹치는 부분 어떻게?

5 [3] 2 0 o
6 [3] 2 1 o
16 [1, 16] 2 2 => 해결
6 [4] 2 1 o
11 [1, 4] 1 2 => 해결
11 [1, 5] 1 3
5 [1, 2, 3, 4, 5] 0
200000000 [100000000] 5 18181818 o
'''
import math
def solution(n, stations, w):
    # n = 11
    # stations = [1,4]
    # w = 1
    
    answer = 0
    top = []
    
    
    for i in stations:
        start, end = i-w, i+w
        if start <= 1:
            start = 1
        if end >= n:
            end = n
        top.append((start,end))
        
    answer = 0
    scope = w*2 +1
    for i in range(len(top)):
        start,end = top[i]
        # print(start,end)
        if i == 0: # 첫번째 top 이면 0 칸의 개수는
            tmp = start-1
            answer += math.ceil(tmp/scope) 
        else:
            b_start,b_end = top[i-1]
            # if start <= b_end : # 범위가 겹치는 경우
                # continue
            tmp = start - b_end - 1
            answer += math.ceil(tmp/scope) 
            # print('semi answer', answer)
        
        if i == len(top)-1: #마지막 탑의 경우 => 뒷처리
            tmp = n - end
            answer += math.ceil(tmp/scope) 
            
        # print('answer',answer)
            
        
        
    
        
    return answer