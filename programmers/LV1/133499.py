# [연습문제] 옹알이 (2)

# aya, ye, woo, ma 네 가지 발음만 조합 가능. 같은 발음 연속 불가
# 조카가 발음할 수 있는 단어의 개수를 return

# 많이 비효율적이라고 생각
def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]

    for i in babbling:
        prev = ''
        length = 0
        able = True
        while(length < len(i)):
            if i[length : length + 2] in word:
                if prev == i[length : length + 2]:
                    able = False
                    break
                prev = i[length : length + 2]
                length += 2
            elif i[length : length + 3] in word:
                if prev == i[length : length + 3]:
                    able = False
                    break
                prev = i[length : length + 3]
                length += 3
            else:
                able = False
                break
        if able:
            answer += 1
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))


def solution(babbling):
    answer = 0
    for i in babbling:
        for j in ['aya','ye','woo','ma']:
            if j * 2 not in i:
                i = i.replace(j, ' ')
        if len(i.strip()) == 0:
            answer += 1
    return answer
