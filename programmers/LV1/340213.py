#prev 10초 전(현재시간 10초 미만은 처음), next 10초 후(남은시간 10초 미만은 끝), 오프닝 자동 건너뛰기 3가지 기능

def solution(video_len, pos, op_start, op_end, commands):
    video_len = string_to_time(video_len)
    pos = string_to_time(pos)
    op_start = string_to_time(op_start)
    op_end = string_to_time(op_end)
    answer = cal_time(video_len, pos, op_start, op_end, commands)

    return time_to_string(answer)

#문자열("00:00") > 숫자(초)
def string_to_time(input_time):    
    mm = int(input_time[:2])
    ss = int(input_time[-2:])
    return mm * 60 + ss

#숫자(초) > 문자열("00:00")
def time_to_string(time):
    mm = time // 60
    ss = time % 60
    if mm < 10:
        mm = "0" + str(mm)
    if ss < 10:
        ss = "0" + str(ss)
    return str(mm) + ":" + str(ss)

def skip_opening(time, op_start, op_end):
    m_time = time
    if (m_time >= op_start) and (m_time <= op_end):
        m_time = op_end
    return m_time

def invalid_time(video_len, time):
    if time < 0:
        time = 0
    if time > video_len:
        time = video_len
    return time

def cal_time(video_len, pos, op_start, op_end, commands):
    time = pos
    for i in range(len(commands)):
        time = skip_opening(time, op_start, op_end)
        if commands[i] == "next":
            time += 10
        if commands[i] == "prev":
            time -= 10
        time = invalid_time(video_len, time)
    time = skip_opening(time, op_start, op_end)
    return time