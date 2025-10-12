n, m = list(map(int, input().split()))
grid = [list(input()) for _ in range(n)]

directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

result = 0
search = 'LEE'
for i in range(n):
    for j in range(m):
        for dx, dy in directions:
            if not (0 <= i+dx*2 < n and 0 <= j+dy*2 < m):
                continue
            flag = True
            for k in range(3):
                flag &= search[k] == grid[i + dx*k][j + dy*k]
            if flag:
                result += 1

print(result)