# [연습문제] 문자열 나누기
# 문자열 s 입력. 첫 글자를 x라고 했을 때, x와 x가 아닌 글자 수가 같을 때까지 

def solution(s):
    answer = 0
    dic = {}
    sList = []

    for i in s:
        if i not in dic:
            dic[i] = 0
        dic[i] += 1
        if i not in sList:
            sList.append(i)
        
        if len(sList) >= 2:
            x = sList[0]
            notx = 0
            for i in range(1, len(sList)):
                notx += dic[sList[i]]
            if dic[x] == notx:
                answer += 1
                dic = {}
                sList = []
    if len(sList) > 0:
        answer += 1
    return answer
# 처음에 각 문자별로 카운팅해야 하는 줄 알고 dic, list 활용했으나... x와 x가 아닌 수여서 바꿔야할듯

print(solution("aaabbaccccabba"))


def solution(s):
    answer = 0
    x = 0
    notx = 0
    for i in s:
        if x == notx:
            answer += 1
            a = i
        if i == a:
            x += 1
        else:
            notx += 1
    return answer

#deque활용
from collections import deque

def solution(s):

    answer = 0

    q = deque(s)    
    while q:
        a, b = 1, 0
        x = q.popleft()    

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1

    return answer