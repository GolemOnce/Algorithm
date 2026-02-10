# [연습문제] 기사단원의 무기
# 각 기사에게는 1번부터 number까지 번호가 지정
# 번호의 약수의 개수만큼의 공격력인 무기 사야함
# 제한 수치 넘으면 공격력 2짜리 사야함

def solution(number, limit, power):
    answer = 0

    for i in range(1, number + 1):
        weapon = div(i)
        if weapon > limit:
            answer += power
        else:
            answer += weapon

    return answer

def div(number):
    num = 0
    for i in range(1, number + 1):
        if i ** 2 > number:
            return num
        if i ** 2 == number:
            num += 1
            return num
        elif number % i == 0:
            num += 2
    return num

print(solution(10, 3, 2))