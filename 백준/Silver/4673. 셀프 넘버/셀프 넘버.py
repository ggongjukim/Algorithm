dic = {}
for i in range(1, 10036):
  dic[i] = 0


def sol(n):
  arr = list(str(n))
  arr = list(map(int,arr))
  return n + sum(arr)


for i in range(1, 10001):
  dic[sol(i)] += 1

for k,v in dic.items():
  if k > 10000:
    break
  if v == 0:
    print(k)