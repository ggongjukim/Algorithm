from collections import deque
def solution(rows, columns, queries):
    # if rows == 100 : return 
    answer = []
    arr = [[i+(j-1)*columns for i in range(1,columns+1)]for j in range(1,rows+1)]
    # print(arr)
    queries = deque(queries)
    while queries:
        now = queries.popleft()
        change =[]
        s, e = now[:2], now[2:]
        s = [s[0]-1, s[1]-1]
        e = [e[0]-1, e[1]-1]
        start = arr[s[0]][s[1]]
        
        # print("s e", s, e)

        for i in range(s[0],e[0]): # 위로 이동
            change.append(arr[i][s[1]])
            arr[i][s[1]] = arr[i+1][s[1]]
            # print("a", change)
            
        for i in range(s[1],e[1]): # 왼쪽으로 이동
            change.append(arr[e[0]][i])
            arr[e[0]][i] = arr[e[0]][i+1]   
            # print("c",change)
        
        for i in range(e[0],s[0],-1): # 아래로 이동
            change.append(arr[i][e[1]])
            arr[i][e[1]] = arr[i-1][e[1]] 
            # print("b", change)
        
            
        for i in range(e[1],s[1],-1): # 오른쪽 이동
            change.append(arr[s[0]][i])
            arr[s[0]][i] = arr[s[0]][i-1]
            if i == s[1]+1:
                arr[s[0]][i] = start
            # print("d",change)

                 
        
        # print(arr)
        answer.append(min(change))
    return answer