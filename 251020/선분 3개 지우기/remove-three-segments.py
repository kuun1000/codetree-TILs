n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]

def non_overlapped(l1, l2, l3):
    cnt = [0] * (101)
    for i in range(n):
        if i in [l1, l2, l3]:
            continue
        
        a, b = arr[i]
        for j in range(a, b+1):
            cnt[j] += 1
    
    for x in cnt:
        if x > 1:
            return False
    return True


ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if non_overlapped(i, j, k):
                ans += 1

print(ans)