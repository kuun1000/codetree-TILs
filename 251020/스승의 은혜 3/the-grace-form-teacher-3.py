n, b = list(map(int, input().split()))
arr = [tuple(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: sum(x))

ans = 0
for i in range(n):
    money = arr[i][0] // 2 + arr[i][1]
    cnt = 1
    
    tmp = []
    for j in range(n):
        if i != j:
            tmp.append(sum(arr[j]))
    tmp.sort()

    for cost in tmp:
        if money + cost < b:
            money += cost
            cnt += 1
        else:
            break

    ans = max(ans, cnt)

print(ans)