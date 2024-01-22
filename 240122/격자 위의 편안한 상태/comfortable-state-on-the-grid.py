n, m = tuple(map(int, input().split()))

grid = [[0 for _ in range(n)] 
        for _ in range(n)]

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

# 격자 내에 있는지
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    x, y = r-1, c-1
    grid[x][y] = 1
    
    cnt = 0
    # 현재 위치에 대해, 인접 위치 탐색
    for dx, dy in zip(dxs, dys):    
        nx = x + dx
        ny = y + dy
        # 인접 위치가 격자 내에 위치하고, 1인 경우
        if in_range(nx, ny):
            if grid[nx][ny] == 1:
                cnt += 1
        
    if cnt == 3:
        print(1)
    else:
        print(0)