import sys

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

ans = -sys.maxsize
for i in range(n):
    operate_time = [0] * 1001
    for j in range(n):
        if i == j:
            continue
        a, b = arr[j]
        for k in range(a, b):
            operate_time[k] = 1
    
    ans = max(ans, operate_time.count(1))

print(ans)