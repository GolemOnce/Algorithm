# [연습문제] 과일 장수
# 1 ~ k점 k점이 최상품 
# 한 상자에 사과 m개, p점이 가장 낮은 점수 > 한 상자의 가격 p * m

def solution(k, m, score):
    answer = 0
    boxes = len(score)
    score.sort(reverse = True)
    i = m - 1
    while(i < boxes):
        answer += (score[i] * m)
        i += m

    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))

# 로직은 생각을 했던 한 줄 코딩
def solution2(k, m, score):

    return sum(sorted(score)[len(score) % m : : m]) * m

print(solution2(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution2(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))