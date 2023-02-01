# 길이가 N인 정수 배열 A, B
# s 값 가장 작게 만들기 위해 A를 재 배열 B는 재배열 안됨
# s 의 최솟 값
# a를 힙으로 만들어서 조지기
import heapq
N = int(input())
A =list(map(int,input().split()))
B = list(map(int,input().split()))

# print(A,B)
heapq.heapify(A)
B = sorted(B, reverse=True)
S = 0
for i in range(N):
    S += heapq.heappop(A) * B[i]
print(S)