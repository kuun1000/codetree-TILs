# 클래스 선언
class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng 
        self.math = math 

# 정수 n 입력 받기
n = int(input())

# 학생 정보 입력 받기
students = []
for _ in range(n):
    name, kor, eng, math = input().split()
    students.append(Student(name, int(kor), int(eng), int(math)))

# 국어, 영어, 수학 순서대로 내림차순 정렬하기
students.sort(key=lambda x:(-x.kor, -x.eng, -x.math))

# 정렬 결과 출력하기
for student in students:
    print(student.name, student.kor, student.eng, student.math)