def count_gold(x, y, k):
    cnt = 0
    for dx in range(-k, k+1):
        for dy in range(-(k-abs(dx)), k - abs(dx)+1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == 1:
                    cnt += 1
    return cnt

def is_profitable(count, k):
    profit = count * m
    cost = k*k + (k+1)*(k+1)

    return True if profit >= cost else False

n, m = list(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(n):
        k = 0
        while k*k + (k+1)*(k+1) <= n * n * m:
            count = count_gold(i, j, k)
            if is_profitable(count, k):
                ans = max(ans, count)
            k += 1

print(ans)            