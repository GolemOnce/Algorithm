# [완전탐색] 소수 찾기


from itertools import permutations
def solution(numbers):
    answer = 0
    num_set = set()
    for i in range(1, len(numbers) + 1):
        for per in permutations(numbers,i):
            num = 0
            for dig in range(-1, -len(per) - 1, -1):
                num += int(per[dig]) * (10 ** (-dig - 1))
            num_set.add(num)
    print(num_set)
    for i in num_set:
        if i > 1:
            is_prime = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    is_prime = False
            if is_prime: answer += 1
    return answer

print(solution("17"))
print(solution("011"))

# 따봉 1위... 음
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)