import sys

n, c, g, h = list(map(int, input().split()))

min_prefs, max_prefs = [], []
for _ in range(n):
    a, b = list(map(int, input().split()))
    min_prefs.append(a)
    max_prefs.append(b)
min_range, max_range = min(min_prefs) - 1, max(max_prefs) + 1

ans = -sys.maxsize
for temp in range(min_range, max_range+1):
    workload = 0
    for i in range(n):
        if temp < min_prefs[i]:
            workload += c
        elif min_prefs[i] <= temp <= max_prefs[i]:
            workload += g
        elif temp > max_prefs[i]:
            workload += h
    ans = max(ans, workload)

print(ans)