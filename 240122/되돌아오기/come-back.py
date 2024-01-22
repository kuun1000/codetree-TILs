dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
mapper = {'E': 0, 'S': 1, 'W': 2, 'N': 3} # 동, 서, 남, 북

N = int(input())

x, y = 0, 0  # 현재 위치
dir_num = 0  # 이동 방향
sec = 0      # 걸린 시간
answer = -1  # 정답 

for _ in range(N):
    direction, distance = input().split()
    dir_num = mapper[direction]
    distance = int(distance)

    for _ in range(distance):
        sec += 1
        x, y = x + dxs[dir_num], y + dys[dir_num]

        if x == 0 and y == 0: # 시작점으로 돌아온 경우
            answer = sec
            break

print(answer)