arr = []
idx = -1
answer = 0
def solution(word):
    global arr,answer
    answer = 0
    char = ['A', 'E', 'I', 'O', 'U']
    def check(array,w):
        temp = ''
        for i in array:
            temp += char[i]
        # print(temp,w,idx)
        return w == temp
    
    def sol(cur_num,w):
        global arr,idx,answer
        idx +=1 
        # print(arr, idx)
        
        if check(arr,w):
            answer = idx
            # print('check',idx,answer)
            return idx
        
        if cur_num == 5+1:
            return
        for i in range(5):
            # if len(arr) >= 1 and arr[-1] > i :
            #     continue
            arr.append(i)
            sol(cur_num + 1,w)
            arr.pop()
            
            
    sol(1,word)
    # print("ans",answer)
    
    return answer