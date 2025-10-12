import sys

arr = list(map(int, input()))
n = len(arr)

result = -sys.maxsize
for i in range(n):
    arr[i] = 1 - arr[i]

    num = 0
    for j in range(n):
        num = num * 2 + arr[j]
    
    result = max(result, num)
    arr[i] = 1 - arr[i]

print(result)