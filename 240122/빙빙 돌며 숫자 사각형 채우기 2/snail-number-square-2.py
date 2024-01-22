n, m = tuple(map(int, input().split()))
grid = [[0 for _ in range(m)] for _ in range(n)]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1] # 동, 남, 서, 북
dir_num = 0 # 이동 방향

# 현재 위치, 처음 칸은 1로 설정
x, y = 0, 0
grid[x][y] = 1

# 격자 내에 있는지
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 모든 칸에 대해 
for i in range(2, m * n + 1):
    # 이동 후의 위치
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or grid[nx][ny] != 0: # 격자 밖을 벗어나거나 이미 방문한 경우
        dir_num = (dir_num + 1) % 4                     # 방향 번호 1 증가

    x, y = x + dxs[dir_num], y + dys[dir_num]   # 현재 방향으로 이동
    grid[x][y] = i

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()