# [연습문제] 과제 진행하기

# 과제 시작 시간이 되면 진행 중이던 과제 멈추고 새로운 과제 시작
# 과제를 끝내면 다음 과제 먼저 멈춘 과제 진행(가장 최근에 멈춘 과제)

# 과제 배열, 멈춘 과제 배열(스택)

# 조건문이 너무 많이 쓰인 것 같아서 좀 아쉬운데.. not bad?

def solution(plans):
    answer = []
    stack = []
    plans.sort(key = lambda x: x[1], reverse = True)

    # 시작 시간 세팅
    work = plans.pop()
    cur_time = work[1]

    while(True):
        done_time = cal_time(cur_time, work[2])
        
        if plans:
            if done_time > plans[-1][1]:
                remain = cal_time_time(done_time, plans[-1][1])
                stack.append([work[0], "", remain])
                work = plans.pop()
                cur_time = work[1]

            elif done_time == plans[-1][1]:
                answer.append(work[0])
                cur_time = done_time
                work = plans.pop()

            elif stack:
                answer.append(work[0])
                cur_time = done_time
                work = stack.pop()

            else:
                answer.append(work[0])
                work = plans.pop()
                cur_time = work[1]

        elif stack:
            answer.append(work[0])
            work = stack.pop()
            
        else:
            answer.append(work[0])
            break

    return answer

# 시간 계산 - 포맷팅 활용
def cal_time(cur, take):
    hour, minute = map(int, cur.split(":"))
    total = hour * 60 + minute + int(take)
    hour = (total // 60)
    minute = total % 60

    return f"{hour:02d}:{minute:02d}"

def cal_time_time(done, next):
    c_hour, c_minute = map(int, done.split(":"))
    n_hour, n_minute = map(int, next.split(":"))

    c_total, n_total = c_hour * 60 + c_minute, n_hour * 60 + n_minute

    total = c_total - n_total

    return str(total)

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
# print(cal_time("12:30", 30))

# 개선점 변수명, 함수명 개선, 조건 분기 함수화, 튜플 언패킹
def solution(plans):
    answer = []
    stack = []
    
    # 시작 시간 기준 정렬 (역순)
    plans.sort(key=lambda x: x[1], reverse=True)
    
    # 첫 과제 시작
    name, start_time, duration = plans.pop()
    current_time = start_time
    
    while True:
        finish_time = add_time(current_time, duration)
        
        # 다음 과제 시작 전에 완료 못하면 중단
        if plans and finish_time > plans[-1][1]:
            remaining = time_diff(finish_time, plans[-1][1])
            stack.append((name, remaining))
            name, current_time, duration = plans.pop()
            continue
        
        # 과제 완료
        answer.append(name)
        
        # 종료 조건
        if not plans and not stack:
            break
        
        # 다음 과제 선택
        name, current_time, duration = get_next_task(
            plans, stack, finish_time
        )
    
    return answer


def get_next_task(plans, stack, current_time):
    """다음 수행할 과제 결정"""
    # 완료 시간과 동시에 다음 과제 시작
    if plans and current_time == plans[-1][1]:
        return plans.pop()
    
    # 멈춘 과제 이어하기
    if stack:
        name, duration = stack.pop()
        return (name, current_time, duration)
    
    # 새 과제 시작 (시간 점프)
    return plans.pop()


def add_time(time_str, minutes):
    """시각에 분 더하기"""
    h, m = map(int, time_str.split(':'))
    total_minutes = h * 60 + m + int(minutes)
    return f"{total_minutes // 60:02d}:{total_minutes % 60:02d}"


def time_diff(later, earlier):
    """두 시각의 차이 (분)"""
    later_min = sum(int(x) * m for x, m in zip(later.split(':'), [60, 1]))
    earlier_min = sum(int(x) * m for x, m in zip(earlier.split(':'), [60, 1]))
    return str(later_min - earlier_min)