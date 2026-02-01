# [연습문제] 대충 만든 자판
# 1번 키부터 차례대로 할당된 문자들이 순서대로 담긴 문자열배열 keymap
# 입력하려는 문자열들이 담긴 문자열 배열 targets

def solution(keymap, targets):
    answer = []
    for words in targets:
        total = 0
        can_make = 0
        for word in words:
            find = False
            click = 100
            for key in keymap:
                if word in key:
                    click = min(click, key.index(word) + 1)
                    find = True
            if find:
                total += click
                can_make += 1
        if can_make == len(words):
            answer.append(total)
        else:
            answer.append(-1)

    return answer


print(solution(["AGZ", "BSSS"], ["ASA","BGZ"]))

# 딕셔너리 활용해서 한 번 찾은 키는 재활용
def solution2(keymap, targets):
    answer = []
    dic = {}

    for key in keymap:
        for idx, word in enumerate(key):
            dic[word] = min(idx + 1, dic[word]) if word in dic else idx + 1

    for words in targets:
        click = 0
        for word in words:
            if word not in dic:
                click = -1
                break
            click += dic[word]
        answer.append(click)
    
    return answer


print(solution2(["AGZ", "BSSS"], ["ASA","BGZ"]))