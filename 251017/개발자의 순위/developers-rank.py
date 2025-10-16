k, n = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(k)]

win = [[True] * (n+1) for _ in range(n+1)]
for result in arr:
    for i in range(n):
        for j in range(i+1, n):
            a, b = result[i], result[j]
            win[a][b] = win[a][b]
            win[b][a] = False

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j and win[i][j]:
            ans += 1

print(ans)