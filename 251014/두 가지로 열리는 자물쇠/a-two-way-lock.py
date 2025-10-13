n = int(input())
a1, b1, c1 = list(map(int, input().split()))
a2, b2, c2 = list(map(int, input().split()))

def is_distance(i, j, k):
    if (abs(a1-i) <= 2 or abs(a1-i) >= n-2) and (abs(b1-j) <= 2 or abs(b1-j) >= n-2) and (abs(c1-k) <= 2 or abs(c1-k) >= n-2):
        return True
    if (abs(a2-i) <= 2 or abs(a2-i) >= n-2) and (abs(b2-j) <= 2 or abs(b2-j) >= n-2) and (abs(c2-k) <= 2 or abs(c2-k) >= n-2):
        return True
    return False

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if is_distance(i, j, k):
                ans += 1

print(ans)