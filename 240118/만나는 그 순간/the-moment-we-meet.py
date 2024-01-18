# 최대 이동시간
MAX_R = 1000 * 10000

n, m = tuple(map(int, input().split()))

# A의 위치 기록
a = [0] * (MAX_R + 1) # 1초부터 이동 -> 0번째 사용 X
time_a = 1

for _ in range(n):
    d, t = input().split()
    t = int(t)

    if d == "R": # 오른쪽 -> 이전 위치 + 1
        for _ in range(t):
            a[time_a] = a[time_a - 1] + 1
            time_a += 1 # 시간 1초 증가

    else: # 왼쪽 -> 이전 위치 - 1
        for _ in range(t):
            a[time_a] = a[time_a - 1] - 1
            time_a += 1 # 시간 1초 증가

# B의 위치 기록 
b = [0] * (MAX_R + 1) # 1초부터 이동 -> 0번째 사용 X
time_b = 1
for _ in range(m):
    d, t = input().split()
    t = int(t)

    if d == "R": # 오른쪽 -> 이전 위치 + 1
        for _ in range(t):
            b[time_b] = b[time_b - 1] + 1
            time_b += 1

    else: # 왼쪽 -> 이전 위치 - 
        for _ in range(t):
            b[time_b] = b[time_b - 1] - 1
            time_b += 1

i = 1
while True:
    # 이동 종료 후에도 만나지 않는 경우
    if i == time_a: # A와 B의 총 이동시간 같음
        print(-1)
        break

    if a[i] == b[i]:
        print(i)
        break
    i += 1