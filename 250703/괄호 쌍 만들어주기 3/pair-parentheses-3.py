A = input()

# Please write your code here.
result = 0
for i in range(len(A)):
    if A[i] == '(':
        for j in range(i+1, len(A)):
            if A[j] == ')':
                result += 1

print(result)