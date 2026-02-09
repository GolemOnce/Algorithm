# [연습문제] 명예의 전당 (1)
# k등보다 점수 높으면 명전 입성

def solution(k, score):
    answer = []
    board = []
    for i in score:
        if len(answer) < k:
            board.append(i)
        else:
            if i > board[-1]:
                board[-1] = i
        board = sorted(board, reverse = True)
        answer.append(board[-1])
    return answer



print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))