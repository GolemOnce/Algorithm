# [2021 KAKAO BLIND RECRUITMENT] 신규 아이디 추천

# 아이디의 길이는 3자 이상 15자 이하
# 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용
# 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.

#1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다. -> lower()
#2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다. -> 
#3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다. -> '..' -> '.'
#4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다. -> id[0], [-1] == '.' -> 
#5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
#6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다. 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
#7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# 배열로 치환
def solution(new_id):
    answer = ''
    # 1단계 - lower함수로 소문자 치환, 배열로 치환
    answer = list(new_id.lower())
    # 2단계 - 영어 소문자, 숫자, -_.가 아닌 인덱스 배열에 담고 del answer[-1]부터 삭제(인덱스 밀림 방지)
    str_list = 'abcdefghijklmnopqrstuvwxyz-_.0123456789'
    remove_list = []
    for i in range(len(answer)):
        if answer[i] not in str_list:
            remove_list.append(i)
    for i in range(len(remove_list) - 1, -1, -1):
        del answer[remove_list[i]]
    # 3단계 - '.' 다음에 '.'이 오면 해당 인덱스 삭제대상에 추가
    remove_list = []
    for i in range(len(answer)):
        if i != len(answer) - 1:
            if answer[i] == '.' and answer[i + 1] == '.':
                remove_list.append(i)
    for i in range(len(remove_list) - 1, -1, -1):
        del answer[remove_list[i]]
    # 4, 5단계
    if len(answer) == 0:
        answer = ['a']
    elif len(answer) == 1:
        if answer[0] == '.':
            answer = ['a']
    else:
        if answer[-1] == '.':
            del answer[-1]
        if answer[0] == '.':
            del answer[0]
    # 6단계
    if len(answer) > 15:
        answer = answer[0:15]
    if answer[-1] == '.':
        del answer[-1]
    # 7단계
    while(len(answer) < 3):
        answer.append(answer[-1])

    return "".join(answer) # 문자열로 변환

print(solution(	"...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

# 정규식, 활용할 수 있는 내부 함수들을 몰라서 어렵게 접근한건 맞지만 1단계수준이 아닌 것 같다
# 아무래도 배열로 만들어서 하려다보니 for문돌리면서 온몸비틀기 하는 느낌이 강한듯

#문자열 그대로 활용
def solution2(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer

# 정규식
import re

def solution3(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st