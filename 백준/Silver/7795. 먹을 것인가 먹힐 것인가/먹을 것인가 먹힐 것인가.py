'''
심해에는 두 종류 생명체 A, B

A는 B를 먹는다
A는 작은 먹이만 먹는다

A의 수 N    B의 수 M

'''
T = int(input())
def sol():
    a,b = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A = sorted(A,reverse=True) # 8 7 3 1 1
    B = sorted(B,reverse=True) # 6 3 1
    # print(A,B)
    s, e = 0 , len(B)-1 # 0 2
    ans = 0
    i = 0
    while True:
        if i == a:
            break

        if s > e:
            s = 0
            i += 1
            continue

        # print("A,B",A[i],B[s])
        if A[i] > B[s]: # 8 > 6
            ans += e-s+1 # 2-0+1
            i += 1 # 다음 A
            continue

        else: # 3 < 6
            s += 1
    return ans

for i in range(T):
    print(sol())
        
