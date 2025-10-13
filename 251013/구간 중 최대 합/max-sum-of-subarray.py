n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

ans = 0
for i in range(n-k+1):
    cur_sum = sum(arr[i:i+k])
    ans = max(ans, cur_sum)

print(ans)