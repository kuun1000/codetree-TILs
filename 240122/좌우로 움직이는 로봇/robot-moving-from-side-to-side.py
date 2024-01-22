MAX_D = 1000000

n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_D + 1), [0] * (MAX_D + 1)

## A
time_a = 1  # 현재 시간(t)
for _ in range(n):
    t, d = input().split()
    t = int(t)
    
    if d == "L":
        for _ in range (t):
            pos_a[time_a] = pos_a[time_a - 1] - 1
            time_a += 1 
    else:
        for _ in range (t):
            pos_a[time_a] = pos_a[time_a - 1] + 1
            time_a += 1 

## B
time_b = 1  # 현재 시간(t)
for _ in range(n):
    t, d = input().split()
    t = int(t)
    
    if d == "L":
        for _ in range (t):
            pos_b[time_b] = pos_b[time_b - 1] - 1
            time_b += 1 
    else:
        for _ in range (t):
            pos_b[time_b] = pos_b[time_b - 1] + 1
            time_b += 1 

## 보정
diff = len(pos_a) - len(pos_b)
if diff > 0:
    pos_b += [pos_b[-1] * diff]
elif diff < 0:
    pos_a += [pos_a[-1] * diff]

## 위치 비교 
prev_pos, cur_pos = 0, 0
cnt = 0
for i in range(1, len(pos_a)):
    prev_pos = int(pos_a[i-1] != pos_b[i-1])    # 이전 위치 다른지
    cur_pos = int(pos_a[i] == pos_b[i])         # 현재 위치 같은지

    if prev_pos and cur_pos:
        cnt += 1

print(cnt)