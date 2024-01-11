# Spy 클래스 선언
class Spy:
    def __init__(self, secretCode, meetingPoint, time):
        self.secretCode = secretCode
        self.meetingPoint = meetingPoint
        self.time = time

# 비밀코드, 접선 장소, 시간 입력받기
code, point, time = input().split()

# Spy 객체 생성
spy = Spy(code, point, int(time))

# Spy 객체의 멤버 변수 출력
print(f"secret code : {spy.secretCode}")
print(f"meeting point : {spy.meetingPoint}")
print(f"time : {spy.time}")