# [2023 KAKAO BLIND RECRUITMENT] 택배 배달과 수거하기

# 일렬로 나열된 n개의 집
# i번째 집은 i만큼 떨어져있음 i번째 집은 j번째 집과 j-i만큼 떨어져있음
# 트럭에 상자 cap개만큼 실을 수 있음
# 4, 5, 배달 [1, 0, 3, 1, 2], 수거 [0, 3, 0, 4, 0]
# 출발할 때, cap개수만큼 싣고, 최대한 먼 집부터 배송
# deliveries[i], pickups[i] <= cap이라 마지막 집 한 번만 들르기 가능
# 현재 택배 + 수거 > cap되는 지점에서는 가는길에 배달내리고(먼 집 앞집부터 첫 집 순서) 수거
# 
# 가는 길에 배달 내릴 때는 가능한 먼 집부터 내리기

# 4, 5, 배달[1, 0, 3, 1, 2], 수거[0, 3, 0, 4, 0]
# 2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]
def solution(cap, n, deliveries, pickups):
    answer = 0

    d = 0
    p = 0

    for i in range(n-1, -1, -1):

        cnt = 0

        d -= deliveries[i]
        p -= pickups[i]

        while d < 0 or p < 0:
            d += cap
            p += cap
            cnt += 1

        answer += (i + 1) * 2 * cnt

    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))

# https://school.programmers.co.kr/questions/43364