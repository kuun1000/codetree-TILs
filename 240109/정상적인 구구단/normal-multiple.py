# 1. 정수 n 입력받기
n = int(input())

# 2. n번째 단에 대해
for i in range(1, n+1):
    # 3. n번째 결과 출력하기
    for j in range(1, n+1):
        print(f"{i} * {j} = {i * j}", end="")
        if j != n: # 마지막 단이 아닌 경우에만 끝에 ", " 출력하기 
            print(",", end=" ")
    print()