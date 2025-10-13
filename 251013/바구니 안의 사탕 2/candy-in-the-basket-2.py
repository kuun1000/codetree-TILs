n, k = list(map(int, input().split()))
arr = [0] * 101

for _ in range(n):
    candy, basket = list(map(int, input().split()))
    arr[basket] += candy

ans = 0
for i in range(101):
    left = max(0, i - k)
    right = min(100, i + k)
    ans = max(ans, sum(arr[left:right + 1]))

print(ans)