binary = list(map(int, list(input())))
length = len(binary)
num = 0

for i in range(length):
    num = num * 2 + int(binary[i])

print(num)