# [깊이/너비 우선 탐색(DFS/BFS)] 타겟 넘버

# BFS
from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((numbers[0], 0))
    q.append((-numbers[0], 0))
    while(q[0][1] < len(numbers) - 1):
        total, idx = q.popleft()
        q.append((total + numbers[idx + 1], idx + 1))
        q.append((total - numbers[idx + 1], idx + 1))
    for i in q:
        if i[0] == target:
            answer += 1
    return answer

# 재귀 활용
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
