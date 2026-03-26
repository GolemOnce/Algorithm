# [월간 코드 챌린지 시즌1] 삼각 달팽이

# 수학적으로 1행씩 채우는 방법 있을 것 같긴 한데..
# 2차원 배열을 만들고, flat하는 방식 사용
# ㅣㅡ\방향 숫자 채우기 반복
def solution(n):
    answer = []
    board = [[0] * n for _ in range(n)]
    num = 1
    start_row, start_col = 0, 0
    repeat_row, repeat_col, repeat_dia = n, n - 1, n - 2
    last_row, last_num = n - 1, n * (n + 1) / 2
    while (num <= last_num):
        # 아래로 ㅣ
        for i in range(repeat_row):
            board[start_row + i][start_col] = num
            num += 1
        # 오른쪽으로 ㅡ
        for i in range(repeat_col):
            board[last_row][start_col + i + 1] = num
            num += 1
        # 대각 왼쪽위로 \
        for i in range(repeat_dia):
            board[last_row - i - 1][start_col + repeat_col - i - 1] = num
            num += 1
        # 시작 위치, 반복횟수, 끝열 조정
        start_row += 2
        start_col += 1
        repeat_row -= 3
        repeat_col -= 3
        repeat_dia -= 3
        last_row -= 1
    # 2차원 배열 answer에 1차원으로 담기
    for i in range(n):
        for j in range(i + 1):
            answer.append(board[i][j])
    return answer


print(solution(6))


# 내 코드는 온몸비틀기라면 이 코드는 쭉쭉 뻗은 스트레칭같다
def solution(n):
    dx=[0, 1, -1]
    dy=[1,0,-1]
    b=[[0] * i for i in range(1, n + 1)]
    x, y = 0, 0
    num = 1
    d = 0
    while num <= (n + 1) * n // 2:
        b[y][x]=num
        ny = y + dy[d]
        nx = x+dx[d]
        num += 1
        if 0 <= ny < n and 0 <= nx <= ny and b[ny][nx] == 0:
            y, x = ny, nx
        else:
            d = (d + 1) % 3
            y += dy[d]
            x += dx[d]
    return sum(b, [])