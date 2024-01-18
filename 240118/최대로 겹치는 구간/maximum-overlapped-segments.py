n = int(input())

offset = 100
checked = [0] * (offset * 2)

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))
    x1 += offset
    x2 += offset

    for i in range(x1-1, x2-1):
        checked[i] += 1

print(max(checked))