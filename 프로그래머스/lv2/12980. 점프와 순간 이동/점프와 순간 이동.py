# now +k => 점프
# now*2 => 순간이동
# 건전지 사용량 : 순간이동 0, k점프 -k =>순간이동 더 효율적
# n으로 간다
# 점프 최소화 => 건전지 사용량의 최솟값
# 5    +1 1*2 2*2 +1
# 5    -1 2*2 2*1 -1
# 6    +1 1*2 +1 3*2
# 6    2*3 -1 2*1 -1
# 5000 +1 1*2 2*2 4*2 8*2 16*2 32*
# 5000 2*2500 2*1250 625*2 -1 624*2 312*2 156*2 78*2 39*2 -1 38*2 -1 18 
def solution(n):
    ans = 0
    while n !=0:
        if n%2 == 0:
            n = n//2
        else :
            n -=1
            ans +=1
    return ans