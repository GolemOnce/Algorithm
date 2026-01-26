# board[h][w]기준 +- 1칸 색 같은 칸 return

def solution(board, h, w):
    count = 0
    n = len(board)
    dh, dw = [0, 1, -1, 0], [1, 0 , 0, -1]
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if  0 <= h_check < n and 0 <= w_check < n:
            if board[h][w] == board[h_check][w_check]:
                count += 1
    return count

# 파이썬은 부등호 한 덩어리 가능
# 선언할때 한 줄에 여러 변수 선언하기