# [연습문제] 요격 시스템
# A 나라가 발사한 폭격 미사일은 x축에 평행한 직선 형태의 모양이며 개구간을 나타내는 정수 쌍 (s, e) 형태로 표현
# B 나라는 특정 x 좌표에서 y 축에 수평이 되도록 미사일을 발사
# 개구간 (s, e)에서는 요격 불가능
# 0 <= s <= e <= 100,000,000 O(nlogn)까지 가능?

def solution(targets):
    answer = 0
    targets.sort(key = lambda x: x[1])
    end = 0

    for s, e in targets:
        if s >= end:
            end = e
            answer += 1

    return answer


print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))

# 