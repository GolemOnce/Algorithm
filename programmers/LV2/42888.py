# [2019 KAKAO BLIND RECRUITMENT] 오픈채팅방

# 문자열 포맷팅 f"{}"활용
def solution(record):
    answer = []
    dic = dict()
    for case in record:
        if case[0] == "E" or case[0] == "C":
            inout, uid, nick = case.split()
            dic[uid] = nick
    for case in record:
        if case[0] == "E":
            inout, uid, nick = case.split()
            answer.append(f"{dic[uid]}님이 들어왔습니다.")
        elif case[0] == "L":
            inout, uid = case.split()
            answer.append(f"{dic[uid]}님이 나갔습니다.")

    return answer