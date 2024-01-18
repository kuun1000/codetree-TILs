MAX_R = 1000 * 100

n = int(input())

tile = [0] * (2 * MAX_R + 1)
cur = MAX_R
for _ in range(n):
    x, c = tuple(input().split())
    x = int(x)

    if c == "L":
        while x > 0:
            tile[cur] = 1
            x -= 1

            if x: 
                cur -= 1 
    else:
        while x > 0:
            tile[cur] = 2
            x -= 1

            if x:
                cur += 1

w, b = 0, 0
for elem in tile:
    if elem == 1:
        w += 1
    elif elem == 2:
        b += 1

print(w, b)