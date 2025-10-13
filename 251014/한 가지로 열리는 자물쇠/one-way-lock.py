n = int(input())
a, b, c = list(map(int, input().split()))

def is_distance(i, j, k):
    if abs(i - a) > 2 or abs(j - b) > 2 or abs(k - c) > 2:
        return True
    return False

ans = n * n * n 
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(0, 10):
            if i == j == k and is_distance(i, j, k):
                ans -= 1

print(ans)