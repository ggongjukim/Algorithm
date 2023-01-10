# 첫줄 N
# 출력 N 자리수 중 소수인것
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())
# 맨 앞자리 2 3 5 7
# 그 뒤 자리 => 홀수 1 3 5 7 9
start = [2, 3, 5, 7]
odd = [1,3, 5, 7,9]
answer = []

def DFS(num):

    # print(num, len(str(num)))
    if len(str(num)) >= N:
        answer.append(num)
        # print('길이 걸림',num)
    else:
        for i in odd: # 21 23
            # print('else',num,i,len(str(num)))
            IsPrime = False
            for j in range(2,int((int(str(num)+str(i)))/2+1)):
                if (int(str(num)+str(i))) % j == 0 :
                    IsPrime = True
                    break
            if not IsPrime:
                DFS(int(str(num)+str(i)))




DFS(2)
DFS(3)
DFS(5)
DFS(7)

for i in answer:
    print(i)