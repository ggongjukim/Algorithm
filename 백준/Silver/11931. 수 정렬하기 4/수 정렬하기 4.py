n = int(input())
arr = [int(input()) for i in range(n)]
arr = sorted(arr,reverse=True)
for i in arr:
  print(i)