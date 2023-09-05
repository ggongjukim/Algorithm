def solution(s):
  result = len(s)
  minlen = len(s)
  # print('len(s)',len(s))
  for k in range(1,len(s)//2+1): # 2부터 절반까지 
    total = 1
    compare = s[0:k]
    finish=''


    for i in range(0+k, len(s)+k,k):
      # print(k,i,compare)
      if compare == s[i:i+k]:
        total += 1
      else :
        if total == 1:
          finish += compare
        else:
          finish += str(total)+compare
        compare = s[i:i+k]
        total = 1

    minlen = min(len(finish),minlen)
  return minlen