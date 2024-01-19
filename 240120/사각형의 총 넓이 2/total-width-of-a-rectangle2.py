OFFSET = 100

n = int(input())

# 좌표 평면
grid = [[0 for _ in range(2 * OFFSET)] 
        for _ in range(2 * OFFSET)]

for _ in range(n):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = 1

# 2차원 배열 -> 1차원 배열 -> 합 
print(sum(sum(grid, [])))