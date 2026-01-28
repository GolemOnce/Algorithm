# [연습문제] 추억 점수

# 사진 속 인물 [], 그리움 점수 [] 합산 = 사진의 그리움 점수
# input) 사람이름 [], 사람별 그리움 점수 [], 사진 속 인물 [][]
# 결과는 사진 별로

def solution(name, yearning, photo):
    answer = []
    name_score = {}
    
    for i in range(len(name)):
        name_score[name[i]] = yearning[i]
    # 지금처럼 1:1대응이 되면 name_score = dict(zip(name, yearning)) 으로 줄여서 사용 가능

    for i in range(len(photo)):
        photo_score = 0
        photo_score = sum([name_score.get(j, 0) for j in photo[i]])
        answer.append(photo_score)

    return answer

# 아예 딕셔너리 사용하지 않고 index로 접근하는 것도 좋음 (name, yearning, photo 길이 <= 100) 속도는 딕셔너리가 빠를듯?
# 한 줄 코딩
def solution2(name, yearning, photo):
    return [sum(yearning[name.index(j)] for j in i if j in name) for i in photo]

# 인덱싱
def solution3(name, yearning, photo):
    answer = []
    for i in photo:
        score = 0
        for j in i:
            if j in name:
                score += yearning[name.index(j)]
        answer.append(score)
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))