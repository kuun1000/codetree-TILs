MAX_R = 1000 * 100

n = int(input())
tile = [0] * (2 * MAX_R + 1)
black = [0] * (2 * MAX_R + 1)
white = [0] * (2 * MAX_R + 1)

cur = MAX_R
for _ in range(n):
    x, direction = tuple(input().split())
    x = int(x)

    if direction == "L":
        while x > 0:
            tile[cur] = 1
            white[cur] += 1
            x -= 1
        
            if x:
                cur -= 1

    else:
        while x > 0:
            tile[cur] = 2
            black[cur] += 1
            x -= 1

            if x:
                cur += 1

w, b, g = 0, 0, 0 
for i in range(2 * MAX_R + 1):
    if black[i] >= 2 and white[i] >= 2:
        g += 1
    elif tile[i] == 1:
        w += 1
    elif tile[i] == 2:
        b += 1

print(w, b, g)