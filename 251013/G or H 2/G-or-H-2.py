n = int(input())

arr = [0] * 101
for _ in range(n):
    pos, char = input().split()
    arr[int(pos)] = 1 if char == 'G' else 2

ans = 0
for i in range(101):
    for j in range(i+1, 101):
        if arr[i] == 0 or arr[j] == 0:
            continue

        cnt_g, cnt_h = 0, 0
        for k in range(i, j+1):
            if arr[k] == 1:
                cnt_g += 1
            if arr[k] == 2:
                cnt_h += 1
        
        if cnt_g == 0 or cnt_h == 0 or cnt_g == cnt_h:
            ans = max(ans, j-i)

print(ans)