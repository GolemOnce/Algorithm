# [연습문제] 마법의 엘리베이터

# -1, +1, -10, +10, -100, +100 등과 같이 절댓값이 10**c (c ≥ 0 인 정수) 형태인 정수들이 적힌 버튼
# 현재 층 + 버튼이 0 미만일 시 움직이지 않음
# 버튼 한 번당 마돌 1개.
# 최소한의 버튼을 눌러서 현재 층 > 0층으로 이동하라
# 일 십 백 천... 순서로 5보다 크면 + 작으면 -, 같으면? 다음 자릿수 숫자로 판별 - 내리기 우선

def solution(storey):
    answer = 0
    while storey > 0:
        storey, moves = divmod(storey, 10)
        if moves > 5 or (moves == 5 and storey % 10 >= 5):
            moves = 10 - moves
            storey += 1
        answer += moves
    return answer

print(solution(555))

# divmod(a, b)내장 함수
# a를 b로 나눈 몫, 나머지를 튜플로 반환