import sys
INT_MIN = -sys.maxsize

a = list(map(int, input()))
n = len(a)

# Please write your code here.
result = INT_MIN
for i in range(n):
    a[i] = 1 - a[i]

    num = 0
    for j in range(n):
        num = num * 2 + a[j]

    result = max(result, num)

    a[i] = 1 - a[i]

print(result)