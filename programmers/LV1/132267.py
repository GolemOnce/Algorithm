# [연습문제] 콜라 문제
# 빈 병 최초 n개 빈 병 a개를 가져가면 새 콜라 b개를 준다

# 교환하지 못하고 남은 빈 병 개수를 저장할 변수 remain
# remain이 a개가 되면 새 콜라 b개 추가로 받음

def solution(a, b, n):
    answer = 0
    remain = n

    while (True):
        gain = remain // a
        remain = remain % a
        remain += gain * b
        answer += gain * b
        if remain < a:
            break

    return answer

print(solution(2, 1, 20))
print(solution(3, 1, 20))

# 생각해보니 remain 굳이 쓸 필요 없이 현재 콜라병 개수 n으로 퉁쳐도 괜찮을 듯
def solution2(a, b, n):
    answer = 0

    while (n >= a):
        answer += n // a * b
        n = n % a + (n // a) * b
    return answer

print(solution2(2, 1, 20))
print(solution2(3, 1, 20))