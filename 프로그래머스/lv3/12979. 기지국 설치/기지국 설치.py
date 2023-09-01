import math
# 투포인터...?
def solution(n, stations, w):
    answer = 0
    s = 0 
    ran = w*2+1
    for i in stations:
        
        e = (i-1)-(w)-1
        # print(s,e)
        answer += math.ceil((e-s+1)/ran)
        s = (i-1)+w+1
    
    # 끝이 처리가 안되어있는 경우
    if not (n-1 >= stations[-1] - 1 -w and n-1 <= stations[-1] -1 +w):
        e = n-1
        answer +=  math.ceil((e-s+1)/ran)
    return answer