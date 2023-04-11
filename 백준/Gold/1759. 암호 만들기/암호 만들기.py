"""
서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열
아까온 애가 또 올 수 없음 => 중복 안됨
visited
"""
l,c = map(int,input().split())
arr = list(map(str,input().split()))
arr = sorted(arr)
# print(arr)
visited = [False] * len(arr)
letter = ['a','e','i', 'o', 'u']

def printvisited():
  temp = []
  for i in range(len(visited)):
    if visited[i]:
      temp.append(arr[i])
  # print(visited)
  # l 이 3이면 모음이 1개, 2개는 안됨
  # l 이 4이면 모음이 1-2개, 3개는 안됨
  cntLetter = 0
  for i in letter:
    if i in temp:
      cntLetter += 1
  
  if not (1 <= cntLetter <= l - 2):
    return
  print(''.join(temp))


def sol(cnt,last_idx):
  if cnt == l:
    printvisited()
    return

  for i in range(last_idx+1,len(arr)):
    visited[i] = True
    sol(cnt+1,i)
    visited[i] = False

for i in range(len(arr)):
  visited[i] = True
  sol(1,i)
  visited[i] = False