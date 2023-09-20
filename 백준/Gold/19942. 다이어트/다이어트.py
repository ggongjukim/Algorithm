'''
다이어트
식재료 N개 중에 몇개 선택해서 영양분이 일정 이상 되어야한다
100 70 90 10 이상이 되는 경우 생각
비용이 최소

사전순으로 빠른것
'''
N = int(input())
cp, cf, cs, cv = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(N)]
ans = []
p,f,s,v,c = 0,0,0,0,0
answer = []
is_answer = True
def back(count):
    global p,f,s,v,c,is_answer
    if p >= cp and f >= cf and s >= cs and v >= cv : # 조건을 만족하면
        # print(ans, c) # 금액 출력
        answer.append([c,ans[:]])        
        return
    
    if count == N:# 모든 칸 다 돌았다면
        is_answer = False
        return
    
    for i in range(N):
        if len(ans) > 0 and ans[-1] >= i:
            continue 
        dp, df, ds, dv, dc = arr[i]
        bp,bf,bs,bv,bc = p,f,s,v,c # 이전꺼
        np, nf, ns, nv, nc = p+dp, f+df, s+ds, v+dv, c+dc
        p,f,s,v,c = np,nf,ns,nv,nc
        ans.append(i)
        back(count+1)
        # back(np,nf,ns,nv,nc,count + 1)
        p,f,s,v,c = bp,bf,bs,bv,bc
        ans.pop()
        # back(p,f,s,v,c,count+1) ## ? ?

back(0)

if is_answer:
    answer = sorted(answer, key = lambda x : (x[0],x[1]))

    print(answer[0][0])
    for i in answer[0][1]:
        print(i+1, end=' ')
else:
    print(-1)
# answer = sorted(answer, key = lambda x : (x[0],x[1]))
# # if len(ans[0][1]) == 1:
#     # print(answer)
# # print(answer)
# print(answer[0][0])
# for i in answer[0][1]:
#     print(i+1, end=' ')
    

    

