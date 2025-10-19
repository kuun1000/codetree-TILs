n, b = list(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    current = arr[i][0] // 2 + arr[i][1]
    cnt = 1
    if current > b:
        break
    
    for j in range(n):
        if i == j:
            continue
        current += sum(arr[j])
        
        if current > b:
            current -= sum(arr[j])
            break
        cnt += 1
    ans = max(ans, cnt)

print(ans)