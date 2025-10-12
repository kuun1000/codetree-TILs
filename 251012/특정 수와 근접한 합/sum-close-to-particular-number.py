n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = s
base = sum(arr)
for i in range(n-1):
    for j in range(i+1, n):
        current = base - arr[i] - arr[j]
        result = min(result, abs(s - current))

print(result)