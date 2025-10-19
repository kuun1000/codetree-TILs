n, b = list(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x:(x[0]//2 + x[1]))

ans = -1
for i in range(n):
    money = arr[i][0] // 2 + arr[i][1]
    cnt = 1
    if money > b:
        break
    
    for j in range(n):
        if i == j:
            continue
        money += sum(arr[j])
        
        if money > b:
            money -= sum(arr[j])
            break
        cnt += 1
    ans = max(ans, cnt)

print(ans)