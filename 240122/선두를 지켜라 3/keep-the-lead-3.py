MAX_T = 1000 * 1000

n, m = tuple(map(int, input().split()))
pos_a, pos_b  = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

## A
time_a = 1 
for _ in range(n) :
    v, t = tuple(map(int, input().split())) 

    for _ in range(t):
        pos_a[time_a] = pos_a[time_a - 1] + v
        time_a += 1

## B
time_b = 1
for _ in range(m) :
    v, t = tuple(map(int, input().split())) 

    for _ in range(t):
        pos_b[time_b] = pos_b[time_b - 1] + v
        time_b += 1

## 조합 비교
cnt, cur = 0, 0 # 조합 바뀐 횟수, 현재 조합(1: A 앞섬 2: B앞섬 3: 동일)
for i in range(1, time_a):
    # A가 B보다 앞서 있고, 선두가 A가 아닌 경우
    if pos_a[i] > pos_b[i]: 
        if cur != 1:
            cnt += 1
        cur = 1
     # B가 A보다 앞서 있고, 선두가 B가 아닌 경우
    elif pos_a[i] < pos_b[i]:
        if cur != 2:
            cnt += 1
        cur = 2
     # A와 B가 동일하고, 이전은 그렇지 않았을 경우
    else:
        if cur != 3:
            cnt += 1
        cur = 3 

print(cnt)