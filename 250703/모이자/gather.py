n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
distances = []
for i in range(n):
    distance = 0
    for j in range(n):
        distance += A[j] * abs(i-j)
    distances.append(distance)

print(min(distances))