# n, 수열 입력 받기
n = int(input())
arr = [int(input()) for _ in range(n)]

max_cnt = 0 # 최대 횟수
# cnt = 0 # 동일한 숫자가 나오는 횟수 
# for i in range(n):
#     # 2(1)번째 원소부터 현재 값과 이전값 같은 경우
#     if i > 0 and arr[i-1] == arr[i]:
#         # 해당 그룹에 대해 횟수 1 증가
#         cnt += 1
#     # 1(0)번째 원소 또는 현재값과 이전값 다른 경우
#     else:
#         # 새로운 그룹 -> 횟수 1로 초기화
#         cnt = 1
    
#     # 현재 최대 횟수와 현재 그룹의 횟수 중 최대값
#     max_cnt = max(max_cnt, cnt)

# # 정답 출력
# print(max_cnt)

cnt = 1 # 동일한 숫자가 나오는 횟수 
for i in range(1, n):
    # 2(1)번째 원소부터 현재 값과 이전값 같은 경우
    if arr[i-1] == arr[i]:
        # 해당 그룹에 대해 횟수 1 증가
        cnt += 1
    # 1(0)번째 원소 또는 현재값과 이전값 다른 경우
    else:
        # 새로운 그룹 -> 횟수 1로 초기화
        cnt = 1
    
    # 현재 최대 횟수와 현재 그룹의 횟수 중 최대값
    max_cnt = max(max_cnt, cnt)

# 정답 출력
print(max_cnt)