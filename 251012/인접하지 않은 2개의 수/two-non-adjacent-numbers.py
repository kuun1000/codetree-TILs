import sys

n = int(input())
arr = list(map(int, input().split()))

result = -sys.maxsize
for i in range(n-1):
    for j in range(i+2, n):
        num = arr[i] + arr[j]
        result = max(result, num)

print(result)