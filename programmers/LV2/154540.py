# [연습문제] 무인도 여행

# 'X'는 바다, 숫자는 무인도 한 칸의 식량(1일당 1). 연결된 땅이 하나의 무인도 단위
# 모든 섬 오름차순 정렬
# dfs(while, 재귀), bfs 등등 많은 방법이 있겠지만 BFS는 많이 써봤으니까 DFS 재귀형식으로 헤보고싶어서 사용
import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    width, length = len(maps[0]), len(maps)
    visited = [[False] * width for _ in range(length)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    foods = 0

    def move(r, c):
        nonlocal foods
        foods += int(maps[r][c])
        visited[r][c] = True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr > length - 1 or nc < 0 or nc > width - 1:
                continue
            if maps[nr][nc] != 'X' and not visited[nr][nc]:
                move(nr, nc)
        return foods

    for r in range(length):
        for c in range(width):
            # 탐색하지 않은 섬 발견 시 foods 초기화 후 dfs 돌면서 합산한 foods answer에 추가
            if maps[r][c] != 'X' and not visited[r][c]:
                foods = 0
                move(r, c)
                answer.append(foods)
    
    return sorted(answer) if answer else [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))

# bfs
from collections import deque

def solution(maps):
    answer = []
    width, length = len(maps[0]), len(maps)
    visited = [[False] * width for _ in range(length)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

    def move(r, c):
        foods = 0
        queue = deque([(r, c)])
        visited[r][c] = True
        while queue:
            r, c = queue.popleft()
            foods += int(maps[r][c])
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr > length - 1 or nc < 0 or nc > width - 1:
                    continue
                if maps[nr][nc] != 'X' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        return foods

    for r in range(length):
        for c in range(width):
            if maps[r][c] != 'X' and not visited[r][c]:
                answer.append(move(r, c))

    return sorted(answer) if answer else [-1]

# dfs (while+stack)
def solution(maps):
    answer = []
    width, length = len(maps[0]), len(maps)
    visited = [[False] * width for _ in range(length)]
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]

    def move(r, c):
        foods = 0
        stack = [(r, c)]
        visited[r][c] = True
        while stack:
            r, c = stack.pop()
            foods += int(maps[r][c])
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nr > length - 1 or nc < 0 or nc > width - 1:
                    continue
                if maps[nr][nc] != 'X' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    stack.append((nr, nc))
        return foods

    for r in range(length):
        for c in range(width):
            if maps[r][c] != 'X' and not visited[r][c]:
                answer.append(move(r, c))

    return sorted(answer) if answer else [-1]