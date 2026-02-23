# [연습문제] 숫자 짝꿍

# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍
# 3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000 -> 2중 for문 힘듦
# 


def solution(X, Y):
    answer = ''
    dicx = {}
    dicy = {}

    for i in range(10):
        dicx[i], dicy[i] = 0, 0

    for i in X:
        dicx[int(i)] += 1
    for i in Y:
        dicy[int(i)] += 1
    
    # 9 ~ 1 순서대로 추가
    for i in range(9, 0, -1):
        if dicx[i] != 0 or dicy[i] != 0:
           loop = min(dicx[i], dicy[i])
           for _ in range(loop):
               answer += str(i)
    # 0 추가할땐 answer가 비어있다면 1번만 추가
    loop = min(dicx[0], dicy[0])
    for _ in range(loop):
        if answer == '0':
            return answer
        answer += '0'
    return answer if answer != '' else '-1'

print(solution("100", "2345"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))

#count 내장함수를 이용하면 간단히 압축 가능
def solution2(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer