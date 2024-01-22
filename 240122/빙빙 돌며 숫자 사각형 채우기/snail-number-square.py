n, m = tuple(map(int, input().split()))
answer = [[0] * m for _ in range(n)]

# 격자 내부에 존재하는지
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] # 시계 방향 순환하도록
x, y = 0, 0
dir_num = 0

answer[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0: # 격자 밖을 벗어나거나 이미 방문한 경우
        dir_num = (dir_num + 1) % 4                     # 방향 번호 1 증가

    x, y = x + dxs[dir_num], y + dys[dir_num]   # 현재 방향으로 이동
    answer[x][y] = i

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()