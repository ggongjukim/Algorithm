def solution(today, terms, privacies):
    
    answer = []
    # 전처리
    due = {}
    for i in terms:
        name, term = i.split(' ')
        due[name] = int(term)
    # print(due)
    
    duedate =[]
    for i in privacies:
        date, name = i.split(' ')
        y,m,d = map(int, date.split('.'))
        # print(y,m,d)
        # 각각의 duedate 구하기
        term = due[name]
        if term >= 12: term = [term//12,term%12,-1]
        else: term = [0,term,-1]
        
        #년도 구하기 
        temp = [y+term[0],m+term[1],d+term[2]]
        # 정리하기
        if temp[1] >= 13:
            temp[0]+=1
            temp[1] -= 12
        if temp[2] <=0:
            temp[1] -= 1
            temp[2] += 28
            if temp[1] >= 13: # 한번더
                temp[0]+=1
                temp[1] -= 12
        duedate.append([str(temp[0]),str(temp[1]).zfill(2),str(temp[2]).zfill(2)])
    # print(duedate, today)
    today = today.split('.')
    today = ''.join(today)
    # print(today)
    for idx,i in enumerate(duedate):
        if int(today) > int(''.join(i)):
            answer.append(idx+1)
         
            
    return answer