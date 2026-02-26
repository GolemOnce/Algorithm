# [2022 KAKAO BLIND RECRUITMENT] 신고 결과 받기

# 같은 사람 여러번 신고해도 1회치만 적용
from collections import defaultdict

def solution(id_list, report, k):
    answer = []

    # 유저별 메일 받을 수
    mail = defaultdict(int)
    # user_id를 신고한 유저들 리스트
    reported_list = {user_id : [] for user_id in id_list}

    # 중복 신고 제거 후 딕셔너리에 추가
    new_report = set(report)
    for i in new_report:
        fr, to = i.split()
        reported_list[to].append(fr)

    for i in reported_list:
        if len(reported_list[i]) >= k:
            for j in reported_list[i]:
                mail[j] += 1

    for i in id_list:
        answer.append(mail[i])

    return answer
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

# 좀 느려도 깔끔한 버전 (다른 사람 풀이)
def solution2(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

# solution2에서 시간복잡도 개선(index() > 딕셔너리)
def solution3(id_list, report, k):
    idx = {user: i for i, user in enumerate(id_list)}  # O(1) 접근
    reports = {x: 0 for x in id_list}
    answer = [0] * len(id_list)

    new_report = set(report)
    
    for r in new_report:
        reports[r.split()[1]] += 1

    for r in new_report:
        if reports[r.split()[1]] >= k:
            answer[idx[r.split()[0]]] += 1

    return answer