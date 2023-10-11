'''
농장에 울타리를 지어용
근처 농장 소가 안온다
화남

이웃 농장 소중 방문 가능한 소가 있지만
문은 하나고 긴 검문을 받는다
N마리의 소가 방문하러 왔다

소가 도착 시간과 검문 받는 시간은 소마다 다르다

5 7 8 12
'''
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)] 
# 2 1 / 5 7 / 8 3 => 2 5 8
# 2 1 / 2 2 / 2 3
# 2 3 / 3 5 / 5 8
# 2 5 / 5 10 / 10 18
# 1 1 / 2 1 / 2 1 / 2 1
# 1 2 / 2 3 / 3 4 / 4 5
arr = sorted(arr)
# print("arr",arr)
# 최대가 몇이지?
time = [0] * ((100 * 1000000)+1) # 가능해?..
start = arr[0][0] #2
end = start + arr[0][1] #3
# print("s,e",start,end)
for i in range(1,len(arr)):
    s,t = arr[i] # 5, 7
    if end < s: # 끝난시간보다 늦게옴
        start = s # 5
        end = start + t # 5 + 7
    elif end > s: # 2 2 / 3 6 // 5 12 / 8 3 
        start = end # 4 // 12
        end = start + t # 4 + 6 // 12 + 3
    else: # 2 1 / 3 4 // 1 2 / 2 1 => 
        end = s + t
        start = end
    # print(start, end) 
print(end)



