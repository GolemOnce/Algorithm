# [월간 코드 챌린지 시즌3] 빛의 경로 사이클
# 방향 = [아, 왼, 위, 오]
# 좌표 = [x, y, 방향index]
# 이미 탐색한 부분도 중복해서 탐색하기 때문에 시간 초과로 실패
def solution(grid):
    answer = []
    # 빛의 출발점
    q = []
    # 빛은 모서리에서만 출발
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                q.append([i, j, k])
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]
    routes = set()
    for start in q:
        c_routes = [start]
        visited = {tuple(start): 0}  # {상태: 인덱스}
        while(True):
            cr, cc, cd = c_routes[-1]
            if grid[cr][cc] == 'R':
                nd = (cd + 1) % 4
            elif grid[cr][cc] == 'L':
                nd = (cd - 1) % 4
            else:
                nd = cd
            # 파이썬은 음수 % 양수 = 양수로 보정됨 (-1 % 3 = 2) C/JAVA는 불가능
            nr = (cr + dr[nd]) % len(grid)
            nc = (cc + dc[nd]) % len(grid[0])
            
            key = (nr, nc, nd)
            if key in visited:  # O(1)
                idx = visited[key]
                c_routes = c_routes[idx:]
                break
            # 루트 추가            
            visited[key] = len(c_routes)
            c_routes.append([nr, nc, nd])
        # 정렬 후 배열 삽입
        c_routes.sort()
        key = tuple(map(tuple, c_routes))
        routes.add(key)

    return sorted(len(route) for route in routes)

# print(solution(["SL","LR"]))
# print(solution(["S"]))

# -> 전역 visited활용, 배열 저장하고 꺼내는 for문 합치기
def solution(grid):
    R, C = len(grid), len(grid[0])
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]
    
    global_visited = set()  # 전역 방문 체크
    routes = set()
    
    for i in range(R):
        for j in range(C):
            for k in range(4):
                start = (i, j, k)
                if start in global_visited:
                    continue  # 이미 처리된 상태 스킵
                
                path = []
                visited = {}
                cur = start
                
                while cur not in visited and cur not in global_visited:
                    visited[cur] = len(path)
                    path.append(cur)
                    cr, cc, cd = cur
                    if grid[cr][cc] == 'R':
                        nd = (cd + 1) % 4
                    elif grid[cr][cc] == 'L':
                        nd = (cd - 1) % 4
                    else:
                        nd = cd
                    cur = ((cr + dr[nd]) % R, (cc + dc[nd]) % C, nd)
                
                if cur in visited:
                    # 새 사이클 발견
                    cycle = path[visited[cur]:]
                    routes.add(tuple(sorted(cycle)))
                    for state in cycle:
                        global_visited.add(state)
                
                # tail 포함 전체 경로도 global_visited에 추가
                for state in path:
                    global_visited.add(state)
    
    return sorted(len(r) for r in routes)