n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(n-m+1):
    seq = a[i:i+m]
    if len(set(seq) - set(b)) == 0:
        ans += 1

print(ans)            