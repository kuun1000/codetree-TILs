n, m = tuple(map(int, input().split()))

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
dir_num = 0
grid = [[0 for _ in range(m)] for _ in range(n)]
x, y = 0, 0
grid[x][y] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(1, m*n):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if in_range(nx, ny) and grid[nx][ny] == 0:
        x, y = x + dxs[dir_num], y + dys[dir_num]
        grid[x][y] = i + 1
    else:
        dir_num = (dir_num + 1) % 4
        x, y = x + dxs[dir_num], y + dys[dir_num]
        grid[x][y] = i + 1

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()