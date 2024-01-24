# 변수 선언 및 입력
A = list(input())
n = len(A)  # 문자열의 길이 
cnt = 0 # 괄호 쌍의 개수

for i in range(n):  # 모든 원소 중에서  
    if A[i] == "(":     # "("인 원소에 대해서
        for j in range(i, n):   # 이후 원소 중에서 
            if A[j] == ")":         # ")"인 원소 탐색
                cnt += 1

print(cnt)