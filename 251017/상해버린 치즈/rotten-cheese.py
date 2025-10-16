N, M, D, S = list(map(int, input().split()))

eat_log = [[] for _ in range(N + 1)]
sick_time = [None] * (N + 1)
cheese_eaten_by = [[] for _ in range(M + 1)]

for _ in range(D):
    p, m, t = list(map(int, input().split()))
    eat_log[p].append((m, t))
    cheese_eaten_by[m].append(p)

for _ in range(S):
    p, t = list(map(int, input().split()))
    sick_time[p] = t

possible = [True] * (M+1)    
for m in range(1, M+1):
    for p in range(1, N+1):
        if sick_time[p] is None:
            continue
        
        ate_times = [t for cheese, t in eat_log[p] if cheese == m]
        if not ate_times or min(ate_times) >= sick_time[p]:
            possible[m] = False
            break

print(sum(possible))