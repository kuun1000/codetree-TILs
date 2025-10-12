import sys

n = int(input())
arr = list(map(int, input().split()))

result = sys.maxsize
for i in range(n):  # 선택된 집
    distance = 0
    for j in range(n):
        distance += arr[j] * abs(i - j)
    result = min(result, distance)

print(result)