# [완전탐색] 전력망을 둘로 나누기

# n개의 송전탑이 트리 형태로 연결
# 전선들 중 하나를 끊어서 송전탑 개수가 가능한 비슷하도록 나눌 때, 송전탑 개수 차이
# bfs
# 뭔가 아이디어는 같은데, 제대로 코드를 짜내지 못함...
from collections import defaultdict, deque

def bfs(graph, start):
    visited = [start]
    q = deque([start])
    n = 1

    while q:
        node = q.popleft()

        for adjacent in graph[node]:
            if adjacent not in visited:
                visited.append(adjacent)
                q.append(adjacent)
                n += 1

    return n


def solution(n, wires):
    answer = -1


    arr = []

    for i in wires:
        graph = defaultdict(list)
        x, y = i
        for j in wires:
            if i == j:
                continue
            a, b = j
            graph[a].append(b)
            graph[b].append(a)

        n1 = bfs(graph, x)
        n2 = bfs(graph, y)

        arr.append(abs(n1 - n2))

    answer = min(arr)

    return answer