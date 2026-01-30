# [연습문제] 덧칠하기 / 정답률 65%
# n 벽 길이(0~100,000), m 롤러 길이(0~100,000), section 페인트칠 해야 하는 칸
# 이게 왜 LV2였는지 이해 불가 오류였는듯, 로직 1분만에 짜고 너무 단순해서 의심했는데 맞음;;

def solution(n, m, section):
    answer = 0
    roller = 0
    for i in section:
        if i < roller:
            continue
        else:
            roller = m + i
            answer += 1

    return answer



print(solution(20, 3, [1,2,3,6,11,14,17]))

# continue 하지 말고 그냥 넘어가면 되니까 반대 기준으로 좀 더 간결하게
def solutuin2(n, m, section):
    answer = 1
    roller = section[0]
    for i in section:
        if i > roller:
            roller = roller + m - 1
            answer += 1
    return answer