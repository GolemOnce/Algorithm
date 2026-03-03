# [2023 KAKAO BLIND RECRUITMENT] 이모티콘 할인행사

# n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매
# 할인률은 10 20 30 40% 중 하나. 이모티콘 별로 개별적용

# 사용자들은 아래 기준에 따라 이모티콘 구매 또는 플러스 구독
# 일정 비율 이상 할인하는 이모티콘 전부 구매
# 구매 비용이 일정 가격 이상일 시, 구매 취소 > 플러스 서비스 가입

# 플러스 가입이 우선 > 그 다음이 판매액
# 행사 목적을 최대한으로 달성했을 때의 이모티콘 플러스 서비스 가입 수와 이모티콘 매출액을 1차원 정수 배열에 담아 return

# users[i] = [할인률, 서비스가입액]
# 1. 이모티콘 할인률별 가격 조합(순열) (4 x n개) > product 함수
# 2. 조합별 유저 for문 돌려서 멤버십, 가입금액 계산
# 3. membership, sales 최대인 조합 찾기 > 리스트 만들어서 람다 정렬 or 변수 2개 담아서 max로 각각 비교
from itertools import product
def solution(users, emoticons):
    answer = []
    # 1. 이모티콘 할인률별 가격 조합(순열) (4 x n개) > product 함수
    discount_emoticon = list(product([10, 20, 30, 40], repeat=len(emoticons)))

    # 2. 조합별 유저 for문 돌려서 멤버십, 가입금액 계산
    for case in discount_emoticon:
        membership, sales = 0, 0

        for user in users:
            cur_membership, cur_sales = 0, 0

            for discount, emoticon in zip(case, emoticons):
                if discount >= user[0]:
                    cur_sales += (emoticon * (100 - discount) // 100)
                if cur_sales >= user[1]:
                    cur_membership += 1
                    break
            if cur_membership == 1:
                membership += 1
            else:
                sales += cur_sales
        answer.append([membership, sales])
    
    return sorted(answer, key=lambda x: (-x[0], -x[1]))[0]

print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))

# product함수(itertools), zip함수(내장) 활용
# product 함수
# arr = list(product(arr1, arr2)) > arr1의 요소와 arr2의 요소의 순열을 tuple로 만들어서 반환
# ex) arr1 = [1, 2, 3], arr2 = ['a', 'b', 'c'] -> arr = [(1, 'a'), (1, 'b'), ... (3, 'b'), (3, 'c')]
# arr = list(product(arr1, repeat=반복횟수))
# ex) arr1 = [1, 2, 3], repeat = 3 -> arr = [[1, 1], [1, 2], ... [3, 2], [3, 3]]

# zip함수
# arr = list(zip(arr1, arr2)) > arr1의 요소와 arr2의 요소를 tuple로 만들어서 반환
# ex) arr1 = [1, 2, 3], arr2 = ['a', 'b', 'c'] -> arr = [(1, 'a'), (1, 'b'), ... , (3, 'b'), (3, 'c')]