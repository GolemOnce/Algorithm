# [PCCP 기출문제] 3번 / 아날로그 시계

# 초침이 시침/분침과 겹칠 때마다 알람이 울리는 기능
# 특정 시간 동안 알람이 울린 횟수계산

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start_time, end_time = ttos(h1, m1, s1), ttos(h2, m2, s2)
    exh, exm, exs = 0, 0, 0
    cur_time = start_time 

    while (cur_time <= end_time):
        # hh시침, mm분침, ss초침
        hh = (cur_time % 43200) / 120
        mm = (cur_time % 3600) / 10
        ss = (cur_time % 60) * 6

    # 0도 부근에서 360 > 0 이 되고, ex) 시침or분침 35x와 초침 0을 비교할 때 ss > mm ss > hh, mm > hh 판별이 안됨
    # 정상적으로 카운팅 되게 적당한 값 범위 내 보정
        if ss == 0:
            ss = 360
            if mm < 10:
                mm += 360
            if hh < 10:
                hh += 360

        if hh == mm == ss:
            answer += 1
        else:
            if exs < exh and ss >= hh:
                answer += 1
            if exs < exm and ss >= mm:
                answer += 1
        exh, exm, exs = hh, mm, ss
        cur_time += 1
        
    return answer


def ttos(h, m ,s):
    sec = h * 3600 + m * 60 + s
    return sec


print(solution(0, 5, 30, 0, 7, 0))
# print(solution(12, 0, 0, 12, 0, 30))
# print(solution(1, 5, 5, 1, 5, 6))
