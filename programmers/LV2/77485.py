# [2021 Dev-Matching: 웹 백엔드 개발자(상반기)] 행렬 테두리 회전하기

def solution(rows, columns, queries):
    answer = []
    board = [[(row * columns + col + 1) for col in range(columns)] for row in range(rows)]    

    for case in queries:
        sr, sc, er, ec = case
        sr -= 1 # 1
        sc -= 1 # 1
        er -= 1 # 4
        ec -= 1 # 3
        num = []
        tmp = board[sr][sc]
        # 첫행 우측이동
        for i in range(sc, ec):
            num.append(tmp)
            tmp = board[sr][i + 1]
            board[sr][i + 1] = num[-1]
        # 끝열 아래이동
        for i in range(sr, er):
            num.append(tmp)
            tmp = board[i + 1][ec]
            board[i + 1][ec] = num[-1]
        # 끝행 좌측이동
        for i in range(ec, sc, -1):
            num.append(tmp)
            tmp = board[er][i - 1]
            board[er][i - 1] = num[-1]
        # 첫열 위로이동
        for i in range(er, sr, -1):
            num.append(tmp)
            tmp = board[i - 1][sc]
            board[i - 1][sc] = num[-1]
        answer.append(min(num))
    return answer



# deque의 rotate() 활용
from collections import deque
def solution(rows, columns, queries):
    arr = [[i+columns*j for i in range(1,columns+1)] for j in range(rows)]
    answer, result = deque(), []
    for i in queries:
        a,b,c,d = i[0]-1,i[1]-1,i[2]-1,i[3]-1
        for x in range(d-b):
            answer.append(arr[a][b+x])
        for y in range(c-a):
            answer.append(arr[a+y][d])
        for z in range(d-b):
            answer.append(arr[c][d-z])
        for k in range(c-a):
            answer.append(arr[c-k][b])
        answer.rotate(1)
        result.append(min(answer))
        for x in range(d-b):
            arr[a][b+x] = answer[0]
            answer.popleft()
        for y in range(c-a):
            arr[a+y][d] = answer[0]
            answer.popleft()
        for z in range(d-b):
            arr[c][d-z] = answer[0]
            answer.popleft()
        for k in range(c-a):
            arr[c-k][b] = answer[0]
            answer.popleft()
    return result