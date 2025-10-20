from collections import Counter

x, y = list(map(int, input().split()))

ans = 0
for i in range(x, y+1):
    nums = Counter(str(i))
    if len(nums) == 2 and min(nums.values()) == 1:
        ans +=1

print(ans)