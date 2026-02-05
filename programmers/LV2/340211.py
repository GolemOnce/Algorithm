# [PCCP 기출문제] 3번 / 충돌위험 찾기
# (r, c)와 같이 2차원 좌표로 나타낼 수 있는 n개의 포인트 (1~n 고유번호)
# 로봇마다 정해진 운송 경로가 존재, 운송 경로는 m개의 포인트로 구성
# 운송 시스템에 사용되는 로봇은 x대이고, 모든 로봇은 0초에 동시에 출발
# 1초마다 r 좌표와 c 좌표 중 하나가 1만큼 감소하거나 증가한 좌표로 이동
# 항상 최단 경로로 이동, 여러 가지일 경우, r 좌표가 변하는 이동을 c 좌표가 변하는 이동보다 먼저

def solution(points, routes):
    answer = 0
    rc = len(routes) # 로봇 수
    rr = len(routes[0])# 로봇 경로 수
    rl = [[0] * 2 for _ in range(rc)] # 로봇들의 현재 좌표
    rd = [[[0] * 2 for _ in range(rr)] for _ in range(rc)] # 로봇들의 목적좌표 리스트
    rs = [1] * rc # 로봇들 도착지 인덱스

    # rl, rd 세팅
    for idx, route in enumerate(routes):
        rl[idx][0] = points[route[0] - 1][0]
        rl[idx][1] = points[route[0] - 1][1]
        tl = []
        for i in route:
            tl.append(points[i - 1])
        rd[idx] = tl

    # 시뮬레이션 시작
    while (True):
        # 충돌 여부 체크
        dump = []
        for i in range(len(rl)):
            for j in range(i + 1, len(rl)):
                if rl[i] == rl[j] and rl[i][0] != -1:
                    dump.append(rl[i]) # 같은 좌표면 dump리스트 추가
        answer += len(set(map(tuple, dump))) # 중복 제거

        # 이후 움직이기
        for rn, robot in enumerate(rl):
            r, c = robot[0], robot[1]
            # 이미 탈출한 로봇 스킵
            if r == -1 and c == -1:
                continue

            if r > rd[rn][rs[rn]][0]:
                rl[rn][0] -= 1
            elif r < rd[rn][rs[rn]][0]:
                rl[rn][0] += 1
            else:
                if c > rd[rn][rs[rn]][1]:
                    rl[rn][1] -= 1
                elif c < rd[rn][rs[rn]][1]:
                    rl[rn][1] += 1 
                else:
                    if rs[rn] == len(rd[rn]) - 1: # 다음 목직지 없으면 탈출
                        rl[rn][0], rl[rn][1] = -1, -1
                    else:
                        rs[rn] += 1 # 다음 목적지 있으면 다음 목적지 기준으로 move
                        if r > rd[rn][rs[rn]][0]:
                            rl[rn][0] -= 1
                        elif r < rd[rn][rs[rn]][0]:
                            rl[rn][0] += 1
                        else:
                            if c > rd[rn][rs[rn]][1]:
                                rl[rn][1] -= 1
                            elif c < rd[rn][rs[rn]][1]:
                                rl[rn][1] += 1 
                        
        if rl.count([-1, -1]) == rc: # 모든 로봇이 탈출 시 종료
            break
            
    return answer


print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]))

# 더 나은 코드
def solution(points, routes):
    answer = 0
    rc = len(routes)          # 로봇 수
    rl = [[0, 0] for _ in range(rc)]  # 로봇들의 현재 좌표
    rd = [[] for _ in range(rc)]      # 로봇들의 목적좌표 리스트
    rs = [1] * rc            # 로봇들 목적지 인덱스 (현재 목표: rd[rn][rs[rn]])

    # rl, rd 세팅
    for idx, route in enumerate(routes):
        r0, c0 = points[route[0] - 1]
        rl[idx][0], rl[idx][1] = r0, c0
        rd[idx] = [points[i - 1] for i in route]

    def move_one_step(r, c, tr, tc):
        # 규칙: r 먼저 맞추고, 그 다음 c
        if r != tr:
            return (r - 1, c) if r > tr else (r + 1, c)
        if c != tc:
            return (r, c - 1) if c > tc else (r, c + 1)
        return (r, c)  # already at target

    # 시뮬레이션
    while True:
        # 1) 충돌 체크 (현재 위치 기준)
        pos_count = {}
        for r, c in rl:
            if r == -1 and c == -1:
                continue
            pos_count[(r, c)] = pos_count.get((r, c), 0) + 1
        # 같은 칸에 2대 이상이면 그 칸을 1번으로 카운트
        answer += sum(1 for v in pos_count.values() if v >= 2)

        # 2) 이동
        for rn in range(rc):
            r, c = rl[rn]
            if r == -1 and c == -1:   # 탈출한 로봇
                continue

            # 현재 목표
            tr, tc = rd[rn][rs[rn]][0], rd[rn][rs[rn]][1]

            # 이미 목표 도착이면 다음 목표로 넘김(여러 개 연속 도착도 처리)
            while r == tr and c == tc:
                if rs[rn] == len(rd[rn]) - 1:
                    rl[rn][0], rl[rn][1] = -1, -1  # 탈출
                    break
                rs[rn] += 1
                tr, tc = rd[rn][rs[rn]][0], rd[rn][rs[rn]][1]

            # 탈출했으면 이동 없음
            if rl[rn][0] == -1 and rl[rn][1] == -1:
                continue

            # 한 칸 이동
            nr, nc = move_one_step(r, c, tr, tc)
            rl[rn][0], rl[rn][1] = nr, nc

        # 종료 조건
        if rl.count([-1, -1]) == rc:
            break

    return answer
