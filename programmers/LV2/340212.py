# [PCCP 기출문제] 2번 / 퍼즐 게임 챌린지
# 현재 퍼즐의 난이도를 diff, 현재 퍼즐의 소요 시간을 time_cur, 이전 퍼즐의 소요 시간을 time_prev, 당신의 숙련도를 level
# diff ≤ level이면 퍼즐을 틀리지 않고 time_cur
# diff > level이면, 퍼즐을 총 diff - level번 틀립니다. 퍼즐을 틀릴 때마다, time_cur만큼의 시간을 사용하며, 추가로 time_prev만큼의 시간을 사용해 이전 퍼즐

# diffs, times 길이가 30만이라 O(n^2)은 시간초과 날 것 같아서 이진탐색 활용함
def solution(diffs, times, limit):
    answer = 0
    first, last = 1, max(diffs)

    while (first <= last):
        mid = (first + last) // 2
        if puzzle(diffs, times, mid) == limit:
            return mid
        if puzzle(diffs, times, mid) < limit:
            last = mid - 1
        elif puzzle(diffs, times, mid) >= limit:
            first = mid + 1
    answer = first
    return answer

def puzzle(diffs, times, level):
    total_time = 0
    for i in range(len(diffs)):
        gap = 0 if level > diffs[i] else diffs[i] - level
        if i == 0:
            total_time += times[i] * (gap + 1)
        elif gap == 0:
            total_time += times[i]
        else:
            total_time += (times[i-1] + times[i]) * gap + times[i]
    
    return total_time


print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))
