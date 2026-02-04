# [2023 KAKAO BLIND RECRUITMENT] 개인정보 수집 유효기간
# 1~n번으로 분류되는 개인정보 n, 유효기간만큼 보관 후 파기, 1달은 28일
# 오늘 날짜로 파기해야 할 개인정보 번호
# 오늘 날짜를 의미하는 문자열 today, 약관의 유효기간을 담은 1차원 문자열 배열 terms와 수집된 개인정보의 정보를 담은 1차원 문자열 배열 privacies가 매개변수

def solution(today, terms, privacies):
    answer = []
    dic = {}
    for i in terms:
        abc, deadline = i.split()
        dic[abc] = int(deadline)

    # 오늘 날짜 파싱 + int변환
    ty, tm, td = map(int, today.split('.'))
    tt = (tm - 1) * 28 + td

    # 인덱스, 값 모두 활용하기 위해 enumerate
    for idx, i in enumerate(privacies):
        # 유저 케이스 돌면서 파싱+변환
        start, abc = i.split()
        uy, um, ud = map(int, start.split('.'))
        
        # 보관 기간 계산 (년, 월)
        dy, dm = dic[abc] // 12, dic[abc] % 12
        uy, um = uy + dy, um + dm
        if um > 12:
            uy += 1
            um -= 12

        # 년은 그대로 두고, 월, 일을 일 기준으로 변환한 일수를 uu에 담음
        uu = (um - 1) * 28 + ud

        # 오늘 날짜와 비교
        if ty > uy:
            answer.append(idx + 1)
        elif ty == uy and tt >= uu:
            answer.append(idx + 1)
        else:
            continue

    return answer



print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))

# 굳이 월, 일만 변환할 필요는 없다... 그제? 연도 12 * 28로 월, 일과 같이 묶어버리면 더 깔끔할듯
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution2(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire