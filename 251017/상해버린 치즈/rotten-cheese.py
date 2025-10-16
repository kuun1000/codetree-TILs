from collections import defaultdict

# 입력
N, M, D, S = map(int, input().split())

eat_log = [[] for _ in range(N + 1)]          # p -> [(m, t), ...]
cheese_eaten_by = [[] for _ in range(M + 1)]  # m -> [p, p, ...]  (중복 가능, 나중에 set 처리)
sick_time = [None] * (N + 1)                  # p -> earliest sick time

for _ in range(D):
    p, m, t = map(int, input().split())
    eat_log[p].append((m, t))
    cheese_eaten_by[m].append(p)

# 아픈 기록: 사람별로 가장 이른 시간만 저장
for _ in range(S):
    p, t = map(int, input().split())
    if sick_time[p] is None or t < sick_time[p]:
        sick_time[p] = t

# 1) 각 아픈 사람 p에 대해, p가 아프기 전에 먹은 치즈들의 집합을 만든다.
cheese_before = []
for p in range(1, N + 1):
    if sick_time[p] is None:
        continue  # 안 아픈 사람은 후보 필터에 영향 없음
    t_sick = sick_time[p]
    eaten = {m for (m, t) in eat_log[p] if t < t_sick}  # 반드시 t < t_sick !!!
    cheese_before.append(eaten)

# 아픈 사람이 한 명도 없다면 어떤 치즈가 상했는지 모른다 → 전체 치즈가 후보
if not cheese_before:
    possible_cheeses = set(range(1, M + 1))
else:
    # 2) 모든 아픈 사람이 '아프기 전에' 먹은 치즈의 교집합 = 후보 치즈
    possible_cheeses = set.intersection(*cheese_before) if cheese_before else set()

# 3) 후보 치즈마다 그 치즈를 먹은 '서로 다른 사람 수'를 세고 최댓값
answer = 0
for m in possible_cheeses:
    cnt = len(set(cheese_eaten_by[m]))  # 중복 제거가 핵심
    if cnt > answer:
        answer = cnt

print(answer)
