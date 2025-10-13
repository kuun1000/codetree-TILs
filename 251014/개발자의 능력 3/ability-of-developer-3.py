import sys

arr = list(map(int, input().split()))
n = len(arr)

def get_diff(i, j, k):
    sum1 = arr[i] + arr[j] + arr[k]
    sum2 = sum(arr) - sum1
    return abs(sum1 - sum2)

ans = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            ans = min(ans, get_diff(i, j, k))

print(ans)