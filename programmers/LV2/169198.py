# [연습문제] 당구 연습

# 가로 길이 m, 세로 길이 n, 공이 놓인 위치 좌표를 나타내는 두 정수 startX, startY
# 무조건 1쿠션으로 맞춰야함
# 공 맞출 경우의 수 4가지 (세로변 쿠션 2가지, 가로변 쿠션 2가지) 비교 후 작은 쪽으로 계산하면 될 듯, 코너는 고려할 필요 없다 가로세로보다 무조건 김
# 기울기 개념으로 접근? (3,7)>(7,3)을 보내기 위해 (3,7)>(x,0)or(0,y)>(7,3)
# 하지 않고 그냥 선대칭이동 해서 계산하자 소수점 나오면 피곤해

# 10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]

def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        temp = 10**100
        # y = n 대칭 / startX와 X가 같고 startY가 n과 y 사이에 있으면 불가능 (x==startX and y > startY의 역)
        if x != startX or y < startY:
            temp = min(temp, (2 * n - startY - y)**2 + (startX - x)**2)
        # y = 0 대칭 / startX와 X가 같고 startY가 0과 y 사이에 있으면 불가능 (y==startX and y < startY의 역)
        if x != startX or y > startY:
            temp = min(temp, (-startY - y)**2 + (startX - x)**2)
        # x = m 대칭 / startY와 Y가 같고 startX가 m과 x 사이에 있으면 불가능 (y==startY and x > startX의 역)
        if y != startY or x < startX:
            temp = min(temp, (2 * m - startX - x)**2 + (startY - y)**2)
        # x = 0 대칭 / startY와 Y가 같고 startX가 0과 x 사이에 있으면 불가능 (y==startY and x < startX의 역)
        if y != startY or x > startX:
            temp = min(temp, (-startX - x)**2 + (startY - y)**2)
        answer.append(temp)
    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))