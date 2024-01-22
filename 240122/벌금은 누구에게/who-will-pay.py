n, m, k = tuple(map(int, input().split()))

# 학생별 벌칙 횟수
penalty_cnt = [0] * (n + 1)

first = -1
for _ in range(m):
    target = int(input())

    # 벌칙 받는 학생의 값 1 증가
    penalty_cnt[target] += 1

    # 해당 학생의 벌칙 횟수가 k 이상인 경우
    if penalty_cnt[target] >= k:
        first = target
        break

print(first)