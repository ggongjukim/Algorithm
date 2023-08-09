'''
수행해야할 작업 N개

각 작업마다 걸리는 시간 정수로 주어임

몇 작업 사이에는 선행관계
어떤 작업 수행하기 위해 반드시 먼저 완료되어야할 작업들

K번 작업에 대해 선행 관계에 있는 작업들의 번호 1이상 k-1 이하

첫줄 N
두번째 줄 ~ N+1 
1번 작업 걸리는 시간, 그 작업에 대해 선행 관계에 있는 작업들의 개수, 선행 관계 작업 번호

'''
N = int(input())
arr = [[] for _ in range(N+1)]
time = [0 for _ in range(N+1)]
for i in range(1,N+1):
    tmp = list(map(int,input().split()))
    if tmp[1] == 0:
        arr[i] = [tmp[0]]
    else:
        arr[i] = [tmp[0], tmp[1:]]
    # time[i] = tmp[0]

# for i in arr:
#     print(i)

for i in range(1,len(arr)):
    temp = 0
    if len(arr[i]) > 1 : 
        for j in arr[i][1]:
            temp = max(temp, arr[j][0])
    # print('arr',arr)
    arr[i][0] += temp
    # print(arr)
arr[0].append(0)
arr = sorted(arr, key = lambda x : (-x[0]))
print(arr[0][0])