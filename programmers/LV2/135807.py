# [연습문제] 숫자 카드 나누기

# 1또는 2를 만족하는 가장 큰 양의 정수 a
# 1. 철수 모든 카드 숫자를 나눌 수 있고, 영희 모든 카드 숫자 못 나누는 수
# 2. 영희 모든 카드 숫자를 나눌 수 있고, 철수 모든 카드 숫자 못 나누는 수
# A의 최대 공약수 찾고, B의 숫자랑 비교
# B의 최대 공약수 찾고, A의 숫자랑 비교?
from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    answer = 0
    a = reduce(gcd, arrayA)
    b = reduce(gcd, arrayB)
    a_bool, b_bool = True, True
    for i in arrayB:
        if i % a == 0:
            a_bool = False
    for i in arrayA:
        if i % b == 0:
            b_bool = False
    if a_bool and b_bool:
        answer = max(a, b)
    elif a_bool and not b_bool:
        answer = a
    elif not a_bool and b_bool:
        answer = b
    else:
        answer = 0    
    return answer

print(solution([10, 17], [5, 20]))
print(solution([10, 20], [5, 17]))
print(solution([14, 35, 119], [18, 30, 102]))

# 일일이 boolean으로 비교하는거 좀 안예뻐보임. 그냥 하나의 배열에 담아
# all()함수 활용해서 for문도 축약
def solution(arrayA, arrayB):
    answer = []
    a, b = reduce(gcd, arrayA), reduce(gcd, arrayB)
    if all(i % a for i in arrayB):
        answer.append(a)
    if all(i % b for i in arrayA):
        answer.append(b)
    return max(answer) if answer else 0


# math.gcd 두 수의 최대공약수 반환
# 파이썬 3.9 이상에서는 gcd(1, 2, 3,...) 매개 변수 3개 이상 가능
# 파이썬 3.9 미만에서는 gcd(1, 2) 매개 변수 2개만 가능
# reduce, gcd 모두 활용해서 일일이 비교