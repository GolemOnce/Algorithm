# [연습문제] 할인 행사

# 회원등록시 10일간 할인 구매 가능
# 회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 
from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    
    dic = dict()
    for i in range(len(want)):
        dic[want[i]] = number[i]
    # dic = dict(zip(want, number))로 압축 가능

    for i in range(0, len(discount) - 9):
        dis_dic = defaultdict(int)
        for j in discount[i:i+10]:
            dis_dic[j] += 1
        if all(dic[item] <= dis_dic[item] for item in want):
            answer += 1
    #  for i in range(len(discount)-9):
    #     if dic == Counter(discount[i:i+10]): 
    #         answer += 1
    # Counter활용 가능
    # sum(number) == 10이 보장돼있어서 dic == Counter로 비교가능

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))

