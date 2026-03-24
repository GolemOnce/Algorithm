# [2021 KAKAO BLIND RECRUITMENT] 메뉴 리뉴얼

# 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성
# 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합
# course = [2,3,5]기준 2개 조합 중 가장 많은, 3개 조합 중 가장 많은, 5개 조합 중 가장 많은

# Counter 사용하지 않는 방식으로 하려다 보니 너무 복잡해짐
# 문제 자체도 너무 이해하기 어렵게 되어있어서 더 어렵게 느껴짐
from itertools import combinations

def solution(orders, course):
    answer = set()
    dish_list = set()
    for order in orders:
        for co in course:
            for i in combinations(order, co):
                dish_list.add(i)
    print(sorted(dish_list))
    for co in course:
        tmp = []
        for comb in dish_list:
            if len(comb) == co:
                count = 0
                for order in orders:
                    existed = True
                    for dish in comb:
                        if dish not in order:
                            existed = False
                    if existed:
                        count += 1
                if count >= 2:
                    tmp.append((comb, count))
        tmp = (sorted(tmp, key = lambda x: -x[1]))
        for i in tmp:
            if i[1] == tmp[0][1]:
                answer.add(''.join(sorted(i[0])))
    return sorted(answer)


# Counter() + most_common()
import itertools
import collections

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]