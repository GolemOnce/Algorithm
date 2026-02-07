# [PCCP 기출문제] 2번 / 석유 시추
# 세로(깊이) n, 가로(너비) m 격자모양 땅
from collections import deque

def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[False] * m for _ in range(n)]
    oil_num_list = [[0] * m for _ in range(n)]
    oil_dic = {}
    oil_num = 0
    cnt = 0
    for i in range(m):
        oil_cnt = 0
        cnt_list = set()
        for j in range(n):
            if land[j][i] == 1 and not visited[j][i]:
                oil_num += 1
                q = deque([(j, i)])
                oil_num_list[j][i] = oil_num
                cnt_list.add(oil_num_list[j][i])
                while q:
                    row, col = q.popleft()
                    if visited[row][col]:
                        continue
                    cnt += 1
                    visited[row][col] = True
                    oil_num_list[row][col] = oil_num
                    for k in range(4):
                        nr = row + dr[k]
                        nc = col + dc[k]
                        if 0 <= nr < n and 0 <= nc < m:
                            if land[nr][nc] == 1 and not visited[nr][nc]:
                                q.append([nr, nc])
                oil_dic[oil_num] = cnt
                cnt = 0
            elif visited[j][i]:
                cnt_list.add(oil_num_list[j][i])
        for j in cnt_list:
            oil_cnt += oil_dic[j]
        answer = max(oil_cnt, answer)

    return answer
# 너무 .. 지저분하다
print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))


def solution2(land):
    n, m = len(land), len(land[0])
    visited = [[True]*m for _ in range(n)]
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    oil_cnt = [0]*m
    for i in range(n):
        for j in range(m):
            if land[i][j] and visited[i][j]:
                visited[i][j] = False
                s = [(i,j)]
                col = set()
                oil = 0
                while s:
                    x, y = s.pop()
                    col.add(y)
                    oil += 1
                    for dx, dy in delta:
                        X, Y = x+dx, y+dy
                        if 0<=X<n and 0<=Y<m and land[X][Y] and visited[X][Y]:
                            visited[X][Y] = False
                            s.append((X,Y))
                for y in col:
                    oil_cnt[y] += oil
    return max(oil_cnt)