# [탐욕법(Greedy)] 구명보트

# 그리디 - 가장 무거운 사람 + 가장 가벼운 사람 조합이 최선의 조합
# pop하는 것도 비용이 크다...(시간초과) 인덱스 투 포인터로 활용
def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    first, last = 0, len(people) - 1
    while(first <= last):
        remain = limit - people[first]
        if people[last] <= remain:
            last -= 1
        first += 1
        answer += 1
    return answer