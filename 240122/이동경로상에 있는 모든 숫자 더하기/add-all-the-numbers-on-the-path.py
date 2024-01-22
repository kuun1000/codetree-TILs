dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

N, T = tuple(map(int, input().split()))
x, y = N // 2, N // 2

# 격자 내에 있는지
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

commands = list(input())

grid = [list(map(int, input().split())) for _ in range(N)]

dir_num = 0    # 이동 방향
sum_val = grid[x][y]    # 이동 경로 상의 합

for cmd in commands:
    # 왼쪽으로 방향 회전
    if cmd == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    # 오른쪽으로 방향 회전
    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4
    # F: 현재 방향으로 1칸 이동
    else:
        # 이동 후의 위치
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        # 격자 안에 있는 경우
        if in_range(nx, ny):
            sum_val += grid[nx][ny]
            x, y = nx, ny

print(sum_val)