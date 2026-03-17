# [2022 KAKAO BLIND RECRUITMENT] k진수에서 소수 개수 구하기

# 양의 정수 n을 k진수로 바꿨을 때, 변환된 수 안에 아래 조건에 맞는 소수(Prime number)가 몇 개인지 알아보려 합니다.

# 1. 0P0처럼 소수 양쪽에 0이 있는 경우
# 2. P0처럼 소수 오른쪽에만 0이 있는 경우
# 3. 0P처럼 소수 왼쪽에만 0이 있는 경우
# P처럼 소수 양쪽에 아무것도 없는 경우
# P = 각 자릿수에 0을 포함하지 않는 소수. k진법으로 보았을 때가 아닌, 10진법으로 보았을 때 소수여야 한다
import math
def solution(n, k):
    answer = 0
    num = ''
    # 소수 판별
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    # 10진법 > k진법 변환
    while(n > 0):
        n, r = divmod(n, k)
        num += str(r)
    # 1자리부터 추가됐기 때문에 순서 뒤집어주고 '0'기준으로 스플릿
    trans_num = num[::-1].split('0')

    # i == P 판별 후 정답 추가, 빈 문자열 예외처리
    for i in trans_num:
        if i == '':
            continue
        if is_prime(int(i)):
            answer += 1
    return answer

# print(solution(437674, 3))
print(solution(110011, 10))