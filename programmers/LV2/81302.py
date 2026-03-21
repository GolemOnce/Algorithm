# [2021 카카오 채용연계형 인턴십] 거리두기 확인하기

# 맨해튼 거리 = |r1 - r2| + |c1 - c2| 2이하 금지 ( 파티션 있으면 가능)
# 대기실 수 5, 가로 5, 세로 5
# 1. for문 돌면서 P자리 기준, 2칸 내에 P가 있고, 사이에 X가 없으면 (DFS)
# 2. P자리, X자리 리스트업하고 P좌표 조합 사이에 X 있는지 (완탐)
# 2번 방식 채택
from itertools import combinations
def solution(places):
    answer = []
    for room in range(5):
        bool = True
        p_list = [] # 좌석 좌표
        x_list = [] # 파티션 좌표
        for r in range(5):
            for c in range(5):
                if places[room][r][c] == 'P':
                    p_list.append([r, c])
                elif places[room][r][c] == 'X':
                    x_list.append([r, c])
        print(p_list, x_list)
        for a, b in combinations(p_list, 2):
            dis = abs(a[0] - b[0]) + abs(a[1] - b[1]) # 맨해튼 거리 계산
            if dis == 1: # 1이면 위반
                bool = False
                break
            elif dis == 2: # 2이면 사이에 파티션 있어야함
                if a[0] == b[0]: # 같은 행
                    if [a[0], (a[1]+b[1])//2] not in x_list:
                        bool = False
                        break
                elif a[1] == b[1]: # 같은 열
                    if [(a[0]+b[0])//2, a[1]] not in x_list:
                        bool = False
                        break
                else: # 대각
                    if [a[0], b[1]] not in x_list or [b[0], a[1]] not in x_list:   
                        bool = False
                        break
        answer.append(1 if bool else 0)
    return answer

print(solution(	[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))