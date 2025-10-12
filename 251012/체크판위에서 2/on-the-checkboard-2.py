r, c = list(map(int, input().split()))
grid = [list(input().split()) for _ in range(r)]

result = 0
for i in range(r):
    for j in range(c):
        for k in range(i+1, r-1):
            for l in range(j+1, c-1):
                if grid[0][0] != grid[i][j] and grid[i][j] != grid[k][l]:
                    result += 1
                
print(result)