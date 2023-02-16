# 사과 1점부터 k점
# 사과 한상자의 가격 : 가장 낮은 점수 p * m
# 최대 이익을 계산
# 이익 발생 않는 경우 0 return
def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    # print(score)
    if len(score) < m:
        return 0
    for i in range(m-1,len(score),m):
        # print(i,score[i])
        answer += score[i] *m        
    return answer