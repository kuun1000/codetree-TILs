n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            candidate = [i, j, k]
            is_possible = True

            for num, strike, ball in arr:
                num = list(map(int, str(num)))
                s = b = 0

                for x in range(3):
                    if candidate[x] == num[x]:
                        s += 1
                    elif candidate[x] in num:
                        b += 1
                
                if s != strike or b != ball:
                    is_possible = False
                    break

            if is_possible:
                ans += 1

print(ans)