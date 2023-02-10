# # row H column W
# # 최대공약수? 
# import math
# import sys
# def solution(w,h):
#     w,h = 5,3
#     answer = 1
#     gcd = math.gcd(w,h) # 최대공약수 36
#     lcm = gcd * w//gcd * h//gcd
#     dw, dh = lcm//w, lcm//h # 2 3
#     line = 0 # 라인이 지나는 칸의 개수
#     beforey = 0 # 라인의 y값
#     for i in range(1,dw+1):
#         y = dh/dw * i
#         line +=  math.ceil(y)- beforey
#         beforey = math.floor(y)
#     answer = w*h - (line * gcd)
#     return answer

import math
def solution(w,h):
    return (w*h)-(w+h-math.gcd(w,h))