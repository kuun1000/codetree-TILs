n, t = tuple(map(int, input().split()))
nums = list(map(int, input().split()))

# 최대 길이, 연속 길이
max_length, length = 0, 0

for i in range(n):
    # 1번째 원소부터, 이전 원소와 현재 원소가 t보다 큰 경우
    if i > 0 and nums[i] > t and nums[i-1] > t:
        length += 1

    else:
        length = 1

    max_length = max(max_length, length)

print(max_length)