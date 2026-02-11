# [연습문제] 두 원 사이의 정수 쌍
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인 서로 다른 크기의 원이 두 개
# 반지름을 나타내는 두 정수 r1, r2가 매개변수
# 두 원 사이의 공간에 x, y좌표가 모두 정수인 점의 개수 (원 위의 점 포함)
from math import ceil, floor, sqrt

def solution(r1, r2):
    answer = 0
    big = r2**2
    small = r1**2
    for i in range(1, r2 + 1):
        if i < r1:
            answer += (floor(sqrt(big - i**2)) - ceil(sqrt(small - i**2)) + 1)
        else:
            answer += (floor(sqrt(big - i**2)) + 1)
    answer *= 4

    return answer

print(solution(3, 10))