# [2022 KAKAO TECH INTERNSHIP] 성격 유형 검사하기

# 1(매우 비동의)~7(매우 동의)
# 1, 7 - 3점 / 2, 6 - 2점 / 3, 5 - 1점 / 4 - 0점
# 1번 지표 R, T /  2번 지표 C , F / 3번 지표 J, M / 4번 지표 A, N
# survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나

# choices 값 4를 빼서 앞, 뒤문자 딕셔너리 값에 각각 빼기, 더하기

from collections import defaultdict

def solution(survey, choices):
    answer = ''
    dic = defaultdict(int)
    
    for i in range(len(survey)):
        dic[survey[i][0]] -= (choices[i] - 4)
        dic[survey[i][1]] += (choices[i] - 4)

    answer += 'R' if dic['R'] >= dic['T'] else 'T'
    answer += 'C' if dic['C'] >= dic['F'] else 'F'
    answer += 'J' if dic['J'] >= dic['M'] else 'M'
    answer += 'A' if dic['A'] >= dic['N'] else 'N'

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))