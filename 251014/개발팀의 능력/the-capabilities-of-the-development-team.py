import sys

arr = list(map(int, input().split()))
n = len(arr)

def get_diff(a, b, c, d, e):
    team1 = arr[a] + arr[b]
    team2 = arr[c] + arr[d]
    team3 = arr[e]

    return max(team1, team2, team3) - min(team1, team2, team3)

ans = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if k == i or k == j:
                continue
            for l in range(k+1, n):
                if l == i or l == j:
                    continue
                for m in range(n):
                    if m in (i, j, k, l):
                        continue
                    ans = min(ans, get_diff(i, j, k, l, m))

print(ans)