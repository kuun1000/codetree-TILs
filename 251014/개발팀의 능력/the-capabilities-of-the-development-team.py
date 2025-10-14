skills = list(map(int, input().split()))
n = 5
min_diff = float('inf')
found = False

for i in range(n):
    for j in range(i+1, n):
        team1 = skills[i] + skills[j]
        remain1 = [x for x in range(n) if x not in [i, j]]
        
        for a in range(len(remain1)):
            for b in range(a+1, len(remain1)):
                team2 = skills[remain1[a]] + skills[remain1[b]]
                last_idx = [x for x in remain1 if x not in [remain1[a], remain1[b]]][0]
                team3 = skills[last_idx]
                
                teams = [team1, team2, team3]
                
                # 팀 능력치가 모두 달라야 함
                if len(set(teams)) < 3:
                    continue
                
                diff = max(teams) - min(teams)
                min_diff = min(min_diff, diff)
                found = True

if found:
    print(min_diff)
else:
    print(-1)
