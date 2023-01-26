N, k = map(int, input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
award =[]
for _ in range(k):
  award.append(arr.pop())
print(award.pop())