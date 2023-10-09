'''
근손실
하루 지날때마다 중량이  K만큼 감소

N 개의 운동 키트
하루에 1개씩
어떤 키트 쓸지 맘대로 결정
N일 동안 한번씩만 사용 가능

중량이 500이상으로 유지하도록 N일간의 운동 플랜 세우기
1일차부터 N일차까지의 모든 기간동안 어떤 시점 에서라도 중량이 500보다 작아지지않도록
'''
N,K = map(int,input().split())
kit = list(map(int,input().split()))
arr = []
ans = 0

def check():
  mus = 500
  for i in arr:
    mus = mus - K + kit[i]
    if mus < 500:
      return False
  return True
  
def back(cnt):
  global ans
  if cnt == N:
    # print(arr)
    if check():
      ans += 1
    return

  for i in range(N):
    if i in arr:
      continue
    arr.append(i)
    back(cnt + 1)
    arr.pop()
back(0)
print(ans)