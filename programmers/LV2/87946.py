# [완전탐색] 피로도
# 탐험을 시작하기 위해 필요한 "최소 필요 피로도"와 던전 탐험을 마쳤을 때 소모되는 "소모 피로도"
# 유저의 현재 피로도 k와 각 던전별 "최소 필요 피로도", "소모 피로도"가 담긴 2차원 배열 dungeons 가 매개변수로 주어질 때, 유저가 탐험할수 있는 최대 던전 수를 return 하도록 solution 함수를 완성
# dungeons < 8 ... 완탐 ?
# 순열 이용 완탐
from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for p in permutations(dungeons):
        energy = k
        cnt = 0
        for dungeon in p:
            need, use = dungeon
            if energy - need < 0:
                break
            energy -= use
            cnt += 1
        answer = max(cnt, answer)
    return answer

# ---------------------------------- 
# DFS
def solution(k, dungeons):
    n = len(dungeons)
    answer = 0
    visited = [False] * n
    def dfs(energy, count):
        nonlocal answer
        answer = max(count, answer)
        for i in range(n):
            need, use  = dungeons[i]
            if energy >= need and not visited[i]:
                visited[i] = True
                dfs(energy - use, count + 1)
                visited[i] = False
    dfs(k, 0)
    return answer

# ----------------------
# 한줄코딩?
solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])