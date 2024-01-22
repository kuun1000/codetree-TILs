#     동 남 서  북
dx = [1, 0, -1, 0] 
dy = [0, -1, 0, 1]

x, y = 0, 0 # 위치
dir_num = 3 # 방향: 북

# N개의 명령 입력 받음
cmds = list(input())

for cmd in cmds:

    if cmd == 'L': # 반시계방향 90도 방향 전환
        dir_num = (dir_num - 1 + 4) % 4 

    elif cmd == 'R': # 시계방향 90도 방향 전환
        dir_num = (dir_num + 1) % 4 
    
    else: # 현재 방향으로 1칸 이동 
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)