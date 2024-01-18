a, b, c, d = tuple(map(int, input().split()))

start_time = a * 60 + b
end_time = c * 60 + d
elasped_time = end_time - start_time

print(elasped_time)