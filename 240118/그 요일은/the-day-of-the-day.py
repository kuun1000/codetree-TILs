def total_days(m, d):
    nums_of_day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    tot_days = 0
    for i in range(1, m):
        tot_days += nums_of_day[i]
    tot_days += d

    return tot_days

def whichDay(string):
    day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    idx = day_of_week.index(string)
    return idx

def countDay(diff, day):
    cnt = 0
    for i in range(1, diff+1):
        if i % 7 == day:
            cnt += 1
    
    return cnt




m1, d1, m2, d2 = tuple(map(int, input().split()))
A = input()

diff = total_days(m2, d2) - total_days(m1, d1)
day = whichDay(A)
cnt = countDay(diff, day)

print(cnt)