# 클래스 선언
class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

# 입력 받기
n = int(input())
students = []
for _ in range(n):
    name, height, weight = input().split()
    students.append(Student(name, int(height), int(weight)))

# 키를 기준으로 오름차순 정렬
students.sort(key=lambda x:x.height)

# 정렬된 결과 출력
for i in range(n):
    print(students[i].name, students[i].height, students[i].weight)