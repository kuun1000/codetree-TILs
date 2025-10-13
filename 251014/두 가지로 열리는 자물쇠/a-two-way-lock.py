n = int(input())
a1, b1, c1 = list(map(int, input().split()))
a2, b2, c2 = list(map(int, input().split()))

def near(x, y):
    return min(abs(x - y), n - abs(x - y)) <= 2

def is_distance(i, j, k):
    return (
        (near(i, a1) and near(j, b1) and near(k, c1)) or
        (near(i, a2) and near(j, b2) and near(k, c2))
    )

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if is_distance(i, j, k):
                ans += 1

print(ans)