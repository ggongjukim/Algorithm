n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [False] * n
ans = []
result =[]
def check():
  start = 0
  link = 0
  for i in range(len(ans)):
    for j in range(i+1,len(ans)):
      start += arr[ans[i]][ans[j]] + arr[ans[j]][ans[i]]  
  reverse_ans = []
  for i in range(n):
    if i in ans:
      continue
    reverse_ans.append(i)
  # print(ans,reverse_ans)
  for i in range(len(reverse_ans)):
    for j in range(i+1,len(reverse_ans)):
      link += arr[reverse_ans[i]][reverse_ans[j]] + arr[reverse_ans[j]][reverse_ans[i]] 
      
  return abs(start - link)
  
def sol(cnt, last_idx):
  if cnt == n//2:
    result.append(check())
    return
  for i in range(last_idx+1,n):
    ans.append(i)
    sol(cnt+1,i)
    ans.pop()
sol(0,-1)
print(min(result))