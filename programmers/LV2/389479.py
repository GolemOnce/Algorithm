# [2025 프로그래머스 코드챌린지 2차 예선] 서버 증설 횟수 / 정답률 53%

# 어느 시간대의 이용자가 m명 미만 증설 필요없다(즉 서버 1 : 이용자 m)
# n x m명 이상 (n + 1) x m명 미만이라면 최소 n대의 증설된 서버가 운영
# 한 번 증설한 서버는 k시간 동안 운영 (k = 5일 때 10시 시작 ~ 15시 종료)

def solution(players, m, k):
    answer = 0
    limit = [m] * 24
    
    for i, player in enumerate(players):        
        if player >= limit[i]:
            install = (player - limit[i]) // m + 1
            answer += install
            for j in range(i, i + k):
                if j < 24:
                    limit[j] += install * m

    return answer

print(solution([0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 1, 1))