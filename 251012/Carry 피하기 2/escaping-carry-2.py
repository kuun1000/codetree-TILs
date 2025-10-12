import sys

def no_carry(a, b, c):
    a, b, c = a.zfill(5), b.zfill(5), c.zfill(5)
    for i in range(5):
        if int(a[i]) + int(b[i]) + int(c[i]) >= 10:
            return False
    return True

n = int(input())
arr = list(input() for _ in range(n))

result = -1
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if no_carry(arr[i], arr[j], arr[k]):
                result = max(result, int(arr[i])+int(arr[j])+int(arr[k]))

print(result)