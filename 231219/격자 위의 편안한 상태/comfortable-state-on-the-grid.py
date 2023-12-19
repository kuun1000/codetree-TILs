N, M = tuple(map(int, input().split()))

grid = [[0 for _ in range(N)] 
        for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for _ in range(M):
    r, c = tuple(map(int, input().split()))
    x, y = r-1, c-1
    grid[x][y] = 1
    
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if in_range(nx, ny):
            if grid[nx][ny] == 1:
                cnt += 1
        
    if cnt == 3:
        print(1)
    else:
        print(0)