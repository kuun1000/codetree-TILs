A = list(input())

cnt = 0
length = len(A)
for i in range(length):
    if A[i] == '(':
        for j in range(i+1, length):
            if A[j] == ')':
                cnt += 1

print(cnt)