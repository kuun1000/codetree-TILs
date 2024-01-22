n = int(input())
arr = [[0] * n for _ in range(n)]

# 격자 내에 있는지
def in_range(x,y) :
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, -1, 0, 1],[-1, 0, 1, 0] # 왼쪽, 위쪽, 오른쪽, 아래쪽
cur_dir = 0 # 이동 방향

x,y = n -1, n -1    # 현재 위치
arr[x][y] = n ** 2  # 처음 위치는 n * n으로 설정

# 외부에서 시작하여 안으로 
for i in range(n * n -1, 0, -1) :
    # 이동 후의 위치
    nx, ny = x + dxs[cur_dir], y + dys[cur_dir]
    # 격자 내에 있지 않거나 이미 방문한 경우
    if not in_range(nx, ny) or arr[nx][ny] != 0 :
        cur_dir = (cur_dir + 1) % 4 # 방향 회전
    
    x, y = x + dxs[cur_dir], y + dys[cur_dir]
    arr[x][y] = i

for row in arr :
    for elem in row :
        print(elem, end = " ")
    print()