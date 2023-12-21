R, C = tuple(map(int, input().split()))
grid = [list(input().split())
        for _ in range(R)]

start = grid[0][0]
cnt = 0

if start == grid[R-1][C-1]:
    print(cnt)
else:
    first = []
    for i in range(1, R-2):
        for j in range(1, C-2):
            if start != grid[i][j]:
                first.append((i, j))
    for x, y in first:
        current = grid[x][y]
        for i in range(x+1, R-1):
            for j in range(y+1, C-1):
                if current != grid[i][j]:
                    cnt += 1
    print(cnt)