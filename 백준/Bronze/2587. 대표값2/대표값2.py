arr =[]
for _ in range(5):
    arr.append(int(input()))
               
mean = sum(arr)/5
arr = sorted(arr)
print(int(mean))
print(arr[2])
