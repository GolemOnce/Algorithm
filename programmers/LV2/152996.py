# [연습문제] 시소 짝꿍

# 중심으로부터 2m, 3m, 4m거리에 좌석이 있는 시소
# 두 명이 마주보고 탔을 때 평형상태 - 시소 짝꿍
# 무게x거리로 계산
# weights의 길이 10만 이하
# a가 2m일 때, b 2m, b 3m, b 4m > 1, 1.5, 2
# a가 3m일 때, b 2m, b 3m, b 4m > 2/3, 1, 4/3
# a가 4m일 때, b 2m, b 3m, b 4m > 1/2, 3/4, 1
# 위 7가지 경우 수 중 큰 수(2/3, 4/3, 2)만 비교함 (중복방지)
# 100, 100, 100 처럼 3명 있으면 100,100 한 쌍 아니고 n*(n-1)/2가지

from collections import Counter
def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for i in range(100, 1001): # 1:1, 2:3, 2:4, 3:4 인 경우의 수(중복 방지를 위해 큰 수랑만 비교)
        if counter[i] > 0:
            answer += (counter[i] * (counter[i]-1))/2 # 1:1 조합 nC2 = n(n-1)/2
            answer += counter[i] * counter[i * 3 / 2] # 2:3
            answer += counter[i] * counter[i * 2] # 2:4
            answer += counter[i] * counter[i * 4 / 3] # 3:4
    
    return answer

print(solution([100,180,360,100,270]))

# Counter 활용
# = 요소의 개수를 세는 딕셔너리 서브클래스
# 일반 dict와 달리 KeyError 없이 0 반환 장점

# 리스트
c = Counter([1, 1, 2, 3, 3, 3])
# Counter({3: 3, 1: 2, 2: 1})

# 문자열
c = Counter("abracadabra")
# Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# 딕셔너리로 직접 생성
c = Counter({'a': 3, 'b': 2})

# 키워드 인자
c = Counter(a=3, b=2)

