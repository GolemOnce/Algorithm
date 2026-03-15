# [연습문제] 혼자 놀기의 달인

# 1~100 숫자가 있는 100장의 카드. 
# 2이상 100이하 자연수를 정해 그 수보다 작거나 같은 숫자 카드들을 준비하고, 준비한 카드의 수만큼 작은 상자를 준비하면 게임을 시작

# 준비된 상자에 카드를 한 장씩 넣고, 상자를 무작위로 섞어 일렬로 나열합니다. 상자가 일렬로 나열되면 상자가 나열된 순서에 따라 1번부터 순차적으로 증가하는 번호 지정
# 임의의 상자 하나를 선택해 카드 확인. 카드에 적힌 숫자의 번호에 해당하는 상자 선택 후 카드 확인.
# 이미 열려있는 상자가 나오면 n번 상자 그룹.
# 아직 열리지 않은 남은 상자 중 무작위로 선택 후 반복. 모든 상자가 1번 그룹이면 0 출력.
# 1번 상자 그룹의 상자 수과 2번 상자 그룹의 상자 수를 곱한 값이 게임의 점수
# 최고점수 구하기. 
from collections import defaultdict
def solution(cards):
    group = defaultdict(list)
    group_num = 1
    card_idx = 0
    n = len(cards)
    opened = [False] * n
    while(not all(opened)):
        if opened[card_idx - 1]:
            card_idx = opened.index(False) + 1
            group_num += 1
        else:
            opened[card_idx - 1] = True
            group[group_num].append(cards[card_idx])
            card_idx = cards[card_idx] - 1
    group = [len(v) for v in group.values()]
    group.sort(reverse = True)
    return group[0] * group[1] if len(group) != 1 else 0

print(solution([8,6,3,7,2,5,1,4]))