# [연습문제] 푸드 파이터 대회

def solution(food):
    answer = ''
    table = []
    for i, v in enumerate(food):
        if i == 0:
            continue
        ad = v // 2
        for _ in range(ad):
            table.append(i)
    
    for i in range(len(table)):
        answer += str(table[i])
    answer += "0"
    for i in range(len(table) - 1, -1, -1):
        answer += str(table[i])
    return answer

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))

# 확실히 깔끔한 버전
def solution(food):
    answer ="0"
    for i in range(len(food) - 1, 0, -1):
        c = int(food[i] / 2)
        while c > 0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer