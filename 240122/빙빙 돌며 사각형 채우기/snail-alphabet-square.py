n, m = tuple(map(int, input().split()))
grid = [[0 for _ in range(m)] for _ in range(n)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 오른쪽, 아래쪽, 왼쪽, 위쪽
dir_num = 0 # 이동 방향

x, y = 0, 0 # 현재 위치
grid[x][y] = chr(ord('A'))  # 처음 위치는 A로 설정

# 격자 내에 있는지
def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 모든 위치에 대해
for i in range(1, m*n):
    # 이동 후의 위치
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    # 격자 내에 있지 않거나 이미 방문한 경우
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4 # 방향 회전
        
    x, y = x + dxs[dir_num], y + dys[dir_num]
    grid[x][y] = chr(i % 26 + ord('A'))

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=' ')
    print()