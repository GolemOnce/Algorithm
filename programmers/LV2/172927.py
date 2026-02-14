# [연습문제] 광물 캐기

# 다곡, 철곡, 돌곡 각각 0 ~ 5개 가지고 있다
# 곡\광 다/철/돌
# 다곡 - 1/1/1
# 철곡 - 5/1/1
# 돌곡 - 25/5/1
# 어느 곡괭이든 광물 5개까지만 캘 수 있다
# 한 번 사용한 곡괭이는 5번 다 써야함
# 곡괭이를 하나 선택해서 광물 5개를 연속으로 캐고, 다음 곡괭이를 선택해서 광물 5개를 연속으로 캐는 과정을 반복하며, 더 사용할 곡괭이가 없거나 광산에 있는 모든 광물을 캘 때까지 과정을 반복
# 작업을 끝내기까지 필요한 최소한의 피로도를 return

def solution(picks, minerals):

    answer = 0

    m_dict = { "diamond": 0, "iron": 0, "stone": 0 }
    dict = {0: (1, 1, 1), 1: (5, 1, 1), 2: (25, 5, 1)}

    array = []

    # 곡괭이보다 광석이 많은 경우 대비. (테스트 케이스 8번)
    length = min(sum(picks) * 5, len(minerals))

    # 5칸마다 광석의 개수를 셈
    for i in range(length):
        m_dict[minerals[i]] += 1            
        if (i + 1) % 5 == 0 or i == len(minerals) - 1:
            array.append([m_dict["diamond"], m_dict["iron"], m_dict["stone"]])
            m_dict["diamond"], m_dict["iron"], m_dict["stone"] = 0, 0, 0

    # 다이아, 철, 돌 순서로 정렬해준다.
    array.sort(key = lambda x: (x[0], x[1], x[2]), reverse = True)

    # 다이아, 철, 돌 곡괭이 순서로 사용해서 정렬된 광석을 캠
    for dia, iron, stone in array:
        for i in range(3):
            if picks[i]:
                picks[i] -= 1
                answer += dia * dict[i][0] + iron * dict[i][1] + stone * dict[i][2]
                break

    return answer


print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))

def solution(picks, minerals):
    def solve(picks, minerals, fatigue):
        if sum(picks) == 0 or len(minerals) == 0:
            return fatigue
        result = [float('inf')]
        for i, fatigues in enumerate(({"diamond": 1, "iron": 1, "stone": 1},
                                      {"diamond": 5, "iron": 1, "stone": 1},
                                      {"diamond": 25, "iron": 5, "stone": 1},)):
            if picks[i] > 0:
                temp_picks = picks.copy()
                temp_picks[i] -= 1
                result.append(
                    solve(temp_picks, minerals[5:], fatigue + sum(fatigues[mineral] for mineral in minerals[:5])))
        return min(result)

    return solve(picks, minerals, 0)