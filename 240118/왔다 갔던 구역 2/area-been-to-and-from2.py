OFFSET = 1000
MAX_R = 2000

n = int(input())
sections = []

cur = 0

for _ in range(n):
    x, direction = tuple(input().split())
    x = int(x)

    if direction == "L":
        left = cur - x
        right = cur 
        cur -= x

    else:
        left = cur
        right = cur + x
        cur += x

    sections.append([left, right])

checked = [0] * (MAX_R + 1)

for x1, x2 in sections:
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    for i in range(x1, x2):
        checked[i] += 1

cnt = 0
for elem in checked:
    if elem >= 2:
        cnt += 1

print(cnt)