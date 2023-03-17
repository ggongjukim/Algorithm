E,M,S = list(map(int,input().split(' ')))
if E == 15 :
    E = 0
if M == 28 :
    M =0
if S == 19:
    S = 0
for x in range(1,7990):

    if x%15 == E and x%28 == M and x%19 == S :
        print(x)
        break