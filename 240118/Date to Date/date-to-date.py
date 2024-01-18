num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = tuple(map(int, input().split()))

start_days = sum([num_of_days[i] for i in range(m1)]) + d1
end_days = sum([num_of_days[i] for i in range(m2)]) + d2
elapsed_days = end_days - start_days + 1

print(elapsed_days)