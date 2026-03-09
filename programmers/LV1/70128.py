# [월간 코드 챌린지 시즌1] 내적

# 길이가 같은 a, b 주어짐 내적구하기
# 내적 : a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1]

# 한줄코딩
def solution(a, b):
    return sum(i * j for i, j in zip(a, b))

print(solution([1, 2, 3, 4], [-3, -1, 0, 2]))

def solution(a, b):
    answer = 0
    for i, j in zip(a, b):
        answer += i * j
    return answer