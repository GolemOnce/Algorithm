# [완전탐색] 카펫

def solution(brown, yellow):
    answer = []
    sum_len_wid = (brown // 2) + 2
    for width in range(3, sum_len_wid // 2 + 1):
        length = sum_len_wid - width
        cur_yellow = (length - 2) * (width - 2)
        if cur_yellow == yellow:
            answer = [length, width]

    return answer

# 수학 문제처럼 푼 사람들이 많음
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

# 근의 공식
import math
def solution(brown, yellow):
    w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    return [w,h]