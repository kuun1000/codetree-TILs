n = int(input())

checked = [0] * 100
for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))

    for i in range(x1-1, x2):
        checked[i] += 1

print(max(checked))