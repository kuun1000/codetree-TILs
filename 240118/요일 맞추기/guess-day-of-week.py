def total_days(m, d):
    nums_of_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    tot_days = 0
    for i in range(1, m):
        tot_days += nums_of_day[i]
    tot_days += d

    return tot_days

def whichDay(days):
    day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    day = day_of_week[days % 7]
    return day


m1, d1, m2, d2 = tuple(map(int, input().split()))

diff = total_days(m2, d2) - total_days(m1, d1)
day = whichDay(diff)

print(day)