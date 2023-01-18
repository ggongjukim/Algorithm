from collections import deque
def solution(numbers, target):
  count =0
  visited = [False]* len(numbers)
  queue = deque()
  queue.append([numbers[0],0])
  queue.append([-1*numbers[0],0])
  visited[0] = True

  while queue:

    currentNode = queue.popleft() # currentNode = 1
    if currentNode[1] == len(numbers)-1:
      break
    queue.append([currentNode[0]+numbers[currentNode[1]+1],currentNode[1]+1])
    queue.append([currentNode[0]-numbers[currentNode[1]+1],currentNode[1]+1])
    
    if currentNode[1]+1 == len(numbers)-1:
      if queue[-1][0] == target :
        count += 1
      if queue[-2][0] == target :
        count += 1

  answer = count
  return answer