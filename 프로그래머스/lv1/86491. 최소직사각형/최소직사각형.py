def solution(sizes):
    answer = 0
    big =[]
    small = []
    for i in sizes:
        big.append(max(i))
        small.append(min(i))
        
    return max(big) * max(small)