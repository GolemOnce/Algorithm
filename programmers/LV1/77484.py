# [2021 Dev-Matching: 웹 백엔드 개발자(상반기)] 로또의 최고 순위와 최저 순위

# 0은 지워진 번호. 당첨번호 일수도, 아닐수도 있다.
# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19] 
# 최고 순위와 최저 순위
# win_nums에서 lottos와 일치하는 번호 다 지운다
# len(win_nums) == 못 맞힌 수. 못 맞힌 수에 따라 등수 판별
# 못 맞힌 수가 0개 = 1등, 1개 2등... 5개, 6개 6등

def solution(lottos, win_nums):
    answer = []
    rank = [1, 2, 3, 4, 5, 6, 6]
    var = 0
    for number in lottos:
        if number in win_nums:
            win_nums.remove(number)
        if number == 0:
            var += 1
    remain = len(win_nums)
    return [rank[remain - var], rank[remain]]

print(solution([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]))
