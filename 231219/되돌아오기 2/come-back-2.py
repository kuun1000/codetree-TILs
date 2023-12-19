dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dir_num = 3
nx, ny = 0, 0
cnt = 0
flag = False

commands = list(input())
for cmd in commands:
    if cmd == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        nx = nx + dx[dir_num]
        ny = ny + dy[dir_num]
    cnt += 1
    
    if nx == 0 and ny == 0:
        flag = True
        break

if flag:
    print(cnt)
else:
    print(-1)