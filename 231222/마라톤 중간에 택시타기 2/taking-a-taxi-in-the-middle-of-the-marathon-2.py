import sys

n = int(input())
arr = [list(map(int, input().split()))
        for _ in range(n)
]

min_dist = sys.maxsize
for i in range(1, n-1):
    dist = 0
    prev_idx = 0
    for j in range(1, n):
        if i == j:
            continue
        dist += abs(arr[prev_idx][0] - arr[j][0]) + abs(arr[prev_idx][1] - arr[j][1])
        prev_idx = j
    min_dist = min(min_dist, dist)
print(min_dist)