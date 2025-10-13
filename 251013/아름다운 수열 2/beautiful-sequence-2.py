from collections import Counter 

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

cb = Counter(b)
ca = Counter(a[:m])
ans = 0

if ca == cb:
    ans += 1

for i in range(m, n):
    ca[a[i]] += 1           # 새로 들어온 수 추가
    ca[a[i - m]] -= 1       # 빠지는 수 제거
    
    if ca[a[i - m]] == 0:   # 0인 항목은 삭제
        del ca[a[i - m]]
    
    if ca == cb:
        ans += 1

print(ans)