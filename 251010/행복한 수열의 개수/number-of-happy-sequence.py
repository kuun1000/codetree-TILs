def is_happy(seq):
    cnt = 1
    for i in range(1, n):
        if seq[i] == seq[i-1]:
            cnt += 1
            if cnt >= m:
                return True
        else:
            cnt = 1
    return m <= 1 or False

n, m = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0

for i in range(n):
    row = grid[i]
    ans += 1 if is_happy(row) else 0

for j in range(n):
    col = [grid[i][j] for i in range(n)]
    ans += 1 if is_happy(col) else 0

print(ans)