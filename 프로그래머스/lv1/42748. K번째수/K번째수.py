def solution(array, commands):
  answer = []

  for x in commands:
    i = int(x[0])-1
    j = int(x[1])
    k = int(x[2])-1
    print(i,j,k)
    temp = array[i:j]
    temp.sort()
    answer.append(temp[k])
  return answer