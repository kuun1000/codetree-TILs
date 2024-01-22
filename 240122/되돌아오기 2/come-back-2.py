dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # 동, 남, 서, 북

dir_num = 3     # 이동 방향
nx, ny = 0, 0   # 현재 위치
sec = 0         # 걸린 시간
ans = -1        # 정답

commands = list(input())
for cmd in commands:

    if cmd == 'L': # 왼쪽 90도 회전
        dir_num = (dir_num - 1 + 4) % 4

    elif cmd == 'R': # 오른쪽 90도 회전
        dir_num = (dir_num + 1) % 4

    else:   # F: 현재 방향으로 1칸 전진
        nx = nx + dx[dir_num]
        ny = ny + dy[dir_num]

    sec += 1
    
    if nx == 0 and ny == 0: # 시작점으로 돌아온 경우
        ans = sec
        break

print(ans)