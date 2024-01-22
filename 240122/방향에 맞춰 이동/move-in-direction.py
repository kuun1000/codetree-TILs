#     동 남  서 북
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# n 입력 받기
n = int(input())

x, y = 0, 0
for _ in range(n):
    cmd_dir, dist = input().split()
    dist = int(dist)

    if  cmd_dir == 'E':
        dir_num = 0 # 이동 방향의 인덱스

    elif    cmd_dir == 'S':
        dir_num = 1

    elif    cmd_dir == 'W':
        dir_num = 2

    else:
        dir_num = 3

    # 방향에 따라 거리만큼 이동
    x += dx[dir_num] * dist
    y += dy[dir_num] * dist

print(x, y)