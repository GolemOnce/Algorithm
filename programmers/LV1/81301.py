# [2021 카카오 채용연계형 인턴십] 숫자 문자열과 영단어

# 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다.
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성
# "one4seveneight" > 1478

def solution(s):
    answer = ''
    str_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tmp = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            tmp += i
        if tmp in str_list:
            answer += str(str_list.index(tmp))
            tmp = ''
    return int(answer)


print(solution("one4seveneight"))

def solution2(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)

print(solution2("one4seveneight"))