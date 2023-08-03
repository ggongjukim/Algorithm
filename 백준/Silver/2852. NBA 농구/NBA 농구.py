N = int(input())
arr = []
score ={1 : 0, 2: 0 }
timescore = {1 : 0, 2: 0}

for i in range(N):
  win , time = list(map(str,input().split()))
  win = int(win)
  h,s = list(map(int,time.split(':')))
  time = h * 60 + s
  arr.append([win, time])
arr.append([-1,2880]) # 마지막 추가


for i in range(1, len(arr)):
  w = 0
  time = arr[i][1] - arr[i-1][1] # 간격
  # print('i',arr[i])
  
  if arr[i-1][0] in score.keys():
    score[arr[i-1][0]] += 1
  # print('score',score)
  
  if score[1] > score[2]:
    w = 1
  elif score[1] == score[2]:
    continue
  else:
    w = 2
  
  timescore[w] += time

  # print(timescore)
  # print("---------------")
  
for i in timescore.values():
  # print(i)
  h,v = i//60 , i%60
  print(str(h).zfill(2) +':'+ str(v).zfill(2))