a, b = tuple(map(int, input().split()))
n = list(map(int, input()))

num = 0
length = len(n)
for i in range(length):
    num = num * a + n[i]

digits = []
while True:
    if num < b:
        digits.append(num)
        break
    
    digits.append(num % b)
    num //= b

for digit in digits[::-1]:
    print(digit, end="")