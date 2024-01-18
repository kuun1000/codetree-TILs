a, b, c = tuple(map(int, input().split()))

start_time = 11 * 24 * 60 + 11 * 60 + 11
end_time = a * 24 * 60 + b * 60 + c
elapsed_time = end_time - start_time

if elapsed_time < 0:
    print(-1)
else:
    print(elapsed_time)