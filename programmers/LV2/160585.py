# [연습문제] 혼자서 하는 틱택토
# 선공 "O", 후공 "X" 나올 수 있는 판인지 판별
# "O" 가 빙고가 된 경우 "X"보다 1개 많고, "X"가 빙고인 경우 "O"와 "X"의 개수가 같음
# "X"가 "O"보다 많을 수는 없다
# 1. O, X 둘 다 빙고 X
# 2. O가 X보다 적음 X
# 3. O, X 차이가 1초과 X
# 4. O가 이겼을 땐, X보다 하나 많아야함

def solution(board):
    answer = 1
    o_cnt = 0
    x_cnt = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'O':
                o_cnt += 1
            if board[row][col] == 'X':
                x_cnt += 1
    # o_cnt = sum(row.count('X') for row in board)
    # x_cnt = sum(row.count('O') for row in board)
    diff = o_cnt - x_cnt
    if diff < 0 or diff > 1:
        answer = 0
    elif is_bingo(board, 'O'):
        if diff != 1:
            answer = 0 
        if is_bingo(board, 'X'):
            answer = 0
    elif is_bingo(board, 'X') and diff != 0:
        answer = 0

    return answer

def is_bingo(board, player: str):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        elif board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))