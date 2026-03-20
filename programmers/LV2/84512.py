# [완전탐색] 모음사전

# 수학적으로 푸려다 실패...
# 그냥 무식하게 배열 만들고 인덱스검색
# 중복순열 product(`iterable`, repeat = `순열 요소 수`)
from itertools import product
def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    str_list = []
    for j in range(1, 6):
        for i in product(arr, repeat = j):
            str_list.append("".join(i))
    str_list.sort()
    return str_list.index(word) + 1


# 원래 하고싶었던 수학적 계산 방법
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer