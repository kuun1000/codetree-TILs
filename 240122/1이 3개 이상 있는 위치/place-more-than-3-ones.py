n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 위치가 격자 안에 들어오는지 판단
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

# 인접한 위치 중 1의 개수
def adjacent_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] == 1:
            cnt += 1
    
    return cnt

cnt = 0
for i in range(n):
    for j in range(n):
        if adjacent_cnt(i, j) >= 3:
            cnt += 1

print(cnt)