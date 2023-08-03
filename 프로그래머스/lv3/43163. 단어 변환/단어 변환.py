'''
begin -> target 가장 짧은 변환 과정
words
인접행렬로 1단어씩 다른 거 인접 행렬로 만들기 
BFS 구하깅 => 최단거리 
'''

from collections import deque
que = deque([])
def solution(begin, target, words):
    answer = 0
    grid = {} # grid = {hot : [], dot : [] ..}
    visited = {}
    words.append(begin)
    
    for i in words:
        grid[i] = []
        visited[i] = False
    
    
    for key, val  in grid.items(): # key : hot
        # print('key', key)
        for i in words: # dot
            cnt = 0
            if key == i: # 같은 글자는 패스
                continue
                
            tmp = key    
            for ch in i: # d o t
                if ch in tmp: # 여기 문제
                    # print('걸림')
                    cnt += 1
                    tmp = tmp.replace(ch,'',1)
                    # print(ch,tmp)
            if cnt == len(begin) - 1:
                val.append(i)
    # print('grid',grid)       
    # print('visited',visited)
    def BFS():
        
        
        while que:
            start,cnt = que.popleft()
            if start == target:
                return cnt

            for i in grid[start]:

                if visited[i] == True:
                    continue

                que.append([i, cnt + 1])
                visited[i] = True
                
            

            # print('que',que)       
            # print('visited',visited)   
            # print('cnt', cnt)
            # print('---------------------')
        return 0
    
    visited[begin] == True
    que.append([begin,0])
    # BFS()
    test = BFS()
    # if test == null:
        # test = 0
    answer = test
    return answer