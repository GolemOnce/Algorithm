# [연습문제] 우박수열 정적분

# 콜라츠 추측 - 모든 자연수에 대해 아래 작업 반복 시 항상 1로 만들 수 있다
# 1. 짝수면 2로 나눔
# 2. 홀수면 3을 곱하고 1을 더함
# 3. 1보다 크면 1번부터 반복

# 해서 나온 꺾은선그래프를 정적분.
# (0, 0)은 전체 구간

def solution(k, ranges):
    answer = []
    collatz = []
    x, y = 0, k

    while (y > 1):
        collatz.append((x, y))
        if y % 2 == 0:
            y //= 2
        else:
            y *= 3
            y += 1
        x += 1
    collatz.append((x, y))
    n = collatz[-1][0]

    for a, b in ranges:
        tmp = 0
        if a == n + b:
            answer.append(0.0)
        elif a > n + b:
            answer.append(-1.0)
        else:
            tmp += sum(collatz[i][1] for i in range(a, n + b + 1))
            tmp += sum(collatz[i][1] for i in range(a + 1, n + b))
            answer.append(tmp / 2)
    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))
print(solution(3, [[0,0], [1,-2], [3,-3]]))

# 어차피 x값 == 인덱스라 y값만 저장해도 됨
def solution2(k, ranges):
    answer = []
    collatz = [k]
    while (k > 1):
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        collatz.append(k)
    n = len(collatz) - 1

# 적분도 a==b==0을 굳이 추가할 필요 없음
    for a, b in ranges:
        tmp = 0
        if a == n + b:
            answer.append(0.0)
        elif a > n + b:
            answer.append(-1.0)
        else:
            tmp += sum(collatz[i] for i in range(a, n + b + 1))
            tmp += sum(collatz[i] for i in range(a + 1, n + b))
            answer.append(tmp / 2)
    return answer

print(solution2(5, [[0,0],[0,-1],[2,-3],[3,-3]]))
