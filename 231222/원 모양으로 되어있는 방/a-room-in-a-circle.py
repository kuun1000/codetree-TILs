import sys

n = int(input())
arr = [int(input())
        for _ in range(n)
]

min_dist = sys.maxsize
for i in range(n):
    dist = 0
    prev_idx = i
    for j in range(i+1, n+i):
        # print(prev_idx, j%n)
        # print(f"{arr[j%n]} * {abs(j-i)} = {arr[j%n]*abs(j-i)}") 
        dist += arr[j%n]*abs(j-i)
        # print(dist)
        prev_idx = j%n
    min_dist = min(min_dist, dist)
    # print(min_dist)
    # print()
print(min_dist)