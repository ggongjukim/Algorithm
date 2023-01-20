def solution(numbers):
  # numbers =[0,0,0,70]
  answer = ''
  dic = {}
  temp = list(map(str,numbers))
  for i in temp:
        if len(i) == 1:
            num = int(i*4)
        elif len(i) == 2:
            num = int(i*2)
        elif len(i) ==3:
            num = int(i+i[0])
        else:
            num = int(i)
            
        try :
            dic[i].append(num)
        except :
            dic[i] =[]
            dic[i].append(num)
        
  # print(dic)
  dic = sorted(dic.items(),key= lambda item: item[1],reverse=True)
    
  for k,v in dic:
    answer += str(k)*len(v)
  # print(answer)
  
  if int(answer) == 0:
        answer = '0'
    
  return answer