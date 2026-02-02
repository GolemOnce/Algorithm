# [연습문제] 카드뭉치
# 영어 단어가 적힌 카드 뭉치 두 개
# 문자열로 이루어진 배열 cards1, cards2와 원하는 단어 배열 goal이 매개변수
# goal을 만들 수 있으면 Yes, 없으면 No return
# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다.

def solution(cards1, cards2, goal):
    a_idx, b_idx = -1, -1

    for word in goal:
        if word in cards1:
            idx = cards1.index(word)
            if a_idx == -1 or a_idx + 1 == idx:
                a_idx = idx
            else:
                return "No"
        elif word in cards2:
            idx = cards2.index(word)
            if b_idx == -1 or b_idx + 1 == idx:
                b_idx = idx
            else:
                return "No"

        else:
            return "No"
    
    return "Yes"

# pop, index 0 활용 단순 로직
def solution2(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"


print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

# 카드를 사용하지 않고 다음 카드로 넘어갈 수 없습니다. 문제 똑바로 읽자
#  ["a", "b", "c"], ["d", "e", "f"], ["a", "d", "f"] > No나와야하는데 Yes임
def wrong_logic(cards1, cards2, goal):
    a_idx, b_idx = 0, 0
    for word in goal:
        if word in cards1:
            idx = cards1.index(word)
            if a_idx > idx:
                return "No"
            a_idx = idx
            
        elif word in cards2:
            idx = cards2.index(word)
            if b_idx > idx:
                return "No"
            b_idx = idx
    
    return "Yes"


