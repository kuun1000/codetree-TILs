# 변수 선언 및 입력
n = int(input())
people = list(map(int, input().split()))
distance = [0] * n  # 지점별 이동거리 합 

for i in range(n):      # 각 지점별로 
    for j in range(n):      # 모든 지점에 대해
        distance[i] += people[j] * abs(i - j)   # 이동거리 = 인원 수 x 해당 지점과 현재 지점과의 거리 차

print(min(distance))