# 1. n 입력 받기
n = int(input())

# 2. n개의 줄에 걸쳐 단어 입력 받기
arr = [input() for _ in range(n)]

# 3. 정렬하기
sorted_arr = sorted(arr)

# 4. n개의 줄에 걸쳐 정렬된 단어 출력하기
for elem in sorted_arr:
    print(elem)