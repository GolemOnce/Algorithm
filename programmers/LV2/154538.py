# [연습문제] 숫자 변환하기

# 자연수 x를 y로 변환
# 세 가지 연산 가능
# 1. x + n
# 2. x * 2
# 3. x * 3
# x, y, n이 주어질 때 x를 y로 변환하기 위해 필요한 최소 연산 횟수 return
# 불가능하다면 -1 return
# 1. y가 x의 2,3배수배면 바로 3->2 나누기 처리
# 2. 아니라면 y에서 x의 2,3배수배가 될때까지 n을 뺀다
# 를 생각했으나 n이 remain//3보다 큰 경우 값이 틀림.. -> 최소 횟수 구하기에 적절하지 않음..
# 최소횟수? BFS로 그냥 x에서 키워가는 방식으로 풀어보자
# 이미 연산한 숫자는 최소값이 이미 나온 상태이니 걸러준다 > 중복연산시 타임아웃

from collections import deque
def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    cal = set()
    while(q):
        num, cnt = q.popleft()
        if num == y:
            return cnt
        # if num > y:
        if num > y or num in cal:
            continue
        cal.add(num)
        q.append((num + n, cnt + 1))
        q.append((num * 3, cnt + 1))
        q.append((num * 2, cnt + 1))
    return -1

print(solution(1, 1000000, 1))