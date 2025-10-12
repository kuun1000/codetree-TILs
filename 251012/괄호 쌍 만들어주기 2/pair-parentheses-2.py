arr = list(input())
n = len(arr)

result = 0
for i in range(n-3):
    if arr[i] == '(' and arr[i+1] == '(':
        for j in range(i+2, n-1):
            if arr[j] == ')' and arr[j+1] == ')':
                result += 1

print(result)