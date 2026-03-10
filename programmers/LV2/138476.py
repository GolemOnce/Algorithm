# [연습문제] 귤 고르기

# 수확한 귤 중 'k'개를 골라 상자 하나에 담아 판매
# 크기별로 분류, 서로 다른 종류의 수를 최소화

# 6, [1, 3, 2, 5, 4, 5, 2, 3]일 때 1, 4를 제외한 6개 선택 시 2, 3, 5로 3가지(최소)
# 딕셔너리에 담고, 딕셔너리를 개수 순으로 정렬, 순서대로 0보다 작아질 때까지 k값에서 빼기
from collections import defaultdict, Counter
def solution(k, tangerine):
    answer = 0
    dic = defaultdict(int)
    for i in tangerine:
        dic[i] += 1
    n_dic = sorted(dic.items(), key=lambda x: -x[1])
    for i in n_dic:
        k -= i[1]
        answer += 1
        if k <= 0:
            break
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))

# value 사용할때 -> Counter
def solution2(k, tangerine):
    answer = 0
    cnt = Counter(tangerine)

    for v in sorted(cnt.values(), reverse = True):
        k -= v
        answer += 1
        if k <= 0:
            break
    return answer