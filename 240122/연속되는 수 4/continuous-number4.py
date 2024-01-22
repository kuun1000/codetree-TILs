# 숫자의 개수 및 숫자 입력 받기
n = int(input())
arr = [int(input()) for _ in range(n)]

# 최대 길이, 연속 길이
max_length, length = 0, 0

for i in range(n):
    if i > 0 and arr[i-1] < arr[i]:
        length += 1
    else:
        length = 1
    
    max_length = max(max_length, length)

print(max_length)