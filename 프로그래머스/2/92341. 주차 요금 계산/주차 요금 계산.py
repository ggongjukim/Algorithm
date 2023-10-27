'''
입차 출차 
입차 입차 출차 이런건 없는거지?

'''
import math
def solution(fees, records):
    answer = []
    b_time, b_fee, per_time, per_fee = fees
    dic = {}
    dic2 = {}
    for i in records:
        t, num, move = i.split()
        
        # print(t,num,move)
        if num in dic.keys():
            dic[num].append((t,move))
        else:
            dic[num] = [(t,move)]
            
    # 번호 - 주차시간 딕셔너리 초기화        
    for i in dic.keys():
        dic2[i] = 0
        # dic2[i] = []
    # print(dic)

    for k in dic.keys():   
        s = len(dic[k])-1 # 뒤에서 부터 시작
        time = 0
        # print("k",k, "s", s, "dic[k][s][1]",dic[k][s][1])

        while s >= 0:
            if dic[k][s][1] == 'OUT': # 마지막이 출차기록이면
                out_time = dic[k][s][0]
                in_time = dic[k][s-1][0]
                s -= 2

            else:
                out_time = '23:59'
                in_time = dic[k][s][0] # 18:59
                s -= 1
            oh,om = map(int,out_time.split(':'))
            ih,im = map(int,in_time.split(':'))
            time += oh*60 + om - (ih*60 + im)
            # print("time",oh*60 + om - (ih*60 + im))
            # s -= 2
            
        dic2[k] = time
        # dic2[k].append(time)
        
    # print(dic2)
    dic2 = sorted(dic2.items(), key = lambda x: x[0])
    # print("dic2",dic2)
    
    for i in dic2:
        no, t = i
        if t <= b_time:
            tmp = b_fee
        else:
            # print("(t- b_time)",no, (t- b_time))
            # print("")
            tmp =  b_fee + math.ceil((t- b_time) /per_time)* per_fee
        answer.append(tmp)
    # print(answer)
    return answer