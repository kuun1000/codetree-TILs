import sys

arr = list(input())
n = len(arr)

base = 0
for i in range(n):
    if arr[i] == '1':
        base += 2 ** (n-i-1)

result = base
for i in range(n): 
    if arr[i] == '0':
        result = max(result, base + 2 ** (n-i-1))

print(result)