n, k = list(map(int, input().split()))
arr = [0] * 101

for _ in range(n):
    candy, basket = list(map(int, input().split()))
    arr[basket] += candy

ans = 0
for i in range(k, 100-k):
    max_val = sum(arr[i-k:i+k+1])
    ans = max(ans, max_val)

print(ans)