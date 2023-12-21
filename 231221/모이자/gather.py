import sys

n = int(input())
places = list(map(int, input().split()))

min_val = sys.maxsize
for i in range(n):
    sum_dist = 0
    for j in range(n):
        sum_dist += places[j] * abs(i - j)
    min_val = min(min_val, sum_dist)

print(min_val)