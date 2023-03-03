# 스택
N = int(input())
def sol(arr):
    stack =[]
    for i in arr:
        if i == "(":
            stack.append(i)
        else: # )
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
        # print(stack)
    if stack == []:
        return "YES"
    else:
        return "NO"
    

for _ in range(N):
    now = list(input())
    print(sol(now))

