# 선행스킬 : 스킬 전에 배우는 스킬
# 순서!
# skill에 없는 스킬은 아무때나 가능
# 가능한 개수
# 이중 포문 긔?
# visited 있어야함
# graph를 만들어주자!?
# 중복도 있나??? BDB 이렇게?
from collections import deque
def solution(skill, skill_trees):
    answer=len(skill_trees)
    gskill = {}
    for i in range(len(skill)-1):
        gskill[skill[i]] = skill[i+1]
    while skill_trees:
        check = list(skill_trees.pop())
        temp = check[:]
        for i in range(len(check)):
            if check[i] not in skill:
                temp.remove(check[i])                
        check = temp[:]
        for i in range(len(check)):
            if check[i] == skill[i]:
                pass
            else:
                answer -=1
                break
            
        
    return answer