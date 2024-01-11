n = int(input())
arr = list(map(int, input().split()))

# 오름차순
arr.sort()
print(*arr)

# 내림차순
arr.sort(reverse=True)
print(*arr)