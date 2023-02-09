# 부서별로 물품 구배에 필요 금액 조사
# 합? 그걸로 풀어야대나?

def solution(d, budget):
    answer = 0
    d = sorted(d,reverse=True) # 5 4 3 2 1
    while budget >0:       
        if not d:
            break
        budget -= d.pop()
        if budget >=0:
            answer+=1
    return answer