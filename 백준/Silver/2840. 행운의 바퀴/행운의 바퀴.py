'''
바퀴 시계방향

바퀴 K번 돌림
바퀴를 돌릴때마다 글자가 변하는 횟수와 어떤 글자에서 회전을 멈추었는지

기록을 바탕으로 바퀴에 있는 알파벳 찾기

입력
첫줄 : 바퀴칸 수 N / 바퀴 돌리는 횟수 K
둘줄 : 가리키는 글자가 몇번 바뀌는지 S, 회전 멈춤시 가리킨 글자

출력 
마지막 회전에서 
화살표가 가리키는 문자부터 
시계방향으로 
결정 못하는 칸 ?
행운바퀴 없다면 !
8 8
4 V
3 I
7 T
7 A
6 R
5 N
1 O -1
9 H -9

H O N I T A V R
o o o o o o o o

B A
'''
N, K = map(int, input().split())
arr = []
cir = ['?'] * N
give = []
for _ in range(K):
  num, ch = map(str, input().split())
  num = int(num)
  arr.append((num, ch))
  give.append(ch)
# print(arr)

cur_idx = 0
cir[0] = arr[-1][1]  # H

is_can = True

# 회전 판 개수보다 주어진 알파벳이 많은 경우 => 29 에서 틀림
give = set(give)
if N < len(give):
  is_can = False
  # print("3번이유")

while len(arr) > 1:
  num, ch = arr.pop()

  put_ch = arr[-1][1]  # 넣어야하는 애
  cur_idx = cur_idx + num

  if cur_idx >= N:
    cur_idx = cur_idx % N

  if cir[cur_idx] == '?':  # 해당 자리가 물음표여야하고
    cir[cur_idx] = put_ch
  else:  # 물음표가 아니면 검사
    if cir[cur_idx] != put_ch:
      is_can = False
      break
  # print("cir",cir)
  # print("arr",arr)

# 마지막 검사 => 29% 에서 틀
# num, ch = arr[0]
# cur_idx = cur_idx + num
# if cur_idx >= N:
#   cur_idx = cur_idx % N
# if cir[cur_idx] == ch:
#   is_can = False

for i in cir:  # 같은 글자가 나오면 안됨 =>29% 에서 틀림
  if i == '?':
    continue
  if cir.count(i) != 1:
    is_can = False

print(''.join(cir) if is_can else "!")
