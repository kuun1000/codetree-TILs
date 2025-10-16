n, b = tuple(map(int, input().split()))
prices = [int(input()) for _ in range(n)]

prices.sort()

ans = 0
for i in range(n):
    discounted = prices[i] // 2
    total = discounted
    count = 1

    for j in range(n):
        if i == j:
            continue
        if total + prices[j] <= b:
            total += prices[j]
            count += 1
        else:
            break
    
    ans = max(ans, count)

print(ans)