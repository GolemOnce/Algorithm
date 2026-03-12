# [연습문제] 롤케이크 자르기

# 토핑 가짓수가 같으면 공평하게 나눠진 것
# a, b set()으로 만들고 len(set())가 같으면 되는 거 아닌가? 했는데 시간초과

# 시간초과
def solution(topping):
    answer = 0

    for i in range(len(topping)):
        a, b = set(topping[:i]), set(topping[i:])
        if len(a) == len(b):
            answer += 1
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))

# 딕셔너리
def solution2(topping):
    answer = 0
    a, b = {}, {}
    for i in topping:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1

    for i in topping:
        if a[i] == 1:
            a.pop(i)
        else:
            a[i] -= 1
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
        if len(a.keys()) == len(b.keys()):
            answer += 1
    return answer

print(solution2([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution2([1, 2, 3, 1, 4]))

# 이 문제도 Counter가 유용하다
from collections import Counter

def solution3(topping):
    answer = 0
    dic = Counter(topping)
    set_dic = set()
    answer = 0

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1

    return answer