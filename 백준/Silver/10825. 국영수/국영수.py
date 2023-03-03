# 국어 내림차순
# 영어 오름차순
# 수학 내림차순

N = int(input())
arr = []
for _ in range(N):
    name, ko, en, math = list(map(str,input().split(' ')))
    arr.append([name,int(ko),int(en),int(math)])
arr = sorted(arr, key=lambda x : (-x[1],x[2],-x[3],x[0]))

for i in arr:
    print(i[0])
