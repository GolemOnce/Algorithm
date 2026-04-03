# [2019 KAKAO BLIND RECRUITMENT] 후보키

from itertools import combinations
def solution(relation):
    answer = []
    columns = len(relation[0])
    column = [i for i in range(columns)]
    for size in range(1, columns + 1):
        for comb in combinations(column, size):
            unique = True # 유일성 여부
            comb_list = [] # (중복 확인용) 튜플(리스트 형태) 저장소
            for row in relation:
                tmp_list = [] # 현재 튜플(리스트 형태) 담을 리스트
                for key in comb:
                    tmp_list.append(row[key])
                if tmp_list in comb_list: # 중복 시 유일성
                    unique = False
                    break
                else:
                    comb_list.append(tmp_list) # 현재 튜플(리스트 형태) 저장
            if unique: # 유일성 만족한다면
                # 최소성 검증
                minimal = True
                for sub_size in range(1, size):
                    for sub in combinations(comb, sub_size):
                        sub = sub[0] if sub_size == 1 else sub
                        if sub in answer:
                            minimal = False
                if minimal: answer.append(comb[0]) if size == 1 else answer.append(comb)
    return len(answer)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
