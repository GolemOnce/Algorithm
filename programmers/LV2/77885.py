# [월간 코드 챌린지 시즌2] 2개 이하로 다른 비트

# 비트 = 2진수
# 비트로 변환 후 str로 자리수 일일이 비교가며 더하면 0x111111....1같은 애들이 문제
# 다음 수가 0x1000000...0이 될 것이기 때문에 최대 10**14만회 언저리의 연산이 일어남
# 수학적으로 접근 필요
# 101 5 / 011 3
# 110 6 / 101 5
# 10111 23 / 101111 47
# 11011 27 / 110111 55
# 2 ** (연속하는 1의 수 - 1)만큼 더하기
def solution(numbers):
    answer = []
    for number in numbers:
        # 2진법 문자열로 반환( ex) 0b1011 )
        bin_number = bin(number)
        # 마지막 자리가 1이면 1이 연속 몇 번 나오는 지 찾는다
        index = -1
        if bin_number[-1] == '1':
            while(bin_number[index] == '1'):
                index -= 1
            else:
                index += 1
            tmp = 2 ** (-(index + 1))
            answer.append(number + tmp)
        else:
            answer.append(number + 1)
    return answer


def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer