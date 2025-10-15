import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = sys.maxsize
for i in range(n):
    max_x, min_x, max_y, min_y = -sys.maxsize, sys.maxsize, -sys.maxsize, sys.maxsize
    for idx, (x, y) in enumerate(arr):
        if i == idx:
            continue
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)
    area = (max_x - min_x) * (max_y - min_y)
    ans = min(ans, area)
        
print(ans)