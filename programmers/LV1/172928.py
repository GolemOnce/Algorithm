# [연습문제] 공원 산책
# park 2차원 배열. park[i] S : 시작지점, O :이동가능한 통로, X : 장애물
# 이동 못하면 스킵

def solution(park, routes):
    answer = []
    width = len(park[0])
    height = len(park)

    for i in range(height):
        for j in range(width):
            if park[i][j] == "S":
                answer = [i, j]
                break

    for i in routes:
        op, n = i.split()
        n = int(n)
        curr_row, curr_col = answer[0], answer[1]
        can_move = True
        if op == "E":
            if curr_col + n > width - 1:
                continue
            for col in range(1, n + 1):
                if park[curr_row][curr_col + col] == "X":
                    can_move = False
            if can_move:
                curr_col = curr_col + n

        elif op == "W":
            if curr_col - n < 0:
                continue
            for col in range(1, n + 1):
                if park[curr_row][curr_col - col] == "X":
                    can_move = False
            if can_move:
                curr_col = curr_col - n

        elif op == "N":
            if curr_row - n < 0:
                continue
            for row in range(1, n + 1):
                if park[curr_row - row][curr_col] == "X":
                    can_move = False
            if can_move:
                curr_row = curr_row - n
        
        elif op == "S":
            if curr_row + n > height - 1:
                continue
            for row in range(1, n + 1):
                if park[curr_row + row][curr_col] == "X":
                    can_move = False
            if can_move:
                curr_row = curr_row + n

        answer = [curr_row, curr_col]
    return answer

print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))