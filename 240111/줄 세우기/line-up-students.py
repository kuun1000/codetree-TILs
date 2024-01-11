# 클래스 선언
class Student:
    def __init__(self, height, weight, index):
        self.height = height 
        self.weight = weight
        self.number = index

# n 입력 받기
n = int(input())

# 학생 정보 입력 받기
students = []
for i in range(n):
    h, w = list(map(int, input().split()))
    students.append(Student(h, w, i+1))

# 키: 내림차순, 몸무게: 내림차순, 번호: 오름차순 정렬
students.sort(key=lambda x:(-x.height, -x.weight, x.index))

# 정렬 결과 출력하기
for student in students:
    print(student.height, student.weight, student.index)