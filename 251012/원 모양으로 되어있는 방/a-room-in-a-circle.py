import sys

n = int(input())
arr = [int(input()) for _ in range(n)]

result = sys.maxsize
for i in range(n):  # 시작하는 방 선택
    sum_dist = 0
    for j in range(n):  # 이동 거리 계산
        dist = (n - i + j) % n
        sum_dist += dist * arr[j]
    
    result = min(result, sum_dist)

print(result)