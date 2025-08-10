import sys
input = sys.stdin.readline

def counting_sort_by_digit(arr, pos):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for num in arr:
        index = (num // pos) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    for i in range(n-1, -1, -1):
        index = (arr[i] // pos) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output

def radix_sort(arr):
    max_num = max(arr)
    pos = 1
    result = arr[:]

    while max_num // pos > 0:
        result = counting_sort_by_digit(result, pos)
        pos *= 10

    return result 

n = int(input())
arr = list(map(int, input().split()))   

result = radix_sort(arr)
print(*result)