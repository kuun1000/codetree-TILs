MAX_D = 1000000

n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_D + 1), [0] * (MAX_D + 1)

## A
time_a = 1  # 현재 시간(t)
for _ in range(n):
    t, d = tuple(input().split())
    # t초 동안, 이전 값 + 방향에 따른 값 (R: +1, L: -1)
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

## B
time_b = 1  # 현재 시간(t)
for _ in range(m):
    t, d = tuple(input().split())
    # t초 동안, 이전 값 + 방향에 따른 값 (R: +1, L: -1)
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1


## 보정
if time_a > time_b:
    for i in range(time_b, time_a):
        pos_b[i] = pos_b[i-1]

elif time_a < time_b:
    for i in range(time_a, time_b):
        pos_a[i] = pos_a[i-1]


## 위치 비교 
time_max = max(time_a, time_b)
cnt = 0
for i in range(1, time_max):
    # 이전 위치 다른지 & 현재 위치 같은지
    if pos_a[i - 1] != pos_b[i - 1] and pos_a[i] == pos_b[i]:
        cnt += 1

print(cnt)