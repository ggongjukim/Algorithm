from itertools import permutations


def solution(numbers):
  answer = []
  numbers = list(numbers)
  candidate = []

  # 조합 모두 하기
  for i in range(1, len(numbers) + 1):

    temp = list(permutations(numbers, i))
    temp = list(set(temp))
    for j in temp:
      if j[0] == '0':
        continue
      candidate.append(''.join(j))


  for i in candidate:
    answer.append(i)
    for j in range(1,int(i)):
      if int(i)%j == 0 and j !=1 and j !=i:
        answer.pop(-1)
        break

  if '1' in answer:
    answer.remove('1')

  return len(answer)