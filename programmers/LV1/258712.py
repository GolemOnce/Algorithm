# [2024 KAKAO WINTER INTERNSHIP] 가장 많이 받은 선물 
# 친구들의 이름을 담은 1차원 문자열 배열 friends 
# 이번 달까지 친구들이 주고받은 선물 기록을 담은 1차원 문자열 배열 gifts가 매개변수

def solution(friends, gifts):
    answer = 0
    pp = len(friends)

    idx_dic = {}

    # 선물 지수 dic 초기화
    for i in friends:
        idx_dic[i] = 0
    
    # 선물 지수 카운팅
    for i in gifts:
        fr, to = i.split()
        idx_dic[fr] += 1
        idx_dic[to] -= 1
        
    # i, j 비교해서 i가 받는 선물 여부, 개수 카운트
    for i in range(pp):
        take_gift = 0
        for j in range(pp):
            give = 0 # i가 받은 선물
            gnt = False # i, j가 서로 주고받음
            if i != j:
                for k in gifts:
                    fr, to = k.split()
                    if friends[i] == fr and friends[j] == to:
                        gnt = True
                        give += 1
                    if friends[i] == to and friends[j] == fr:
                        gnt = True
                        give -= 1
            if gnt and give > 0:
                take_gift += 1
            elif gnt and give < 0:
                continue
            else:
                if idx_dic[friends[i]] > idx_dic[friends[j]]:
                    take_gift += 1
        answer = max(answer, take_gift)
    return answer