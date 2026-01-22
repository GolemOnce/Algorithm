def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        late = False
        for j in range(len(timelogs[i])):
            day_week = (startday + j) % 7
            if day_week == 0 or day_week == 6:
                continue
            if adjust_time(schedules[i]) < timelogs[i][j]:
                late = True
                break
        if not late:
            answer += 1
    return answer

def adjust_time(time):
    hour = time // 100
    minute = time % 100
    minute += 10
    if minute >= 60:
        hour += 1
        minute -= 60
    return hour * 100 + minute
