# [정렬] 가장 큰 수

# 예제 2인 [3, 30, 34, 5, 9]를 예로 들면, 3, 30, 34중 옳은 순서는 34,3,30이다
# 하지만 단순히 str(x)로만 정렬을 하면 34,30,3이 나옴 
# 1~2번째 자리 수 (0-index, 이미 0자리 수+문자열 길이 기준 정렬이고 최대가 1000이라 2번째 자리까지만 비교)까지 고려할 필요 있음
# 3, 30을 비교하는 것이 관건 ... 3을 333으로, 30을 303030 등으로 만들고 비교하면 둘 중 어느 쪽이 더 먼저 오는지 판별 가능
def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key = lambda x: str(x) * 3, reverse = True)
    for i in numbers:
        answer += str(i)
    return '0' if all(x == '0' for x in answer) else answer