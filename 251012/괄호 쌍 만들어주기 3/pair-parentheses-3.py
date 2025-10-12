a = list(input())
n = len(a)

result = 0
for i in range(n):
    if a[i] == '(':
        for j in range(i+1, n):
            if a[j] == ')':
                result += 1

print(result)