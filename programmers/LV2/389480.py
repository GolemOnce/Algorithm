# [2025 프로그래머스 코드챌린지 2차 예선] 완전범죄
# 물건 i를 훔칠 때 A도둑이 info[i][0]개의 A에 대한 흔적, B도둑이 info[i][1]개의 B에 대한 흔적
# 흔적 수는 1~3
# A도둑 흔적 누적 개수 n개 이상 검거, B도둑 흔적 누적 개수 m개 이상 검거 n, m은 120이하
# 두 도둑 모두 경찰에 붙잡히지 않도록 모든 물건을 훔쳤을 때, A도둑이 남긴 흔적의 누적 개수의 최솟값을 return (불가능시 -1)
# dp? dfs?

# DFS
def solution(info, n, m):
    global answer

    answer = n
    
    # i : 훔친개수, a : a 총 흔적, b : b 총 흔적 visited에 담길 예정
    visited = set()

    def dfs(i, a, b):
        global answer

        visited.add((i, a, b))
        if a >= n or b >= m: return
        if a >= answer: return
        if i == len(info) and a < answer:
            answer = a
            return
        
        # B가 훔침
        if (i + 1, a, b + info[i][1]) not in visited:
            dfs(i + 1, a, b + info[i][1])
        # A가 훔침
        if (i + 1, a + info[i][0], b) not in visited:
            dfs(i + 1, a + info[i][0], b)

    dfs(0, 0, 0)

    return answer if answer != n else -1


print(solution([[1, 2], [2, 3], [2, 1]], 4, 4))

# DP
def solution2(info, n, m):
    dp = [[[False] * m for _ in range(n)] for _ in range(len(info) + 1)]
    dp[0][0][0] = True
    
    for i, (info_a, info_b) in enumerate(info):
        for A in range(n):
            for B in range(m):
                if dp[i][A][B]:
                    # A 도둑이 훔치는 경우
                    na = A + info_a
                    nb = B + info_b
                    if na < n:
                        dp[i+1][na][B] = True
                
                    # B 도둑이 훔치는 경우
                    if nb < m:
                        dp[i+1][A][nb] = True
    
    for a in range(n):
        for b in range(m):
            if dp[len(info)][a][b]:
                return a
    
    return -1

print(solution2([[1, 2], [2, 3], [2, 1]], 4, 4))