# [월간 코드 챌린지 시즌1] 이진 변환 반복하기

def solution(s):
    cnt = 0
    zero = 0
    while (s != '1'):
        zero += s.count('0')
        s = s.replace('0', '')
        s = bin(s)[2:]
        cnt += 1

    return [cnt, zero]

# replace도 낭비
def solution(s):
    cnt, zero = 0, 0
    while s != '1':
        net += 1
        num = s.count('1')
        zero += (len(s) - num)
        s = bin(num)[2:]
    return [cnt, zero]