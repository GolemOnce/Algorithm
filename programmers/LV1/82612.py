# [위클리 챌린지] 부족한 금액 계산하기

# 요금 price, N번째 이용 시 N배
# 현재 가진 돈 money, count번 탔을 때 모자라는 금액

def solution(price, money, count):
    answer = 0
    for i in range(1, count + 1):
        answer += price * i

    return answer - money if answer > money else 0

print(solution(3, 20, 4))

# 등차수열 합 이용하는 방식 - 하려다가 처음엔 그냥 for문으로 작성
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
