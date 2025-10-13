n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i, n):
        if i == j:
            ans += 1
        else:
            avg = sum(arr[i:j+1]) / len(arr[i:j+1])
            if avg in arr[i:j+1]:
                ans += 1

print(ans)