MAX_T = 250

N, K, P, T = tuple(map(int, input().split()))

t_x, t_y = [0] * (MAX_T + 1), [0] * (MAX_T + 1) # 시간별 기록
hs_num = [K] * (N + 1)                      # 전염 가능한 잔여 악수 횟수
infected = [0] * (N + 1)                    # 감염된 개발자
infected[P] = 1                             # 처음 감염된 개발자


# 시간별 악수한 개발자 
for _ in range(T):
    t, x, y = tuple(map(int, input().split()))
    t_x[t], t_y[t] = x, y

# 시간별 감염 여부
for i in range(1, MAX_T + 1):
    x, y = t_x[i], t_y[i]
    # 둘 중 하나라도 감염된 경우
    if (x != 0 and y != 0):

        # x, y 감염된 상태 & x 또는 y가 전염 가능한 상태
        if infected[x] != 0 and infected[y] != 0:
            hs_num[x] = (hs_num[x] - 1) if hs_num[x] > 0 else 0
            hs_num[y] = (hs_num[y] - 1) if hs_num[y] > 0 else 0

        # x 감염된 상태 & 전염 가능한 상태
        elif infected[x] != 0 and hs_num[x] > 0:
            hs_num[x] -= 1
            infected[y] = 1

        # y 감염된 상태 & 전염 가능한 상태
        elif infected[y] != 0 and hs_num[y] > 0:
            hs_num[y] -= 1
            infected[x] = 1

for elem in infected[1:]:
    print(elem, end='')