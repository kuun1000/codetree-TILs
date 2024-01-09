# 1. 정수 n 입력받기
n = int(input())

# 2. n개의 원소를 리스트로 입력받기
arr = list(map(int, input().split()))

# 3. 리스트의 각 원소에 대해 제곱하여 리스트에 저장하기
sq_arr = [elem * elem for elem in arr]

# 4. 리스트의 값 출력하기
print(*sq_arr)