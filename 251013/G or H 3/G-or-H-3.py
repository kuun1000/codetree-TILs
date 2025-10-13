n, k = list(map(int, input().split()))
x, c = [], []

for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

positions = [0] * (max(x) + 1)

for pos, char in zip(x, c):
    positions[pos] = 1 if char == 'G' else 2

max_score = 0
for i in range(1, max(x) - k + 1):
    score = sum(positions[i:i+k+1])
    max_score = max(max_score, score)

print(max_score)