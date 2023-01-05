# 재귀 피보나치
countfin = 0
countfibo = 0

def fin(n):
  global countfin
  if n ==1 or n==2:
    countfin += 1
    return 1
  else:
    return fin(n-1) + fin(n-2)


N = int(input())
f = [0]*(N+1)
f[1] = 1
f[2] = 1
def fibonacci(n):
  global countfibo
  for i in range(3, n+1):
    countfibo += 1
    f[i] = f[i-1] + f[i-2]
  return f[n]

fin(N)
fibonacci(N)
print(countfin, countfibo)

