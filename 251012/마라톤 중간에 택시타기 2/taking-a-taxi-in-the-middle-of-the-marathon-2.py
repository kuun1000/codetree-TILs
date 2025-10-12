import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = sys.maxsize
for i in range(1, n-1): # 건너뛸 체크포인트
    dist = 0
    prev = 0
    for j in range(1, n): # 현재 체크포인트
        if i == j:
            continue
        dist += abs(arr[prev][0] - arr[j][0]) + abs(arr[prev][1] - arr[j][1])
        prev = j

    result = min(result, dist)

print(result)