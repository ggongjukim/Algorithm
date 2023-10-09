'''
절사 평균
절사 평균 or 보정 평균

절사 평균
양쪽 두개 제외 
소수점 이하 셋째 자리에서 반올림

보정 평균
양쪽 끝 두개를 가장 가까운 것으로 교체

N개의 점수, K값 제외 개수
절사평균과 보정평균을 계산해주세요

3 0
2
3
4
'''
N, K = map(int, input().split())
arr = [float(input()) for _ in range(N)]
arr = sorted(arr)

z_arr = arr[K:N - K]
z = sum(z_arr) / (N - (K * 2)) 


b = (sum(z_arr) + z_arr[0] * K + z_arr[-1] * K) / N

z += 0.00000001
b += 0.00000001
# print(format(z))
# print(format(b))

#z = round(z, 2)
#b = round(b, 2)

print(format(z,".2f"))
print(format(b,".2f"))
