# [완전탐색] 최소직사각형

# 명함을 가로 또는 세로로 넣을 수 있는 지갑의 크기를 구하라

def solution(sizes):
    #a, b중 작은 수들의 최대값, 큰 수들의 최대값
    big_max, small_max = 0, 0
    for a, b in sizes:
        # a가 큰 수
        if a >= b:
            big_max = max(a, big_max)
            small_max = max(b, small_max)
        # b가 큰 수
        else:
            big_max = max(b, big_max)
            small_max = max(a, small_max)
    return big_max * small_max


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))