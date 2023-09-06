'''
NN 지도
각 칸에 그 높이 적혀 있음

이 지도에서 지나갈 수 있는 길이 몇개인지

길 : 한 행 또는 한 열 전부

길에 속한 모든 칸 높이 같아야한다
경사로를 놓아서 지날갈 수 있는 길을 만들 수 있다
경사로는 높이가 항상 1, 길이는 L

경사로 높은 칸 낮은 칸 연결
- 낮은 칸에 높고 L개의 연속된 칸에 경사로 바닥이 모두 접해야한다
- 칸 차이는 1
- 낮은 칸 높이 모두 같아야하고 L개의 칸이 연속이어야함

아래와 같은 경우 경사로 불가
- 경사로 놓은곳에 또 경사로 x
- 차이 1아님
- 낮은 지점의 칸 높이가 모두 같지 않거나 L개가 연속 되지 않은 경우

- 행 검사
- 열 검사

문자열 압축?
3 2 2 1 1 1
3 2 1 

2 2 3 2 2 1
2 3 2 1

2 2 2 3 2 1
2 2 3 2 1 

0 1 2 3 4 5  3  / 1 2
1 1 1 2 2 2 지금
1 1 2 2

0 1 2 3 4 5  3
2 2 2 1 1 1
'''
N, L = map(int,input().split())
# N, L = 10, 2
grid = [list(map(int,input().split())) for _ in range(N)]
ans = 0

def check(tmp):
    is_line = True
    visited = [0 for _ in range(N)]
    if tmp.count(tmp[0]) == N: # 모두 같은 값
        # print('같은값',tmp)
        return is_line 
    
    for i in range(1,N):
        if tmp[i] - tmp[i-1] == 1: # 진행 2 - 1
            s,e = i-L, i-1
            for j in range(s,e+1):
                if j not in range(0,N):
                    is_line = False
                    break
                if visited[j] == 1:
                    is_line = False
                    break
                    
                if tmp[j] != tmp[i-1]: #
                    is_line = False
                    break
                visited[j] = 1
        elif tmp[i] - tmp[i-1] > 1:
            is_line = False
            break
    

        if tmp[i] - tmp[i-1] == -1: # 1-2
            s,e = i, i+L 
            for j in range(s,e):
                if j not in range(0,N):
                    is_line = False
                    break
                if visited[j] == 1:
                    is_line = False
                    break
                if tmp[j] != tmp[i]: #
                    is_line = False
                    break
                visited[j] = 1
        elif tmp[i] - tmp[i-1] < -1:
            is_line = False
            break
    

    # if is_line:
        # print(tmp)
    return is_line

def check_down(fix): # 위 -> 아래
    tmp = [grid[i][fix] for i in range(N)]
    # print(tmp)
    return check(tmp)

def check_right(fix): # 왼 -> 오 
    tmp = [grid[fix][i] for i in range(N)]
    # print(tmp)
    return check(tmp)

for i in range(N):
    ans += 1 if check_down(i) else 0

for i in range(N):
    ans += 1 if check_right(i) else 0

print(ans)

# a = [1,1,2,3,3,2] # 1 1 2 3 3 2
# a = [2,2,3,5,3,1,1,1,1,1] 
# [1, 1, 2, 2, 3, 3, 3, 3, 3, 4]
# a = [4, 4, 4, 5, 5, 5, 5, 5, 5, 3]

# print(check(a))