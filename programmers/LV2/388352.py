# [2025 프로그래머스 코드챌린지 1차 예선] 비밀 코드 해독
# 1부터 n까지의 서로 다른 정수 5개가 오름차순으로 정렬된 비밀 코드
# m번의 시도 가능
# m번의 시도 후, 비밀 코드로 가능한 정수 조합의 개수
# n이 정수범위, q는 정수 m * 5 2차원 배열, 시스템 응답을 담은 1차원 정수 배열 ans

# combinations라는 날먹 함수가 있다.
from itertools import combinations

def solution(n, q, ans):
    answer = 0
    num_list = [i for i in range(1, n + 1)]
    
    for comb in combinations(num_list, 5):
        able = True
        for idx, case in enumerate(q):
            cnt = 0
            for i in comb:
                if i in case:
                    cnt += 1
            if cnt == ans[idx]:
                continue
            else:
                able = False
                break
        if able: answer += 1

    return answer
     

print(solution(15, [[2, 3, 9, 12, 13], [1, 4, 6, 7, 9], [1, 2, 8, 10, 12], [6, 7, 11, 13, 15], [1, 4, 10, 11, 14]], [2, 1, 3, 0, 1]))

# 파이썬 고수; 근데 다 combinations를 쓰네.. 하긴 이거 안쓰면 5중 for문 돌려야한다
def solution2(n, q, ans):
    f = list(combinations(range(1, n + 1), 5))

    for g, cnt in zip(q, ans):
         f = [code for code in f if len(set(code) & set(g)) == cnt]

    return len(f)