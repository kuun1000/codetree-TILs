# 변수 선언 및 입력
n, t = tuple(map(int, input().split()))
x, y, c_dir = tuple(input().split())

dxs, dys = [0, 1, -1,  0], [1, 0,  0, -1]   # 0, 3번이 서로 반대, 1, 2번이 서로 반대가 되도록

# 각 알파벳 별 방향 번호
mapper = {'R': 0, 'D': 1, 'U': 2, 'L': 3}

x, y, m_dir = int(x) - 1, int(y) - 1, mapper[c_dir]

# 격자 내부에 존재하는지
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx, ny = x + dxs[m_dir], y + dys[m_dir]

    if in_range(nx, ny):    # 격자 내부에 존재하는 경우
        x, y = nx, ny

    else:                   # 격자 끝에 도달한 경우
        m_dir = 3 - m_dir   # 방향을 뒤집음

print(x + 1, y + 1)