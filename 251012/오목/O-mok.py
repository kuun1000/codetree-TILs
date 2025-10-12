n = 19
grid = [list(map(int, input().split())) for _ in range(n)]

direction = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

winner = 0
mid_x, mid_y = 0, 0
for i in range(n):
    for j in range(n):
        for dx, dy in direction:
            if not (grid[i][j] and 0 <= i+dx*4 < n and 0 <= j+dy*4 < 19):
                continue
            flag = True
            for k in range(5):
                flag &= grid[i][j] == grid[i + dx*k][j + dy*k]
            if flag:
                winner = grid[i][j]
                mid_x, mid_y = i + dx*2, j + dy*2

print(winner)
if winner != 0:
    print(mid_x+1, mid_y+1)