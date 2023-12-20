n = int(input())
places = list(map(int, input().split()))
distance = [0] * n

for i in range(n):
    sum_val = 0
    for j in range(n):
        sum_val += places[j] * abs(i - j)
    distance[i] = sum_val

print(min(distance))