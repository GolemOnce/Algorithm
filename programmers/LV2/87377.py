# [위클리 챌린지] 교점에 별 만들기

# Ax + By + C = 0으로 표현할 수 있는 n개의 직선

# 이 직선의 교점 중 정수 좌표에 별을 그림
# 모든 별을 포함하는 최소한의 격자판 크기
# 별이 그려진 좌표 "*", 나머지 "."

# ax + by + c = 0
# dx + ey + f = 0
# 크래머 공식
# x = (-ce + bf) / (ae - bd)
# y = (-af + cd) / (ae - bd)

from itertools import combinations
def solution(line):
    answer = set()
    for i in combinations(line, 2):
        line1, line2 = i
        a, b, c = line1
        d, e, f = line2
        if (a*e) - (b*d) == 0:
            continue
        # 정수 판별 후 정수시에만 추가
        if (-c*e + b*f) // (a*e - b*d) == (-c*e + b*f) / (a*e - b*d) and (-a*f + c*d) // (a*e - b*d) == (-a*f + c*d) / (a*e - b*d):
            answer.add(((-c*e + b*f) // (a*e - b*d), (-a*f + c*d) // (a*e - b*d)))
    # 교점이 하나일 경우
    if len(answer) == 1:
        return ["*"]
    
    # 격자판[board] 크기 설정
    xmax, xmin = max([i[0] for i in answer]), min([i[0] for i in answer])
    ymax, ymin = max([i[1] for i in answer]), min([i[1] for i in answer])
    x_len, y_len = abs(xmax - xmin), abs(ymax - ymin)

    # '.'로 우선 채운 후
    board = [['.'] * (x_len + 1) for _ in range(y_len + 1)]

    # answer의 좌표에 해당하는 부분 '*'로 변환
    for i in answer:
        x, y = i
        x -= xmin
        y -= ymin
        board[y][x] = '*'

    # 배열 > 문자열 변환 ----> 2차원 (['.', '*'])배열 > 1차원 문자열('.*') 배열
    board = ["".join(row) for row in board]

    # 행 역순으로 출력 - answer의 좌표는 x, y 모두 +방향이지만, board 2차원배열은 x(열)는 +방향, y(행)는 -방향이기때문
    return board[::-1]

# 수학적으로 계산할 게 너무 많아서 직접 출력, 검증 하는 데 시간이 너무 오래 걸렸다.
# 여러모로 에러도 많이 만나고 생각한 방식이 가능한지 여부를 확인하는 데에도 시간이 많이 소요.
# 한 줄 코딩도 있던데 나만 이렇게 어렵게 접근하는게 맞나 싶어서 불안함이 컸던 문제

#한 줄 코딩... 이해하기를 포기함
solution = lambda line: (lambda rx, ry, s: ["".join("*" if (x, y) in s else "." for x in rx) for y in ry])(*((lambda i, j, s: (range(min(i), max(i) + 1), range(max(j), min(j) - 1, -1), s))(*(lambda s: ([v for v, _ in s], [v for _, v in s], s))(set((x // z, y // z) for x, y, z in [(b * f - e * d, e * c - a * f, a * d - b * c) for (a, b, e) in line for (c, d, f) in line] if z and not (x % z or y % z))))))