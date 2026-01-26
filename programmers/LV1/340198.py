def solution(mats, park):
    start_point = []
    start_point = find_start(park)
    answer = 0
    my_length = 0
    for i in start_point:
        my_length = max(my_length, max_length(i, park))

    for i in sorted(mats, reverse = True):
        if i <= my_length:
            answer = i
            break

    return -1 if answer == 0 else answer

def find_start(park):
    start_point = []
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "-1":
                start_point.append((i, j))
    return start_point

def max_length(start_point, park):
    h, w = len(park), len(park[0])
    x, y = start_point
    if park[x][y] != "-1":
        return 0
    max_k = min(h - x, w - y)
    k = 1
    for nk in range(2, max_k + 1):
        r = x + nk - 1
        c = y + nk - 1

        for j in range(y, y + nk):
            if park[r][j] != "-1":
                return k
            
        for i in range(x, x + nk - 1):
            if park[i][c] != "-1":
                return k
        k = nk    
    return k

# all()함수 이용하는 편이 더 깔끔.
# 공원에서 공간을 먼저 찾고 가능한 돗자리를 찾는 것보다 돗자리를 기준으로 공간을 찾는 것이 더 나은 듯