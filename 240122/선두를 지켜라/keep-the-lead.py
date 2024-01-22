MAX_T = 1000 * 1000
n, m = tuple(map(int, input().split()))

pos_a = [0] * (MAX_T + 1) # A의 초별 위치
pos_b = [0] * (MAX_T + 1) # B의 초별 위치

## A
time_a = 1  # 현재 시간(t)
for _ in range(n):
    v, t = tuple(map(int, input().split()))
    
    # t초 동안, 이전 위치 + 속도
    for _ in range (t):
        pos_a[time_a] = pos_a[time_a - 1] + v
        time_a += 1 

## B
time_b = 1  # 현재 시간(t)
for _ in range(m):
    v, t = tuple(map(int, input().split()))
    
    # t초 동안, 이전 위치 + 속도
    for _ in range (t):
        pos_b[time_b] = pos_b[time_b - 1] + v
        time_b += 1 


cnt = 0     # 선두가 바뀌는 횟수
cur = 0     # 선두 1: A, 2: B
for i in range(1, time_a):
    if pos_a[i] > pos_b[i]: # A가 B보다 앞서 있을 떄
        if cur == 2:            # 기존 선두가 B였던 경우
            cnt += 1                # 횟수 1 증가
        cur = 1             # 선두를 A로 변경

    elif pos_a[i] < pos_b[i]:   # B가 A보다 앞서 있을 때
        if cur == 1:                # 기존 선두가 A였던 경우
            cnt += 1                    # 횟수 1 증가
        cur = 2                 # 선두를 B로 변경

print(cnt)