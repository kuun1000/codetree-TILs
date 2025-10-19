import sys

n, b = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]
base = [sum(elem) for elem in arr]

ans = 0
for i in range(n):
    first_cost = arr[i][0] // 2 + arr[i][1]
    if first_cost > b:
        continue
    
    remain = b - first_cost
    cnt = 1
    
    others = [base[j] for j in range(n) if j != i]
    others.sort()

    for cost in others:
        if remain >= cost:
            remain -= cost
            cnt += 1
        else:
            break

    if cnt > ans:
        ans = cnt

print(ans)