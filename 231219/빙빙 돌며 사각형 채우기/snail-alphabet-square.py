n, m = tuple(map(int, input().split()))

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0
grid = [[0 for _ in range(m)] for _ in range(n)]
x, y = 0, 0
grid[x][y] = chr(ord('A'))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

for i in range(1, m*n):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    if in_range(nx, ny) and grid[nx][ny] == 0:
        x, y = x + dxs[dir_num], y + dys[dir_num]
        grid[x][y] = chr(i + ord('A'))
    else:
        dir_num = (dir_num + 1) % 4
        x, y = x + dxs[dir_num], y + dys[dir_num]
        grid[x][y] = chr(i + ord('A'))

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()