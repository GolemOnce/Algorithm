# [연습문제] 둘만의 암호
# 두 문자열 s, skip / 자연수 index
# s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿈
# z다음은 a, skip에 있는 알파벳은 건너뜀

# 알파벳 리스트 만들지 않는 버전
def solution(s, skip, index):
    answer = ''
    s_list = []
    skip_list = []

    for i in range(len(s)):
        s_list.append(ord(s[i]))

    for i in range(len(skip)):
        skip_list.append(ord(skip[i]))

    for i in s_list:
        loop = index
        while(loop > 0):
            i += 1
            if i >= 123:
                i -= 26
            if i not in skip_list:
                loop -= 1
        answer += chr(i)

    return answer


print(solution("aukks", "wbqd", 5))
# 답은 "happy"

# 문자열 사용
def solution(s, skip, index):
    atoz = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for i in skip:
        atoz.remove(i)

    answer = ''
    for i in s:
        answer += atoz[(atoz.index(i)+index)%len(atoz)]

    return answer