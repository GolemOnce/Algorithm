# [연습문제] 리코쳇 로봇

# 게임판 위의 장애물(D)이나 게임판 가장자리까지 부딪힐 때까지 미끄러져 움직이는 것이 한 번의 이동(route += 1)
# G에 도달할 수 있는 최소 이동, 불가능하다면 -1
# 최단거리 찾기 -> DFS보다는 BFS
# BFS 이용, 멈춘 곳을 visited[][] = True로 만듦. 
# True인 곳에 멈추면 continue, 목적지(G)면 answer + 1 리턴, 처음 도착한 곳이면 True만들고 좌표와 길이 deque에 추가

from collections import deque

def solution(board):
    answer = 0
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    width, height = len(board[0]), len(board)
    visited = [[False] * width for _ in range(height)]
    q = deque()
    for i in range(height):
        for j in range(width):
            if board[i][j] == 'R':
                q.append([i, j, 0])
                visited[i][j] = True
                break
    while q:
        s = q.popleft()
        for i in range(4):
            r, c, answer = s
            while True:
                r += dr[i]
                c += dc[i]
                if r < 0 or r >= height or c < 0 or c >= width:
                    break
                elif board[r][c] == 'D':
                    break
            r -= dr[i]
            c -= dc[i]
            if visited[r][c] == True:
                continue
            elif board[r][c] == 'G':
                return answer + 1
            else:
                visited[r][c] = True
                q.append([r, c, answer + 1])
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))