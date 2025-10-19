x, y = list(map(int, input().split()))

ans = -1
for i in range(x, y+1):
    ans = max(ans, sum(list(map(int, str(i)))))

print(ans)