def solution(dirs):
    answer = 0
    start = [0,0]
    way = [[0,0]]
    road = {}
    for num,i in enumerate(dirs):
        if i == "U":
            end = [way[-1][0],way[-1][1]+1]
        elif i =="D":
            end = [way[-1][0],way[-1][1]-1]
        elif i =="R":
            end = [way[-1][0]+1,way[-1][1]]
        elif i =="L":
            end = [way[-1][0]-1,way[-1][1]]
        #범위 내인지 확인
        if not(end[0] >= -5 and end[0]<=5 and end[1] >=-5 and end[1] <=5):
            continue
        
        # print("now", num+1,str(end) in road,way[-1],end,road)
#         #지나간 길인지 확인 start -> end
        if str(end) in road and way[-1] in road[str(end)]: # 지나간 점이고 지나간 길이면
            # print("\n지나간길",road, "\n")
            way.append(end)
            continue            
        
#         #반대쪽도 지나간 길인지 확인
        # print("now", num+1,str(way[-1]) in road,way[-1],end,road)
        if str(way[-1]) in road and end in road[str(way[-1])]:
            # print("지나간길")
            way.append(end)
            continue
        
        try: road[str(way[-1])].append(end)
        except: road[str(way[-1])] = [end]
        
        try: road[str(end)].append(way[-1])
        except: road[str(end)] = [way[-1]]
        way.append(end)
        
    # print(num+1,"way",way,"\n",road)
    answer = road.values()
    # print("answer",answer)
    count = 0
    for i in answer:
        count += len(i)
    return count//2