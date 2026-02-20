# [연습문제] 삼총사

# 학생은 각자 정수 번호를 가짐. 학생 3명의 정수 번호의 합이 0이면 삼총사
# 삼총사를 만들 수 있는 방법의 수 return

# 3중 for문을 쓰거나 combinations모듈 활용하거나
from itertools import combinations

def solution(number):
    answer = 0

    for comb in combinations(number, 3):
        if sum(comb) == 0:
            answer += 1

    return answer

print(solution([-3, -2, -1, 0, 1, 2, 3]))