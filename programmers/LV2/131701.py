# [연습문제] 연속 부분 수열 합의 개수

# 원형 수열.
# 부분 수열의 합으로 만들 수 있는 수의 개수 출력 중복 제외

# 1. 길이 i : 1 ~ len(elements) for문
# 2. elements에서 길이 i인 부분 수열 합산
# 3. 시작점 바꿔가며 2번 과정 len(elements)만큼 반복 
# 완전 탐색 -> 시간초과
def solution(elements):
    answer = set()
    n = len(elements)
    for i in range(1, len(elements) + 1):
        for j in range(n):
            total = 0
            for k in range(i):
                total += elements[(j + k) % n]
            answer.add(total)
    return len(answer)

print(solution([7,9,1,1,4]))

# 시작점(인덱스)잡고 1~n회 더해가면서 set함수에 추가
# 시작점 + 1 반복 idx = n - 1까지
def solution2(elements):
    answer = set()
    n = len(elements)
    for start in range(n):
        total = 0
        for i in range(1, n + 1):
            total += elements[(i + start) % n]
            answer.add(total)
    return len(answer)

print(solution2([7,9,1,1,4]))
