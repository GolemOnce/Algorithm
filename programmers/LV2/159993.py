# [연습문제] 미로 탈출

# 각 칸은 통로 또는 벽으로 구성, 통로로만 지나갈 수 있음
# 통로들 중 한 칸에 레버, 문이 있고, 레버에 갔다와야 문으로 나갈 수 있다
# 최단거리 구하시오 ... BFS 쓰라는거지?
from collections import deque

def solution(maps):
    a, b = 0, 0
    width, length = len(maps[0]), len(maps)
    # 이왕 2중 for문 돌리는 거 S, L, E 다 찾아서 저장해둠
    for i in range(length):
        for j in range(width):
            if maps[i][j] == 'S':
                start = (i, j)
            if maps[i][j] == 'L':
                lever = (i, j)
            if maps[i][j] == 'E':
                end = (i, j)
    # 저장해둔 좌표값으로 출발점 > 도착점 거리 return 길이 없으면 0
    def move(maps, start:tuple, end:tuple):
        r, c = start
        er, ec = end
        dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
        dist = [[-1] * width for _ in range(length)]
        dist[r][c] = 0
        q = deque()
        q.append(start)
        while(q):
            r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr > length - 1 or nc < 0 or nc > width - 1:
                    continue
                if maps[nr][nc] != 'X' and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                if nr == er and nc == ec:
                    return dist[r][c] + 1
        return 0
    # 출발점 > 레버, 레버 > 출구 거리 각각 계산해서 더하기
    a = move(maps, start, lever)
    b = move(maps, lever, end)
    # 길이 없으면 -1, 있으면 a + b
    return -1 if a == 0 or b == 0 else a + b



print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
