import sys

arr = list(map(int, input().split()))
n = len(arr)

def get_diff(a, b, c, d):
    team1 = arr[a] + arr[b]
    team2 = arr[c] + arr[d]
    team3 = sum(arr) - team1 - team2

    return max(team1, team2, team3) - min(team1, team2, team3)

ans = sys.maxsize
for i in range(6):
    for j in range(i+1, 6):
        for k in range(6):
            if k == i or k == j:
                continue
            for l in range(k+1, 6):
                if l == i or l == j:
                    continue
                ans = min(ans, get_diff(i, j, k, l))


print(ans)