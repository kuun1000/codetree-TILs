n, m = list(map(int, input().split()))
grid = [list(input()) for _ in range(n)]

directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

result = 0
for i in range(n):
    for j in range(m):
        # 첫 글자가 L이 아닌 경우 제외
        if grid[i][j] != 'L':
            continue

        for dx, dy in directions:
            curt = 1
            cx, cy = i, j
            while True:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    break
                if grid[nx][ny] != 'E':
                    break
                curt += 1
                cx, cy = nx, ny
            
            if curt >= 3:
                result += 1

print(result)