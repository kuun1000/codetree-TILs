n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_coin = 0
for i in range(n-2):
    for j in range(n-2):
        num = 0
        for row in grid[i:i+3]:
            num += sum(row[j:j+3])
        max_coin = max(max_coin, num)

print(max_coin)