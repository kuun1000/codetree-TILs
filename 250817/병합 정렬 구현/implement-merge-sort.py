n = int(input())
arr = list(map(int, input().split()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_ = merge_sort(left)
    right_ = merge_sort(right)

    return merge(left_, right_)

def merge(left, right):
    i, j = 0, 0
    sorted_arr = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr

result = merge_sort(arr)
print(*result)