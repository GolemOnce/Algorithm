# [월간 코드 챌린지 시즌3] n^2 배열 자르기

    # 1 2 3 
    # 2 2 3 
    # 3 3 3
    # n = 4   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
    # 1 2 3 4 1 2 3 4 2 2 3 4 3 3  3  4  4  4  4  4
    # 2 2 3 4
    # 3 3 3 4
    # 4 4 4 4
    # n > 10,000,000 O(n^2)불가능 수학적으로 접근해
    # right-left < 100,000 nlogn까지 
    # new_arr는 1,2,3...n, 2,2,3,4,...,n+1, 3,3,3,4,5..
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        q = i // n + 1
        r = i % n + 1
        answer.append(max(q, r))
    return answer

# q, r 안으로 집어넣어
def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(max(i // n + 1, i % n + 1))
    return answer