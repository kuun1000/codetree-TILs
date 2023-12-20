dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

N, T = tuple(map(int, input().split()))
x, y = N // 2, N // 2

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

commands = list(input())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

cdir = 0
sum_val = grid[x][y]
for cmd in commands:
    if cmd == 'L':
        cdir = (cdir - 1 + 4) % 4
    elif cmd == 'R':
        cdir = (cdir + 1) % 4
    else:
        nx, ny = x + dxs[cdir], y + dys[cdir]
        if in_range(nx, ny):
            sum_val += grid[nx][ny]
            x, y = nx, ny

print(sum_val)