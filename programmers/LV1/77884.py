# [월간 코드 챌린지 시즌2] 약수의 개수와 덧셈

# 두 정수 left, right
# 약수의 개수가 짝수? > 제곱수가 아니다라는 수학적 사실에 근거
import math
def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if math.isqrt(i) ** 2 == i:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13, 17))

# math 사용 x
def solution2(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution2(13, 17))